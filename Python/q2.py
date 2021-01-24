def check_palindrome_number(num):
    digit_in_num = []
    digit_in_num = digits(num)
    for i in range (0, int(len(digit_in_num)/2)):
        if digit_in_num[i] != digit_in_num[-i-1]:
            return False
    return True

def count(num):      #to count digits in num
    count_digits = 0
    while (num != 0):
        count_digits = count_digits + 1
        num = int(num / 10)
    return count_digits

def digits(num):            #once place will have location of 0
    digits_list = []
    while (num != 0):
        digits_list.append(int(num % 10))
        num = int(num/10)
    return digits_list

def mirror(n, even_digits):
    final_number = 0
    if(even_digits):
        digit_in_n = digits(n)
        num_of_digits_in_n = count(n)
        for j in range (0,num_of_digits_in_n):
            final_number += (digit_in_n[j] * int(10**(j + num_of_digits_in_n)))
            final_number += (digit_in_n[j] * int(10**(num_of_digits_in_n -j -1)))
        return final_number
    else:
        store_digit = int(n % 10)
        palindrome_num = mirror(int(n/10), True)
        num_of_digits_in_n = count(n)
        first_half = int(palindrome_num / (10**(num_of_digits_in_n - 1)))
        second_half = int(palindrome_num % (10**(num_of_digits_in_n - 1)))
        first_half = first_half*10 + store_digit
        return ((first_half*(10**(num_of_digits_in_n -1))) + second_half)

number = int(input("Enter the palindrome number : "))
if check_palindrome_number(number):
    if count(number) % 2 != 0:
        temp_num = int(number / (10**(int(count(number)/2))))
        if(count(temp_num) == count(temp_num + 1)):
            print(mirror(temp_num + 1, False))
        else:
            print(mirror(int((temp_num + 1)/10), True))
    if count(number) % 2 == 0:
        temp_num = int(number / (10**(int(count(number)/2))))
        if(count(temp_num) == count(temp_num + 1)):
            print(mirror(temp_num + 1, True))
        else:
            print(mirror(temp_num + 1, False))
else:
    print("Your number is not a palindrome number ")
