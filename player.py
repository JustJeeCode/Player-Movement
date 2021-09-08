# Player movement script by JustJeeCode
# 8/9/21

player = '.'
pos = 0

print('To move [A:Left][D:Right][S:Down]\n')
print(player)

while True:
    movement = input('')
    print('\n' * 50)

    if movement == 'd':
        pos += 3
        print(' ' * pos + player)
    elif movement == 'a':
        pos -= 3
        print(' ' * pos + player)
    elif movement == 's':
        print('\n')
        print(' ' * pos + player)
        
