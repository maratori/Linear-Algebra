# Linear Algebra Python Module

Single-file python module **linear_algebra.py** implements basic `Vector` and `Matrix` classes.


## Features

- Vector*number, Vector/number
- Vector+Vector, Vector-Vector
- Vector*Vector <==> Vector.dot(Vector)
- Vector.cross(Vector)
- Vector.normalize()

- Matrix*number, Matrix/number
- Matrix+Matrix, Matrix-Matrix
- Matrix*Matrix, Matrix*Vector, Vector*Matrix
- Matrix.transpose()
- Matrix.trace()
- Matrix.det()
- Matrix.eigenvalues()


## Usage

- Copy file `linear_algebra.py` to your project
- Use `from linear_algebra import *`
- Use `Vector` and `Matrix` classes


## Examples

### Working with Vector

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

### Working with Matrix

```python
from linear_algebra import *

m1 = Matrix(2, 3) # zero matrix with 2 rows and 3 columns
m2 = Matrix.Zero(2, 3) # zero matrix with 2 rows and 3 columns
m1 == m2 # True
m1.size == (2, 3) # True
m1.isZero() # True
m1 == 0 # True

m3 = Matrix.Identity(3) # identity matrix 3x3
m4 = Matrix([[1,0,0], [0,1,0], [0,0,1]]) # identity matrix 3x3
m3 == m4 # True
m3.size == (3, 3) # True
m3.isIdentity() # True
m3 == 1 # True

m5 = Matrix.FromListOfRows([[1,2,3], [4,5,6]]) # matrix from list of rows
m6 = Matrix.FromListOfCols([[1,4], [2,5], [3,6]]) # matrix from list of columns
m5 == m6 # True
print m5 # [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]
repr(m5) == "Matrix([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])" # True

m7 = Matrix.RowFromVector([1,2,3])
m8 = Matrix.ColFromVector([1,2,3])
print m7 # [[1.0, 2.0, 3.0]]
print m8 # [[1.0], [2.0], [3.0]]
m7.transpose() == m8 # True

m9 = Matrix.Diagonal([1,2,3])
print m9 # [[1.0, 0.0, 0.0], [0.0, 2.0, 0.0], [0.0, 0.0, 3.0]]
```

## List of all attributes

<details>
<summary>Show</summary>

> ### Vector Static Methods
> 
> - Vector.`Zero`(int) -> Vector
> - Vector.`FromList`(iterable) -> Vector
> 
> ### Vector Properties
> 
> - Vector.`size` -> int
> - Vector.`values` -> list
> - Vector.`magnitude` -> float
> 
> ### Vector Methods
> 
> - Vector.`isZero`() -> bool
> - Vector.`isNormalized`() -> bool
> - Vector.`asList`() -> list
> - Vector.`dot`(other) -> float
> - Vector.`cross`(other) -> Vector
> - Vector.`round`(ndigits=0) -> Vector
> - Vector.`floor`() -> Vector
> - Vector.`ceil`() -> Vector
> - Vector.`trunc`() -> Vector
> - Vector.`normalize`() -> Vector
> - Vector.`__str__`() -> str
> - Vector.`__repr__`() -> str
> - Vector.`__len__`() -> int
> - Vector.`__iter__`() -> iter
> - Vector.`__getitem__`(key) -> float or Vector
> - Vector.`__setitem__`(key, value)
> - Vector.`__eq__`(other) -> bool
> - Vector.`__ne__`(other) -> bool
> - Vector.`__pos__`() -> Vector
> - Vector.`__neg__`() -> Vector
> - Vector.`__add__`(other) -> Vector
> - Vector.`__sub__`(other) -> Vector
> - Vector.`__mul__`(other) -> Vector or float
> - Vector.`__rmul__`(other) -> Vector
> - Vector.`__div__`(other) -> Vector

> ### Matrix Static Methods
> 
> - Matrix.`Zero`(int, int) -> Matrix
> - Matrix.`Identity`(int) -> Matrix
> - Matrix.`FromListOfRows`(iterable) -> Matrix
> - Matrix.`FromListOfCols`(iterable) -> Matrix
> - Matrix.`RowFromVector`(iterable) -> Matrix
> - Matrix.`ColFromVector`(iterable) -> Matrix
> - Matrix.`Diagonal`(iterable) -> Matrix
> 
> ### Matrix Properties
> 
> - Matrix.`size` -> tuple
> - Matrix.`m` -> int
> - Matrix.`n` -> int
> - Matrix.`rows` -> list
> - Matrix.`cols` -> list
> 
> ### Matrix Methods
> 
> - Matrix.`isZero`() -> bool
> - Matrix.`isIdentity`() -> bool
> - Matrix.`isScalar`() -> bool
> - Matrix.`isVector`() -> bool
> - Matrix.`isSquare`() -> bool
> - Matrix.`isDiagonal`() -> bool
> - Matrix.`isSymmetric`() -> bool
> - Matrix.`asList`() -> list
> - Matrix.`getRow`(n) -> Vector
> - Matrix.`getCol`(n) -> Vector
> - Matrix.`getDiagonal`() -> Vector
> - Matrix.`asScalar`() -> float
> - Matrix.`asVector`() -> Vector
> - Matrix.`transpose`() -> Matrix
> - Matrix.`round`(n=0) -> Matrix
> - Matrix.`floor`() -> Matrix
> - Matrix.`ceil`() -> Matrix
> - Matrix.`trunc`() -> Matrix
> - Matrix.`trace`() -> float
> - Matrix.`det`() -> float
> - Matrix.`eigenvalues`() -> list
> - Matrix.`__str__`() -> str
> - Matrix.`__repr__`() -> str
> - Matrix.`__getitem__`(key) -> float
> - Matrix.`__setitem__`(key, value)
> - Matrix.`__eq__`(other) -> bool
> - Matrix.`__ne__`(other) -> bool
> - Matrix.`__pos__`() -> Matrix
> - Matrix.`__neg__`() -> Matrix
> - Matrix.`__add__`(other) -> Matrix
> - Matrix.`__sub__`(other) -> Matrix
> - Matrix.`__mul__`(other) -> Matrix
> - Matrix.`__rmul__`(other) -> Matrix
> - Matrix.`__div__`(other) -> Matrix

</details>


## Changelog

### 0.2.0 [2017-05-21]

- Add `Matrix` class
- Add comparison of matrices
- Add all operations with matrices (`+`, `-`, `*`, `/`)
- Add matrix*vector and vector*matrix
- Add other matrix methods
- Add matrix_tests.py
- Fix some comments
- Fix vector_tests.py
- Eigenvalues implemented for matrices: diagonal, 2x2, symmetric 3x3

### 0.1.0 [2017-05-14]

- Add `Vector` class
- Add comparison of vectors
- Add all operations with vectors (`+`, `-`, `*`, `/`, `.dot`, `.cross`)
- Add other vector methods


> _Readme last update 2017-05-21_