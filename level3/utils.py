import jwt
from datetime import datetime, timedelta
from django.conf import settings

def generate_jwt_token(data):
    expiration = datetime.utcnow() + timedelta(hours=1)
    payload = {
        'exp': expiration,
        'data': data
    }
    return jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')

def decode_jwt_token(token):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        return payload['data']
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None
