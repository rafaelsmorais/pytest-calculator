import pytest
import Calculator

calculator = Calculator.Calculator()

class TestSomar:
    def test_somar_positivo(self):
        assert calculator.somar(2,2) == 4
    
    def test_somar_negativo(self):
        assert calculator.somar(3,-2) == 1
        assert calculator.somar(-2,3) == 1

class TestSubtrair:
    def test_subtrair_positivo(self):
        assert calculator.subtrair(2,2) == 0
    
    def test_subtrair_negativo(self):
        assert calculator.subtrair(3,-2) == 5
        assert calculator.subtrair(-2,3) == -5

class TestMultiplicar:
    def test_multiplicar_positivo(self):
        assert calculator.multiplicar(2,2) == 4
        assert calculator.multiplicar(3,1) == 3
        assert calculator.multiplicar(5,0) == 0
    
    def test_multiplicar_negativo(self):
        assert calculator.multiplicar(3,-2) == -6
        assert calculator.multiplicar(-2,3) == -6

class TestDividir:
    def test_dividir_positivo(self):
        assert calculator.dividir(2,2) == 1.0
        assert calculator.dividir(3,1) == 3.0
        assert calculator.dividir(4,2) == 2.0
    
    def test_dividir_negativo(self):
        assert calculator.dividir(6,-2) == -3.0
        assert calculator.dividir(-8,4) == -2.0
