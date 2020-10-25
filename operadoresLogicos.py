while True :
    print('[T] = True\n[F] = False')
    a = b = 'x'
    while a != 'T' and a != 'F' :
        a = input('  a:  ').upper()[0]
    while b != 'T' and b != 'F' :
        b = input('  b:  ').upper()[0]
    if a == 'T' :
        A = True
    else :
        A = False
    if b == 'T' :
        B = True
    else :
        B = False
    print(f'\na: {A}\nb: {B}\n')

    #and
    print('AND = ', end='')
    if A and B :
        print('Verdadeiro')
    else:
        print('Falso')

    #or
    print('OR = ', end='')
    if A or B :
        print('Verdadeiro')
    else:
        print('Falso')

    #not
    print('NOT = ', end='')
    print(f'a: {not A} / b: {not B}')

    #nand
    print('NAND = ', end='')
    if not (A and B) :
        print('Verdadeiro')
    else:
        print('Falso')

    #nor
    print('NOR = ', end='')
    if not (A or B) :
        print('Verdadeiro')
    else:
        print('Falso')

    #xor
    print('XOR = ', end='')
    if A is not B :
        print('Verdadeiro')
    else:
        print('Falso')

    #xnor
    print('XNOR = ', end='')
    if A is B :
        print('Verdadeiro')
    else:
        print('Falso')
    
    op = input('[S] para continuar:  ').lower()
    if op != 's' :
        break
