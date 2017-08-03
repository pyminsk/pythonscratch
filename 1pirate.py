#pirate game
from random import randint
pirate_secret = randint(1, 99)
tries = 0
guess = 0
print ("Эй на палубе! Я Ужасный пират Робертс, и у меня есть секрет!")
print ("Это число от 1 до 99. Я дам тебе 6 попыток.")
print ("Твой вариант?")
print (pirate_secret) ############ otladka
while guess != pirate_secret and tries < 6:
   key = input()
   guess = int(key)
   tries = tries+1 

   if guess < pirate_secret:
        print ("Это слишком мало, презренный пес!")
   elif guess > pirate_secret:
        print ("Это слишком много, сухопутная крыса!")
   elif guess == pirate_secret:
        print ("Хватит! Ты угадал мой секрет!")
         
else:
        print ("Попытки кончились!")
        print ("Это число ", pirate_secret)
        print ("Попыток было", tries)
    
