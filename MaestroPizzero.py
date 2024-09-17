from pizza import Pizza

class MaestroPizzero:

    def __init__(self, nombre): #constructor
        self.nombre = nombre
        self.pizzasPorCocinar = []
        self.pizzasPorEntregar =  []
    
    def __str__(self):
         return f"Maestro Pizzero: {self.nombre}"
    
#Comando: Cambia el estado de un objeto o de la aplicación (modifica datos).
    def establecerNombre(self, nombre):
            self.nombre = nombre

    def tomarPedido(self,var):
        if not var:
            raise ValueError("El pedido no puede estar vacío")
        pizza = Pizza(var) #creacion del objeto
        self.pizzasPorCocinar.append(pizza) #se agrega a pizzas por cocinar
        return pizza

    def cocinar(self):
        if self.pizzasPorCocinar:
            cooked =  self.pizzasPorCocinar.copy()
            for pizza in cooked:
                 self.pizzasPorEntregar.append(pizza)
        self.pizzasPorCocinar = [] #reinicia la lista (actualiza el estado)

    def entregar(self, pizzas):
        max_deliver = 2  # cuántas pizzas se puede entregar
        cantidad = len(pizzas)  

        if cantidad <= 0:
            print("No hay pizzas para entregar")
        else:
            print(f"El pizzero {self.nombre} ha entregado {cantidad} pizzas.")
            return pizzas 
        
        if not self.pizzasPorEntregar:  #verifica si la lista esta vacia, y retorna la lista vacia
            return []

        amount_pizzas = min(max_deliver, len(self.pizzasPorEntregar), cantidad)#cuántas pizzas se entregarán, tomando en cuenta el límite

        toSend = []
        for _ in range(amount_pizzas):
            pizza = self.pizzasPorEntregar.pop(0)  # Extraer la pizza y eliminar de la lista
            toSend.append(pizza)
    
        return toSend

# Consulta: Solo lee y devuelve información sin modificar el estado.
    def obtenerNombre(self): 
        return self.nombre
    
    def obtenerPizzasPorCocinar(self): 
        return self.pizzasPorCocinar

    def obtenerPizzasPorEntregar(self):
        return self.pizzasPorEntregar
    

