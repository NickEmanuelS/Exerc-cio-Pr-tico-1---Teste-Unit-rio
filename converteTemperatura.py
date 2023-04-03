def converteTemperatura(celsius):
    fahrenheit = (celsius * 1.8) + 32
    print(str(celsius )+ " graus Celsius é igual a " + str(fahrenheit )+ " graus Fahrenheit.")
    return fahrenheit


#Testes
import unittest

class TestConverteTemperatura(unittest.TestCase):
    
    def test_zero_celsius(self):
        self.assertEqual(converteTemperatura(0), 32)
        
    def test_dez_graus_celsius(self):
        self.assertEqual(converteTemperatura(10), 50)
        
    def test_vinte_graus_celsius(self):
        self.assertEqual(converteTemperatura(20), 68)
        
    def test_temperatura_negativa(self):
        self.assertEqual(converteTemperatura(-10), 14)
        
if __name__ == '__main__':
    unittest.main()
