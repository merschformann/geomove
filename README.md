# geomove

[![pypi_version](https://img.shields.io/pypi/v/geomove?label=pypi)](https://pypi.org/project/geomove)[![build](https://github.com/merschformann/geomove/actions/workflows/build.yml/badge.svg)](https://github.com/merschformann/geomove/actions/workflows/build.yml)

Moves points on earth's surface towards a given bearing by a given distance.

## Installation

```bash
pip install geomove
```

## Usage

Move a point west by 10 km:

```python
from geomove import move, Bearing

# Define point
point = (13.4, 52.5)

# Move 
moved_point = move(point, Bearing.WEST, 10)
```

Move a point towards 357° by 5 km:

```python
from geomove import move

# Define point
point = (13.4, 52.5)

# Move
moved_point = move(point, 357, 5)
```
