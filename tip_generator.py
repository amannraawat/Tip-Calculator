print("\n\nWelcome to the tip calculator.")
total_bill = input("What was your total bill? $")
per_tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
no_of_people = int(input("How many people to split the bill? "))

if per_tip==10:
    tip_gen=(10*float(total_bill))/100.0
    new_total_bill = tip_gen + float(total_bill)
    distributed_am = round(new_total_bill / no_of_people , 2)
    print("Each person should pay ${:.2f}".format(distributed_am))

elif per_tip==12:
    tip_gen=(12*float(total_bill))/100.0
    new_total_bill = tip_gen + float(total_bill)
    distributed_am = round(new_total_bill / no_of_people , 2)
    print("Each person should pay ${:.2f}".format(distributed_am))

elif per_tip==15:
    tip_gen=(15*float(total_bill))/100.0
    new_total_bill = tip_gen + float(total_bill)
    distributed_am = round(new_total_bill / no_of_people , 2)
    print("Each person should pay ${:.2f}".format(distributed_am))
    
else:
    print("Invalid input.")
    

