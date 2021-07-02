x = 3
while (x<50):
    x = (((x+3)*2)-1)
    print("Guess my number\nLets play a Guessing game")
    y = int (input("Enter the number"))
    i = 1
    while (y!=x):
        if i == 4:
            print("Oops!You have used all your chances.You lost this game")
            break
        elif y>x:
            print("Your guess is greater than actual number!Try again")
            y = int(input("Enter the number"))
        elif y<x:
            print("Your guess is lower than actual number!Try again")
            y = int(input("Enter the number"))
            i+=1
    if y == x:
         print("You won\nCongratulations!")
         print("You wanna try again")

