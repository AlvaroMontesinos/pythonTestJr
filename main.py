import unittest

# count zeros funtion

def count_zeros(number):
    # inicializamos el contador en 0
    count_zeros =0

    # mientras el numero sera entero mayor a 0 (exista)
    while number>0:
        # leemos el primer digito
        n = number%10
        # si es 0 incrementamos el contador
        if n==0:
            count_zeros+=1
        number=int(number/10)

    return count_zeros


class Test(unittest.TestCase):
    def test_count_zeros(self):
        self.assertEqual(0, count_zeros(1))
        self.assertEqual(1, count_zeros(10))
        self.assertEqual(3, count_zeros(10005))
        self.assertEqual(4, count_zeros(420013001))
        self.assertEqual(0, count_zeros(123456789))

unittest.main()