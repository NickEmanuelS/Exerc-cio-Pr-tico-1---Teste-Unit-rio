def calculaMedia(lista):
    if len(lista) == 0:
        print("\nNão há nenhum item na lista")
        return 0
    else:
        soma = sum(lista)
        media = soma/len(lista)
        print("\nA média da lista {} é igual a: {}" . format(lista, media))
        return media

#Testes
import unittest

class TestCalculaMedia(unittest.TestCase):
    # Teste com lista vazia
    def test_calcula_media_lista_vazia(self):
        self.assertEqual(calculaMedia([]), 0)
    # Teste com um numero 
    def test_calcula_media_lista_com_um_elemento(self):
        self.assertEqual(calculaMedia([10]), 10)
    # Teste com mais de um numero    
    def test_calcula_media_lista_com_elementos(self):
        self.assertEqual(calculaMedia([1, 2, 3, 4, 5]), 3)
    # Teste com numero decimal    
    def test_calcula_media_lista_com_casa_decimal(self):
        self.assertEqual(calculaMedia([8, 7, 4, 9.3, 23]), 10.26)
        
if __name__ == '__main__':
    unittest.main()