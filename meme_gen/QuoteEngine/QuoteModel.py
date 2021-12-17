class QuoteModel:
    """A simple quote"""

    body: str = None
    author: str = None

    def __init__(self, body: str, author: str):
        self.body = body
        self.author = author
