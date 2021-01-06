from __future__ import print_function
player1,player2 = '',''
print("Player 1 is X Player2 is O")
tictac=[['0','0','0'],
         ['0','0','0'],
         ['0','0','0']]
#tictac[2][2]='O'
print("    0    1    2")
end = ' | '
for count, row in enumerate(tictac):
    #if count != 1: end += '---------\n';
    print('--------------')
    #print(str(count).replace(',','|'), row)
    #print ''.join(map(str, count))
    print(*row, sep='  |  ')
for e in range(9):
    if e % 3 ==0:
     print("\n")
     print("Player1  Enter X:")
     r=int(input())
     print("Player1  Enter Y:")
     c = int(input())
     tictac[r][c] = 'x'
    else:
        print("\n")
        print("Player2  Enter X:")
        r = int(input())
        print("Player2  Enter Y:")
        c = int(input())
        tictac[r][c] = 'o'

    print("   0  1  2")
    for count, row in enumerate(tictac):
       #print(count, row)
       print('--------------')
       print(*row, sep='  |  ')
       #print (tictac[0][0])
    if ( (tictac[0][0] and tictac[0][1] and tictac[0][2]) == 'O' ):
        print('You Won')
        break
    if ((tictac[0][0] and tictac[0][1] and tictac[0][2]) == 'X'):
        print('You Won')
        break
    if ((tictac[0][0] and tictac[1][0] and tictac[2][0]) == 'O'):
        print('You Won')
        break
    if ((tictac[0][0] and tictac[1][0] and tictac[2][0]) == 'X'):
        print('You Won')
        break
    if ((tictac[0][0] and tictac[1][0] and tictac[2][0]) == 'O'):
        print('You Won')
        break
    if ((tictac[0][1] and tictac[1][1] and tictac[2][1]) == 'X'):
        print('You Won')
        break
    if ((tictac[0][1] and tictac[1][1] and tictac[2][1]) == 'O'):
        print('You Won')
        break
    if ((tictac[0][2] and tictac[1][2] and tictac[2][2]) == 'X'):
        print('You Won')
        break
    if ((tictac[0][2] and tictac[1][2] and tictac[2][2]) == 'O'):
        print('You Won')
        break
    if ((tictac[0][0] and tictac[1][1] and tictac[2][2]) == 'O'):
        print('You Won')
        break
    if ((tictac[0][0] and tictac[1][1] and tictac[2][2]) == 'X'):
        print('You Won')
        break
    if ((tictac[0][2] and tictac[1][1] and tictac[2][0]) == 'O'):
        print('You Won')
        break
    if ((tictac[0][2] and tictac[1][1] and tictac[2][0]) == 'X'):
        print('You Won')
        break
    else:
        pass



