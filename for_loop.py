float_list = [1.2, 3, 16.42, 10.77, 8.3, 34.21, 2.25]
print(float_list)

for i in range(1, len(float_list)):
    float_list[i] = float_list[i] * 2
    
for num in float_list:
    print(num)

print(float_list)

for i in range(1, 11):
    if i % 2 == 0:
        print(i, ": is even")
    else:
        print(i, ": is odd")

for i in range(1,11, 3):
    print(i)