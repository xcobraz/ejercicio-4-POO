class PruebaExcepciones:
    def __init__(self, cociente, objeto):
        self.cociente = cociente
        self.objeto = objeto
    
    def main(self):
        try:
            print("Ingresando primer try")
            self.cociente = 10000/0
            
        except:
            print("Error: División por cero")
        finally:
            print("Ingresando al primer finally")
        
        try:
            print("Ingresando segundo try")
            self.objeto = None
            self.objeto.upper()
            print("Imprimiento objeto")
            
        except:
            print("División por cero")
            print("Ocurrió una excepción")
        finally:
            print("Ingresando al segundo finally")

if __name__ == "__main__":
    prueba = PruebaExcepciones(0, "")
    prueba.main()