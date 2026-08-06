from app.modules.inventory.models.product import Product
from app.modules.inventory.repositories.base_repository import BaseRepository


class ProductRepository(BaseRepository):
    model = Product
