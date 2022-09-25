seed = 7182

def ran():
    global seed
    s= str(seed**2)
    while(len(s) != 8):
        s="0"+s
    
    seed=int(s[2:6])

    return seed

for i in range(0,15):
    print(ran()," ")
