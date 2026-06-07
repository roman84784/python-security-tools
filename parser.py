import operator
def serch_failed(poisk, n):
    schet=0
    ip_count={}
    for i in poisk:
        if "Failed" in i:
            schet+=1
            ip=i.split()[10]
            if ip in ip_count:
                ip_count[ip]+=1
            else:
                ip_count[ip]=1
    return (sorted(ip_count.items(),key= operator.itemgetter(1),reverse=True))[:n]
with open("auth.log", "r") as poisk:
    n = int(input("Выберете количество смаых повторяющихся айпи адресов: "))
    poisk = poisk.readlines()
    print(serch_failed(poisk,n))
