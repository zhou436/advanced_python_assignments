import cProfile
import primes
import cy_primes

cProfile.run('primes.primes(2000)')
cProfile.run('cy_primes.primes(2000)')