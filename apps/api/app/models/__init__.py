from .audit_log import AuditLog
from .company import Company
from .permission import Permission
from .refresh_token import RefreshToken
from .role import Role
from .role_permission import RolePermission
from .session import Session
from .user import User
from .user_role import UserRole

from app.modules.crm.models import Activity, Contact, Deal, Lead, Note, Stage, Task
