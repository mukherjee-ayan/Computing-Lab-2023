lb = input("Enter lower bound: ").strip()
ub = input("Enter upper bound: ").strip()
n = int(input("Enter number of components: "))

lb = lb.replace(".","")
lb += "0" * (n-len(lb))
lb = int(lb)

ub = ub.replace(".","")
ub += "0" * (n-len(ub))
ub = int(ub)

for i in range(lb,ub+1):
    print(str(i).replace("",".").strip("."))
