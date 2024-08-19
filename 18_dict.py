
student = {
    'name': 'Ivan',
    'age': 16,
    'group': 'PB421'
}
student_2 = dict(name='Pavlo', age=17, group='PV421')
print(type(student), student)
print(type(student_2), student_2)

print(student['name'])
# print(student['surname']) Error
print(student.get('surname'))
print(student.setdefault('name'))
print(student.setdefault('surname'))
print(student)

student.update([('name', 'Sasha'), ('birtday', '24.04.2005')])
print(student)

student['group'] = 'PV421'
print(student)
student['rating'] = 9.5
print(student)

del student['birtday']
print(student)

student.popitem()
print(student)

student.pop('surname')
print(student)

for key in student.keys():
    print(key, '\t')
print()

for value in student.values():
    print(value, '\t')
print()

for key, value in student.items():
    print(key, '-'*15, value,)
print()


clone = student.copy()
print('clone  --> ',clone)
print('origin --> ',student)


# for key in clone.keys():
#     info = input(f'enter {key} ')
#     clone[key] = info

print('clone  --> ',clone)
print('origin --> ',student)


# student.clear()
# print(student)

clone = student.fromkeys(student.keys())
print('clone  --> ',clone)
print('origin --> ',student)


# for key in clone.keys():
#     info = input(f'enter {key} ')
#     clone[key] = info

print('clone  --> ',clone)
print('origin --> ',student)

list_student = [
    student,
    student_2,
    {
        'name':'Igor',
        'age':22,
        'group':'PV421'
    }
]

print(list_student[0])