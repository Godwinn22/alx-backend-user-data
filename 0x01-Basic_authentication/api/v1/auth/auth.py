#!/usr/bin/env python3
"""
Auth class module
"""


from flask import request
from typing import List, TypeVar


class Auth:
    """
    A class to handle authentication for the API.
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Determines if authentication is required based on the path.
        For now, it returns False.
        """
        return False

    def authorization_header(self, request=None) -> str:
        """Returns the value of the Authorization header\
            if present, None otherwise."""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Returns the current user (None for now)."""
        return None
