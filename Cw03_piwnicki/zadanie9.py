from Cw03_piwnicki.file_manager import FileManager
przyklad = FileManager('przykład.txt')
przyklad.update_file('coś_tam')
print(przyklad.read_file())
