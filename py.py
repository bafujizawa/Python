digits = [9]
# for i in range(len(digits)):
#     print(digits[i])
# print(digits[len(digits) - 1])
digits[len(digits) - 1] += 1
if digits[len(digits) - 1] == 10:
    if(len(digits) == 1):
        digits = [1,0]
    else:
        digits[len(digits) - 2] += 1
        digits[len(digits) - 1] -= 10


print(digits)