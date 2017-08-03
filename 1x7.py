# проверяем знание таблицы умножения на 7
print ('проверяем знание таблицы умножения на число 7')      
table = 7
for i in range (1, 9):
    print('What\'s', i, 'x',  table, '?')
    guess = input()
    
    if guess == 'stop':
        break
    
    if guess == 'skip':
        print ('skiping')
        continue

    ans = i*table
    if int(guess) == ans:
          print('Correct')
    else:
          print('No, it\'s', ans)
print('fineshed')
