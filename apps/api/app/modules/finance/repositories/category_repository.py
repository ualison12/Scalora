from app.modules.finance.models.category import Category
from app.modules.finance.repositories.base_repository import BaseRepository


class CategoryRepository(BaseRepository):
    model = Category
