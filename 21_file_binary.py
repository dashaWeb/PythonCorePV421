directory = '20_file_binary'

filename_t = 'file.txt'
filename_b = 'file.dat'


users = [{
    "first_name": "Agosto",
    "last_name": "Valerio",
    "email": "avalerio0@chron.com",
    "birthday": "04.05.2023",
    "average": 6.4
}, {
    "first_name": "Merla",
    "last_name": "Tuminini",
    "email": "mtuminini1@chicagotribune.com",
    "birthday": "20.09.2023",
    "average": 3.9
}, {
    "first_name": "Tabbie",
    "last_name": "Jennick",
    "email": "tjennick2@webeden.co.uk",
    "birthday": "30.04.2023",
    "average": 4.3
}, {
    "first_name": "Bridgette",
    "last_name": "Basezzi",
    "email": "bbasezzi3@businesswire.com",
    "birthday": "21.01.2023",
    "average": 7.9
}, {
    "first_name": "Peggie",
    "last_name": "Ritchley",
    "email": "pritchley4@epa.gov",
    "birthday": "20.03.2022",
    "average": 9.4
}, {
    "first_name": "Ally",
    "last_name": "Hayers",
    "email": "ahayers5@acquirethisname.com",
    "birthday": "04.03.2022",
    "average": 4.9
}, {
    "first_name": "Megan",
    "last_name": "Feeley",
    "email": "mfeeley6@stanford.edu",
    "birthday": "22.03.2022",
    "average": 2.1
}, {
    "first_name": "Jeannie",
    "last_name": "Labbey",
    "email": "jlabbey7@digg.com",
    "birthday": "24.11.2023",
    "average": 7.7
}, {
    "first_name": "Cesaro",
    "last_name": "Dunford",
    "email": "cdunford8@seesaa.net",
    "birthday": "08.04.2024",
    "average": 8.5
}, {
    "first_name": "Filberte",
    "last_name": "Giovannazzi",
    "email": "fgiovannazzi9@newyorker.com",
    "birthday": "03.02.2022",
    "average": 4.0
}]

# import pickle

# with open(f'{directory}/{filename_t}','w') as file:
#     file.write(str(users))

# with open(f'{directory}/{filename_b}','wb') as file:
# #    print(pickle.dumps(users))
#     pickle.dump(users,file)

# with open(f'{directory}/{filename_b}','rb') as file:
#     res_users = pickle.load(file)
#     print(type(res_users))
#     for user in res_users:
#         print(type(user), user)

def printUser(users):
    for user in users:
        print(user)
    print('*'*100)


printUser(users)

users_filter = list(filter(lambda x: int(x['birthday'].split('.')[0]) > 15, users))
printUser(users_filter)

def userMap(user):
    if int(user['birthday'].split('.')[0]) <= 15:
        user['email'] += '*'
    return user

users_map = list(map(userMap,users))
printUser(users_map)


users_sort = sorted(users, key=lambda x: x['average'])
printUser(users_sort)
