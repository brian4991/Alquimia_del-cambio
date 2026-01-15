"""Persistence services - Database repositories."""

from marketing.services.persistence.repository import MarketingRepository
from marketing.services.persistence.sqlalchemy_repository import SQLAlchemyMarketingRepository

__all__ = ["MarketingRepository", "SQLAlchemyMarketingRepository"]
