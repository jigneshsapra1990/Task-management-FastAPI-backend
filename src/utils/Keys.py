class ResponseKeys:
    """Static keys used in API response dictionary structure."""
    STATUS = "status"
    STATUS_CODE = "status_code"
    MESSAGE = "message"
    DATA = "data"
    SUCCESS = "success"
    ERROR = "error"

keys = ResponseKeys()


class TaskKeys:
    """Static field keys used in TaskModel and TaskSchema."""
    ID = "id"
    TITLE = "title"
    DESCRIPTION = "description"
    DUE_DATE = "due_date"
    COMPLETED = "completed"
    IS_COMPLETED = "is_completed"
    NAME = "name"
    EMAIL = "email"
    USERNAME = "username"
    USER_ID = "user_id"
    EXPIRES = "exp"
    ACCESS_TOKEN = "access_token"

Keys = TaskKeys()
