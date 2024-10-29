#!/usr/bin/python3
"""0. Prime Game"""


def isWinner(x, nums):
    """isWinner"""
    def sieve(limit):
        """Use Sieve of Eratosthenes to precompute prime numbers up to limit"""
        is_prime = [True] * (limit + 1)
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(limit**0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, limit + 1, i):
                    is_prime[j] = False
        return is_prime

    # Precompute primes up to the maximum number in nums
    max_n = max(nums) if nums else 0
    is_prime = sieve(max_n)

    # Precompute the number of prime moves possible up to each number
    prime_moves = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_moves[i] = prime_moves[i - 1] + (1 if is_prime[i] else 0)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_moves[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
