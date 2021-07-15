import os

class heroku(object):
    API_ID = int(os.environ.get("API_ID"))
    API_HASH = os.environ.get("API_HASH")
    STRING_SESSION = os.environ.get("STRING_SESSION", None)
    FROM_CHANNEL_ID = int(os.environ.get("FROM_CHANNEL_ID", None))
    TO_CHANNEL_ID = int(os.environ.get("TO_CHANNEL_ID", None))
    CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)
    FILE_TYPE = os.environ.get("FILE_TYPE", None)
