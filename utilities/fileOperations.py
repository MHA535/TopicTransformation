import os

class FileManipulation:
#handles file manipulation

    # creates list of documents in many folders
    def doclist_multifolder(self, folder_name):
        input_file_list = []
        for roots, dir, files in os.walk(folder_name):
            for file in files:
                file_uri = os.path.join(roots, file)
                if file_uri.endswith('txt'): input_file_list.append(file_uri)
        return input_file_list
