from app.modules.inventory.models.supplier import Supplier
from app.modules.inventory.repositories.base_repository import BaseRepository


class SupplierRepository(BaseRepository):
    model = Supplier
