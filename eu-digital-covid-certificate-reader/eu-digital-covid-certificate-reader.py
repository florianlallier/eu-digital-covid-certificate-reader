import sys
import base45
import zlib
import cbor2
from PIL import Image
from pyzbar import pyzbar

filename = sys.argv[1]
image = Image.open(filename)
qrcode = pyzbar.decode(image)
data = qrcode[0].data.decode('UTF-8')

# HCERT to BASE45
base45_format = data[4:]

# BASE45 to ZLIB
zlib_format = base45.b45decode(base45_format)

# ZLIB to CBOR
cbor_format = zlib.decompress(zlib_format)

# CBOR to JSON
json_format = cbor2.loads(cbor2.loads(cbor_format).value[2])

print(json_format)