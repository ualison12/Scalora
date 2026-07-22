from app.modules.finance.models.receivable import Receivable
from app.modules.finance.repositories.base_repository import BaseRepository


class ReceivableRepository(BaseRepository):
    model = Receivable
