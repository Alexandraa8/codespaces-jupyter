factorial_cache = {}
 
def factorial(n):
      if n in factorial_cache:
           return factorial_cache[n]
      elif n == 0:
           return 1
      else:
         result = n * factorial(n-1)
         factorial_cache[n] = result
         return result
