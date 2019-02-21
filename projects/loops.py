#loops

#for loops
for x in range(5):
    print("i will not fight the future ")
    print(x)

print("*******************")
for x in range(12,17):
    print("i will not fight the future ")
    print(x)

games=["mario bros 3", "earth bound", "pilot wings", "mario party"]

for y in games:
    print(y)

numbers = [76, 83, 16, 69, 52, 78, 10, 77, 45, 52, 32, 17, 58, 54, 79, 72, 55, 50, 81, 74, 45, 33, 38, 10, 40, 44, 70, 81, 79, 28, 83, 41, 14, 16, 27, 38, 20, 84, 24, 50, 59, 71, 1, 13, 56, 91, 29, 54, 65, 23, 60, 57, 13, 39, 58, 94, 94, 42, 46, 58, 59, 29, 69, 60, 83, 9, 83, 5, 64, 70, 55, 89, 67, 89, 70, 8, 90, 17, 48, 17, 94, 18, 98, 72, 96, 26, 13, 7, 58, 67, 38, 48, 43, 98, 65, 8, 74, 44, 92]
for number in numbers:
    if number%2==0:
        print(number)
        numbers.remove(number)
odds=set(numbers)
print(odds)

#while loops

age=27

while age < 100:
    print(age)
    age+=1

'''guess = input("guess a number between 1 and 10: ")
while guess != "8":
    guess = input("guess a number between 1 and 10: ")

print("You win!")'''

power=1
while 2**power <= 1000000000:
    #print("it's not")
    #print(power)
    power+=1

print(power)

for x in range(10):
    print(x)
    if x == 5:
        break # leaves the loop
    print("hey there")

print("All Done")

for x in range(10):
    print(x)
    if x == 5:
        continue # leaves this element of the loop but continues at next itteration
    print("hey there")

print("All Done")
