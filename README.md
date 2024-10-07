
# 🎙️ Speech-Enabled Football Player Chatbot by Ghazi Lassoued 🎧

Welcome to the Speech-Enabled Football Player Chatbot! This application allows users to ask questions about Tunisian football players either by typing or speaking. The app then provides responses based on a preloaded dataset of football players, translated into the user's chosen language.

## 🌟 Features

- 🎤 **Speech Recognition**: Users can input their questions via voice, and the app will transcribe the speech to text.
- 💬 **Text Input**: Users can also type their questions directly into the application.
- 🤖 **Chatbot Responses**: The app uses Natural Language Processing (NLP) techniques to provide relevant responses to user queries.
- 🌐 **Multilingual Support**: The app supports multiple languages for speech recognition and translates responses into the user's selected language.

## 📋 Prerequisites

- Python 3.6 or higher
- `pip` package manager

## ⚙️ Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/football-chatbot.git
    cd football-chatbot
    ```

2. **Install required packages**:
    Create a `requirements.txt` file with the following content:
    ```plaintext
    streamlit
    speechrecognition
    nltk
    scikit-learn
    pandas
    googletrans==4.0.0-rc1
    ```
    Then, run:
    ```bash
    pip install -r requirements.txt
    ```

3. **Download necessary NLTK data**:
    Ensure the following NLTK resources are downloaded:
    ```python
    import nltk
    nltk.download('punkt')
    nltk.download('stopwords')
    nltk.download('wordnet')
    ```

## 🚀 Usage

1. **Prepare the Dataset**:
    Ensure you have a `football_players.txt` file in the same directory as `app.py`. This file should contain information about Tunisian football players.

2. **Run the Application**:
    Open a terminal or command prompt, navigate to the directory where `app.py` is located, and run the following command:
    ```bash
    streamlit run app.py
    ```

3. **Access the App**:
    After running the above command, Streamlit will start a local web server and provide you with a URL (typically `http://localhost:8501`). Open this URL in your web browser to access the app.

## 🎨 How to Use

- **Choose API**: Select between Google or Sphinx for speech recognition.
- **Choose Language**: Pick your preferred language from the dropdown list.
- **Type Your Question**: Enter your question about Tunisian football players in the text input field.
- **Record Speech**: Click the "🎤 Record Speech" button to start recording your question. The app will transcribe your speech into text.
- **Get Answer**: The app will fetch and display the most relevant answers to your question in the selected language.
- **Provide Feedback**: Indicate if the answer was helpful.

## 👨‍💻 About the Developer

- **Name**: Ghazi Lassoued
- **Email**: [lassouedghazi21@gmail.com](mailto:lassouedghazi21@gmail.com)
- **LinkedIn**: [https://www.linkedin.com/in/ghazi-lassoued-983419239/](https://www.linkedin.com/in/ghazi-lassoued-983419239/)

