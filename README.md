# Pyfmreader

Version DyNaMo
CAN READ A PSNEX FILE  
In development, not fully stable.
If you find any issues please open an issue at:
https://github.com/jlopezalo/PyFMReader/issues

If you have any questions, contact:
yogesh.saravanan@inserm.fr

## Installation
```
pip install -e git+https://github.com/DyNaMo-INSERM/PyFMReader_DyNaMo@iisc_park#egg=pyfmreader_dynamo    

```

## Usage
```

from pyfmreader import loadfile

NANOSC_FV_PATH = 'tests/testfiles/20200903_Egel2.0_00023.spm'

NANOSC_FV_FILE = loadfile(NANOSC_FV_PATH)

metadata = NANOSC_FV_FILE.filemetadata

piezoimg = NANOSC_FV_FILE.getpiezoimg()

FC = NANOSC_FV_FILE.getcurve(0)

FC_segments = FC.get_segments()

segment_0 = FC_segments[0]
```
