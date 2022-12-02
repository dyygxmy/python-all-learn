# help(__builtins__)

import base64 as B64

# strm = "YmluYXJtAHN0cmluZw=="
strm = "yDjNMM0xyDTKMM8xzDg="
de = B64.b64decode(strm)
print(de)
print(b'\x0c88'.decode())
