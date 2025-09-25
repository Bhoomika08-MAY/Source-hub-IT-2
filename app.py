import streamlit as st
from summary import extractive_summary
import nltk

import nltk

# Ensure punkt resources are available
for resource in ["punkt", "punkt_tab"]:
    try:
        nltk.data.find(f"tokenizers/{resource}")
    except LookupError:
        nltk.download(resource)


# Ensure required resources are available
nltk.download('punkt')
nltk.download('stopwords')

st.set_page_config(page_title="AI Text Summarizer", layout="centered")

st.title("📝 AI Text Summarizer")
st.write("Paste your article below and get a concise summary.")

# Text input
text_input = st.text_area("Enter your article here:", height=300)

# Summary length slider
num_sentences = st.slider("Number of sentences in summary:", min_value=1, max_value=10, value=5)

# Generate summary
if st.button("Generate Summary"):
    if text_input.strip():
        summary = extractive_summary(text_input, num_sentences=num_sentences)
        st.subheader("Summary:")
        st.write(summary)

        # Copy to clipboard
        st.code(summary, language='text')

        # Download as .txt
        st.download_button("📥 Download Summary", summary, file_name="summary.txt", mime="text/plain")
    else:
        st.warning("Please enter some text to summarize.")