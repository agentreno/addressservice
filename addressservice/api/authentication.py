import base64
import binascii
import json
import logging

from django.contrib.auth.models import User
from rest_framework import authentication


class IstioAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        # Istio is validating and rejecting requests based on the JWT
        # At this point users are already authenticated, we are just processing
        # the contents of the JWT to find out which user it is
        user_context_header = request.META.get('HTTP_X_JWT_PAYLOAD', '')

        try:
            user_context = json.loads(base64.b64decode(user_context_header).decode('utf-8'))
            user = User.objects.get_or_create(username=user_context['sub'])
            return user
        except (binascii.Error, json.JSONDecodeError) as e:
            logging.warning(
                f"Invalid or empty auth header from upstream: {user_context_header}",
            )
            logging.warning(e)
            return None
