
for num in range(0,150 + 1):
    print(num)

print("***********************")

for num in range(0,1000 + 1,5):
    print(num)

print("***********************")

for num in range(1,100 + 1):
    if num % 5 == 0:
        print("Coding Dojo")
    else:
        print(num)

print("***********************")

sum = 0
for num in range(0,500000 + 1):
    if num % 2 != 0:
        sum += num
print(sum)

print("***********************")

x = 2018
while(x > 0):
    if x % 2 == 0:
        print(x)
    x -= 4

print("***********************")

lowNum, highNum, mult = 2, 10, 3

for num in range(lowNum, highNum + 1):
    if num % mult == 0:
        print(num)