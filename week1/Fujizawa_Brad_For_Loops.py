# Basics
for i in range(0,151):
    print(i)

# Multiples of 5
for i in range(5,1001,5):
    print(i)

# Counting, the Dojo Way
for i in range(1,101):
    if i % 10 == 0:
        print('Coding Dojo')
    elif i % 5 == 0:
        print('Coding')
    else:
        print(i)

# Whoa, that sucker's huge
sum = 0 
for i in range(500000):
    sum += i
print(sum)

# Countdown by Fours
for i in range(2018, 0, -4):
    print(i)


# Flexible Counter
low_num = 0
high_num = 50
mult = 5

for i in range(low_num, high_num + 1, mult):
    print(i)