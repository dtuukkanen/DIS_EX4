"""
Operations module for Restaurant Management System
Contains add, delete, and update operations
"""

from .add import AddOperations
from .delete import DeleteOperations
from .update import UpdateOperations

__all__ = ['AddOperations', 'DeleteOperations', 'UpdateOperations']
