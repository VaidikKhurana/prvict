"""
What is an apple?
Ans. An apple is a type of fruit.

What is an apple?
Ans. An apple is a fruit.

What is an apple?
Ans. An apple is a red coloured food.

"""
def str_int(input, u_data):
 for char in input:
    if char == 'a':
        u_data.append(1)
    elif char == 'b':
        u_data.append(2)
    elif char == 'c':
        u_data.append(3)
    elif char == 'd':
        u_data.append(4)
    elif char == 'e':
        u_data.append(5)
    elif char == 'f':
        u_data.append(6)
    elif char == 'g':
        u_data.append(7)
    elif char == 'h':
        u_data.append(8)
    elif char == 'i':
        u_data.append(9)
    elif char == 'j':
        u_data.append(10)
    elif char == 'k':
        u_data.append(11)
    elif char == 'l':
        u_data.append(12)
    elif char == 'm':
        u_data.append(13)
    elif char == 'n':
        u_data.append(14)
    elif char == 'o':
        u_data.append(15)
    elif char == 'p':
        u_data.append(16)
    elif char == 'q':
        u_data.append(17)
    elif char == 'r':
        u_data.append(18)
    elif char == 's':
        u_data.append(19)
    elif char == 't':
        u_data.append(20)
    elif char == 'u':
        u_data.append(21)
    elif char == 'v':
        u_data.append(22)
    elif char == 'w':
        u_data.append(23)
    elif char == 'x':
        u_data.append(24)
    elif char == 'y':
        u_data.append(25)
    elif char == 'z':
        u_data.append(26)
def sim(trainvalue, fedvalue, provide_sim=None, provide_anomaly=None, provide_all=None):
    trainvalue = list(trainvalue)
    fedvalue = list(fedvalue)

    trainvalue_sim_increase = 100 / len(trainvalue)
    fedvalue_sim_increase = 100 / len(fedvalue)
    sim = 0
    runTime = -1
    anomaly =[]
    word_sim = []
    for i in fedvalue:
        runTime = runTime + 1
        while len(trainvalue) < len(fedvalue):
         trainvalue.append(0)
        else:
         if i == trainvalue[runTime]:
            sim = sim + fedvalue_sim_increase
            word_sim.append(i)
         else:
            anomaly.append(fedvalue.index(i))
         
    if provide_sim  == True:
        return sim, word_sim
    elif provide_anomaly == True:
        return sim, anomaly    
    elif provide_all == True:
        return sim, anomaly, word_sim
    else:
        return sim

prompt = "What is an apple?"
prompt_descriptions = [
    "An apple is a fruit that is rich in vitamins, fiber, and antioxidants.",
    "An apple is a fruit that grows on deciduous trees and is harvested in the fall.",    
]
print(sim("An apple is a fruit that is rich in vitamins, fiber, and antioxidants.", "An apple is a fruit that grows on deciduous trees and is harvested in the fall."))
        

