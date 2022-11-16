#Conversion Calculator
#By: Liza Méndez

#user input regarding the length to convert
#get the unit from the user
#convert the length to the correct unit
#output the answer to the user

user_number = float(input("What number would you like to convert? "))
user_unit = input("What unit is your number? ")

#to convert inches to millimeters -->> in x 25.4
#to convert millimeters to inches --> mm / 25.4

#user gives unit in inches
#conv_number = user_number * 25.4
conv_number = user_number / 25.4
if (user_unit == 'in'):
    #perform mm to in
    conv_number = user_number * 25.4
    conv_unit == 'mm'

elif (user_unit == 'mm'):
    #perform in to mm
    conv_number = user_number / 25.4
    conv_unit = 'in'
else:
    print('That is not a valid unit')

print(conv_number)
print(user_unit)