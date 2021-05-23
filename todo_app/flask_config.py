import os


class Config:
    """Base configuration variables."""
    TRELLO_TO_DO_LIST_ID = os.environ.get('TRELLO_TO_DO_LIST_ID')
    TRELLO_TOKEN = os.environ.get('TRELLO_TOKEN')
    TRELLO_KEY = os.environ.get('TRELLO_KEY')
    TRELLO_DONE_LIST_ID = os.environ.get('TRELLO_DONE_LIST_ID')
