import re


def validate_email(value):
    return re.match(r"[^@]+@[^@]+\.[^@]+", value) is not None


def validate_phone(value):
    return re.match(r"^\+7 \d{3} \d{3} \d{2} \d{2}$", value) is not None


def validate_date(value):
    return re.match(r"\d{2}\.\d{2}\.\d{4}", value) is not None or re.match(r"\d{4}-\d{2}-\d{2}", value) is not None


def validate_text(value):
    return isinstance(value, str) and len(value) > 0


def get_field_type(value):
    if validate_date(value):
        return "date"
    elif validate_phone(value):
        return "phone"
    elif validate_email(value):
        return "email"
    else:
        return "text"
