while True:


    answer = input("What you like to play  (yes/no)  ")

    if answer.lower().strip() == "yes":

        answer = input("You reach a crossroad, would you like to left or rigth?: ").lower().strip()
        if answer == "left":
            answer = input("you encounter a MONSTER, would you like to run or attack?")
        
            if answer == "atteck":
                print("That was not the greater idea, you lost!")
            else:
                print("Good choice, you made it awey sefely.")

                answer = input("You see a car and a plane. Whith would you like to take? (car/plane) ")

                if answer == "plane":
                    print("Unfortunately you do not know how to fly... Game is over!")
                else:
                    print("You won")



        elif answer == "reigth": 
            print("You walk aimlessly to the rigth and fall on a patch of ice. You injure your leg and cannot continue. Game over!")
        
        else:
            print("Invalid choice, you lost!")      

    else:
        print("That's to bad")
        break    