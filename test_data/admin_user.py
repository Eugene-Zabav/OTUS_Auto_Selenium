import random

_admin = [
    ("user", "bitnami"),
]


def get_admin_user():
    return random.choice(_admin)
