name = input("Enter your name: ").capitalize()
age = input("Enter your name: ")
while True:
    if (name.isascii and age.isdigit): 
        print(f"Hello, {name}, you are {age} old")
        break
    else:
        print("Name or age is incorrect")
        