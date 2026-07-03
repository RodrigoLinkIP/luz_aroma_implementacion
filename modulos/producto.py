class Estado:
    def __init__(self, nombre: str):
        self.nombre = nombre
        
class Categoria:
    def __init__(self, id: int, nombre: str):
        self.id = id
        self.nombre = nombre
        
class Producto:
    def __init__(self, id: int, nombre: str, caracteristicas: str, aroma: str,
                 tamannio: str, precio: float, costo: float, stock: int,
                 estado: Estado, categoria: Categoria):
        self.id = id
        self.nombre = nombre
        self.caracteristicas = caracteristicas
        self.aroma = aroma
        self.tamannio = tamannio
        self._precio = precio
        self.costo = costo
        self._stock = stock
        self.estado = estado
        self.categoria = categoria
        
    @property
    def precio(self):
        return self._precio
    
    @property
    def stock(self):
        return self._stock
    
    def __str__(self):
        return f"{self.nombre} - ${self.precio:.2f} (Stock: {self.stock})"
    
    def hay_stock(self) -> bool:
        return self.stock > 0
    
    def actualizar_precio(self, nuevo_precio: float):
        if nuevo_precio < 0:
            raise ValueError("El precio no puede ser negativo")
        self._precio = nuevo_precio
        
    def actualizar_stock(self, nuevo_stock: int):
        if nuevo_stock < 0:
            raise ValueError("El stock no puede ser negativo")
        
        if self.hay_stock():
            self._stock += nuevo_stock
        else:
            self._stock = nuevo_stock
    
    def disminuir_stock(self, cantidad: int):
        if cantidad > self.stock:
            raise ValueError(f"La cantidad ({cantidad}) supera el stock disponible ({self.stock}).")
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero.")
        
        self._stock -= cantidad
        
class Catalogo:

    def __init__(self):
        self._productos: list[Producto] = []

    def agregar_producto(self, producto: Producto) -> None:
        self._productos.append(producto)

    def obtener_producto(self, id_producto: int) -> Producto | None:
        for producto in self._productos:
            if producto.id == id_producto:
                return producto
        return None

    def listar_productos(self) -> list[Producto]:
        return list(self._productos)

    def eliminar_producto(self, id_producto: int) -> bool:
        producto = self.obtener_producto(id_producto)
        if producto is None:
            return False
        self._productos.remove(producto)
        return True