"""
Exceptions and throwables for various purposes

---

Copyright (c) 2025 Sakuragasaki46.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
See LICENSE for the specific language governing permissions and
limitations under the License.

This software is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
"""

class MissingConfigError(LookupError):
    """
    Config variable not found.

    Raised when a config property is marked as required, but no property with
    that name is found.
    """
    pass


class MissingConfigWarning(MissingConfigError, Warning):
    """
    A required config property is missing, and the application is assuming a default value.
    """
    pass


class LexError(SyntaxError):
    """
    Illegal character or sequence found in the token stream.
    """

class InconsistencyError(RuntimeError):
    """
    This program is in a state which it's not supposed to be in.
    """

class NotFoundError(LookupError):
    """
    The requested item was not found.
    """
    # Werkzeug et al.
    code = 404

class BabelTowerError(NotFoundError):
    """
    The user requested a language that cannot be understood.
    """

__all__ = (
    'MissingConfigError', 'MissingConfigWarning', 'LexError', 'InconsistencyError', 'NotFoundError'
)