import base64
from typing import Union
from Crypto.Cipher import AES


class ECB(object):
    def __init__(self, key: Union[bytes, str]):
        """
        Create a new AES cipher for ECB.
        :param key: It must be 16, 24 or 32 bytes long (respectively for *AES-128*,
        *AES-192* or *AES-256*).
        """
        self.key = key if isinstance(key, bytes) else key.encode('utf-8')
        self.cipher = AES.new(self.key, AES.MODE_ECB)

    def encrypt(self, src: Union[bytes, str]) -> str:
        """
        encrypt string
        :param src: String to be encrypted
        :return: base64 encoded string
        """
        src = src if isinstance(src, bytes) else src.encode("utf-8")
        length = 16 - (len(src) % 16)
        src += b'\x10' * length
        data = self.cipher.encrypt(src)
        return base64.b64encode(data).decode('utf-8')

    def decrypt(self, src: str) -> str:
        """
        decrypt string
        :param src: base64 encoded string
        :return: decode string
        """
        return self.cipher.decrypt(base64.b64decode(src)).strip(b'\x10').decode("utf-8")
