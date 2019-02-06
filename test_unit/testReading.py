from utilities.fileOperations import FileManipulation
from utilities.textProcessing import TextParser
from utilities.ldaTools import LdaOperator

import os


fm = FileManipulation()
tp = TextParser()
ld = LdaOperator()

doc_folder = 'train'
doc_list = fm.doclist_multifolder(doc_folder)


_loc = 'C:\\Users\\terry\\Documents\\Programming\\PyCharmProjects\\TopicTransformation\\files\\output\\'
model = ld.loadLDAModel(_loc+'lda_m.model')
dic = tp.loadDictionary(_loc+'test.d')

text = "I am a text with a lot of word on it system computer terry infrastructure"
text2 = ['human', 'machine', 'interface', 'considers', 'state', 'undesirable',
         'unnecessary', 'harmful', 'instead', 'promotes', 'stateless',
         'society', 'anarchy', 'seeks', 'diminish', 'even', 'abolish',
         'authority', 'conduct', 'human', 'corey', 'cogdell', 'born',
         'september', '2', '1986', 'selection', 'placed', 'first', 'junior',
         'women', 's', 'trap', 'competition', 'day', 'made', 'national',
         'team', 'score',  'also', 'placed', 'third', 'computer', 'systems',
         'humans', 'industry']

# for doc in doc_list:
#     print('Document: ', doc)
#     exit()

# for doc in doc_list:
#     text = fm.readFile(doc)
#     text = tp.cleanText(text)
#     file_path = doc.split('\\')
#     label = file_path[-2]
#     print('DOC_PATH:', doc)
#     print('CLASS: ', label)
#     print('FILE_PATH: ', file_path)
#     print('DOC_TEXT: ', text)
#     print()