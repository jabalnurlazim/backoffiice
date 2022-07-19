"""
Serializers for the Auth API View.
"""
from django.contrib.auth import (
    get_user_model,
    authenticate,
    )
from django.utils.translation import gettext as _

from rest_framework import serializers

from core.utils import Util


class AuthTokenSerializer(serializers.Serializer):
    """Serializer for the user auth token."""
    email = serializers.EmailField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False,
    )

    def validate(self, attrs):
        """Validate and authenticate the user."""
        email = attrs.get('email')
        password = attrs.get('password')

        user = authenticate(
            request=self.context.get('request'),
            username=email,
            password=password,
        )
        if not user:
            msg = _('Unable to authenticate with provided credentials.')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs


class ResetPasswordSerializer(serializers.Serializer):
    """Serializer for the user object."""
    email = serializers.EmailField()

    class Meta:
        fields = ['email']

    def validate(self, attrs):
        email = attrs.get('email', None)
        exist = get_user_model().objects.filter(email=email).exists()

        if exist:
            user = get_user_model().objects.get(email=email)
            password = get_user_model().objects.make_random_password()
            user.set_password(password)
            user.save(update_fields=['password'])

            email_body = 'Hi ' + user.name  + '. \n\nThis would be you new password: <b>' + password + '</b>'

            data = {
                'email_body': email_body,
                'to_email': user.email,
                'email_subject': 'Reset Password',
            }

            Util.send_email(data)
        elif not exist:
            msg = _('User is not existing in our database. Please try again.')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs
