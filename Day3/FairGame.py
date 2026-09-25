print("Welcome to the Rollercoaster!")

ride = str(input("Would you like to ride the rollercoaster? (Y/N) "))
bill = 0
if ride.upper() == "N":
    print("Have fun at other rides! Bye!")
    exit
elif ride.upper() == 'Y':
    #if here, wants to ride the rollercoaster
    height = int(input("What is your height in cm? "))

    if height >= 120:
        print("You can ride the rollercoaster!")
        #only 18+ can ride
        age = int(input("What is your age? "))

        if age <13:
            print("You can ride the rollercoaster but need a booster seat.")
            bill = 5
            print(f"Children ticket: ${bill}")
        elif age >= 13 and age < 18:
            print("You can ride the rollercoaster but bring an adult along!")
            bill = 7
            print(f"Youth ticket: ${bill}")
        elif 45 <= age <= 55:         
            print("Everything is going to be ok. Enjoy a free ride on us!")
        else:
            print("You can ride the rollercoaster!")
            bill = 12
            print(f"Adult ticket: ${bill}")

        wants_photo = (input("Do you want a photo taken? (Y/N): "))
        if wants_photo.upper() == 'Y':
            bill += 3
            print(f"Your total bill is: ${bill}")
        
    else:
        print("Sorry you have to grow taller before you can ride...")
else:
    print("Invalid input. Bye.")
