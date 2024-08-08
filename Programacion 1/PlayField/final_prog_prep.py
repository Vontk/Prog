def extract(adn_string):
    list_of_adn = []
    for num in range(0, (len(adn_string))//3):
        list_of_adn.append(adn_string[(num*3):(num*3+3)])
    return list_of_adn


def transform(list_of_adn):
    list_of_arn = []
    arn_adenine = 0
    arn_cytosine = 0
    arn_guanine = 0
    arn_uracil = 0
    transition = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}
    for adn in list_of_adn:
        arn = ''
        for string in adn:
            arn += transition[string]
        list_of_arn.append(arn)
    for arn in list_of_arn:
        for string in arn:
            if string == 'A':
                arn_adenine += 1
            elif string == 'C':
                arn_cytosine += 1
            elif string == 'G':
                arn_guanine += 1
            elif string == 'U':
                arn_uracil += 1
            else:
                pass
    list_of_data = [list_of_arn, arn_adenine, arn_cytosine, arn_guanine, arn_uracil]
    return list_of_data


def load(list_of_data):
    print(f'ARN obtenido: {list_of_data[0]}')
    print(f'Cantidad de adenina: {list_of_data[1]}')
    print(f'Cantidad de citosina: {list_of_data[2]}')
    print(f'Cantidad de guanina: {list_of_data[3]}')
    print(f'Cantidad de uracil: {list_of_data[4]}')
    global ARN
    global ADENINE
    global CYTOSINE
    global GUANINE
    global URACIL
    ARN = list_of_data[0]
    ADENINE = list_of_data[1]
    CYTOSINE = list_of_data[2]
    GUANINE = list_of_data[3]
    URACIL = list_of_data[4]

adn = 'ACTGACTGGTCATGTCATCTTGCAG'

load(transform(extract(adn)))

print(ARN)
print(ADENINE)
print(CYTOSINE)
print(GUANINE)
print(URACIL)

