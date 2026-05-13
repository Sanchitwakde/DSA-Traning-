# num = int(input("Enter you mobile number: "))
num = input("Enter your mobile number: ")
count = 0
s = str(num)
if s.isdigit():
    if len(s)==10:
        if s.startswith(6,7,8):
            print("num is valid ")
        else:
            print("not valid")
