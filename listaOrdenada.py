def listaOrdenada ( lista ) :
    if len ( lista ) < 2:
        print("A lista " + str(lista) + " está ordenada")
        return True
    crescente = all ( lista [ i ] <= lista [ i +1] for i in range ( len ( lista )-1) )
    decrescente = all ( lista [ i ] >= lista [ i +1] for i in range ( len (lista ) -1) )
    return crescente or decrescente


#Testes
import unittest

class TestListaOrdenada(unittest.TestCase):
    # Teste com lista vazia
    def test_lista_vazia(self):
        self.assertTrue(listaOrdenada([]))
    # Teste com lista crescente    
    def test_lista_crescente(self):
        self.assertTrue(listaOrdenada([1,2,3,4,5]), msg="A lista está ordenada")
    # Teste com lista decrescente    
    def test_lista_decrescente(self):
        self.assertTrue(listaOrdenada([5,4,3,2,1]), msg="A lista está ordenada")
    # Teste com lista desordenada    
    def test_lista_desordenada(self):
        self.assertFalse(listaOrdenada([3,1,5,2,4]), msg="A lista está desordenada")
        
if __name__ == '__main__':
    unittest.main()