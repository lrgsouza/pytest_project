#implementar os testes para a calculadora.py utilizando pytest

import calculadora

def test_somar():
    assert calculadora.somar(2, 2) == 4

def test_subtrair():
    assert calculadora.subtrair(2, 2) == 0

def test_multiplicar():
    assert calculadora.multiplicar(2, 2) == 4

def test_multiplicar_erro():
    assert calculadora.multiplicar(3, 7) != 3

def test_dividir():
    assert calculadora.dividir(2, 2) == 1
