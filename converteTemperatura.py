def converteTemperatura(celsius):
    fahrenheit = (celsius * 1.8) + 32
    print(str(celsius )+ " graus Celsius é igual a " + str(fahrenheit )+ " graus Fahrenheit.")
    return fahrenheit


#Testes
import unittest

class TestConverteTemperatura(unittest.TestCase):
    # Teste com 0Cº 
    def test_zero_celsius(self):
        self.assertEqual(converteTemperatura(0), 32)
    # Teste com 10Cº    
    def test_dez_graus_celsius(self):
        self.assertEqual(converteTemperatura(10), 50)
    # Teste com 1000Cº (numero grande)    
    def test_mil_graus_celsius(self):
        self.assertEqual(converteTemperatura(1000), 1832)
    # Teste com temperatura negativa    
    def test_temperatura_negativa(self):
        self.assertEqual(converteTemperatura(-10), 14)
        
if __name__ == '__main__':
    unittest.main()
