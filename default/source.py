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
from utilities.fileOperations import FileManipulation
from utilities.corpusDoc2Bow import MyCorpus
from utilities.ldaTools import LdaOperator

# logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

if __name__ == '__main__':
    params = CommandLine()  # command line parameter validation
    tp = TextParser()  # text operations
    fm = FileManipulation()  # file operations
    lda_operator = LdaOperator()

    # Execution selection
    dict_flag = params.tr_flag
    in_fname = os.path.join(ppydir_name, params.input_folder)
    ou_fname = os.path.join(ppydir_name, params.output_folder)
    lda_flag = params.lda_flag
    lda_file = os.path.join(ppydir_name, params.lda_model)
    lda_usage = params.lda_use

    if dict_flag:  # Save dictionary and MM
        dic = tp.createDictionary(in_fname, ou_fname)
        corpus_mm = MyCorpus(in_fname, dic)
        tp.createMMCorpus(corpus_mm, params.corpus_mm)
    else:  # Load dictionary and MM
        corpus_path = os.path.join(ppydir_name, params.corpus_mm)
        dic = tp.loadDictionary(ou_fname)
        corpus_mm = tp.loadMMCorpus(corpus_path)

    # LDA - Step
    if lda_flag:  # LDA Model Train
        dimensions = 300
        update = 1
        chunks = 10000
        epochs = 1
        random = 1
        min_prob = 0.0  # if default value is used (0.1), topics < min_prob are not presented
        multi_core = True  # single or multiple cores LDA
        worker_num = 4  # if running multicore set number of cores

        start_time = time.monotonic()  # overall runtime start
        lda_model = lda_operator.trainLDAModel(corpus_mm, dic, dimensions, update, chunks, epochs, random, min_prob,
                                               multi_core, worker_num)
        print('SUCCESS: LDA Model built in %s' % (timedelta(seconds=time.monotonic() - start_time)))
        lda_operator.saveLDAModel(lda_model, lda_file)
    else:  # LDA Model Load
        lda_model = lda_operator.loadLDAModel(lda_file)

    # Apply LDA
    if lda_usage:  # Either from Produced/Loaded LDA Model/Dictionary
        print('Applying LDA to (Un)seen documents')
        doc_read = os.path.join(ppydir_name, params.document_read)
        doc_write = os.path.join(ppydir_name, params.document_write)
        doc_list = fm.doclist_multifolder(doc_read)
        lda_operator.ldaDocVector(doc_list, doc_write, lda_model, dic)
    else:
        print('LDA - Not applied. Exiting program')
        exit()
