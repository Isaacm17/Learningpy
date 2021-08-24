class calculadora():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b 

    def sub(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        return self.a / self.b

def activar():
    while True:
        print("---Menu--- Presione un numero para acceder a las opciones")
        print("""
1.-Suma
2.-Resta
3.-Multiplicacion
4.-Division
5.-Salir        
        """)
        op = int(input(">>> "))
        if op in (1,2,3,4,5):
            try:
                a1 = int(input("Ingrese el primer numero: "))
            except ValueError as error:
                print(f"Usted ingreso un valor erroneo {error}")
                break
            try:
                b1 = int(input("Ingrse el segundo numero: "))
            except ValueError as error:
                print(f"Usted ingreso un valor erroneo {error}")
                break
            cl = calculadora(a1, b1)
            if op==5:
                break
            if op==1:
                
                print(" ---Resultado--- ")
                print(f" {a1} + {b1} = {cl.add()}")
                print(" ")
                
            elif op==2:
                
                print(" ---Resultado--- ")
                print(f" {a1} - {b1} = {cl.sub()}")
                print(" ")
                
            elif op==3:
                
                print(" ---Resultado--- ")
                print(f" {a1} * {b1} = {cl.multiply()}")
                print(" ")
                
            elif op==4:
                
                print(" ---Resultado--- ")
                print(f" {a1} / {b1} = {cl.divide()}")
                print(" ")
                
        else:
            print("____________________Ingrese una opcion (numero) valido________________________")
