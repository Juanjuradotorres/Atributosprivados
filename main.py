"""HoLA"""
from classVenta import Venta

venta = Venta()
venta.set_id_venta(1)
venta.set_fecha("10/01/2021")
venta.set_cliente("Juan Jurado")
venta.set_productos({"Producto 1": 12, "Producto 2": 60, "Producto 3": 45})

# Mostrar los detalles de la venta
venta.mostrar_detalle()