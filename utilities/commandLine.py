import argparse
import distutils.util as util
import csv
import pandas as pd  # Optional but recommended for handling large CSV files

class CommandLine:
    input_folder = None
    output_folder = None
    tr_flag = None
    corpus_mm = None
    document_read = None
    document_write = None
    lda_flag = None
    lda_model = None
    lda_use = None
    csv_file = None  # Add this to store CSV file path

    # constructor for parameters
    def __init__(self):
        parser = self.commandLineParameters()
        args = parser.parse_args()
        self.input_folder = args.in_f
        self.output_folder = args.on_f
        self.tr_flag = args.tr_flag
        self.corpus_mm = args.mm_f
        self.document_read = args.dr_f
        self.document_write = args.dw_f
        self.lda_flag = args.lda_flag
        self.lda_model = args.lda_m
        self.lda_use = args.lda_u
        self.csv_file = args.csv_f  # Capture the CSV file path

        # After parsing arguments, you can now process the CSV file
        if self.csv_file:
            self.process_csv()

    # parameter list for command line
    def commandLineParameters(self):
        parser = argparse.ArgumentParser(description="BSD_Parser - Extract Synset information from documents")
        parser.add_argument('--input', type=str, action='store', dest='in_f', metavar='<folder>', required=True,
                            help='input folder to read document(s)')
        parser.add_argument('--output', type=str, action='store', dest='on_f', metavar='<folder>', required=False,
                            help='output folder to write document(s)')
        parser.add_argument('--train', type=util.strtobool, action='store', dest='tr_flag', metavar='<variable>', required=True,
                            help='Generates dictionary file from text-corpus', choices=[True, False])
        parser.add_argument('--mmf', type=str, action='store', dest='mm_f', metavar='<folder>', required=False,
                            help='Matrix Market - corpus.mm - absolute path location')
        parser.add_argument('--docr', type=str, action='store', dest='dr_f', metavar='<folder>', required=False,
                            help='DocRead - Bulk file to apply LDA topics - 1-doc-line <doc#label>')
        parser.add_argument('--docw', type=str, action='store', dest='dw_f', metavar='<folder>', required=False,
                            help='DocWrite - Bulk file (CSV) with LDA topics and class - 1-doc-line')
        parser.add_argument('--lda', type=util.strtobool, action='store', dest='lda_flag', metavar='<variable>', required=True,
                            help='Save (True) or Load (False) LDA Model wrt to --ldam', choices=[True, False])
        parser.add_argument('--ldam', type=str, action='store', dest='lda_m', metavar='<folder>', required=False,
                            help='Location for LDA Model to be saved or loaded')
        parser.add_argument('--ldau', type=util.strtobool, action='store', dest='lda_u', metavar='<variable>', required=True,
                            help='[True] - Apply LDA model to documents on --docr. [False] - Exit program', choices=[True, False])
        # New argument for CSV file
        parser.add_argument('--csv', type=str, action='store', dest='csv_f', metavar='<file>', required=False,
                            help='CSV file containing documents with source and page content')

        return parser

    # Method to process the CSV file
    def process_csv(self):
        try:
            # Using pandas to read the CSV file
            df = pd.read_csv(self.csv_file)
            # Assuming columns are named 'Source' and 'Page_Content'
            for index, row in df.iterrows():
                source = row['Source']
                page_content = row['Page_Content']
                print(f"Source: {source}, Page Content: {page_content}")
            
            # Alternatively, you can use csv module:
            # with open(self.csv_file, mode='r', encoding='utf-8') as file:
            #     reader = csv.DictReader(file)
            #     for row in reader:
            #         source = row['Source']
            #         page_content = row['Page_Content']
            #         print(f"Source: {source}, Page Content: {page_content}")
        except Exception as e:
            print(f"Error processing CSV file: {e}")

if __name__ == "__main__":
    CommandLine()
