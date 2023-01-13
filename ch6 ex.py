def print_x_eyes():
    print('x  x')


def print_o_eyes():
    print('o  o')


def face(eyes):
    eyes()
    print(' >  ')
    print('----')

face(print_x_eyes)
