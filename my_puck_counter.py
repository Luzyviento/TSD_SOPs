pucks = {'ROLO122007': {'OM1_12':1},'ROLO121969': {'OM1_16':1}, 'ROLO122070': {'OM1_20':1}}

while True:
    print('Enter a barcode or D to display all: (Q to quit)')
    name = input()
    if name == 'Q':
        break

    if name == 'D':
        pucks.values()

    if name in pucks.keys():

        print(' added quantity of one to ' + name)

    else:
        print('I do not have reference information for ' + name)
        print('What is shade_size?')
        shade_size = input()
        pucks[name] = {shade_size:1}
        print('Puck database updated.') 
