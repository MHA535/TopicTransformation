# import
import os
import sys

# python module absolute path
pydir_name = os.path.dirname(os.path.abspath(__file__))
ppydir_name = os.path.dirname(pydir_name)

# python path definition
sys.path.append(os.path.join(os.path.dirname(__file__), os.path.pardir))

# local-imports
from utilities.commandLine import CommandLine
from utilities.fileOperations import FileManipulation
from utilities.textProcessing import TextParser

if __name__ == '__main__':
    # params = CommandLine()  # command line parameter validation
    # fio = FileManipulation()
    tp = TextParser()

    t = tp.removeStopWords(['i','am','a','potato'])
    print(t)

    # in/ou relative location
    # in_fname = os.path.join(ppydir_name, params.input_folder)
    # ou_fname = os.path.join(ppydir_name, params.output_folder)