print('список словарей, которые содержат поля имя, возраст, пол')
print('При помощи переменной persons найдите и сохраните в переменную следующую информацию:')
print('      - Количество всех людей?')
print('      - Сколько мужчин, сколько женщин?')
print('      - Посчитать сколько совершено летних персон')
print('      - Список всех имён')
print('      - 3 самых встречающих имён')
print('      - Вывести все имена мужчин старше 35, имя которого начинается с F')

persons = [
    {
        "name": "Anna",
        "age": 15,
        "gender": "female"
    }, {
        "name": "Malex",
        "age": 16,
        "gender": "male"
    }, {
        "name": "Ganna",
        "age": 17,
        "gender": "female"
    }, {
        "name": "Alex",
        "age": 18,
        "gender": "male"
    }, {
        "name": "Alex",
        "age": 19,
        "gender": "female"
    }, {
        "name": "Alex",
        "age": 20,
        "gender": "male"
    }, {
        "name": "Jane",
        "age": 30,
        "gender": "female"
    }, {
        "name": "Kolya",
        "age": 35,
        "gender": "male"
    },{
        "name": "Victoriya",
        "age": 36,
        "gender": "female"
    },{
        "name": "Feder",
        "age": 37,
        "gender": "male"
    },{
        "name": "Olga",
        "age": 38,
        "gender": "female"
    },{
        "name": "Kolya",
        "age": 39,
        "gender": "male"
    }
]

cnt = len(persons)
n = 0
cnt_f = 0
cnt_m = 0
cnt18 = 0
cnt35 = 0
name35 = list()
sname35 = ''
name_all = ''


while cnt > n:
    if persons[n]['gender'] == 'female':
       cnt_f += 1
    if persons[n]['gender'] == 'male':
       cnt_m += 1    
    if int(persons[n]['age']) > 17:
        cnt18 += 1
    if  int(persons[n]['age']) > 35 and persons[n]['gender'] == 'male' and list(persons[n]['name'])[0] == 'F':
        cnt35 += 1
        name35.append(persons[n]['name'])
        sname35 = sname35 + ' ' + str(persons[n]['name'])
        print(persons[n]['name'])      
    
    name_all = name_all + ' ' + str(persons[n]['name'])
    n += 1



print('Количество всех людей :', cnt)
print('Кол-во женжин :', cnt_f, ', кол-во мужчин :', cnt_m)
print('Кол-во совершенолетних :', cnt18)
print('Список всех имен :', name_all)
print('имена мужчин старше 35, имя которых начинается с F', name35, 'Всего :', cnt35)




