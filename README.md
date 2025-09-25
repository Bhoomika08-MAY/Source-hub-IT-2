# 📝 AI Text Summarizer

An interactive web app built with **Streamlit** and **NLTK** for generating extractive summaries from long text articles.

---

## 🚀 Features

* Paste any article or text and get a concise summary
* Adjustable number of sentences in the summary
* Download summary as a `.txt` file
* Simple and clean user interface

---

## ⚙️ Installation


   ```

1. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   # On Windows
   .\venv\Scripts\activate
   # On Mac/Linux
   source venv/bin/activate
   ```

2. Install required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

---

## 📦 Requirements

Create a `requirements.txt` file with:

```txt
streamlit
nltk
```

---

## ▶️ Usage

Run the app with:

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`.

---

## 🛠️ How it works

* Uses **NLTK’s Punkt tokenizer** to split text into sentences
* Removes stopwords and punctuation
* Calculates word frequency
* Scores each sentence based on important words
* Selects the top N sentences as the summary

---

## 🎥 Demo Video


Watch the demo of the AI Text Summarizer in action:

[▶️ Click to view demo]((https://raw.githubusercontent.com/Bhoomika08-MAY/Source-hub-IT-2/main/assets/demo.mp4))

---


