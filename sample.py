print("1. INSURANCE")
print("2. HEALTH AND LIFE")
i=int(input("Enter your choice:"))
if i==1:
    class Insuranceclass:
        def __init__(self,policynum,monthly_premium):
            self.policynum=policynum
            self.monthly_premium=monthly_premium
        def display(self):
            print("POLICY NUMBER:",policynum)
            print("MONTHLY PREMIUM:",monthly_premium)
    lis=[]
    for i in range(2):
        policynum=int(input("Enter policy number:"))
        monthly_premium=int(input("Enter monthly premium"))
        obj=Insuranceclass(policynum,monthly_premium)
        lis.append(obj)
    for j in lis:
        j.display()
        

if i==2 or i==1:
    class health_life(Insuranceclass):
        def __init__(self,policy,monthly_pay):
            self.policy=policy
            self.monthly_pay=monthly_pay
        def display1(self):
            super()
            print("POLICY AVAIL:",policy)
            print("COST PER MONTH:",monthly_pay)
            
    lis1=[]
    for i1 in range(2):
        policy=input("Enter policy type:")
        monthly_pay=int(input("Enter monthly pay:"))
        obj1=health_life(policy,monthly_pay)
        lis1.append(obj1)
    for j1 in lis1:
        j1.display1()
   
        
