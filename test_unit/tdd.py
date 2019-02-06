import unittest
import os

from utilities.fileOperations import FileManipulation
from utilities.textProcessing import TextParser


class TestTopicTransformation(unittest.TestCase):

    # reading file
    def test_read_file(self):
        fm = FileManipulation()
        self.assertEqual('I am a file', fm.readFile('file_01.txt'))

    # document list - recursive
    def test_doc_list(self):
        fm = FileManipulation()
        docs = fm.doclist_multifolder('train')
        self.assertEqual('train'+os.sep+'A'+os.sep+'d1.txt', docs[0])
        self.assertEqual('train'+os.sep+'B'+os.sep+'d3.txt', docs[2])

    # sub-directory class reading
    def test_subdir_folder(self):
        fm = FileManipulation()
        docs = fm.doclist_multifolder('train')
        file_path = docs[1].split(os.sep)
        self.assertEqual('A', file_path[-2])

    # text cleaner - tokenize and stop word removal
    def test_doc_cleaner(self):
        fm = FileManipulation()
        tp = TextParser()
        file_location = 'train'+os.sep+'B'+os.sep+'d5.txt'
        doc = fm.readFile(file_location)
        text = tp.cleanText(doc)
        self.assertEqual('computer', text[0])
        self.assertEqual('systems', text[2])
        self.assertEqual('potatoes', text[-1])