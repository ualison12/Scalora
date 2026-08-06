from sqlalchemy.orm import Session

from app.modules.platform.models.admin_user import AdminUser
from app.modules.platform.models.audit_log import PlatformLog
from app.modules.platform.models.backup import Backup
from app.modules.platform.models.billing_event import BillingEvent
from app.modules.platform.models.deployment import Deployment
from app.modules.platform.models.plan import Plan
from app.modules.platform.models.sdk_key import SDKKey
from app.modules.platform.models.subscription import Subscription
from app.modules.platform.models.webhook import Webhook


class PlatformService:
    def create_plan(self, db: Session, *, company_id: int, name: str, price: float, billing_period: str) -> Plan:
        plan = Plan(company_id=company_id, name=name, price=price, billing_period=billing_period)
        db.add(plan)
        db.commit()
        db.refresh(plan)
        return plan

    def create_subscription(self, db: Session, *, company_id: int, plan_id: int, status: str) -> Subscription:
        subscription = Subscription(company_id=company_id, plan_id=plan_id, status=status)
        db.add(subscription)
        db.commit()
        db.refresh(subscription)
        return subscription

    def create_billing_event(self, db: Session, *, company_id: int, subscription_id: int, amount: float, status: str) -> BillingEvent:
        billing_event = BillingEvent(company_id=company_id, subscription_id=subscription_id, amount=amount, status=status)
        db.add(billing_event)
        db.commit()
        db.refresh(billing_event)
        return billing_event

    def create_webhook(self, db: Session, *, company_id: int, name: str, endpoint: str) -> Webhook:
        webhook = Webhook(company_id=company_id, name=name, endpoint=endpoint)
        db.add(webhook)
        db.commit()
        db.refresh(webhook)
        return webhook

    def create_sdk_key(self, db: Session, *, company_id: int, name: str, key: str) -> SDKKey:
        sdk_key = SDKKey(company_id=company_id, name=name, key=key)
        db.add(sdk_key)
        db.commit()
        db.refresh(sdk_key)
        return sdk_key

    def create_admin_user(self, db: Session, *, company_id: int, username: str, role: str) -> AdminUser:
        admin_user = AdminUser(company_id=company_id, username=username, role=role)
        db.add(admin_user)
        db.commit()
        db.refresh(admin_user)
        return admin_user

    def create_log_entry(self, db: Session, *, company_id: int, level: str, message: str) -> PlatformLog:
        log_entry = PlatformLog(company_id=company_id, level=level, message=message)
        db.add(log_entry)
        db.commit()
        db.refresh(log_entry)
        return log_entry

    def create_backup(self, db: Session, *, company_id: int, name: str, status: str) -> Backup:
        backup = Backup(company_id=company_id, name=name, status=status)
        db.add(backup)
        db.commit()
        db.refresh(backup)
        return backup

    def create_deployment(self, db: Session, *, company_id: int, environment: str, version: str) -> Deployment:
        deployment = Deployment(company_id=company_id, environment=environment, version=version)
        db.add(deployment)
        db.commit()
        db.refresh(deployment)
        return deployment

    def get_dashboard(self, db: Session, *, company_id: int) -> dict[str, int]:
        plans_count = db.query(Plan).filter(Plan.company_id == company_id).count()
        active_subscriptions = db.query(Subscription).filter(Subscription.company_id == company_id, Subscription.status == "active").count()
        webhooks_count = db.query(Webhook).filter(Webhook.company_id == company_id).count()
        deployments_count = db.query(Deployment).filter(Deployment.company_id == company_id).count()
        return {
            "plans_count": plans_count,
            "active_subscriptions": active_subscriptions,
            "webhooks_count": webhooks_count,
            "deployments_count": deployments_count,
        }
