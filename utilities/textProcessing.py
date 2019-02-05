import nltk
from nltk.corpus import stopwords
from stop_words import get_stop_words
from collections import defaultdict
from gensim.corpora import Dictionary
from gensim import corpora

# in case these libraries are not installed
# nltk.download('punkt')
# nltk.download('stopwords')

# some definitions
stopWords = get_stop_words('en')  # list of stopwords/english PyPl
# stopWords = set(stopwords.words('english')) # list of stopwords/english NLTK
tokenizer = nltk.tokenize.RegexpTokenizer(r'\w+')  # regex tokenization


class TextParser:

    # removes stopwords from list of words
    def removeStopWords(self, words):
        clean_words = [w for w in words if w not in stopWords]
        return clean_words

    # returns tokenized words
    def tokenizeWords(self, words_str):
        words = str(words_str.lower())
        return tokenizer.tokenize(words)

    # creates a dictionary of words in a document - one at a time
    def createDictionary(self, input_file, output_file):
        dictionary = Dictionary()
        for line in open(input_file, 'r', encoding='utf-8', errors='ignore'):
            words = self.tokenizeWords(line)
            words = self.removeStopWords(words)
            dictionary.add_documents([words])
        self.saveDictionary(dictionary, output_file)
        return dictionary

    # save [texts] in Matrix Market format
    def createMMCorpora(self, dictionary, texts):
        corpus = [dictionary.doc2bow(text) for text in texts]
        corpora.mmcorpus.MmCorpus.serialize('files/oi.mm', corpus)

    # test dictionary
    def playDic(self, dictionary, texts):
        corpus = [dictionary.doc2bow(text) for text in texts]
        print('Corpus: ', corpus)

    # creates a dictionary of words in a document - one at a time
    def removeWordCount(self, words, cutoff):
        clean_frequency = dict()
        for key, value in words.items():
            if value > cutoff:
                clean_frequency[key] = value
            else:
                pass
        return clean_frequency

    # creates a dictionary with word frequency of corpus
    def frequencyCounter(self, input_file):
        frequency_words = defaultdict(int)
        for line in open(input_file, 'r', encoding='utf-8', errors='ignore'):
            words = self.tokenizeWords(line)
            words = self.removeStopWords(words)
            for word in words:
                frequency_words[word] += 1
        return frequency_words

    # saves dictionary for later use
    def saveDictionary(self, dictionary, output_file):
        print('Dictionary: ', dictionary.token2id)
        dictionary.save(output_file)

    # loads dictionary (id2word)
    def loadDictionary(self, dict_path):
        dic = corpora.Dictionary.load(dict_path)
        # print('#Dictionary# ', dic.token2id)
        return dic