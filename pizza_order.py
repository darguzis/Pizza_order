#  First try:


print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
price = 0

if size == "S" or size == "s":
    price += 15
    if pepperoni == "Y" or pepperoni == "y":
        price += 2
    else:
        price = price
    if extra_cheese == "Y" or extra_cheese == "y":
        price += 1
    else:
        price = price
    print("Your final bill is: $" + str(price) + ".")
elif size == "M" or size == "m":
    price += 20
    if pepperoni == "Y" or pepperoni == "y":
        price += 3
    else:
        price = price
    if extra_cheese == "Y" or extra_cheese == "y":
        price += 1
    else:
        price = price
    print("Your final bill is: $" + str(price) + ".")
elif size == "L" or size == "l":
    price += 25
    if pepperoni == "Y" or pepperoni == "y":
        price += 3
    else:
        price = price
    if extra_cheese == "Y" or extra_cheese == "y":
        price += 1
    else:
        price = price
    print("Your final bill is: $" + str(price) + ".")
else:
    print("Invalid option try again!")


# Better version:


print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
price = 0

if size == "S" or size == "s":
    price += 15
elif size == "M" or size == "m":
    price += 20
elif size == "L" or size == "l":
    price += 25
else:
    print("Invalid option, choose again!")

if pepperoni == "Y" or pepperoni == "y":
    if size == "S" or size == "s":
        price += 2
    else:
        price += 3

if extra_cheese == "Y" or extra_cheese == "y":
    price += 1

print(f"Your total price: ${price}")
