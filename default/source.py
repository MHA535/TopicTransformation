# import
import os
import sys
import logging
import time
from datetime import timedelta

# python module absolute path
pydir_name = os.path.dirname(os.path.abspath(__file__))
ppydir_name = os.path.dirname(pydir_name)

# python path definition
sys.path.append(os.path.join(os.path.dirname(__file__), os.path.pardir))

# local-imports
from utilities.commandLine import CommandLine
from utilities.textProcessing import TextParser
from utilities.corpusDoc2Bow import MyCorpus
from utilities.ldaTools import Lda_Operator

# logging
# logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

if __name__ == '__main__':
    params = CommandLine()  # command line parameter validation
    tp = TextParser()

    # selecting type of execution
    dict_flag = params.save_dict
    in_fname = os.path.join(ppydir_name, params.input_folder)
    ou_fname = os.path.join(ppydir_name, params.output_folder)

    if dict_flag:  # Save dictionary and MM
        dic = tp.createDictionary(in_fname, ou_fname)
        corpus_mm = MyCorpus(in_fname, dic)
        tp.createMMCorpus(corpus_mm, params.corpus_mm)
    else:  # Load dictionary and MM
        corpus_path = os.path.join(ppydir_name, params.corpus_mm)
        dic = tp.loadDictionary(ou_fname)
        corpus_mm = tp.loadMMCorpus(corpus_path)

    # Train LDA phase - Parameters
    document = "A survey of user opinion of computer system response time"
    lda_operator = Lda_Operator()
    dimensions = 10
    update = 1
    chunks = 2
    epochs = 1

    # overall runtime start
    start_time = time.monotonic()
    lda_model = lda_operator.trainLDAModel(corpus_mm, dic, dimensions, update, chunks, epochs)
    print('LDA Model built in %s' % (timedelta(seconds=time.monotonic() - start_time)))

    # Building Bulk file in <1-doc-line,label>
    lda_operator.documentVector(params.document_read, params.document_write, lda_model, dic)

    # doc_bow = dic.doc2bow(document.split())
    # doc_lda = lda_model[doc_bow]
    # print('DOC_LDA-TYPE: ', type(doc_lda[0]))
    # f, v = doc_lda[0]
    # print('Feature: ', f, type(f))
    # print('Value: ', v, type(v))
    # print('DOC_LDA: ', doc_lda)





