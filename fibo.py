num_01, num_02 = 0, 1
count = 0
prime_num = 0
list_of_fibonacci = []

while count < 100:
    list_of_fibonacci.append(num_01)
    # print(num_01)
    nth = num_01 + num_02
    num_01 = num_02
    num_02 = nth
    count += 1
x = list(map(int, input().strip().split()))


def prime_number_check(user_input):
    prime_val = 0
    if user_input > 1:
        for i in range(2, user_input):
            if (user_input % i) == 0:
                break
            else:
                prime_val = user_input
    return prime_val


new_list = []
for user_input in x:
    prime_num = prime_number_check(user_input)
    occured_times = list_of_fibonacci.count(prime_num)
    if prime_num > 0 and occured_times > 0:
        new_list.append(prime_num)


new_set = set(new_list)
s = list(new_set)
occ_list = []

for i in s:
    occured_times_new = new_list.count(i)
    occ_list.append(occured_times_new)
for i in range(len(s)):
    print(s[i], occ_list[i])


