def calculate_tip():
 cost = input("What is the cost?")
 cost = int(cost)
 tip_percent = input("What is the tip percentage?")
 tip_percent = float(tip_percent) 
 return cost * (tip_percent / 100)  

print(calculate_tip())
