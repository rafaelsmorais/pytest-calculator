import pytest
import Calculator

calculator = Calculator.Calculator()

def test_somar_positivo():
    assert calculator.somar(2,2) == 4
