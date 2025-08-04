import random
print("welcome to paper rock scissors gaming")
print("1.paper \n 2.rock \n 3.scissor")
while True:
    result=""
    
    user_choice=int(input("enter the your choice:"))

    if user_choice ==1:
        user_choice="paper"
    elif user_choice== 2:
        user_choice="rock"
    else:
        user_choice="scissors"

    

    choice=random.randint(1,3)
    if choice==1:
        choice="paper"
    elif choice==2:
        choice="rock"
    else:
        choice="scissors"

    print("now it's time for matching")
    print(f"you: {user_choice} computer: {choice}")

    if user_choice==choice:
        result="draw"
        
    elif (user_choice=="paper" and choice=="rock") or (choice=="rock" and user_choice=="paper"):
        
        result="paper"
        
    elif (user_choice == "rock" and choice=="scissors") or (choice=="scissors" and user_choice=="rock"):
        
        result="rock"
    elif (user_choice =="scissors" and choice=="paper") or (choice == "paper" and user_choice=="scissors"):
    
        result="scissors"
        


    if result=="draw":
        print("match drawn")
    elif result==choice:
        print("---  your win---")
    else:
        print("you lost")
        



    print(" are u want try another one say in (y\n)")
    u=input().lower()
    if u !="y":
          break




print("Thanks for playing")
