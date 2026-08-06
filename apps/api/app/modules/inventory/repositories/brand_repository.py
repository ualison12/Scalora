from app.modules.inventory.models.brand import Brand
from app.modules.inventory.repositories.base_repository import BaseRepository


class BrandRepository(BaseRepository):
    model = Brand
