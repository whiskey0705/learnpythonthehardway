from sys import argv

script, filename = argv

txt = open(filename) # txt是一个文件对象（file object）

print(f'Here\'s your file {filename}:')
print(txt.read())

# print('Type the filename again:')
# file_again = input('> ')

file_again = input('Type the filename again: >')

txt_again = open(file_again)

print(txt_again.read())

txt.close()
txt_again.close()