import json
# student = {
#     'name': 'Ivan',
#     'age': 16,
#     'group': 'PB421'
# }

# with open('19_files/student.json','w') as file:
#     file.write(json.dumps(student))


# with open('19_files/student.json','r') as file:
#     student = file.read()
# print(student, type(student))

# student = json.loads(student)
# print(student, type(student))
# print(student['name'], type(student))


# student = {
#     'name': 'Ivan',
#     'age': 16,
#     'group': 'PB421'
# }
# student_2 = dict(name='Pavlo', age=17, group='PV421')
# list_student = [
#     student,
#     student_2,
#     {
#         'name':'Igor',
#         'age':22,
#         'group':'PV421'
#     }
# ]

# with open('19_files/list_students.json','w') as file:
#     file.write(json.dumps(list_student))

# with open('19_files/list_students.json','r') as file:
#     list_student = json.loads(file.read())

# print(list_student[0]['name'])
# list_student = list(list_student)
# list_student.append({
#     'name':'Artur',
#     'age':22,
#     'group':None
# })

# print(list_student)
# with open('19_files/list_students.json','w') as file:
#     file.write(json.dumps(list_student))



import requests

# currency = requests.get('https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=5')


# currency = requests.get('https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=5').content
# currency = json.loads(currency)
# print(type(currency), currency)
# print(type(currency[0]), currency[0])
# print(type(currency[0]['sale']), currency[0]['sale'])

# import requests
# currency = requests.get('https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=5').json()
# print(type(currency), currency)
# print(type(currency[0]), currency[0])
# print(type(currency[0]['sale']), currency[0]['sale'])

# url = 'https://natureconservancy-h.assetsadobe.com/is/image/content/dam/tnc/nature/en/photos/t/n/tnc_11065968.jpg?crop=0%2C2%2C1920%2C1275&wid=828&hei=550&scl=2.318840579710145'

# image = requests.get(url).content
# with open('19_files/winter.jpg','wb') as file:
#     file.write(image)
# print(image)

# url = 'https://pixabay.com/api/?key=14304821-db198647e0592cf253911c94a&q=orange+flowers&image_type=photo&pretty=true&category=animals'

# images = requests.get(url).json()['hits']
# counter = 1
# for img in images:
#     picture = requests.get(img['webformatURL']).content
#     with open(f'19_files/img/{counter}.jpg','wb') as file:
#         file.write(picture)
#     counter+=1
