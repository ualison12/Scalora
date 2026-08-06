from app.modules.inventory.models.category import InventoryCategory
from app.modules.inventory.repositories.base_repository import BaseRepository


class CategoryRepository(BaseRepository):
    model = InventoryCategory
