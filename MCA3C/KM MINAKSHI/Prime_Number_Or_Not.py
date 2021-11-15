# KM MINAKSHI 20712152  MCA 3C GEHU Dehradun

num = int(input("Enter a number to check prime number or not: "))

if num > 1:

    for i in range(2, num):
        if (num % i) == 0:
            print(num, " is not prime number")
            break
    else:
        print(num, " is a prime number")

else:
    print(num, " is not prime number")
