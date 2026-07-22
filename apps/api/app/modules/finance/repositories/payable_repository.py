from app.modules.finance.models.payable import Payable
from app.modules.finance.repositories.base_repository import BaseRepository


class PayableRepository(BaseRepository):
    model = Payable
