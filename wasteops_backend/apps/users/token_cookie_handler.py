from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError


class CookieJWTAuthentication(JWTAuthentication):
    def authenticate(self, request):
        # Get the token from the cookie
        raw_token = request.COOKIES.get('access_token')
        if raw_token is None:
            return None

        try:
            # Use SimpleJWT's token validation
            validated_token = self.get_validated_token(raw_token)
            return self.get_user(validated_token), validated_token
        except TokenError as e:
            raise InvalidToken(e.args[0])
