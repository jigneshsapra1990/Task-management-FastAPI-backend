class RoutesPath:
    """Static route paths for task endpoints."""
    CREATE = "/create"
    GET_ALL = "/all"
    GET_BY_ID = "/{task_id}"
    UPDATE = "/{task_id}"
    DELETE = "/{task_id}"
    CREATER_USER = "/register"
    LOGIN_USER  = "/login"

routes = RoutesPath()


class StatusCode:
    """Standard HTTP status codes used across the application."""
    OK = 200
    CREATED = 201
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    NOT_FOUND = 404
    INTERNAL_SERVER_ERROR = 500

status_code = StatusCode()
