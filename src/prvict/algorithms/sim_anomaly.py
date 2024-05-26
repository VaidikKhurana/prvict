from str_int import *
def sim_anomaly(trained_Data, tuple_data):
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
        if i == trainvalue[runTime]:
            sim = sim + fedvalue_sim_increase
        else:
            anomaly.append(fedvalue.index(i))
    if len(anomaly) == 0:
        return f"Similarity: {sim}"
    else:

        return f"Similarity: {sim}\nAnomalies on index(es) {anomaly}"