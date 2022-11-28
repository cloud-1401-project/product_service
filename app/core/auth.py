from config import stub
from config import auth_pb2


def has_access(method, url, token):
    try:
        token = token.split('Bearer')[1].replace(" ", "").replace("\t", "")
        print(f'token is {token}')
        return stub.HasAccess(auth_pb2.Resource(path=url, method=method, jwt=token)).has_access
    except Exception:
        return False
