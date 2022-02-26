import sys
import base45
import zlib
import cbor2
from PIL import Image
from pyzbar import pyzbar

def main():
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

    # Print vaccination certificate informations
    print("Name, Surname(s) and forename(s): " + json_format[-260][1]["nam"]["fn"] + json_format[-260][1]["nam"]["gn"])
    print("Date of birth: " + json_format[-260][1]["dob"])
    print("Disease or agent targeted: " + json_format[-260][1]["v"][0]["tg"])
    print("Vaccine/prophylaxis: " + json_format[-260][1]["v"][0]["vp"])
    print("Vaccine medicinal product: " + json_format[-260][1]["v"][0]["mp"])
    print("Vaccine marketing authorisation holder or manufacturer: " + json_format[-260][1]["v"][0]["ma"])
    print("Number in a series of vaccinations/doses and the overall number of doses in the series: " + str(json_format[-260][1]["v"][0]["dn"]) + "/" + str(json_format[-260][1]["v"][0]["sd"]))
    print("Date of vaccination: " + json_format[-260][1]["v"][0]["dt"])
    print("Member State of vaccination: " + json_format[-260][1]["v"][0]["co"])
    print("Certificate issuer: " + json_format[-260][1]["v"][0]["is"])


if __name__ == "__main__":
    main()