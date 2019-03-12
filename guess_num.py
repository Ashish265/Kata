#!/usr/bin/python3
guess_count=0
epsilion=0.01
low=0
high=100

print("Please think of a number between 0 and 100")
secret_number=int(input())


mid=(high+low)/2.0
while abs(mid-secret_number) >= epsilion:
	print(" Is your secret number " + str(mid)+ " ? ")
	print("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
	choice_user=input()
	if choice_user == 'h':
		high=mid
	elif choice_user == 'l':
		low=mid
	else:
		print("Game over. Your Secret number was " + str(round(mid,1)))
		break
	mid=(high+low)/2.0
