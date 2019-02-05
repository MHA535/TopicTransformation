# import
import os
import sys
import logging

# python module absolute path
pydir_name = os.path.dirname(os.path.abspath(__file__))
ppydir_name = os.path.dirname(pydir_name)

# python path definition
sys.path.append(os.path.join(os.path.dirname(__file__), os.path.pardir))

# local-imports
from utilities.commandLine import CommandLine
from utilities.fileOperations import FileManipulation
from utilities.textProcessing import TextParser
# from utilities.ldaComponent import MyCorpus

# logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

if __name__ == '__main__':
    params = CommandLine()  # command line parameter validation
    tp = TextParser()

    tmp =[['human', 'interface', 'computer'],
    ['survey', 'macaco', 'computer', 'system', 'response', 'time']]

    # selecting type of execution
    dict_flag = params.save_dict
    in_fname = os.path.join(ppydir_name, params.input_folder)

    # Save or Load dictionary
    if dict_flag:
        ou_fname = os.path.join(ppydir_name, params.output_folder)
        dic = tp.createDictionary(in_fname, ou_fname)
    else:
        di_fname = os.path.join(ppydir_name, params.load_dict)
        dic = tp.loadDictionary(di_fname)
        
    # input has to be one-document per line
    # apply  doc2bow in each document from input
    # run LDA model





