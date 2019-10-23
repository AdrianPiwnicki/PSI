class FileManager:
    def __init__(self, file_name):
        self.file_name = file_name

    def read_file(self):
        op = open(self.file_name, 'r', encoding='utf-8')
        rd = op.read()
        op.close()
        return rd

    def update_file(self, text_data):
        op = open(self.file_name, 'a', encoding='utf-8')
        op.write(text_data)
        op.close()
