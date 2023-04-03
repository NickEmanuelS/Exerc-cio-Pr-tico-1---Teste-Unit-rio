def calculaMedia(lista):
    if len(lista) == 0:
        print("\nNão há nenhum item na lista")
        return 0
    else:
        soma = sum(lista)
        media = soma/len(lista)
        print("\nA média da lista {} é igual a: {}" . format(lista, media))
        return media


import unittest

class TestCalculaMedia(unittest.TestCase):
    
    def test_calcula_media_lista_vazia(self):
        self.assertEqual(calculaMedia([]), 0)
        
    def test_calcula_media_lista_com_um_elemento(self):
        self.assertEqual(calculaMedia([10]), 10)
        
    def test_calcula_media_lista_com_elementos(self):
        self.assertEqual(calculaMedia([1, 2, 3, 4, 5]), 3)
        
    def test_calcula_media_lista_com_casa_decimal(self):
        self.assertEqual(calculaMedia([8, 7, 4, 9.3, 23]), 10.26)
        
if __name__ == '__main__':
    unittest.main()