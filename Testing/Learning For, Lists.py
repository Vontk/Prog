magician_names = ['Mirage Mystique', 'Ember Evergreen', 'Flicker Foxglove', 'Zephyr Zumaya', 'Indigo Inkwell',
                  'Sybil Stardust', 'Arcane Alistair', 'Whisper Willow', 'Illusion Isadora', 'Dashing Desmond',
                  'Seraphina Smoke', 'Raven Runecaster', 'Cordelia Conjurer', 'Jaxon Jynx', 'Emerald Elodie',
                  'Felix Fortune', 'Zia Zenith', 'Cosmo Clearwater', 'Luna Larkspur', 'Trickster Tristan',
                  'Nova Nightshade', 'Willow Weaver', 'Prism Pip', 'Merlin Moonbeam', 'Raven Ramirez', 'Zephyra Zephyr',
                  'Flint Fletcher', 'Illusion Ignacio', 'Mirage Mallory', 'Stardust Scarlett', 'Arcane Alistair',
                  'Emerald Eloise', 'Shadow Skye', 'Whisper Willow', 'Corvus Crowfeather', 'Raven Ravencroft',
                  'Zyla Zarielle', 'Flicker Flameborn', 'Whisper Weaver', 'Mirage Mallory', 'Nova Nightshade',
                  'Cosmo Clearwater', 'Dashing Desmond', 'Jaxon Jynx', 'Ember Evergreen', 'Felix Fortune',
                  'Indigo Inkwell']
for name in magician_names:
    print(f'{name} is a magician')
y = 1
for x in range(100):
    y = y+1
    print(y)
numero = int(input('Enter a number: ') or 42)
for multiplicador in range(1, 11):
    print(f'{numero} x {multiplicador} = {numero * multiplicador}')
for index,name in enumerate(magician_names):
    print(f'{name} the magician no{index + 1}')
print(range(10))
print(list(range(10)))


