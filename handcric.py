import random
import time
def toss(turn):
    while True:
        ch=int(input('Choose heads or tails (Type 1 for heads and 2 for tails): '))
        if ch==1 or ch==2:
            break
        else:
            print('\nEnter either 1 or 2 to continue: ')
            ch=int(input('Choose heads or tails (Type 1 for heads and 2 for tails): '))
            continue
    toss=random.randint(1,2)
    print(".")
    time.sleep(0.8)
    print(".")
    time.sleep(0.8)
    print(".")
    time.sleep(0.8)
    if ch==toss:
        if toss==1:
            print("ITS HEADS!!!")
        else:
            print("ITS TAILS!!!")
        
        print("You won the toss, would you like to bat or bowl first?")
        print("Enter 1 to bat and 2 to bowl: ")
        turn=int(input())
        while True:
            if turn==1 or turn==2:
                break
            else:
                print('\nEnter either 1 or 2 to continue: ')
                time.sleep(0.8)
                print("You won the toss, would you like to bat or bowl first?")
                time.sleep(0.8)
                print("Enter 1 to bat and 2 to bowl: ")
                time.sleep(0.8)
                turn=int(input())
                continue
        time.sleep(1)
        return turn
    else:
         print("You lost the toss")
         time.sleep(0.8)

    if toss==1:
        print("The computer chose to bat first")
        time.sleep(1)
        turn=2
        return turn
    else:
        print("The computer chose to bowl first")
        time.sleep(1)
        turn=1
        return turn

def batting(turn,score,aiscore):
    score=0
    if turn==1:
        time.sleep(0.8)
        print("You will bat now")
        while True:
            aichoice=random.randint(1,6)
            choice=int(input("Enter a number from 1-6: "))
            time.sleep(0.7)
            while True:
                if choice>0 and choice<7:
                    break
                else:
                    print('\nOnly enter numbers between 1 and 6 ')
                    time.sleep(0.8)
                    print("Enter a number from 1-6: ")
                    time.sleep(0.8)
                    choice=int(input())
                    continue
            print("The computer chose: ",aichoice)
            time.sleep(0.7)
            if choice==aichoice:
                print("OUT!! Your score is: ",score)
                time.sleep(0.8)
                print("The computer's target is ",score+1)
                return turn+1,score,aiscore
            else:
                score+=choice
                time.sleep(0.3)
                print("Score: ",score)
            
    if turn==2:
        time.sleep(0.8)
        print("You will bat now")
        while score<=aiscore:
            aichoice=random.randint(1,6)
            choice=int(input("Enter a number from 1-6: "))
            while True:
                if not choice<1 or not choice>6:
                    break
                else:
                    print('\nOnly enter numbers between 1 and 6 ')
                    time.sleep(0.8)
                    print("Enter a number from 1-6: ")
                    time.sleep(0.8)
                    choice=int(input())
                    continue
            time.sleep(0.7)
            print("The computer chose: ",aichoice)
            time.sleep(0.7)
            if choice!=aichoice:
                score+=choice
                time.sleep(0.3)
                print("Score: ",score)
            else:
                print("OUT!! Your score is: ",score)
                if aiscore==score:
                    time.sleep(0.8)
                    print("The match is a draw!!")
                    return turn+1,score,aiscore
                time.sleep(0.8)
                print("You lost by ",aiscore-score," runs")
                return turn+1,score,aiscore
        print("CONGRATS YOU WIN!!")
    else:
        exit()

def bowling(turn,score,aiscore):
    if turn==2:
        time.sleep(0.8)
        print("You will bowl now")
        while aiscore<=score:
            aichoice=random.randint(1,6)
            choice=int(input("Enter a number from 1-6: "))
            time.sleep(0.7)
            print("The computer chose: ",aichoice)
            time.sleep(0.7)
            if choice==aichoice:
                print("OUT!! Computer's score is: ",aiscore)
                if aiscore==score:
                    time.sleep(0.8)
                    print("The match is a draw!!")
                    return turn+1,score,aiscore
                time.sleep(0.7)
                print("CONGRATS YOU WIN!!")
                return turn+1,score,aiscore
            else:
                aiscore+=aichoice
                time.sleep(0.3)
                print("Score: ",aiscore)
        time.sleep(1)
        print("You lose!! :(")
    if turn==1:
        time.sleep(0.8)
        print("You will bowl now")
        while True:
            time.sleep(0.8)
            aichoice=random.randint(1,6)
            choice=int(input("Enter a number from 1-6: "))
            time.sleep(0.7)
            print("The computer chose: ",aichoice)
            time.sleep(0.7)
            if choice==aichoice:
                print("OUT!! Computer's score is: ",aiscore)
                time.sleep(0.8)
                print("Your target: ",aiscore+1)
                return turn+1,score,aiscore
            else:
                aiscore+=aichoice
                time.sleep(0.3)
                print("Score: ",aiscore)
    else:
        exit()

turn=0
score=0
aiscore=0
turn=toss(turn)
if turn==1:
    turn,score,aiscore=batting(turn,score,aiscore)
    turn,score,aiscore=bowling(turn,score,aiscore)
else:
    turn,score,aiscore=bowling(turn-1,score,aiscore)
    turn,score,aiscore=batting(turn,score,aiscore)
