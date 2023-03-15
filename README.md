# EDIParser
[![Python - 3.9.0+](https://img.shields.io/badge/Python-3.9.0%2B-orange)](https://www.python.org/downloads/release/python-390/)


### Installation
Binary installers for the latest released version are at the Python Package Index. Please note that you need to run Python 3.9 or higher to install the [edi-835-parser](https://github.com/keironstoddart/edi-835-parser)

```
pip install edi-835-parser
```

### Usage
```
python3 835_to_csv_parser.py <path_to_directory> <file_name_without_extension>
```
for example:
```
python3 835_to_csv_parser.py ~/Desktop/ edi_file
```
This parser alternatively auto-generates a .xml file in the same <path_to_directory>
