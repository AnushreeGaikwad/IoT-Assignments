#display face value
num = 9361 
temp = num 
print("Face Value")
d = int((num / 1000))
print(f"d = {d}")
c = int((num /100)%10)
print(f"c = {c}")
b = int((num / 10)%10)
print(f"b = {b}")
a = int((num % 10))
print(f"a = {a}")

#display reverse number
num = 9361
reversed_num = 0

while num != 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10

print("Reversed Number : " + str(reversed_num))




