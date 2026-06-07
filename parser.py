with open("auth.log", "r") as file:
    schet=0
    lines = file.readlines()
    for i in lines:
        if "Failed" in i:
            schet+=1
            print(i)
    print(schet)