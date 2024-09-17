from MaestroPizzero import MaestroPizzero
from Mozo import Mozo
from pizza import Pizza
import os
import platform


class TesterPizzeria:
    def main(self):
        maestro_pizzero = MaestroPizzero("Alfredo")
        mozo1 = Mozo('Juan')
        mozo2 = Mozo('Carlos')

        print("Bienvenidos a pizzería de Don Pipo, este es nuestro menú:""\n" +"\n".join(Pizza.VARIEDADES))

        pizzas_selected = self.UserElection()

        maestro_pizzero.tomarPedido(pizzas_selected)
        maestro_pizzero.cocinar()

        pizzas_cooked = maestro_pizzero.entregar(pizzas_selected)
        pizzas_restantes =  []

        if mozo1.obtenerEstadoLibre():
            pizzas_restantes = mozo1.tomarPizzas(pizzas_cooked)  # Mozo 1 toma hasta 2 pizzas
            mozo1.servirPizzas()

        if pizzas_restantes and mozo2.obtenerEstadoLibre():
            mozo2.tomarPizzas(pizzas_restantes)  # Mozo 2 toma las restantes
            mozo2.servirPizzas()


    def UserElection(self):
        election = input("Por favor ingrese el número de la/s pizza/s elegida/s: (ej: 1,3) ")
        self.limpiar_consola()
        selected = []
    
        for i in election.split(','):
            if i.isdigit():
                numero = int(i)
                if 1 <= numero <= len(Pizza.VARIEDADES):
                    selected.append(Pizza.VARIEDADES[numero])
                else:
                  print(f"'{i}' no es un número válido.")
        return selected
    
    def limpiar_consola(self):
        if platform.system() == "Windows":
            os.system("cls")
        else:
            os.system("clear") 

if __name__ == '__main__':
    testerPizzeria = TesterPizzeria()
    testerPizzeria.main() 

