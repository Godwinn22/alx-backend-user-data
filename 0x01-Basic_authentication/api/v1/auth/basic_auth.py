#!/usr/bin/env python3
"""
Basic Auth class module
"""
from .auth import Auth


class BasicAuth(Auth):
    """
    Basic Authentication class, inherits from Auth.
    """

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """Extracts the Base64 part of the Authorizationn header"""
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        # Return the part after "Basic " (6 characters)
        return authorization_header[6:]
