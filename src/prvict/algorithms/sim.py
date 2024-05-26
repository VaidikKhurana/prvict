from str_int import *
def sim(trained_Data, tuple_data):
    trainvalue = []
    str_int(trained_Data, u_data=trainvalue) 
    fedvalue = []
    str_int(tuple_data, u_data=fedvalue)

    trainvalue_sim_increase = 100 / len(trainvalue)
    fedvalue_sim_increase = 100 / len(fedvalue)
    sim = 0
    runTime = -1
    anomaly =[]
    for i in fedvalue:
        runTime = runTime + 1
        if len(trainvalue) < len(fedvalue):
         required_len_Array = len(trainvalue) - len(fedvalue)
         trainvalue.append(0)
        else:
         if i == trainvalue[runTime]:
            sim = sim + fedvalue_sim_increase
         else:
            anomaly.append(fedvalue.index(i))
    if len(anomaly) == 0:
        return sim
    else:
        return sim