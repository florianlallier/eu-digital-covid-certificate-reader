from setuptools import setup

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
    name = 'eu-digital-covid-certificate-reader',
    version = '0.0.1',
    description = 'A simple EU Digital COVID Certificate reader.',
    license = 'MIT',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    author = 'Florian Lallier',
    author_email = 'contact@florianlallier.fr',
    maintainer = 'Florian Lallier',
    maintainer_email = 'contact@florianlallier.fr',
    url = 'https://github.com/florianlallier/eu-digital-covid-certificate-reader',
    packages = ['eu_digital_covid_certificate_reader'],
    install_requires = [
        "base45",
        "cbor2",
        "Pillow",
        "pyzbar"
    ],
    python_requires = '>= 3.6',
    entry_points = {
        'console_scripts': ['eu-digital-covid-certificate-reader = eu_digital_covid_certificate_reader.eu_digital_covid_certificate_reader:main']
    },
    keywords = ['covid', 'certificate', 'qrcode', 'reader'],
    classifiers = [
       "Development Status :: 4 - Beta",
       "Environment :: Console",
       "Intended Audience :: End Users/Desktop",
       "License :: OSI Approved :: MIT License",
       "Natural Language :: English",
       "Operating System :: OS Independent",
       "Programming Language :: Python :: 3",
   ],
)