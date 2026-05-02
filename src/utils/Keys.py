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

Keys = TaskKeys()
