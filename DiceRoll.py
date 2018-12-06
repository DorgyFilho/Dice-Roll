from random import randrange

def showDice(result):
    print("=-----------=")
    if result == 1:
        print('|          |')
        print('|     *    |')
        print('|          |')
    elif result == 2:
        print('|*         |')
        print('|          |')
        print('|         *|')
    elif result == 3:
        print('|*         |')
        print('|     *    |')
        print('|         *|')
    elif result == 4:
        print('|*        *|')
        print('|          |')
        print('|*        *|')
    elif result == 5:
        print('|*        *|')
        print('|     *    |')
        print('|*        *|')
    elif result == 6:
        print('|*    *   *|')
        print('|          |')
        print('|*    *   *|')
    
    print('=-----------=')

def rollDice():
    return randrange(1,6)

def play():
    times = int(input('How much times do you want play?: '))
    for i in range(1, times+1):
        showDice(rollDice())

def main():
    again = 'Y'
    while again == 'Y':
        print('Choose Your Destiny\n1-Play\n2-Exit')
        op = input('Option: ')
        if op == '1':
            play()
        elif op == '2':
            print('See you later.')
            exit()
        else:
            print('Invalid Answer.')
            break
        print()
        print('Do You Want To Try Again? Y or N')
        again = input('Answer: ').upper()
        if again == 'N':
            break
    else:
        print('System Automatically Turned Off.')
        exit()

main()

    
