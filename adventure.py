def main():
    user_input = int(input("Enter 1 to play , 0 to quit : "))
    if user_input == 1:
        print("Let's begin our adventure!!!")
        head_start()
    elif user_input == 0:
        print("We are sorry to see you leave!!!")
    else:
        print("Invalid Input")      
    

def head_start():
    print("You are on a palace and you want to escape from it.Suddenly it's getting dark and you want to see the way out .")
    command_1 = input("There is a lamp and a torch is lying near by.What do you want to pick ? Torch or Lamp : ").lower()
    if command_1 == 'torch':
        print(f"You picked the {command_1}.")
        with_torch()
    elif command_1 == 'lamp':
        print(f"You picked the {command_1}.")
        with_lamp()
    else:
        print("Invalid Input")  

# journey using torch

def with_torch():
    print("Now you entered a big garden full of roses.")
    print("Do you want to smell it or go straight?")
    command_2 = input("Type smell / straight : ").lower()
    if command_2 == 'smell':
        print("You smelled the rose, unfortunately it's a poisonous rose.")
        print("You are now dead!!!")
        print("The End")
    elif command_2 == 'straight':
        print(f"You decided to go {command_2} ahead")
        go_straight()
    else:
        print("Invalid Input")  

def go_straight():
    print("Your torch is not working but still you continued your journey without knowing any path.Suddenly one dragon entered and coming towards you . You can either run or accept your defeat.Choose wisely")
    command_3 = input("Choose between run / accept : ").lower()
    if command_3 == 'run':
        print(f"You {command_3} into a wall, hit and died!!!")
        print("Told you to choose wisely!!!")
        print("The End")
        
    elif command_3 == 'accept':
        print("No need to panic , it's just a ballon dragon.You are brave to accept your defeat infront of dragon.Impressive!!!")
        print("You won this adventure!!!HURRAY!!!")
    else:
        print("Invalid Input")  
        

# journey using lamp

def with_lamp():
    print("You entered a room full of perfumes.Do you want to smell it for long or put a mask on ?")
    command_4 = input("Choose between smell / mask : ").lower()
    if command_4 == 'smell':
        print("Your bad....It's poisoned.You died!!!")
        print("The End")
        
    elif command_4 == 'mask':
        print(f"You put a {command_4} on.")
        with_mask()
    else:
        print("Invalid Input")  

def with_mask():
    print("Now you are going straight ahead.Look there's little wind blowing towards you . Unfortunetly it blow out your lamp.Now you need to decide either stay right there or go ahead into the darkness.")
    command_5 = input("Choose between stay / continue : ").lower()
    if command_5 == 'stay':
        print(f"You choosed to {command_5}.")
        by_staying()
    elif command_5 == 'continue':
        print("You walk into a hole.There is a demon inside .")
        print("Unfortunately you died!!!")
        print("The End")
    else:
        print("Invalid Input")  
        

def by_staying():
    print(" Staying in the dark made you fall asleep.Suddenly a sound echoed from a distance.\'YOU ARE NOW THE CHOSEN ONE.GET UP LITTLE KID\' .and it disppear into thin air. You can either follow the voice or do nothing. ")
    command_6 = input("Choose between follow / stay : ").lower()
    if command_6 == 'stay':
        print("By staying there for the whole night you wake up in the morning and begin your journey by following the light ahead.You found the way out . HURRAY!!!")
        print("You won!!!")
        
    elif command_6 == 'follow':
        print(f"You {command_6} the voice and tripped over into a hole.Unfortunately you DIED!!!!")
        print("The End")
    else:
        print("Invalid Input")           

if __name__ == "__main__":
    main()