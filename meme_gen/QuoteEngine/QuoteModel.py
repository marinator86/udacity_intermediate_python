"""Contains a model class for a Qoute."""
import json


class QuoteModel:
    """A simple quote."""

    body: str = None
    author: str = None

    def __init__(self, body: str, author: str):
        """Construct a QuoteModel."""
        self.body = body
        self.author = author

    def __str__(self):
        """Return a string describing this QuoteModel."""
        return f"QuoteModel: Body={self.body} ; Author={self.author}"
