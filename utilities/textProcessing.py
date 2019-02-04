import nltk
from nltk.corpus import stopwords
from stop_words import get_stop_words


# in case these libraries are not installed
nltk.download('punkt')
nltk.download('stopwords')

# some definitions
stopWords = get_stop_words('en')  # list of stopwords/english PyPl
# stopWords = set(stopwords.words('english')) # list of stopwords/english NLTK

class TextParser:

    def removeStopWords(self, words):
        clean_words = [w for w in words if w not in stopWords]
        return clean_words
    # removes stopwords from list of words

