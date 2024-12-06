import requests

url = 'http://127.0.0.1:5000/get_form'


form_templates = [
    {
        'customer_phone': '+7 123 456 78 90',
        'order_date': '2024-01-15',
        'lead_email': 'test@example.com'
    },
    {
        'user_name': 'John Doe',
        'email': 'john.doe@example.com'
    },
    {
        'order_date': '15.03.2023',
        'product_name': 'Widget X',
        'customer_phone': '+7 987 654 32 10'
    },
    {
        'lead_email': 'another@test.net',
        'comment': 'Some text here',
        'phone': '+7 111 222 33 44'
    }
    ]

for data in form_templates:
    response = requests.post(url, data=data)
    print(response.json())
