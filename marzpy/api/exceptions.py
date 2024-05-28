class NotAuthorized(Exception):
    pass


class AdminAlreadyExists(Exception):
    pass


class AdminNotFound(Exception):
    pass


class UserInvalidEntity(Exception):
    pass


class UserConflict(Exception):
    pass


class UserNotFound(Exception):
    pass


class NodeInvalidEntity(Exception):
    pass


class NodeConflict(Exception):
    pass


class NodeNotFound(Exception):
    pass


class UserTemplateError(Exception):
    pass
