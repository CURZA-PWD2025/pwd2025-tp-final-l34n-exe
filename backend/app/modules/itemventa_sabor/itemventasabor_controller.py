from .itemventasabor_model import ItemVentaSaborModel
from app.modules.item_venta.itemventa_model import ItemVentaModel as ItemVenta
from app.modules.sabor.sabor_model import SaborModel as Sabor

class ItemVentaSaborController:
    @staticmethod
    def get_all() -> list[dict]:
        items_venta_sabor = ItemVentaSaborModel.get_all()
        return items_venta_sabor

    @staticmethod
    def get_one(id) -> dict:
        item_venta_sabor = ItemVentaSaborModel.get_by_id(id)
        return item_venta_sabor

    @staticmethod
    def create(data: dict) -> dict:
        item_venta_id = data["id_item"]
        sabor_id = data["id_sabor"]

        item_venta_data = ItemVenta.get_by_id(item_venta_id)
        sabor_data = Sabor.get_by_id(sabor_id)

        if not item_venta_data:
            return {"mensaje": "El item de venta no existe"}

        if not sabor_data:
            return {"mensaje": "El sabor no existe"}

        item_venta = ItemVenta.deserializar(item_venta_data)
        sabor = Sabor.deserializar(sabor_data)

        item_venta_sabor = ItemVentaSaborModel(
            item_venta=item_venta,
            sabor=sabor
        )
        result = item_venta_sabor.create()
        return {"Creado": result}

    @staticmethod
    def update(data: dict) -> dict:
        item_venta_id = data["id_item"]
        sabor_id = data["id_sabor"]

        item_venta_data = ItemVenta.get_by_id(item_venta_id)
        sabor_data = Sabor.get_by_id(sabor_id)

        if not item_venta_data:
            return {"mensaje": "El item de venta no existe"}

        if not sabor_data:
            return {"mensaje": "El sabor no existe"}

        item_venta = ItemVenta.deserializar(item_venta_data)
        sabor = Sabor.deserializar(sabor_data)

        item_venta_sabor = ItemVentaSaborModel(
            id=data["id"],
            item_venta=item_venta,
            sabor=sabor
        )
        result = item_venta_sabor.update()
        return {"Actualizado": result}


    @staticmethod
    def delete(id:int) -> dict:
        item_venta_sabor = ItemVentaSaborModel(
            id=id
        )
        result = item_venta_sabor.delete()
        return {"Eliminado": result}