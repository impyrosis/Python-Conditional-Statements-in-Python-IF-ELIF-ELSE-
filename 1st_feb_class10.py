# 1. Create a new program in PyCharm where you will check the current weather and display funny messages based on user input.

print(" What kind of weather is it today? ")
weather = str(input())
if weather == 'sunny':
    print("time to put on glasses & shorts")
elif weather == 'clear':
    print ("hangout time")
elif weather == 'rain':
    print ("not again Raincouver")
elif weather == 'rainy':
    print ("not again Raincouver")
elif weather == 'cloudy':
    print("I am not going outside")
elif weather == 'hot':
    print("Lets grab some Ice Cream")
elif weather == 'Snow':
    print("Lets grab our shovel from backyard")
elif weather == 'Storm':
    print("Its time for some power outage")
elif weather == 'Stormy':
    print("Its time for some power outage")
elif weather == 'cold':
    print('noses are red ,fingers are blue, I am tired of winter, what about you ? ')
elif weather == 'windy':
    print(' Be careful with your hat, strong winds blowing ')
else:
    print("Whatever the weather is today, I believe Spring is coming soon")



# 2. If the user enters integer values more than 0 but less than 15 degrees, display a message to wear something related to that weather condition.

print(" What Do you think its temperature today my friend? ")
a = int(input())
if a <= 10: print("its a nice day for light sweater".format(a))
if a > 10: print("I am melting dude".format(a))

# 3. If the user enters integer values more than 15 but less than 35 degrees, display a message to wear something related to that weather condition.

print(" What Do you think its temperature today my friend? ")
a = int(input())
if 15 < a < 35: print("put on sun glasses and get ready for Kayak".format(a))


# 4. If the user enters integer values more than 35 degrees, display a message to wear something related to that weather condition.

print(" What Do you think its temperature today my friend? ")
a = int(input())
if a > 35: print("Yes! I am in formal relationship with my Air Conditioner now".format(a))

# 5. If the user enters integer values less than 0 degrees, display a message to wear something related to that weather condition.

print(" What Do you think its temperature today my friend? ")
a = int(input())
if a < 0: print("Dear Winter, I am breaking up with you. I think its time I start seeing other seasons. Summer is hotter than you".format(a))