# відкрити файл
# прочитати файл
# записати у файл
# закрити файл


#  Read file
# url = r"C:\Users\konopelko\Desktop\PythonCorePV421\17_file_\my_read.txt"

# fileHandler = open(url)
# print(type(fileHandler),fileHandler)
# text = fileHandler.read()
# print(text,type(text),sep='\n')
# # fileHandler.close()

# # fileHandler = open(url)

# fileHandler.seek(0)
# print('way 2 read(15)')
# text = fileHandler.read(15)
# print(text,type(text),sep='\n')

# fileHandler.seek(0)
# print('way 2 readline(15)')
# text = fileHandler.readline()
# print(text,type(text),sep='\n')


# fileHandler.seek(0)
# for line in fileHandler:
#     print(line)

# fileHandler.seek(0)
# text = fileHandler.readlines()
# print(text,type(text),sep='\n')

# fileHandler.close()

# # try:
# #     file = open(url)
# #     test = 5/0
# # except Exception as ex:
# #     print(ex)
# # finally:
# #     file.close()

# with open(url) as file:
#     print(file.read())

# ------------- Write File

# url = r"17_file_/my_write.txt"
# # word = 'World'
# # with open(url,'a') as file:
# #     file.write(word)

# # lines = [
# #     'Integer at nulla bibendum felis laoreet consequat.',
# #     'Sed in mi non ante congue bibendum.',
# #     'Mauris ultricies mi et nisi posuere tristique.'
# # ]
# # # with open(url,'w') as file:
# # #     for line in lines:
# # #         file.write(line+'\n')
# # with open(url,'w') as file:
# #     file.writelines(lines)


# # line = 'Сонце, Хмара, Дощ'
# # with open(url,'w',encoding='utf-8') as file:
# #     file.write(line)

# with open(url,'r',encoding='utf-8') as file:
#     print(file.read())


# def readAllFile(url):
#     with open(url) as file:
#         return file.read()
    
# print(readAllFile('17_file_/my_read.txt'))

# def writeAllLines(name,lines,mode = 'w'):
#     with open('17_file_/' + name + '.txt', mode) as file:
#         file.writelines(lines)

# writeAllLines('test_write',[
#     'Line 1 \n',
#     'Line 2 \n',
#     'Line 3 \n',
# ])

# writeAllLines('test_write',[
#     'Line 4 \n',
#     'Line 5 \n',
#     'Line 6 \n',
# ],mode='a')


url = r'res.txt'
with open(url) as file:
    lines = file.read()

words = lines.split(' ')

def writeWords(url, words):
    with open(url,'w') as file:
        for word in words:
            if len(word)>=7:
                file.write(word+'\n')

writeWords(r'words.txt',words)