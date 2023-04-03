from math import sqrt

def ehPrimo(n):
    prime_flag = 0
    
    if(n > 1):
        for i in range(2, int(sqrt(n)) + 1):
            if (n % i == 0):
                prime_flag = 1
                break
        if (prime_flag == 0):
            print("O número "  + str(n)+ " é primo.")
            return True
        else:
            print("O número "  + str(n)+ " não é primo.")
            return False
    else:
        print("O número "  + str(n)+ " não é primo.")
        return False
    
    
import unittest

class TestEhPrimo(unittest.TestCase):
    
    def test_um_nao_eh_primo(self):
        self.assertFalse(ehPrimo(1))
        
    def test_dois_eh_primo(self):
        self.assertTrue(ehPrimo(2))
        
    def test_tres_eh_primo(self):
        self.assertTrue(ehPrimo(3))
        
    def test_numeros_grandes(self):
        self.assertFalse(ehPrimo(123456789))
        
if __name__ == '__main__':
    unittest.main()