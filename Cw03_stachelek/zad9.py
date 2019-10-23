from Cw03_stachelek.file_menager import FileMenager


file_menager = FileMenager('text.txt')

print(file_menager.read_file())
file_menager.update_file(" Pythonie.")
print(file_menager.read_file())
