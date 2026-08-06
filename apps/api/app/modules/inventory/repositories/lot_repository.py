from app.modules.inventory.models.lot import Lot
from app.modules.inventory.repositories.base_repository import BaseRepository


class LotRepository(BaseRepository):
    model = Lot
