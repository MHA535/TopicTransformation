import nltk
import errno
from nltk.corpus import stopwords
from stop_words import get_stop_words
from collections import defaultdict
from gensim.corpora import Dictionary
from gensim import corpora

# in case these libraries are not installed
nltk.download('punkt')
nltk.download('stopwords')

# some definitions
stopWords = get_stop_words('en')  # list of stopwords/english PyPl
# stopWords = set(stopwords.words('english')) # list of stopwords/english NLTK
tokenizer = nltk.tokenize.RegexpTokenizer(r'\w+')  # regex tokenization


class TextParser:

    # removes stopwords from list of words
    def removeStopWords(self, words):
        words = [w for w in words if w not in stopWords]
        return words

    # returns tokenized words
    def tokenizeWords(self, words_str):
        words = str(words_str.lower())
        return tokenizer.tokenize(words)

    # consolidates all pre-processing for words
    def cleanText(self, words):
        parsed_words = self.tokenizeWords(words)
        parsed_words = self.removeStopWords(parsed_words)
        return parsed_words

    # creates a dictionary of words in a document - one at a time
    def createDictionary(self, input_file, output_file):
        dictionary = Dictionary(prune_at=6000000)
        for line in open(input_file, 'r', encoding='utf-8', errors='ignore'):
            words = self.tokenizeWords(line)
            words = self.removeStopWords(words)
            dictionary.add_documents([words])
        self.saveDictionary(dictionary, output_file)
        return dictionary

    # save [texts] in Matrix Market format
    def createMMCorpus(self, corpus, corpus_name):
        try:
            corpora.mmcorpus.MmCorpus.serialize(corpus_name, corpus)
            print('SUCCESS: Corpus %s in MM format saved' % corpus_name)
        except IOError:
            print('IO ERROR: Cannot save corpus %s' % corpus_name)
            exit()

    # Loads corpus in MM format
    def loadMMCorpus(self, corpus_path):
        try:
            corpus_mm = corpora.mmcorpus.MmCorpus(corpus_path)
            print('SUCCESS: Load MM Corpus %s' % corpus_path)
            return corpus_mm
        except IOError:
            print('ERROR: Cannot load %s MM format' % corpus_path)
            exit()

    # test dictionary
    def playDic(self, dictionary, texts):
        corpus = [dictionary.doc2bow(text) for text in texts]
        print('Corpus: ', corpus)

    # saves dictionary for later use
    def saveDictionary(self, dictionary, output_file):
        try:
            dictionary.save(output_file)
            # print('Dictionary: ', dictionary.token2id)
            print('SUCCESS: Dictionary %s in .d format saved' % output_file)
        except IOError:
            print('IO ERROR: Cannot save dictionary %s' % output_file)
            exit()

    # loads dictionary (id2word)
    def loadDictionary(self, dict_path):
        try:
            dic = corpora.Dictionary.load(dict_path)
            print('SUCCESS: Load dictionary %s' % dict_path)
            return dic
        except IOError:
            print('ERROR: Cannot load dictionary %s' % dict_path)
            exit()

    # creates a dictionary with word frequency of corpus
    def frequencyCounter(self, input_file):
        frequency_words = defaultdict(int)
        for line in open(input_file, 'r', encoding='utf-8', errors='ignore'):
            words = self.tokenizeWords(line)
            words = self.removeStopWords(words)
            for word in words:
                frequency_words[word] += 1
        return frequency_words

    # creates a dictionary of words in a document - one at a time
    def removeWordCount(self, words, cutoff):
        clean_frequency = dict()
        for key, value in words.items():
            if value > cutoff:
                clean_frequency[key] = value
            else:
                pass
        return clean_frequency
