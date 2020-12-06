# findTarget is pipeline for searching phi29 homologs by using HMMER program

## Annotation

Пайплайн написан в рамках GenHack 2020 для рашения задачи - Предсказание полимеразной активности новых Φ29 ДНК-полимераз.

## Requirements

PYTHON:
  * python >= 3.7
  * biopython: `pip3 install biopython`

TOOLS:
  * HMMER: conda install -c conda-forge hammer or from source http://hmmer.org


## Installation

```  
git clone https://github.com/ubercomrade/GenHack.git  
cd GenHack/  
pip install -e .  
```

## Usage
The command `findTarget -h` return:

```
usage: findTarget.py [-h] [-t TMP_DIR] genebank fasta results tag

positional arguments:
  genebank              path to GeneBank file
  fasta                 path to write Fasta (parsed CDS from GeneBank file)
  results               dir to write results
  tag                   tag for output files

optional arguments:
  -h, --help            show this help message and exit
  -t TMP_DIR, --tmp TMP_DIR
                        tmp dir
```
### Example run
```
findTarget.py \
path/to/gbk/12_45.gbk \
path/to/write/parsed/CDS/12_45.fasta \
dir/to/write/res/ \
tag-of-files
```

## License

Copyright (c) 2020 Trituration

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.