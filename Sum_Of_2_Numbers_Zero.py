def check_sum(num_list):
    for num1 in range(len(num_list)):
        for num2 in range(num1 + 1, len(num_list)):
            if num_list[num1] + num_list[num2] == 0:
                return True
    return False

print(check_sum([10, 14, 26, 5, -3, 13, -5]))
