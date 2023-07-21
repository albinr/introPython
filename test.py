# name = input('Enter your name: ')
# print('Hello', name)

# hours = int(input('Enter hours: '))
# rate = int(input('Enter rate: '))

# if hours > 40:
#     extra_time = int(hours - 40) * 1.5 * 10
#     gross_pay = (hours * rate) + extra_time
# else:
#     gross_pay = hours * rate

# print('Pay:', gross_pay)

hours = float(input('Enter Hours: '))
rate = float(input('Enter Rate: '))

if hours > 40:
    extra_time = float(hours - 40) * 1.5 * 10
    gross_pay = (hours * rate) + extra_time
else :
    gross_pay = hours * rate

print(gross_pay)

# celsius = int(input('Enter Temperature in celsius: '))

# fahrenheit = celsius * 1.8 + 32

# print(fahrenheit)

# inp = input('Enter Fahrenheit Temperature: ')

# try:
#     fahr = float(inp)
#     cel = (fahr - 32) * 5.0 / 9.0
#     print(cel)
# except:
#     print('Please enter a number')