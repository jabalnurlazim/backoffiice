"""
Views for the Auth API.
"""
from rest_framework import generics, status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.response import Response


from authentication.serializers import (
    AuthTokenSerializer,
    ResetPasswordSerializer,
)


class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for user."""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ResetPasswordView(generics.GenericAPIView):
    """Create a new auth token for user."""
    serializer_class = ResetPasswordSerializer

    def post(self, request):

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(
            {'success': 'We have sent you your new password.'},
            status=status.HTTP_200_OK
        )
