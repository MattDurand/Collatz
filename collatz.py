# The Number we will perform the Collatz operation on.
int(n) = input("Enter a Positive Integer: ")

#Keep looping until we reach 1.
#Npte: This assumes the Collatz conjecture is true.
while n != 1:
    # Print the current value of n.
    print(n)
    if n % 2 == 0:
        # If n is even, divide it by 2.
        # '//' is used for Integer division.
        n= n // 2
    else:
        # If n is odd, multiply it by 3 and add 1.
        n = (3 * n) + 1

#Finally, print the 1.
print(n)