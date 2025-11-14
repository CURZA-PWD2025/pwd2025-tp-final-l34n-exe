from ...database.conect_db import ConectDB
from ..proveedor.proveedor_model import ProveedorModel as Proveedor
from ..categoria.categoria_model import CategoriaModel as Categoria

class ProductoModel:
    def __init__(self, id:int=0, nombre:str="", precio:float=0.0, stock:int=0, max_sabores:int=1, proveedor:Proveedor=None, categoria:Categoria=None):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.max_sabores = max_sabores
        self.proveedor = proveedor
        self.categoria = categoria

    def serializar(self)->dict:
        return {
            "id": self.id,
            "nombre": self.nombre,
            "precio": self.precio,
            "stock": self.stock,
            "max_sabores": self.max_sabores,
            "proveedor": self.proveedor.serializar() if self.proveedor else None,
            "categoria": self.categoria.serializar() if self.categoria else None
        }

    @staticmethod
    def deserializar(data:dict) -> 'ProductoModel':
        return ProductoModel(
            id=data["id"],
            nombre=data["nombre"],
            precio=data["precio"],
            stock=data["stock"],
            max_sabores=data["max_sabores"],
            proveedor=Proveedor.deserializar(data["proveedor"]) if data.get("proveedor") else None,
            categoria=Categoria.deserializar(data["categoria"]) if data.get("categoria") else None
        )

    @staticmethod
    def get_all() -> list[dict]:
        cnx = ConectDB.get_connect()
        with cnx.cursor(dictionary=True) as cursor:
            try:
                cursor.execute("SELECT * FROM productos")
                rows = cursor.fetchall()
                productos = []
                for row in rows:
                    categoria = Categoria.get_by_id(row["id_categoria"])
                    proveedor = Proveedor.get_by_id(row["id_proveedor"])
                    row["categoria"] = categoria
                    row["proveedor"] = proveedor
                    del row["id_categoria"]
                    del row["id_proveedor"]
                    productos.append(row)
                return productos
            except Exception as exc:
                return {"mensaje": f"Error al obtener los productos: {exc}"}
            finally:
                cnx.close()


    @staticmethod
    def get_by_id(id: int) -> dict:
        cnx = ConectDB.get_connect()
        with cnx.cursor(dictionary=True) as cursor:
            try:
                cursor.execute("SELECT * FROM productos WHERE id=%s", (id,))
                row = cursor.fetchone()
                if row:
                    row["categoria"] = Categoria.get_by_id(row["id_categoria"])
                    row["proveedor"] = Proveedor.get_by_id(row["id_proveedor"])
                    del row["id_categoria"]
                    del row["id_proveedor"]
                return row
            except Exception as exc:
                return {"mensaje":f"Error al obtener el producto: {exc}"}
            finally:
                cnx.close()

    def create(self) -> bool:
        cnx = ConectDB.get_connect()
        with cnx.cursor(dictionary=True)  as cursor:
            try:
                cursor.execute("INSERT INTO productos (nombre, precio, stock, max_sabores, id_proveedor, id_categoria) VALUES (%s, %s, %s, %s, %s, %s)", (self.nombre, self.precio, self.stock, self.max_sabores, self.proveedor.id, self.categoria.id))
                self.id = cursor.lastrowid
                cnx.commit()
                return cursor.rowcount > 0
            except Exception as exc:
                cnx.rollback()
                print({"mensaje": f"Error al crear el producto: {exc}"})
                return False
            finally:
                cnx.close()

    def update(self) -> bool:
        cnx = ConectDB.get_connect()
        with cnx.cursor(dictionary=True) as cursor:
            try:
                cursor.execute(
                    "UPDATE productos SET nombre=%s, precio=%s, stock=%s, max_sabores=%s, id_proveedor=%s, id_categoria=%s WHERE id=%s",
                    (self.nombre, self.precio, self.stock, self.max_sabores, self.proveedor.id, self.categoria.id, self.id)
                )
                cnx.commit()
                return cursor.rowcount > 0
            except Exception as exc:
                cnx.rollback()
                print({"mensaje": f"Error al actualizar el producto: {exc}"})
                return False
            finally:
                cnx.close()

    def delete(self) -> bool:
        cnx = ConectDB.get_connect()
        with cnx.cursor() as cursor:
            try:
                cursor.execute("DELETE FROM productos WHERE id=%s", (self.id,))
                cnx.commit()
                return cursor.rowcount > 0
            except Exception as exc:
                cnx.rollback()
                print({"mensaje": f"Error al borrar el producto: {exc}"})
                return False
            finally:
                cnx.close()


