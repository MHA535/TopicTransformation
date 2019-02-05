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

    # reads an entire file and returns its text
    def read(self, file_name):
        text = ""
        try:
            f = open(file_name, errors="ignore")
            text = f.read()
            f.close()
        except IOError as exc:
            raise ("problem reading file: " + file_name)
        return text
