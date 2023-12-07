from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'system.settings')


application = ProtocolTypeRouter({
    "http": get_asgi_application(),
})

