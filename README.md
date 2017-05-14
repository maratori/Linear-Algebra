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

- Copy file linear_algebra.py to your project
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
v1 == 0 # True

v3 = Vector([2, 5, -6, 4]) # vector form list
v4 = Vector.FromList([2, 5, -6, 4]) # vector form list
v3 == v4 # True
v3.size == 4 # True
v3.magnitude == 9 # True

v3 - v4 == 0 # True
v3 + v4 == 2 * v3 # True
-v3 == Vector([-2, -5, 6, -4]) # True
v3 / 2 == Vector([-1, -2.5, 3, -2]) # True
```


## Changelog

### 1.0.0 - 2017-05-XXXXXXXXXX
- 
- 


> _Readme last update 2017-05-XXXXXXXXX_