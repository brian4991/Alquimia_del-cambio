"""
Base model for marketing domain.

Provides common SQLAlchemy base for all marketing models.
"""

from sqlalchemy.ext.declarative import declarative_base

# Separate base for marketing models to keep them isolated
MarketingBase = declarative_base()
