# Class definition
class Factorial:
    # Calculated values
    _values={0:1}

    # private Factorial calculating
    def _fact(self, n) :
        if n==1 or n==0 :
            self._values[n]=1
            return 1
        m = self._fact(n-1)*n
        self._values[n]=m
        return m

    # Get result from cash or func...
    def Calc(self, n):
        if n in self._values:
            print('From cash:',self._values[n])
        else:
            self._fact(n)
            print('From func:',self._values[n])

# Main programm
f = Factorial()
n=0
try:
    while n.is_integer():
        n = int(input('N> '))
        f.Calc(n)
except ValueError:
    print('End programm...')