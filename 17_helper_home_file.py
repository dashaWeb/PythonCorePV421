
with open('17_file_/my_read.txt') as file:
    lines = file.readlines()

position = None
for i in range(len(lines)):
    if lines[i].find(',') == -1:
        position = i
with open('17_file_/task4.txt','w') as file:
    counter = 0
    for line in lines:
        file.write(line)
        if position == counter:
            file.write('*'*12+'\n')
        counter+=1
    if position == None:
        if line[-1] != '\n':
            file.write('\n')
        file.write('*'*12)


text = 'fkjsdklfj*lkfjalksf&kdjvslk*djhfj&'
text = text.replace('*','~').replace('&','*').replace('~','&')
print(text)