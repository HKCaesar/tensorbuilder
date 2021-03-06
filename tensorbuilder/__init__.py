from builder import TensorBuilder
from tensordata import Data
from phi import utils

T = TensorBuilder(utils.identity)

import patches #import last

########################
# Documentation
########################
import os

def _to_pdoc_markdown(doc):
    indent = False
    lines = []

    for line in doc.split('\n'):
        if "```" in line:
            indent = not indent
            line = line.replace("```python", '')
            line = line.replace("```", '')

        if indent:
            line = "    " + line

        lines.append(line)

    return '\n'.join(lines)

def _read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

_raw_docs = _read("README-template.md")
__version__ = _read("version.txt")
__doc__ = _to_pdoc_markdown(_raw_docs.format(__version__))
