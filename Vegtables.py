# ------------------------------------------------------------
# Import libraries
# ------------------------------------------------------------
import random

# ------------------------------------------------------------
# Constants
# ------------------------------------------------------------
MAX_POSSIBLE_VEG_NUMBER = 20

# ------------------------------------------------------------
# Global variables
# ------------------------------------------------------------
vegName = ""
vegNum = 0
vegNumRandom = 0

# ------------------------------------------------------------
# Main program
# ------------------------------------------------------------
vegName = ""
def askInput():
    global vegName
    vegName = input("Enter the name of your favourite vegetable: ")
    if vegName == "":
        print("[Error] Input cannot be blank!")

vegNum = None
def askInputNum():
    global vegName
    global vegNum

    vegNum = int(input("How many {} do you think you could eat?".format(vegName)))
    if vegNum == None:
        print("[Error] Input cannot be 0!")
        askInputNum()
        return
    
    try:
        int(vegNum)
    except:
        print("[Error] Input must be an integer!")
        askInputNum()
        return

    if vegNum > MAX_POSSIBLE_VEG_NUMBER:
        print("[Error] Input must be below {}!".format(MAX_POSSIBLE_VEG_NUMBER))
        askInputNum()
        return
    


likedVegtables = [ "carrot", "leek", "cauliflower", "peas", "asparagus", "celery", "potato", "onion" ]
        

while vegName == "":
    askInput()

askInputNum()
print ("So you think you can eat " + str(vegNum) + " " + vegName + " do you?")

vegNumRandom = random.randint (1, MAX_POSSIBLE_VEG_NUMBER)

if vegName.lower() not in likedVegtables:
    print("The computer doesnt like your vegtable!")


if vegNumRandom > vegNum:
    print("The computer can eat more than you!")
elif vegNumRandom < vegNum:
    print("You can eat more than the computer!")
else:
    print("You can eat the same amount")



