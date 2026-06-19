class Programador:


    def __init__(self, nombre: str, apellidos: str):

        self.nombre = nombre
        self.apellidos = apellidos


class EquipoMaratonProgramacion:


    def __init__(self, nombre_equipo: str, universidad: str, lenguaje_programacion: str):

        self.nombre_equipo = nombre_equipo
        self.universidad = universidad
        self.lenguaje_programacion = lenguaje_programacion

        # Atributo que define el tamaño actual del equipo (inicia en cero)
        self.tamano_equipo = 0

        # Lista que define los programadores que conforman el equipo

        self.programadores = [None] * 3

    def esta_lleno(self) -> bool:

        return self.tamano_equipo == len(self.programadores)

    def anadir(self, programador: Programador):

        try:
            if self.esta_lleno():
                # Si la lista está llena, se genera la excepción correspondiente
                raise Exception("El equipo está completo. No se pudo agregar programador.")

            # Se asigna el programador a la lista de programadores
            self.programadores[self.tamano_equipo] = programador
            self.tamano_equipo += 1  # Se incrementa el tamaño del equipo

        except Exception as e:
            print(e)

    @staticmethod
    def validar_campo(campo: str):

        try:
            for caracter in campo:
                if caracter.isdigit():
                    # Si el carácter es un dígito se genera la excepción correspondiente
                    raise Exception("El nombre no puede tener dígitos.")

            # Si la longitud del campo es mayor a 20 caracteres, se genera una excepción
            if len(campo) > 20:
                raise Exception("La longitud no debe ser superior a 20 caracteres.")

        except Exception as e:
            print(e)
            raise  # Se vuelve a lanzar para que main() decida si continúa o no


def main():

    try:
        nombre = input("Nombre del equipo = ")
        universidad = input("Universidad = ")
        lenguaje = input("Lenguaje de programación = ")

        equipo = EquipoMaratonProgramacion(nombre, universidad, lenguaje)

        print("Datos de los integrantes del equipo")

        for i in range(3):
            nombre_programador = input("Nombre del integrante = ")
            EquipoMaratonProgramacion.validar_campo(nombre_programador)  # Valida el nombre

            apellidos_programador = input("Apellidos del integrante = ")
            EquipoMaratonProgramacion.validar_campo(apellidos_programador)  # Valida el apellido

            programador = Programador(nombre_programador, apellidos_programador)  # Crea un programador
            equipo.anadir(programador)  # Añade el programador a la lista de programadores

    except Exception as e:
        print(f"No se pudo completar el registro: {e}")


if __name__ == "__main__":
    main()