from gensim.models.ldamodel import LdaModel
from gensim.models.ldamulticore import LdaMulticore
from utilities.textProcessing import TextParser
from utilities.fileOperations import FileManipulation
import os


class LdaOperator:

    # trains a lda model
    def trainLDAModel(self, corpus_mm, dictionary, dimensions, update, chunks, epochs, random=None, min_prob=0.01,
                      multi_core=False, worker_num=3):
        if multi_core:
            lda_model = LdaMulticore(corpus=corpus_mm, id2word=dictionary, num_topics=dimensions,
                                     chunksize=chunks, passes=epochs, random_state=random,
                                     minimum_probability=min_prob, workers=worker_num)
        else:
            lda_model = LdaModel(corpus=corpus_mm, id2word=dictionary, num_topics=dimensions,
                                 update_every=update, chunksize=chunks, passes=epochs, random_state=random,
                                 minimum_probability=min_prob)
        return lda_model

    # creates a a file (one-doc-line) based on features from LDA model with label
    def ldaDocVector(self, input_corpus, output_docvec, lda_model, dic):
        text_parser = TextParser()
        file_manip = FileManipulation()
        SEPARATOR = os.sep  # / for Linux; \\ dor Windows
        SUB_DIR = -2  # position of the subdirectory folder (class name)
        vector_corpus = open(output_docvec, 'w+')
        for file in input_corpus:
            text = file_manip.readFile(file)
            file_path = file.split(SEPARATOR)
            label = file_path[SUB_DIR]
            words = text_parser.cleanText(text)
            feature_values = self.__documentToLDA(words, lda_model, dic)
            doc_representation = feature_values + label + '\n'
            vector_corpus.write(doc_representation)
        vector_corpus.close()
        print('SUCCESS: LDA to Vector completed')

    # parse list of words into list vectors
    def __documentToLDA(self, words, lda_model, dic):
        doc_bow = dic.doc2bow(words)
        doc_lda = lda_model[doc_bow]
        feature_values = self.__ldaVectorHandler(doc_lda)
        # print('#WORDS: ', words)
        # print('#DOC-BOW: ',doc_bow)
        # print('#LDA-Vectors: ', doc_lda)
        return feature_values

    # Extracts the Values for each feature obtained by the LDA_Model
    def __ldaVectorHandler(self, lda_doc):
        feature_values = ''
        SEPARATOR = ','
        for item in lda_doc:
            feat, val = item
            feature_values += str(val) + SEPARATOR
        return feature_values

    # Save LDA model
    def saveLDAModel(self, lda_model, lda_name):
        try:
            lda_model.save(lda_name)
            print('SUCCESS: LDA Model saved: %s' % lda_name)
        except IOError:
            print('ERROR: Cannot save LDA Model: %s' % lda_name)
            exit()

    # loads LDA model
    def loadLDAModel(self, lda_name):
        try:
            lda_model = LdaModel.load(lda_name)
            print('SUCCESS: LDA Model loaded: %s' % lda_name)
            return lda_model
        except IOError:
            print('ERROR: Cannot Load LDA Model: %s' % lda_name)
            exit()
