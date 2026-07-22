from app.modules.finance.models.pix import Pix
from app.modules.finance.repositories.base_repository import BaseRepository


class PixRepository(BaseRepository):
    model = Pix
