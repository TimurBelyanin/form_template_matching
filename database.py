from tinydb import TinyDB
from validators import get_field_type

db = TinyDB('forms_db.json')

form_templates = [
  {
    "name": "User Registration",
    "user_name": "text",
    "email": "email",
    "phone": "phone",
    "birthdate": "date"
  },
  {
    "name": "Order Form",
    "order_date": "date",
    "lead_email": "email",
    "customer_phone": "phone",
    "order_details": "text"
  },
  {
    "name": "Contact Form",
    "user_name": "text",
    "message": "text",
    "contact_email": "email"
  },
  {
    "name": "Login Form",
    "user_name": "text",
    "email": "email"
  }
]


def get_form_template(fields):
    # Пройдемся по всем шаблонам в базе
    for template in db.all():
        match = True
        for field_name, field_value in fields.items():
            if field_name not in template:
                match = False
                break

            field_type_in_template = template[field_name]
            field_type_in_request = get_field_type(field_value)

            if field_type_in_template != field_type_in_request:
                match = False
                break
        if match:
            return template
    return None


def create_test_db(templates=form_templates):
    db.truncate()
    for template in templates:
        db.insert(template)
