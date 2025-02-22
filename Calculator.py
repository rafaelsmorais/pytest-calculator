class Calculator:
    def somar(self, x, y):
        return x + y;
    
    def subtrair(self, x, y):
        return x - y;

    def multiplicar(self, x ,y):
        return x * y;

    def dividir(self, x, y):
        return x / y;
        
    def fatorial(self, n):
        if n == 0:
            return 1
        else:
            return n * self.fatorial(n - 1)

    def potencia(self, x, y):
        return pow(x,y)
