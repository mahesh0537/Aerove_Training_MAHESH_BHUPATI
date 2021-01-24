def check_prime(i):
    max_num = int(i**(1.0/2))
    for j in range (2, max_num+1):
        if i % j == 0:
            return False
    return True

n = int(input("Enter the decimal digits : "))
prime_list = []
for i in range (10**(n-1) , 10**n):
    if i == 1:
        continue
    if check_prime(i) :
        prime_list.append(i)
#print(prime_list)

with open("myFirstFile.txt", "w") as file1:
    last_prime_number = prime_list[0]
    for j in prime_list:
        if j - last_prime_number == 2:
            file1.write(str(last_prime_number))
            file1.write(" ")
            file1.write(str(j))
            file1.write('\n')
        last_prime_number = j