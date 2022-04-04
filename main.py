bill = input("What is current bill? ")
person = input("How many people to split the bill? ")
tip = input("How much tip you want to give? 5%, 10%, 15% or 20% ?")
tip_percent = float(tip)/100*float(bill)
bill_with_tip = float(bill)+tip_percent
bill_per_person = bill_with_tip/int(person)
#print(bill_per_person)
final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person have to pay amount:  {final_amount}")
