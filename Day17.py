#Write your code here
class Calculator:
    def power(self, n , p):
        if((p < 0) or (n < 0)):
            raise Exception('n and p should be non-negative')
        else:
            return n**p