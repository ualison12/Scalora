from app.modules.finance.models.boleto import Boleto
from app.modules.finance.repositories.base_repository import BaseRepository


class BoletoRepository(BaseRepository):
    model = Boleto
