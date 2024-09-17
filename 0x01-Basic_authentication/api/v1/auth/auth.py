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
        Returns:
            - True if the path is None or not in the excluded paths.
            - False if the path is in the excluded paths.
        """
        if path is None:
            return True
        # Ensure both path and excluded paths are slash-tolerant
        if path[-1] != '/':
            path += '/'
        if excluded_paths is None or len(excluded_paths) == 0:
            return True
        if path in excluded_paths:
            return False

        return True

    def authorization_header(self, request=None) -> str:
        """Returns the value of the Authorization header\
            if present, None otherwise."""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Returns the current user (None for now)."""
        return None
