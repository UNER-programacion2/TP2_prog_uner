class Mozo:
    def __init__(self, nom):
        self.nombre = nom
        self.pizzas = []

    def __str__(self) -> str:
         return f" Mozo: {self.nombre}"
    
    def __eq__(self, other):
        return isinstance(other, Mozo) and self.nombre == other.nombre

    def establecerNombre(self, nombre):
            self.nombre = nombre
    
    def tomarPizzas(self, pizzas):
        max_pizzas = 2 - len(self.pizzas) # Solo puede tomar hasta 2 pizzas
        pizzas_a_tomar = pizzas[:max_pizzas]  # Tomar las primeras que pueda servir
        self.pizzas.extend(pizzas_a_tomar)

        print(f"El mozo {self.nombre} ha tomado {len(pizzas_a_tomar)} pizzas para servir.")
        
        return pizzas[max_pizzas:]  # Devolver las restantes que no tomó
    
    def servirPizzas(self):
        if len(self.pizzas) > 0:
            self.pizzas = []
            print("Pizzas servidas!")
        else:
            print("Este mozo no tiene pizzas para servir!")

    #Consultas
    def obtenerNombre(self):
        return self.nombre
    
    def obtenerPizzas(self):
        return self.pizzas 

    def obtenerEstadoLibre(self) -> bool:
        return len(self.pizzas) < 2
        


#mozo1 = Mozo('Alfredo')
#mozo2 = Mozo('Alfredo')  

# # print(mozo1 is mozo2)
#print(mozo1 == mozo2)

#print(id(mozo1))  
# print(id(mozo2))  
