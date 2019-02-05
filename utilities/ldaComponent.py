from gensim import corpora
from utilities.textProcessing import TextParser
from utilities.commandLine import CommandLine


class MyCorpus(object):

    def __init__(self, input_file, dictionary):
        self.input_file = input_file
        self.dictionary = dictionary
    # input_file has to be in one-document per line format

    def __iter__(self):
        text_parser = TextParser()
        for line in open(self.input_file, 'r', encoding='utf-8'):
            words = text_parser.tokenizeWords(line)
            words = text_parser.removeStopWords(words)
            yield self.dictionary.doc2bow(words)
