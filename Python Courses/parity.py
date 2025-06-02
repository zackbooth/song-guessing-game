def main():
    x = int(input("Boy, HWHAT is X? "))

    if is_even(x):
        print("EVEN")

    else:
        print("odd")

def is_even(n):
    return n % 2 == 0 

main()