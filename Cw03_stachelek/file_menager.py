class FileMenager:
    def __init__(self, file_name):
        self.file_name = file_name

    def read_file(self):
        open_txt = open(self.file_name, 'r', encoding='utf-8')
        read_txt = open_txt.read()
        open_txt.close()
        return read_txt

    def update_file(self, text_data):
        open_txt = open(self.file_name, 'a', encoding='utf-8')
        update_txt = open_txt.write(text_data)
        open_txt.close()
        return update_txt
