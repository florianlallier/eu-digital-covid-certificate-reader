import sys
import base45
import zlib
import cbor2
from PIL import Image
from pyzbar import pyzbar

def decode(filename):
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

    return json_format[-260][1]


def get_certificate_type(certificate):
    if "v" in certificate:
        return "v"
    elif "t" in certificate:
        return "t"
    elif "r" in certificate:
        return "r"
    else:
        return None


def print_common_certificate_informations(certificate):
    print("Name, Surname(s) and forename(s): " + certificate["nam"]["fn"] + certificate["nam"]["gn"])
    print("Date of birth: " + certificate["dob"])


def print_vaccination_certificate_informations(certificate):
    print_common_certificate_informations(certificate)
    print("Disease or agent targeted: " + certificate["v"][0]["tg"])
    print("Vaccine/prophylaxis: " + certificate["v"][0]["vp"])
    print("Vaccine medicinal product: " + certificate["v"][0]["mp"])
    print("Vaccine marketing authorisation holder or manufacturer: " + certificate["v"][0]["ma"])
    print("Number in a series of vaccinations/doses and the overall number of doses in the series: " + str(certificate["v"][0]["dn"]) + "/" + str(certificate["v"][0]["sd"]))
    print("Date of vaccination: " + certificate["v"][0]["dt"])
    print("Member State of vaccination: " + certificate["v"][0]["co"])
    print("Certificate issuer: " + certificate["v"][0]["is"])


def print_test_certificate_informations(certificate):
    print_common_certificate_informations(certificate)
    # TODO
    print("This is a test certificate. Not yet implemented.")


def print_recovery_certificate_informations(certificate):
    print_common_certificate_informations(certificate)
    # TODO
    print("This is a recovery certificate. Not yet implemented.")


def main():
    filename = sys.argv[1]
    
    certificate = decode(filename)
    certificate_type = get_certificate_type(certificate)

    if certificate_type == "v":
        # Print vaccination certificate informations
        print_vaccination_certificate_informations(certificate)
    elif certificate_type == "t":
        # Print test certificate informations
        print_test_certificate_informations(certificate)
    elif certificate_type == "r":
        # Print recovery certificate informations
        print_recovery_certificate_informations(certificate)
    else:
        print("Could not read the certificate.")


if __name__ == "__main__":
    main()