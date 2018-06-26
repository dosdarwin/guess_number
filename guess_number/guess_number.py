import random
a1 = int(input('tell me the smallest number you want to guess from:'))
a2 = int(input('tell me the biggest number you want to guess to :'))
d = int(input('Guess the number:'))
x = random.randint(a1, a2)
m = 1
while True:
	if x == d:
		print('congratulation!!!!!!!')
		break
	elif d >= x:
		print("wrong, guess again", "hint:it is SMALLER then the number you are guessing")
		print("this is your", m, "time guess")
		d = int(input('Guess my number:'))
		m = m + 1
	elif d <= x:
		print("wrong, guess again", "hint:it is BIGGER then the number you are guessing")
		print("this is your", m, "time guess")
		d = int(input('Guess my number:'))
		m = m + 1