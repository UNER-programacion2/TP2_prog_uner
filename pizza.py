class Pizza:

    VARIEDADES = [
        '1. Peperoni',
        '2. Anana',
        '3. Fugazza',
        '4. Mortadela',
        '5. Napolitana',
        '6. Primavera',
        '7. Vegetariana',
        '8.  Pesto',
        '9. Calabresa',
        '10. Napolitana'
    ]


    def __init__(self,var):
        self.variedad = var

        if var in Pizza.VARIEDADES:
            self.variedad = Pizza.VARIEDADES[var]
            print(var)
        # else:
        #     self.var = None
        #     print("Variedad de pizza no válida")

    def __str__(self) -> str:
        return f"Variedad: {self.variedad}"

#comando
    def establecerVariedad(self, var):
        self.variedad = var

#consulta
    def obtenerVariedad(self):
        return self.variedad
    

#listPizzas = ['1. Pepperoni','2. Cuatro Quesos','3. Hawaiana','4. Margarita','5. Napolitana','6. Vegetariana','7. Carbonara','8. Calabresa','9. Pesto','10. Rúcula y Jamón']
