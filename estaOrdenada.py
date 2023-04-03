def estaOrdenada(test_list):
    flag = 0
    if(test_list == sorted(test_list)):
        flag = 1

    if (flag) :
        print ("A lista", test_list ,"está ordenada.")
        return True
    else :
        print ("A lista", test_list ,"não está ordenada.")
        return False
    

#Testes    
import unittest

class TestEstaOrdenada(unittest.TestCase):
    # Teste com lista vazia
    def test_lista_vazia(self):
        self.assertEqual(estaOrdenada([]), True)
    # Teste com lista ordenada    
    def test_lista_ordenada(self):
        self.assertEqual(estaOrdenada([1, 2, 3, 4, 5]), True)
    # Teste com lista decrescente    
    def test_lista_nao_ordenada(self):
        self.assertEqual(estaOrdenada([5, 2, 3, 4, 1]), False)
    # Teste com lista vazia    
    def test_lista_com_elementos_iguais(self):
        self.assertEqual(estaOrdenada([1, 1, 1, 1, 1]), True)
        
if __name__ == '__main__':
    unittest.main()