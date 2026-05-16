# num = int(input("Enter you mobile number: "))
num = str(input("Enter your mobile number: "))
# num = str("9877655432")

if num.isdigit():
    if len(num)==10:
        if num.startswith("9"):
            print("num is valid ")
        else:
            print("not valid")
else:
    print("not valid")