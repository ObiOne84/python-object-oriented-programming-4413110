import math

def get_prime_factors(num):
  """The function returns all primes that are factors of the number"""
  factors = []
  divisor = 2
  while divisor <= num:
    if num % divisor == 0:
      factors.append(divisor)
      num = num // divisor
    else:
      divisor += 1
    
  return factors
  

print(get_prime_factors(7))