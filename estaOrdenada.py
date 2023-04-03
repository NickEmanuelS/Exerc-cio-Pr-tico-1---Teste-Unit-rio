def estaOrdenada(test_list):
    
    # print ("Original list : " + str(test_list))
    
    # using naive method to
    # check sorted list
    flag = 0
    if(test_list == sorted(test_list)):
        flag = 1
        
    # printing result
    if (flag) :
        print ("A lista", test_list ,"está ordenada.")
        return True
    else :
        print ("A lista", test_list ,"não está ordenada.")
        return False
    

#Testes    
import unittest

class TestEstaOrdenada(unittest.TestCase):
    
    def test_lista_vazia(self):
        self.assertEqual(estaOrdenada([]), True)
        
    def test_lista_ordenada(self):
        self.assertEqual(estaOrdenada([1, 2, 3, 4, 5]), True)
        
    def test_lista_nao_ordenada(self):
        self.assertEqual(estaOrdenada([5, 2, 3, 4, 1]), False)
        
    def test_lista_com_elementos_iguais(self):
        self.assertEqual(estaOrdenada([1, 2, 3, 3, 4, 5]), True)
        
if __name__ == '__main__':
    unittest.main()