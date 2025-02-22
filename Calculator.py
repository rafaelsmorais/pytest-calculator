class Calculator:
    def somar(x,y):
        return x + y;
    
    def subtrair(x,y):
        return x - y;

    def multiplicar(x,y):
        return x * y;

    def dividir(x,y):
        return x / y;
        
    def fatorial(n):
        if n == 0:
            return 1
        else:
            return n * fatorial(n - 1)

    def potencia(x,y):
        return pow(x,y)
