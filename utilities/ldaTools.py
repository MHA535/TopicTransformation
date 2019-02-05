from gensim.models.ldamodel import LdaModel
from utilities.textProcessing import TextParser


class Lda_Operator:

    # trains a lda model
    def trainLDAModel(self, corpus_mm, dictionary, dimensions, update, chunks, epochs):
        lda_model = LdaModel(corpus=corpus_mm, id2word=dictionary, num_topics=dimensions,
                             update_every=update, chunksize=chunks, passes=epochs)
        # lda_model.save('LDA_Model.model')
        return lda_model

    # creates a a file (one-doc-line) based on features from LDA model with label
    def ldaDocVector(self, input_corpus, output_docvec, lda_model, dic):
        text_parser = TextParser()
        DELIMITER = '#'
        vector_corpus = open(output_docvec, 'w+')
        for line in open(input_corpus, 'r', encoding='utf-8'):
            text, label = str(line).split(DELIMITER)
            words = text_parser.tokenizeWords(text)
            words = text_parser.removeStopWords(words)
            feature_values = self.__documentToLDA(words, lda_model, dic)
            doc_representation = feature_values+label
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
        feature_values=''
        DELIMITER = ','
        for item in lda_doc:
            feat, val = item
            feature_values += str(val)+DELIMITER
        return feature_values
