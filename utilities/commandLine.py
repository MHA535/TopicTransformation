import argparse
import distutils.util as util


class CommandLine:
    input_folder = None
    output_folder = None
    save_dict = None
    corpus_mm = None
    document_read = None
    document_write = None

    # constructor for parameters
    def __init__(self):
        parser = self.commandLineParameters()
        args = parser.parse_args()
        self.input_folder = args.in_f
        self.output_folder = args.on_f
        self.save_dict = args.tr_flag
        self.corpus_mm = args.co_f
        self.document_read = args.dr_f
        self.document_write = args.dw_f

    # parameter list for command line
    def commandLineParameters(self):
        parser = argparse.ArgumentParser(description="BSD_Parser - Extract Synset information from documents")
        parser.add_argument('--input', type=str, action='store', dest='in_f', metavar='<folder>', required=True,
                            help='input folder to read document(s)')
        parser.add_argument('--output', type=str, action='store', dest='on_f', metavar='<folder>', required=False,
                            help='output folder to write document(s)')
        parser.add_argument('--train', type=util.strtobool, action='store', dest='tr_flag', metavar='<variable>', required=True,
                            help='[Optional] Generates dictionary file from text-corpus', choices=[True, False])
        parser.add_argument('--corpus', type=str, action='store', dest='co_f', metavar='<folder>', required=False,
                            help='Matrix Market - corpus.mm - absolute path location')
        parser.add_argument('--docr', type=str, action='store', dest='dr_f', metavar='<folder>', required=False,
                            help='DocRead - Bulk file to apply LDA topics - 1-doc-line <doc#label>')
        parser.add_argument('--docw', type=str, action='store', dest='dw_f', metavar='<folder>', required=False,
                            help='DocWrite - Bulk file (CSV) with LDA topics and class - 1-doc-line')
        return parser