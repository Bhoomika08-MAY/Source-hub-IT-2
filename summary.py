from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from string import punctuation
from collections import defaultdict

print("✅ summary.py loaded")
def extractive_summary(text, num_sentences=5):
    sentences = sent_tokenize(text)
    stop_words = set(stopwords.words('english'))
    word_freq = defaultdict(int)

    for word in word_tokenize(text.lower()):
        if word not in stop_words and word not in punctuation:
            word_freq[word] += 1

    sentence_scores = {}
    for sentence in sentences:
        score = sum(word_freq.get(word.lower(), 0) for word in word_tokenize(sentence))
        sentence_scores[sentence] = score

    ranked_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)
    return ' '.join(ranked_sentences[:num_sentences])