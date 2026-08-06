from app.modules.inventory.models.movement import Movement
from app.modules.inventory.repositories.base_repository import BaseRepository


class MovementRepository(BaseRepository):
    model = Movement
