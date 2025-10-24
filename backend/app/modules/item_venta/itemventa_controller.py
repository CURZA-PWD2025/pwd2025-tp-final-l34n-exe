from .itemventa_model import ItemVentaModel
from app.modules.venta.venta_model import VentaModel
from app.modules.producto.producto_model import ProductoModel

class ItemVentaController:
    @staticmethod
    def get_all() -> list[dict]:
        items_venta = ItemVentaModel.get_all()
        return items_venta

    @staticmethod
    def get_one(id) -> dict:
        item_venta = ItemVentaModel.get_by_id(id)
        return item_venta

    @staticmethod
    def create(data: dict) -> dict:
        venta_id = data["id_venta"]
        producto_id = data["id_producto"]

        venta_data = VentaModel.get_by_id(venta_id)
        producto_data = ProductoModel.get_by_id(producto_id)

        if not venta_data:
            return {"mensaje": "La venta no existe"}

        if not producto_data:
            return {"mensaje": "El producto no existe"}

        venta = VentaModel.deserializar(venta_data)
        producto = ProductoModel.deserializar(producto_data)

        item_venta = ItemVentaModel(
            cantidad=data["cantidad"],
            venta=venta,
            producto=producto
        )
        result = item_venta.create()
        return result


    @staticmethod
    def update(data: dict) -> dict:
        venta_id = data["id_venta"]
        producto_id = data["id_producto"]

        venta_data = VentaModel.get_by_id(venta_id)
        producto_data = ProductoModel.get_by_id(producto_id)

        if not venta_data:
            return {"mensaje": "La venta no existe"}

        if not producto_data:
            return {"mensaje": "El producto no existe"}

        venta = VentaModel.deserializar(venta_data)
        producto = ProductoModel.deserializar(producto_data)

        item_venta = ItemVentaModel(
            id=data["id"],
            cantidad=data["cantidad"],
            venta=venta,
            producto=producto
        )
        result = item_venta.update()
        return result

    @staticmethod
    def delete(id:int) -> dict:
        item_venta = ItemVentaModel(
            id=id
        )
        result = item_venta.delete()
        return result