set1 = {1, 2, 3, "pepe"}
set1.add("jorge")
print(set1)
set2 = set('abcdebcerfba')
print(set2)
notas = {
    "pepe": 1,
    "jorge": 2,
    "ramiro": 3,
    "juanito": 4,
    "facundo": 5,
    "sofia": 6,
    "mateo": 7,
    "gaston": 8,
}
for k in notas:
    notas[k] = notas[k] + 1
    print(notas[k])
for k in notas.keys():
    print(f'{k} el gordo')