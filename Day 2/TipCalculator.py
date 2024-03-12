#Welcome Message
print("Welcome to the tip calculator.")

#Input bill amount and save in float type to variable bill
bill=float(input("What was the total bill? : "))

#Input percentage of tip and store in int type to variable tip_percent
tip_percent=int(input("What percentage tip you would like to give? 10, 12 or 15 ? : "))

#Input number of people
no_of_people=int(input("How many people to split the bill? : "))

#Calculate the amount to be paid by each person after adding tip to the bill
''' Eg: Tip percentage is 10

Total Bill after Tip =  bill + 10 percent of bill

Amount per person= Total Bill after tip / number of people

'''
payment= (bill+((tip_percent/100)*bill))/no_of_people

#------- Print Amount to be paid by each person, rounding upto 2 decimal places (All below statements will give the same answer)------------
#print("Each person should pay: {:.2f}".format(round(payment,2)) )
#print("Each person should pay: %.2f" % round(payment,2))
#print("Each person should pay: {:.2f}".format(payment,2) )
#print("Each person should pay: %.2f" % (payment))
print("Each person should pay: ",round(payment,2))
