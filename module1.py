print("Welcome to Mathsmania")
playing=input("Do you want to play? ")
if playing!="yes":
    quit()
name=input("Enter Your Name: ")

print("Okay, lets start the game",name)
score=0

ans1=input("What is the highest common factor of the numbers 30 and 132? " )
if ans1=="6":
    print("Bravo!!")
    score+=1

else:
    print("Oops Your Answer is wrong!!")

ans1=input("123+4-5+67-89? " )
if ans1=="100":
    print("Bravo!!")
    score+=1

else:
    print("Oops Your Answer is wrong!!")

ans1=input("From the number 0 to the number 1000, the letter 'A' appears only in? ")
if ans1=="1000":
    print("Bravo!!")
    score+=1

else:
    print("Oops Your Answer is wrong!!")

ans1=input("If 1=3, 2=3, 3=5, 4=4, and 5=5, what is 6=? " )
if ans1=="3":
    print("Bravo!!")
    score+=1

else:
    print("Oops Your Answer is wrong!!")

ans1=input("Which number is the equivalent to 3^(4)/3^(2)? " )
if ans1=="9":
    print("Bravo!!")
    score+=1

else:
    print("Oops Your Answer is wrong!!")
ans1=input("Using only the process of addition, how to add eight 8's to get the final number of 1000? " )
if ans1=="888+88+8+8+8":
    print("Bravo!!")
    score+=1

else:
    print("Oops Your Answer is wrong!!")

ans1=input("What is the year 1982 in Roman Numerals? " )
if ans1=="MCMLXXXII":
    print("Bravo!!")
    score+=1

else:
    print("Oops Your Answer is wrong!!")

ans1=input("What is the next number in the following number series: 256, 289, 324, 361, ...? " )
if ans1=="400":
    print("Bravo!!")
    score+=1

else:
    print("Oops Your Answer is wrong!!")

ans1=input("At a christmas party, everyone shook hands with everyone else.There were a totoal of 66 handshakes that happend during the party. How many people were present? " )
if ans1=="12":
    print("Bravo!!")
    score+=1

else:
    print("Oops Your Answer is wrong!!")

ans1=input("What is the value of Pi to four individual decimal places? " )
if ans1=="3.1416":
    print("Bravo!!")
    score+=1

else:
    print("Oops Your Answer is wrong!!")

ans1=input("What does 6 raise to the power of 0 equal? " )
if ans1=="1":
    print("Bravo!!")
    score+=1

else:
    print("Oops Your Answer is wrong!!")

print("Your Score is " +str(score)+ " out of 11")