# Linear Algebra Python Module

Single-file python module **linear_algebra.py** implements basic `Vector` class.


## Features

- Vector + Vector
- Vector - Vector
- Vector * number
- Vector / number
- Vector * Vector <==> Vector.dot(Vector)
- Vector.cross(Vector)
- Vector.normalize()


## Usage

- Copy file `linear_algebra.py` to your project
- Use `from linear_algebra import *`
- Use `Vector` class


## Examples

```python
from linear_algebra import *

v1 = Vector(5) # zero vector with 5 components
v2 = Vector.Zero(5) # zero vector with 5 components
v1 == v2 # True
v1.size == 5 # True
v1.magnitude == 0 # True
v1.values == [0, 0, 0, 0, 0] # True
v1.isZero() # True
v1 == 0 # True

v3 = Vector([2, 5, -6, 4]) # vector form list
v4 = Vector.FromList([2, 5, -6, 4]) # vector form list
v3 == v4 # True
v3.size == 4 # True
v3.magnitude == 9 # True
print v3 # 2.0, 5.0, -6.0, 4.0
repr(v3) == "Vector([2.0, 5.0, -6.0, 4.0])" # True

v3 - v4 == 0 # True
v3 + v4 == 2 * v3 # True
-v3 == Vector([-2, -5, 6, -4]) # True
v3 / 2 == Vector([1, 2.5, -3, 2]) # True
v3 * v4 == 81 # True
v3.dot(v4) == 81 # True

v5 = v3.normalize()
print v5 # 0.2222222222222222, 0.5555555555555556, -0.6666666666666666, 0.4444444444444444
v5 == v3 / v3.magnitude # True
v5.magnitude == 1 # True
v5.isNormalized() # True

v6 = Vector([2, 5, 7])
v7 = Vector([3, 1, 2])
v6.cross(v7) == Vector([3, 17, -13]) # True
```

## Vector Attributes

### Static Methods

- Vector.`Zero`(int) -> Vector
- Vector.`FromList`(iterable) -> Vector

### Properties

- Vector.`size` -> int
- Vector.`values` -> list
- Vector.`magnitude` -> float

### Methods

- Vector.`isZero`() -> bool
- Vector.`isNormalized`() -> bool
- Vector.`asList`() -> list
- Vector.`dot`(other) -> float
- Vector.`cross`(other) -> Vector
- Vector.`round`(ndigits=0) -> Vector
- Vector.`floor`() -> Vector
- Vector.`ceil`() -> Vector
- Vector.`trunc`() -> Vector
- Vector.`normalize`() -> Vector
- Vector.`__str__`() -> str
- Vector.`__repr__`() -> str
- Vector.`__len__`() -> int
- Vector.`__iter__`() -> iter
- Vector.`__getitem__`(key) -> float or Vector
- Vector.`__setitem__`(key, value)
- Vector.`__eq__`(other) -> bool
- Vector.`__ne__`(other) -> bool
- Vector.`__pos__`() -> Vector
- Vector.`__neg__`() -> Vector
- Vector.`__add__`(other) -> Vector
- Vector.`__sub__`(other) -> Vector
- Vector.`__mul__`(other) -> Vector or float
- Vector.`__rmul__`(other) -> Vector
- Vector.`__div__`(other) -> Vector


## Changelog

### v0.1.0 - 2017-05-14
- Vector class
- Vectors comparison
- All operations with vectors (`+`, `-`, `*`, `/`, `.dot`, `.cross`)
- Other vector methods


> _Readme last update 2017-05-14_