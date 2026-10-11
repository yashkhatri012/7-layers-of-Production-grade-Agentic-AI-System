"""
Database Models Export.
This allows simple imports like: `from app.models.database import User, Thread`
"""
from app.models.thread import Thread

# Explicitly define what is exported
__all__ = ["Thread", "User", "Session"]