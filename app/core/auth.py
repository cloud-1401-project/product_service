from config import stub
from config import auth_pb2


def has_access(method, url, token):
    try:
        token = token.split('Bearer')[1].replace(" ", "").replace("\t", "")
        access = stub.HasAccess(auth_pb2.Resource(path=str(url), method=str(method), jwt=token)).has_access
        return access
    except Exception as e:
        print(f'exception is {e}')
        return False
