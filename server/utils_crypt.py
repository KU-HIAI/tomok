# python
import datetime
from telnetlib import ENCRYPT
# 3rd-party
from cryptography.fernet import Fernet

class Crypt():
    def __init__(self, key) -> None:
        self.f = Fernet(key)


    def encrypt(self, str) -> str:
        return self.f.encrypt(str.encode('utf-8')).decode('utf-8')


    def decrypt(self, str) -> str:
        return self.f.decrypt(str.encode('utf-8')).decode('utf-8')


    def file_to_token(self, filename, expired_days=1.0):
        expired_datetime = datetime.datetime.utcnow() + datetime.timedelta(days = expired_days)
        expired_datetime_timestamp = expired_datetime.timestamp()
        filename_with_expired = '_'.join([filename, str(expired_datetime_timestamp)])
        return {'token': self.encrypt(filename_with_expired), 'expired_datetime': expired_datetime}


    def unpack_token(self, token):
        filename_with_expired = self.decrypt(token)
        segments = filename_with_expired.split('_')
        filename = '_'.join(segments[0:-1])
        expired_datetime_timestamp = segments[-1]
        expired_datetime = datetime.datetime.fromtimestamp(float(expired_datetime_timestamp))
        return {'filename': filename, 'expired_datetime': expired_datetime}


    def is_expired(self, token):
        meta = self.unpack_token(token)
        return datetime.datetime.utcnow() > meta['expired_datetime']
        

if __name__ == '__main__':
    # some test codes..
    key = Fernet.generate_key()
    f = Crypt(key)
    token = f.encrypt(str(datetime.datetime.utcnow().timestamp()))
    print(key)
    print(token)
    print(f.decrypt(token))
    print(datetime.datetime.fromtimestamp(float(f.decrypt(token))))