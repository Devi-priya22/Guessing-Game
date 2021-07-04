import random

while True:
    print("\nNUMBER GUESSING GAME\n")
    j=int(input("Enter the number of rounds u need:"))
    y = int (input("\nGuess the number:"))
    s=random.randint(1,100)
    i=1
    while (y!=s):
        if i==j:
            print("Oops!You have used all your chances.You lost this game")
            input("Press any key to continue")
            break
        elif y>s:
            print("Your guess is greater than actual number!Try again")
            y = int(input("Guess the number:"))
            i+=1
        elif y<s:
            print("Your guess is lower than actual number!Try again")
            y = int(input("Guess the number:"))
            i+=1
    if y == s:
         print("You won\nCongratulations!")
         print("You wanna try again?")
         input("Press any key to continue")
