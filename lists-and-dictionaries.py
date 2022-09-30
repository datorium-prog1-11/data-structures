name = 'Anna'
age = 18
height = 1.68
has_car = True

names = ['Anna', 'Oskars', 'Jenifer', 'Anna', 'Mik']
ages = [18, 20, 18, 17, 16]

for i in range(len(names)):
    print(f'{names[i]} is {ages[i]} years old')
    
# Anna is 18 years old
# Oskars is 20 years old
# ...




personal_data = [
    {
        'name': 'Anna', 
        'age': 18, 
        'email': 'anna@somemail.com', 
        'school': 'Dobeles VĢ',        
        'car': {
            'brand': 'Tesla',
            'year': 2022,
            'color': 'Red',
            'engine': 50        
        }
    },
    {
        'name': 'Oskars', 
        'age': 20,
        'email': 'oskars@somemail.com',
        'school': 'Siguldas VĢ',
        'car': {
            'brand': 'Audi',
            'year': 2020,
            'color': 'Black',
            'engine': 2.0        
        }
    },
    {
        'name': 'Jenifer', 
        'age': 17,
        'email': 'jenifer@somemail.com',
        'school': 'Talmācības',
        'car': {
            'brand': 'Toyota',
            'year': 2021,
            'color': 'Silver',
            'engine': 1.5        
        }
    }
]

type(personal_data)
type(personal_data[2])

for data in personal_data:
    print(data['car']['year'])
