import math

x = math.sqrt(16)
print(x)

# CALCULOS NUMERICOS
class CalculosNumericos:
    def __init__(self, numero: float):
        self.numero = numero

    # logaritmo neperiano
    def logaritmo_neperiano(self):
        try:
            if self.numero < 0:
                raise ArithmeticError("recuerda que el valor debe ser un numero positivo para calcular el logaritmo")

            resultado = math.log(self.numero)
            print(f"el logaritmo es: {resultado}")

        except ArithmeticError as e:
            print(e)

    def calcular_raiz(self):
        try:
            if self.numero < 0:
                raise ArithmeticError("recuerda que el valor debe ser un numero positivo para calcular la raiz cuadrada")

            resultado = math.sqrt(self.numero)
            print(f"la raiz cuadrada es: {resultado}")

        except ArithmeticError as e:
            print(e)


def main():
    try:
        entrada = input("Valor numérico = ")
        numero = float(entrada)

        calculos = CalculosNumericos(numero)
        calculos.logaritmo_neperiano()
        calculos.calcular_raiz()

    except ValueError:
        print("Por favor, ingresa un número válido.")


if __name__ == "__main__":
    main()