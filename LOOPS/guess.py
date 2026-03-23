secret_number=7
guess=9
while guess !=secret_number:
    guess=int(input("enter your guess:"))
    if guess== secret_number:
        print("correct! you guessed the number:")
    else:
        print("wrong guess.try again!")
