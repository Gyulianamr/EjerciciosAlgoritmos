#10.	Historial de Navegador Implementa una pila para simular el historial de navegación en un navegador. Agrega una operación para “ir hacia atrás”.
#
class HistorialNavegacion:
    def __init__(self):
        self.pila = []

    def visitar(self, pagina):
        self.pila.append(pagina)

    def ir_hacia_atras(self):
        if len(self.pila) > 1:
            self.pila.pop()
            return self.pila[-1]
        else:
            return "No hay páginas para ir hacia atrás."

    def obtener_ultimo(self):
        if self.pila:
            return self.pila[-1]
        else:
            return "No hay historial."

historial = HistorialNavegacion()
historial.visitar("pagina1.com")
historial.visitar("pagina2.com")
historial.visitar("pagina3.com")

print("Última página visitada:", historial.obtener_ultimo())  # Muestra "pagina3.com"
print("Ir hacia atrás:", historial.ir_hacia_atras())  # Muestra "pagina2.com"
print("Última página visitada después de ir hacia atrás:", historial.obtener_ultimo())  # Muestra "pagina2.com"
