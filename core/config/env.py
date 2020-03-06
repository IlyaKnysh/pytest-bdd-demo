import os
from addict import Dict


def get(key, default=None):
    return os.environ.get(key=key, default=default)


PROJECT_DIRECTORY = os.path.abspath(__file__ + "/../../..")
DEBUG = get('DEBUG', False)

USERS = Dict(
    {
        "Account Manager":
            Dict({
                "email": "email",
                "password": "password"
            }),
    }
)


BASE_URL = "https://url.net"
