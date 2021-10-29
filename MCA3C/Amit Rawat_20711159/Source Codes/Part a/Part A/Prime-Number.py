# AMIT RAWAT MCA 3 - DEHRADUN Campus STD ID-20711159

num=int(input("Enter a number to check prime number or not: "))

if num>1:

    for i in range(2,num):
        if (num % i)==0:
            print(num, " is not prime number")
            break;
    else:
        print(num, " is a prime number")

else:
    print(num, " is not prime number")