import sys

word= "your word"
count = int(len(word)-1)
guess = ''

while count > 0:
    i = input('insert character: ')
    if len(i) != 1:
        print('just enter one character')
        continue
    guess += i
    if i not in word:
        count -= 1
        print('your guess wrong')
        print(f'you have {count} turn')
    win = True
    for ch in word:
        if ch in guess:
            sys.stdout.write(ch)
        else:
            sys.stdout.write('_')
            win = False
    if win == True:
        print("congratulation")
        break
    print()
if win == False:
    print('You lose')
