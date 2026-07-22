from app.modules.finance.models.cost_center import CostCenter
from app.modules.finance.repositories.base_repository import BaseRepository


class CostCenterRepository(BaseRepository):
    model = CostCenter
