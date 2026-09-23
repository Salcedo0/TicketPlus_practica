class InventarioSpy:
    def __init__(self):
        self.veces_consultado = 0
 
    def consultar_disponibilidad(self):
        self.veces_consultado += 1
        return 50
 
Inventario = InventarioSpy()
Inventario.consultar_disponibilidad()
Inventario.consultar_disponibilidad()
Inventario.consultar_disponibilidad()
Inventario.consultar_disponibilidad()
 
print(Inventario.veces_consultado)