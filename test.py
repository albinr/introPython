# name = input('Enter your name: ')
# print('Hello', name)

# hours =  int(input('Enter hours: '))
# rate = int(input('Enter rate: '))
# pay = hours * rate

# print('Pay:', pay)

# celsius = int(input('Enter Temperature in celsius: '))

# fahrenheit = celsius * 1.8 + 32

# print(fahrenheit)

inp = input('Enter Fahrenheit Temperature: ')

try:
    fahr = float(inp)
    cel = (fahr - 32) * 5.0 / 9.0
    print(cel)
except:
    print('Please enter a number')