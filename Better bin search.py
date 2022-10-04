print("binary search")
max = int(input("input the max number"))
min = int(input("input the min number"))
#No im not gonna combine them into one input and then split them later. Norbert.2
numbers =  input("input a number my bot will guess")
print("number is " + str(numbers))
guess = int(max//2)
numbers = float(numbers)
guess = float(guess)
#counter!=4
while(guess!=numbers):
    print("the bot guessed" + str(guess))
    if(guess<numbers):
        print("guess is less than the number you guessed")
        min = guess
        guess = (min + max)//2


    elif(guess>numbers):
        print("guess is greater than the number you guessed")
        max = guess
        guess = (min + max)//2

        
    if(guess==numbers):
        print("Final number has been found")
        print("the bot guessed" + str(guess))



