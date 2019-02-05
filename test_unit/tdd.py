import os
import sys
import unittest

from utilities.fileOperations import FileManipulation
from utilities.commandLine import CommandLine


class TestTopicTransformation(unittest.TestCase):

    # reading file
    def test_read_file(self):
        fm = FileManipulation()
        self.assertEqual('I am a file', fm.read('file_01.txt'))

