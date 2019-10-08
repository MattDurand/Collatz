# The Number we will perform the Collatz operation on.
n = 20

#Keep looping until we reach 1.
#Npte: This assumes the Collatz conjecture is true.
while n != 1:
    # Print the current value of n.
    print(n)
    if n % 2 = 0:
        # If n is even, divide it by two.
        n= n / 2
    else:
        # If n is odd, multiply it by three and add one.
        n = (3 * n) + 1

print(n)