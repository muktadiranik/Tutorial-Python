def sieve_prime(n):
    prime = []
    for i in range(100):
        prime.append(0)

    for i in range(2, n + 1):
        if prime[i] == 0:
            for j in range(i ** 2, n + 1, i):
                prime[j] = 1

    for i in range(2, n):
        if prime[i] == 0:
            print(i, end=" ")

def check_prime(n):
    i = 2
    while i ** 2 <= n + 1:
        if n % i == 0:
            return False
        i = i + 1
    return True

def get_prime(n):
    for i in range(2, n + 1):
        if check_prime(i):
            print(i, end=" ")


if __name__ == "__main__":
    sieve_prime(50)
    print()
    get_prime(50)
