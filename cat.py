students = [
    {"name":'Hermione', "house": 'Gryffindor', "patronus": "Otter"},
    {"name":'Harry', "house": 'Hufflepuff', "patronus": "Badger"},
    {"name":'Ron', "house": 'Ravenclaw', "patronus": "Eagle"},
    {"name":'Draco', "house": 'Slytherin', "patronus": "Snake"} 
]

for student in students:
    print(student['name'], student['house'], student['patronus'], sep=", ")