class Vendedor:
    def __init__(self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = 0
    
    def imprimir(self):
        print(f"Nombre: {self.nombre}")
        print(f"Apellidos: {self.apellidos}")
        print(f"Edad: {self.edad}")
        
    def verificar_edad(self, edad):
        if edad < 18:
            raise ValueError("El vendedor debe ser mayor de edad")
        elif edad <= 0 or edad > 120:
            raise ValueError("La edad no puede ser negativa ni mayor a 120")
        else:
            pass
    
    def main(self):
        self.nombre = input("Ingrese el nombre del vendedor: ")
        self.apellidos = input("Ingrese los apellidos del vendedor: ")
        
        while True:
            try:
                edad_input = input("Ingrese la edad del vendedor: ")
                self.edad = int(edad_input)
                self.verificar_edad(self.edad)
                break
            except ValueError as e:
                print(f"Error: {e}. Por favor, intente nuevamente.")
        
        self.imprimir()
        
if __name__ == "__main__":
    vendedor = Vendedor("", "")
    vendedor.main()