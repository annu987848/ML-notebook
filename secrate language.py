print("decode the secret language!")
word=input("enter a word:")
if word=="ankit"[::-1]:
    print("the decoded word is: tikna")
elif word=="i love u".replace("l","j").replace("e","a"):
    print("the decoded word is: i jova u")
else:
    print("no secret language detected")

name="annu";
country="India"
print(f"Hello, {name}! Welcome to {country}.")
print(f"Letter.format {name} from {country}.")
print("Letter.format {} from {}.".format(name, country))
price=49.99
quantity=3
total=price*quantity
print(f"Total price for {quantity} items is ${total:.2f}.")
