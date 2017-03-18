odds=[]
stake=[]
val=input("Enter decimal odds:")

while val!="":
    x=float(val)
    odds.append(x)
    val=input("Enter stake:")
    x=float(val)
    stake.append(x)
    val=input("Enter decimal odds:")
   
        
    
    
chance=1
for i in odds:
    
    chance=(i-1)/i*chance

risk=0
for i in stake:
    risk=risk+i 
    
multiplier=1
for i in odds:
    multiplier=multiplier*i
        
  
profit=risk*(multiplier-1)
        

        
   

print("Total risk is R"+str(risk))
print("Profit is R"+str(profit))
print("Chances of winning are "+str(chance)+"%")
print(str(multiplier))