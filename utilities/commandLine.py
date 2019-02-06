import argparse
import distutils.util as util


class CommandLine:
    input_folder = None
    output_folder = None
    tr_flag = None
    corpus_mm = None
    document_read = None
    document_write = None
    lda_flag = None
    lda_model = None

    # constructor for parameters
    def __init__(self):
        parser = self.commandLineParameters()
        args = parser.parse_args()
        self.input_folder = args.in_f
        self.output_folder = args.on_f
        self.tr_flag = args.tr_flag
        self.corpus_mm = args.co_f
        self.document_read = args.dr_f
        self.document_write = args.dw_f
        self.lda_flag = args.lda_flag
        self.lda_model = args.lda_m

    # parameter list for command line
    def commandLineParameters(self):
        parser = argparse.ArgumentParser(description="BSD_Parser - Extract Synset information from documents")
        parser.add_argument('--input', type=str, action='store', dest='in_f', metavar='<folder>', required=True,
                            help='input folder to read document(s)')
        parser.add_argument('--output', type=str, action='store', dest='on_f', metavar='<folder>', required=False,
                            help='output folder to write document(s)')
        parser.add_argument('--train', type=util.strtobool, action='store', dest='tr_flag', metavar='<variable>', required=True,
                            help='Generates dictionary file from text-corpus', choices=[True, False])
        parser.add_argument('--corpus', type=str, action='store', dest='co_f', metavar='<folder>', required=False,
                            help='Matrix Market - corpus.mm - absolute path location')
        parser.add_argument('--docr', type=str, action='store', dest='dr_f', metavar='<folder>', required=False,
                            help='DocRead - Bulk file to apply LDA topics - 1-doc-line <doc#label>')
        parser.add_argument('--docw', type=str, action='store', dest='dw_f', metavar='<folder>', required=False,
                            help='DocWrite - Bulk file (CSV) with LDA topics and class - 1-doc-line')
        parser.add_argument('--lda', type=util.strtobool, action='store', dest='lda_flag', metavar='<variable>', required=True,
                            help='Save (True) or Load (False) LDA Model wrt to --lda', choices=[True, False])
        parser.add_argument('--ldam', type=str, action='store', dest='lda_m', metavar='<folder>', required=False,
                            help='Location for LDA Model to be saved or loaded')
        return parser