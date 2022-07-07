# aes-256-ecb-py
> `encrypt` and `dencrypt` by aes-256-ecb for Python

### usage
```python
from src.main import ECB


key = "1fEWUoGzMXITwpRe1fEWUoGzMXITwpRe"
src = "encode_test"

ecb = ECB(key)

encrypt_str = ecb.encrypt(src)

decrypt_str = ecb.decrypt(encrypt_str)
assert encrypt_str == decrypt_str
```
