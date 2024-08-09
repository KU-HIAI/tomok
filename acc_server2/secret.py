# 3rd-party
from connexion.exceptions import OAuthProblem

TOKEN_DB = {
    'f234cf784e7c9669929122343a808bcf9607e425': {
        'uid': 'api connect test'
    },
    'becec424c4eeb8510ad7c819b03889e671c01e87': {
        'uid': 'dev taemin lee'
    }
}


def apikey_auth(token, required_scopes):
    info = TOKEN_DB.get(token, None)

    if not info:
        raise OAuthProblem('Invalid token')

    return info


def get_secret(user) -> str:
    return {"msg:":"{user}님 반갑습니다.".format(user=user)}