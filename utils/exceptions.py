class InvalidEmailError(Exception):
    pass

class InvalidDurationError(Exception):
    pass

email = "abc"
if "@" not in email:
    raise InvalidEmailError("Invalid email address")