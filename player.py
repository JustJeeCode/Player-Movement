# Player movement script by JustJeeCode
# 8/9/21

player = '.'
pos = 0

print('To move press [A:Left][D:Right][S:Down] then [Enter]\n')
print(player)

while True:
    movement = input('')
    print('\n' * 50)

    if movement == 'd':
        pos += 3
        print(' ' * pos + player + '>')
    elif movement == 'a':
        pos -= 3
        print(' ' * pos + '<' + player)
    elif movement == 'w':
        print(' ' * pos + '^')
        print(' ' * pos + player) 
    elif movement == 's':
        print(' ' * pos + player)
        print(' ' * pos + 'v')
    else:
        print(' ' * pos + player)
