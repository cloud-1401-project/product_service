from config import stub
from config import auth_pb2


def has_access(method, url, token, req):
    try:
        token = token.split('Bearer')[1].replace(" ", "").replace("\t", "")
        print(f'token is {token}')
        print(f'url is {url}, {method}')
        access = stub.HasAccess(auth_pb2.Resource(path=str(url), method=str(method), jwt=token)).has_access
        print(f'access is {access}')
        req.is_authenticated = access
        return access
    except Exception as e:
        print(f'exception is {e}')
        return False
