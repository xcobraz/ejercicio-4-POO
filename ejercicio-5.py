# -*- coding: utf-8 -*-
import traceback


class EscribirArchivo:
    """
    Esta clase denominada EscribirArchivo tiene como objetivo escribir
    datos en un archivo de texto.
    """

    @staticmethod
    def main():
        archivo = None
        try:
            archivo = open("prueba.txt", "w")  # Se crea en la carpeta actual del script

            for i in range(10):
                archivo.write(f"Linea {i}\n")

        except Exception as e:
            traceback.print_exc()

        finally:
            try:
                if archivo is not None:
                    archivo.close()
            except Exception as e2:
                traceback.print_exc()


if __name__ == "__main__":
    EscribirArchivo.main()