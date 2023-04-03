def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n-1)
    

#Testes    
import unittest

class TestFatorial(unittest.TestCase):
    # Fatorial de 0
    def test_fatorial_zero(self):
        self.assertEqual(fatorial(0), 1)
    # Fatorial de 1    
    def test_fatorial_um(self):
        self.assertEqual(fatorial(1), 1)
    # Fatorial de 5    
    def test_fatorial_positivo(self):
        self.assertEqual(fatorial(5), 120)
    # Fatorial de numero negativo    
    def test_fatorial_negativo(self):
        with self.assertRaises(ValueError):
            fatorial(-5)
        
if __name__ == '__main__':
    unittest.main()