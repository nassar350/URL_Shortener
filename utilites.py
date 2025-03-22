import zlib
import base64

def shorten_url(long_url):
    short = zlib.crc32(long_url.encode())
    short = base64.urlsafe_b64encode(short.to_bytes(4, 'big')).decode()[:6]
    return short
