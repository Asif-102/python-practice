stringHour = input('Enter Hours: ')
stringRate = input('Enter Rate: ')

try:
    floatingHour = float(stringHour)
    floatingRate = float(stringRate)
except:
    print('Error, please enter numeric input')
    quit()

print(floatingHour, flatingRate)
if floatingHour > 40:
    print('Overtime')
    regularPay = floatingHour * floatingRate
    overTimePay = (floatingHour - 40.0) * (floatingRate*0.5)
    # print(regularPay, overTimePay)
    totalPay = regularPay + overTimePay 
else:
    print('Regular')
    totalPay = floatingHour*floatingRate
print('Pay:', totalPay)