import random

def sim_card():
    ir ="irancl:"+ "0933{}".format(random.randrange(1111111, 9999999))+"\n"
    mci="mci:"+"0915{}".format(random.randrange(1111111, 9999999))+"\n"
    rightel="rightel :"+"0922{}".format(random.randrange(1111111, 9999999))+"\n"

    with open("sim_card.txt","a") as file:
        file.write(str(ir))
        file.write(str(mci))
        file.write(str(rightel))
        print("save number mobile")
        
sim_card()        
    
