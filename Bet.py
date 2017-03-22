strOdds=[]
odds=[]
stake=[]
chance=[]
multiplier=[]

print("Press Enter to Stop")
print()
val=input("Enter decimal odds:")

while val!="":
    strOdds.append(val)
    val=input("Enter stake:")
    print()
    x=float(val)
    stake.append(x)
    val=input("Enter decimal odds:")
   
        
for i in range (len(strOdds)):
    l=strOdds[i].split(" ")
    for j in range(len(l)):
        l[j]=float(l[j])
        
 
    odds.append(l)    
        

for i in odds:
    m=1
    for j in i:
        m=m*j
    multiplier.append(m)

win=0
for i in range (len(stake)):
    win=win+stake[i]*multiplier[i]

risk=0
for i in stake:
    risk=risk+i 
    
profit=win-risk        
 

for i in odds:
    c=1 
    for j in i:
        c=c*(1/j)
    chance.append(c)


totalChance=1
for i in chance:
    totalChance=totalChance*i
totalChance=totalChance*100

none=1
for i in chance:
    none=none*(1-i)
    
atleastone=(1-none)*100    


print()
print("Total risk is R"+str(risk))
print("Profit is R"+"{0:5.2f}".format(profit))
print("Chances of predicting all "+"{0:5.3f}".format(totalChance)+"%")
if len(stake)>1:
    print("Chances of at least one predicition "+"{0:5.3f}".format(atleastone)+"%")
 
