from random import randrange
import time


def main():

    numOfRounds = 6
    gun = [0, 0, 0, 0, 0, 0]
    bullet = randrange(0, 6)
    gun[bullet] = 1
    player = False  
    pc = False  

    print("/********************************/")
    print("    Welcome to russian roulette")
    print("/********************************/")
    time.sleep(2)
    print("You are going to play against the pc")
    time.sleep(2)
    print("There is one gun and one bullet")
    time.sleep(2)

    answer = input(
        "Please press 'm' if you want to start first or 'p' if you want the pc to start first: "
    )

    while answer != "m" and answer != "p":
        answer = input("please enter again ('m' or 'p'): ")

    if answer == 'm':
        turn = "player"
    else:
        turn = "pc"

    while numOfRounds != 0 and (pc == False and player == False):
        print(f"\nRound number {numOfRounds}/6")
        time.sleep(1)
        print("the gun is being loaded")
        time.sleep(3)
        print("the gun is placed on " + ("your head" if turn ==
              "player" else "the cpu of the pc"))
        time.sleep(3)
        print("and...")
        time.sleep(1)
        print("...")
        time.sleep(2)
        print("...")
        time.sleep(2)
        print("...")
        time.sleep(2)

        shot = gun.pop(numOfRounds - 1)

        if shot:
            print("The gun went off!")
            print("You died." if turn == "player" else "The PC died.")
            if turn == "player":  
                player = True
            else:
                pc = True
        else:
            print("Nothing happened. Phew!")
            if turn == "player":  
                turn = "pc"
            else:
                turn = "player"

        time.sleep(2)
        numOfRounds -= 1

    time.sleep(1)
    print("")
    if player:
        print("You died! Better luck next time...")
    else:
        print("You survived!")
    print("Goodbye.")


main()
