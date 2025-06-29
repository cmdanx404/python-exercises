# Project No. 9
# Gross Pay with Exception

hour = input("Enter Hour: ")

try:
    hour = float(hour)
except ValueError:
    print("Error, please enter numeric input for Hour")
    quit()
    
rate = input("Enter Rate: ")
try:
    rate = float(rate)
except ValueError:
    print("Error, please enter numeric input for Rate")
    quit()

if hour < 40:
    pay = round( hour * rate, 2)
    
else:
    overtime = hour - 40
    pay = round( 40 * rate + overtime * rate * 1.5, 2)
    
print (f"Pay: {pay}")