""" A Functional Breakfast """

cheese = 'cheddar'

def mix_and_cook():
    print('Mixing the ingredients')
    print('Greasing the frying pan')
    print('Pouring the mixture into a frying pan')
    print('Cooking the first side')
    print('Flipping it!')
    print('Cooking the other side\n')

def make_omelette():
    global cheese
    cheese = 'swiss'
    mix_and_cook()
    omelette = f'a {cheese} omelette'
    return omelette

def make_pancake():
    mix_and_cook()
    pancake = f'a {cheese} pancake'
    return pancake

def make_fancy_omelette(*ingredients):
    mix_and_cook()
    omelette = f'a fancy omelette with {len(ingredients)} ingredients'
    return omelette

# make breakfast for two
print(f'*** cheese is {cheese} ***\n') #### NOTE TO SELF: Make omelette first, then swap order
barron_breakfast = make_pancake()
print(f'*** cheese is {cheese} ***\n')
olivia_breakfast = make_omelette()
print(f'*** cheese is {cheese} ***\n')

print(f'Barron is having {barron_breakfast}\n')
print(f'Olivia is having {olivia_breakfast}\n')