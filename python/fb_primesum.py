
class Solution:
    # @param A : integer
    # @return a list of integers
    def isPrime(self, x):
        for i in xrange(2, int(x ** 0.5)+1):
            if x % i == 0:
                return False
        return True

    def primesum(self, A):
        for i in xrange(2, A):
            if self.isPrime(i) and self.isPrime(A-i):
                return i, A-i
        return 0, 0
