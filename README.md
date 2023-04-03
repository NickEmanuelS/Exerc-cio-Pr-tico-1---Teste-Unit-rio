# Teste Unitário
Exercício Prático da matéria de Teste e Manutenção de Software - S.I PUC MINAS

# Questão 1
Crie uma função "calculaMedia" que recebe uma lista de números inteiros e retorna a média desses números.

Os casos de testes são:
1. Uma lista vazia
```python
def test_calcula_media_lista_vazia(self):
        self.assertEqual(calculaMedia([]), 0)
output: True
```
2. Lista com um elemento
```python
def test_calcula_media_lista_com_um_elemento(self):
        self.assertEqual(calculaMedia([10]), 10)
output: True
```
3. Lista com vários elementos
```python
def test_calcula_media_lista_com_elementos(self):
        self.assertEqual(calculaMedia([1, 2, 3, 4, 5]), 3)
output: True
```
4. Lista com casa decimal
```python
def test_calcula_media_lista_com_casa_decimal(self):
        self.assertEqual(calculaMedia([8, 7, 4, 9.3, 23]), 10.26)
output: True
```

# Questão 2
Crie uma função "estaOrdenada" que receba uma lista de números inteiros e retorne True se a lista estiver classificada em ordem crescente e False caso contrário.

Os casos de testes são:
1. Uma lista vazia
```python
def test_lista_vazia(self):
        self.assertEqual(estaOrdenada([]), True)
```
2. Lista já ordenada
```python
def test_lista_ordenada(self):
        self.assertEqual(estaOrdenada([1, 2, 3, 4, 5]), True)
```
3. Lista não ordenada
```python
def test_lista_nao_ordenada(self):
        self.assertEqual(estaOrdenada([5, 2, 3, 4, 1]), False)
```
4. Lista com elementos iguais
```python
def test_lista_com_elementos_iguais(self):
        self.assertEqual(estaOrdenada([1, 1, 1, 1, 1]), True)
```

# Questão 3
Crie uma função fatorial que receba um número inteiro e retorne o fatorial desse número. O fatorial de um número é o produto de todos os inteiros positivos de 1 a esse número. Por exemplo, o fatorial de 5 é 5 * 4 * 3 * 2 * 1 = 120.

Os casos de testes são:
1. O fatorial de 0
```python
def test_fatorial_zero(self):
        self.assertEqual(fatorial(0), 1)
output: True
```
2. O fatorial de 1
```python
def test_fatorial_um(self):
        self.assertEqual(fatorial(1), 1)
output: True
```
3. O fatorial de um número positivo (5)
```python
def test_fatorial_positivo(self):
        self.assertEqual(fatorial(5), 120)
output: True
```
4. O fatorial de um número negativo (-5), que retorna um ValueError
```python
def test_calcula_media_lista_vazia(self):
        self.assertEqual(calculaMedia([]), 0)
output: ERROR
```

# Questão 4
Crie uma função "convertTemperature" que receba um valor de temperatura em graus Celsius e retorne o valor equivalente em Fahrenheit. A fórmula para converter Celsius em Fahrenheit é: F = (C * 1,8) + 32.

Os casos de testes são:
1. 0 graus Celsius
```python
def test_zero_celsius(self):
        self.assertEqual(converteTemperatura(0), 32)
```
2. 10 graus Celsius
```python
def test_dez_graus_celsius(self):
        self.assertEqual(converteTemperatura(10), 50)
```
3. 100 graus Celsius
```python
def test_mil_graus_celsius(self):
        self.assertEqual(converteTemperatura(1000), 1832)
```
4. -10 graus Celsius
```python
def test_temperatura_negativa(self):
        self.assertEqual(converteTemperatura(-10), 14)
```

# Questão 5
Crie uma função "ehPrimo" que receba um número inteiro e retorne True se o número for primo e False caso contrário. Um número é primo se for divisível apenas por 1 e por ele mesmo.

Os casos de testes são:
1. O número 1, que não é primo
```python
def test_um_nao_eh_primo(self):
        self.assertFalse(ehPrimo(1))
```
2. 2 que é primo
```python
def test_dois_eh_primo(self):
        self.assertTrue(ehPrimo(2))
```
3. 3 que é primo
```python
def test_tres_eh_primo(self):
        self.assertTrue(ehPrimo(3))
```
4. Um número grande que não é primo
```python
def test_numeros_grandes(self):
        self.assertFalse(ehPrimo(123456789))
```

# Questão 6
A partir da função "listaOrdenada" que recebe uma lista de números e retorna True se a lista estiver em ordem crescente ou decrescente e False caso contrário.

Os casos de testes são:
1. Uma lista vazia, que está ordenada
```python
def test_lista_vazia(self):
        self.assertTrue(listaOrdenada([]))
```
2. Crescente, que está ordenada
```python
def test_lista_crescente(self):
        self.assertTrue(listaOrdenada([1,2,3,4,5]), msg="A lista está ordenada")
```
3. Decrescente, que está ordenada
```python
def test_lista_decrescente(self):
        self.assertTrue(listaOrdenada([5,4,3,2,1]), msg="A lista está ordenada")
```
4. Não está ordenada
```python
def test_lista_desordenada(self):
        self.assertFalse(listaOrdenada([3,1,5,2,4]), msg="A lista está desordenada")
```
