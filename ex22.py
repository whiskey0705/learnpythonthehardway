# 字符串格式化
# fomatter = '{} {} {} \n'
# print(fomatter.format(123, 'abc', True))

# name = 'fomatter'
# print(f'My name is {name} \n') # 注意f和{}

# 字符串换行
# s = 'my name is \n whiskey'
# print(s)
# multi_line = '''
# Creating a life that reflects your values 
# and satisfies your soul is a rare achievement. 
# To invent your own life's meaning is not easy, 
# but it is still allowed, 
# and I think you'll be happier for the trouble.
# '''
# print(multi_line)

# 读写文件
from sys import argv
script, file_name = argv

cur_file = open(file_name)
print(type(cur_file))

data = cur_file.read()
print(data)

# 写入文件
to_file_name = input('enter a filename')
to_file = open(to_file_name, 'w')
to_file.write(data)

cur_file.close()
to_file.close()

# 逐行读取
newfile = open(to_file_name)

newfile.seek(0)

print(newfile.readline())
print(newfile.readline())
print(newfile.readline())