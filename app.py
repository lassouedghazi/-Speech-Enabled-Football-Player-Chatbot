import streamlit as st
import speech_recognition as sr
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords, wordnet
from nltk.stem import WordNetLemmatizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

# Ensure necessary NLTK data is downloaded
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Load the football players dataset from text file
with open('football_players.txt', 'r', encoding='utf-8') as f:
    text_data = f.read()

# Tokenize the text into sentences
sentences = sent_tokenize(text_data)

# Preprocess the data
lemmatizer = WordNetLemmatizer()

def preprocess(sentence):
    words = word_tokenize(sentence)
    words = [word.lower() for word in words if word.lower() not in stopwords.words('english') and word.isalpha()]
    words = [lemmatizer.lemmatize(word) for word in words]
    return " ".join(words)

# Function to find synonyms using WordNet
def get_synonyms(word):
    synonyms = set()
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.add(lemma.name())
    return list(synonyms)

# Function to expand the query with synonyms
def expand_query(query):
    words = query.split()
    expanded_words = []
    for word in words:
        expanded_words.append(word)
        synonyms = get_synonyms(word)
        expanded_words.extend(synonyms)
    return " ".join(set(expanded_words))

# Function to find the most relevant sentences using TF-IDF and cosine similarity
@st.cache_data
def get_most_relevant_sentences(query, num_responses=3):
    query_processed = preprocess(query)
    expanded_query = expand_query(query_processed)

    # Create a TF-IDF vectorizer
    vectorizer = TfidfVectorizer()
    sentences_combined = sentences + [expanded_query]

    # Transform the sentences into TF-IDF vectors
    tfidf_matrix = vectorizer.fit_transform(sentences_combined)

    # Compute cosine similarity
    cosine_similarities = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])

    # Get indices of the most relevant sentences
    most_relevant_indices = cosine_similarities[0].argsort()[-num_responses:][::-1]

    return [sentences[i] for i in most_relevant_indices]

# Speech Recognition
LANGUAGES = {
    'English': 'en-US',
    'French': 'fr-FR',
    'Spanish': 'es-ES',
    'German': 'de-DE',
    'Chinese (Mandarin)': 'zh-CN',
    'Japanese': 'ja-JP',
    'Korean': 'ko-KR',
    'Italian': 'it-IT',
    'Portuguese': 'pt-PT',
    'Russian': 'ru-RU',
    'Arabic': 'ar-SA',
    'Hindi': 'hi-IN',
}

def transcribe_speech(api_choice, lang):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("🎤 Speak now...")
        audio_text = r.listen(source)
        st.info("📝 Transcribing...")

        try:
            if api_choice == "Google":
                text = r.recognize_google(audio_text, language=lang)
            elif api_choice == "Sphinx":
                text = r.recognize_sphinx(audio_text)
            else:
                text = "Invalid API choice"
            return text
        except sr.UnknownValueError:
            return "⚠️ Sorry, I did not understand that."
        except sr.RequestError as e:
            return f"⚠️ Could not request results; {e}"

def main():
    st.title("🎙️ Speech-Enabled Football Player Chatbot by Ghazi Lassoued 🎧")
    st.write("Welcome to the Speech-Enabled Football Player Chatbot! This app allows you to ask questions about Tunisian football players either by typing or speaking.")

    api_choice = st.selectbox("Choose API", ["Google", "Sphinx"])
    lang_choice = st.selectbox("Choose Language", list(LANGUAGES.keys()))
    lang = LANGUAGES[lang_choice]

    user_input = st.text_input("Type your question about Tunisian football players:")

    if st.button("🎤 Record Speech"):
        speech_input = transcribe_speech(api_choice, lang)
        st.write("You said: ", speech_input)
        user_input = speech_input

    if user_input:
        with st.spinner('Fetching answer...'):
            responses = get_most_relevant_sentences(user_input)

        st.subheader('📊 Responses:')
        for i, response in enumerate(responses, start=1):
            st.markdown(f'<p class="result">{i}. {response}</p>', unsafe_allow_html=True)

        feedback = st.radio("Was this answer helpful?", ('Select an option', 'Yes', 'No'))
        if feedback != 'Select an option':
            st.success(f'Thank you for your feedback: {feedback}!')

if __name__ == "__main__":
    main()
