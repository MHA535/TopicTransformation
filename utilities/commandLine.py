import argparse
import distutils.util as util


class CommandLine:
    input_folder = None
    output_folder = None
    output_filename = None
    parser_type = None

    # constructor for parameters
    def __init__(self):
        parser = self.commandLineParameters()
        args = parser.parse_args()
        self.input_folder = args.in_f
        self.output_folder = args.on_f
        self.save_dict = args.tr_flag
        self.load_dict = args.dic_fo

    # parameter list for command line
    def commandLineParameters(self):
        parser = argparse.ArgumentParser(description="BSD_Parser - Extract Synset information from documents")
        parser.add_argument('--input', type=str, action='store', dest='in_f', metavar='<folder>', required=True,
                            help='input folder to read document(s)')
        parser.add_argument('--output', type=str, action='store', dest='on_f', metavar='<folder>', required=False,
                            help='output folder to write document(s)')
        parser.add_argument('--train', type=util.strtobool, action='store', dest='tr_flag', metavar='<variable>', required=True,
                            help='[Optional] Generates dictionary file from text-corpus', choices=[True, False])
        parser.add_argument('--dict', type=str, action='store', dest='dic_fo', metavar='<file>', required=False,
                            help='File absolute path  for the dictionary file')
        return parser