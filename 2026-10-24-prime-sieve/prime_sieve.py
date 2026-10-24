"""Find all prime numbers up to a limit using the Sieve of Eratosthenes."""
import sys


def sieve(limit):
    """Return a list of all primes less than or equal to limit."""
    if limit < 2:
        return []
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for n in range(2, int(limit ** 0.5) + 1):
        if is_prime[n]:
            for multiple in range(n * n, limit + 1, n):
                is_prime[multiple] = False
    return [n for n, flag in enumerate(is_prime) if flag]


def main():
    if len(sys.argv) > 1:
        raw = sys.argv[1]
    else:
        raw = input("Find primes up to: ")
    try:
        limit = int(raw)
    except ValueError:
        print("Please enter a whole number.")
        return
    primes = sieve(limit)
    print(f"Found {len(primes)} primes up to {limit}:")
    print(" ".join(str(p) for p in primes))


if __name__ == "__main__":
    main()
