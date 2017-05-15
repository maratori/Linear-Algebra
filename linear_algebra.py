"""Linear Algebra Module v0.2.0 [2017-05-15]
Module implements Vector and Matrix classes.
Repository: https://github.com/Maratori/Linear-Algebra
"""

__all__ = ["Vector", "Matrix", "VectorError", "MatrixError"]
__version__ = "0.2.0"
__author__ = "Marat Reymers"

import math
import numbers

class VectorError(Exception):
  """An exception class for Vector"""
  pass

class MatrixError(Exception):
  """ An exception class for Matrix """
  pass

class Vector(object):
  """
    class Vector(object):

    A simple vector class with basic operations and operator overloading.

    Constructors:
      Vector(int) -> zero Vector with specified size
      Vector(iterable) -> Vector with components from any iterable object, i.e. list
      Vector(str) not implemented yet

      Vector.Zero(int) <==> Vector(int)
      Vector.FromList(iterable) <==> Vector(iterable)
      Vector.Parse(str) <==> Vector(str)
  """
  
  def __init__(self, arg):
    """
      Vector constructor

      Vector(int) -> zero Vector with specified size
      Vector(iterable) -> Vector with components from any iterable object, i.e. list
      Vector(str) not implemented yet
    """
    if isinstance(arg, numbers.Integral):
      if arg > 0:
        self._vals = [0.]*arg
      else:
        raise ValueError("Argument should be an int > 0 or iterable object. {0} passed instead".format(arg))
    elif isinstance(arg, (str, unicode)):
      raise TypeError("Argument should be an int > 0 or iterable object. {0} passed instead".format(arg))
    else:
      try:
        self._vals = [float(x) for x in arg]
      except:
        raise VectorError("Can't create vector.")
      if len(self._vals) == 0:
        raise VectorError("Vector size should be positive.")
  

  #=============
  #  Properties 
  #=============

  @property
  def size(self):
    """int: read-only vector size (number of components).\nvector.size <==> len(vector)"""
    return len(self)
  
  @property
  def values(self):
    """list: read-only list of components"""
    return list(self._vals)
  
  @property
  def magnitude(self):
    """float: read-only vector magnitude (Euclidean norm)"""
    return math.sqrt(self*self)
  
  
  #=================
  #  Static methods 
  #=================
  
  @staticmethod
  def Zero(size):
    """Vector.Zero(int) -> zero Vector with specified size"""
    if isinstance(size, numbers.Integral):
      if size > 0:
        return Vector(size)
      else:
        raise ValueError("Argument should be an int > 0. {0} passed instead".format(size))
    else:
      raise TypeError("Argument should be an int > 0. {0} passed instead".format(size))

  @staticmethod
  def FromList(x):
    """Vector.FromList(iterable) -> Vector with components from any iterable object, i.e. list"""
    if not isinstance(x, (numbers.Number, str, unicode)):
      return Vector(x)
    else:
      raise TypeError("Argument should be an iterable. {0} passed instead".format(type(x)))

  @staticmethod
  def Parse(value):
    """Vector.Parse(str) -> Vector"""
    if isinstance(value, (str, unicode)):
      return NotImplemented
    else:
      raise TypeError("Argument should be a string. {0} passed instead".format((type(value))))
  
  
  #========
  #  Tests 
  #========
  
  def isZero(self):
    """Check if all components are zero"""
    return self == 0
  
  def isNormalized(self):
    """Check if vector magnitude == 1"""
    return self.magnitude == 1
  
  
  #============
  #  Get parts 
  #============
  
  def asList(self):
    """Get list of components.\nvector.asList() <==> vector.values"""
    return self.values
  
  
  #=================
  #  Linear algebra 
  #=================
  
  def dot(self, other):
    """Get dot product self and passed vector."""
    if not isinstance(other, Vector):
      raise TypeError("Argument should be a Vector.")
    return self*other
  
  def cross(self, other):
    """Get cross product self and passed vector. Works only with vectors of size 3."""
    if len(self) != 3:
      raise NotImplementedError("Cross product is defined only for vectors of size 3. This vector has size {0}".format(len(self)))
    if not isinstance(other, Vector):
      raise TypeError("Argument should be a Vector.")
    if len(other) != 3:
      raise ValueError("Cross product is defined only for vectors of size 3. Passed vector has size {0}".format(len(other)))
    return Vector([self[1]*other[2]-self[2]*other[1], self[2]*other[0]-self[0]*other[2], self[0]*other[1]-self[1]*other[0]])
  
  
  #===============
  #  Get modified 
  #===============
  
  def round(self, ndigits=0):
    """Get vector with rounded components (see help(round))"""
    return Vector([round(x, ndigits) for x in self])
  
  def floor(self):
    """Get vector with floored components (see help(math.floor))"""
    return Vector(map(math.floor, self))
  
  def ceil(self):
    """Get vector with ceiled components (see help(math.ceil))"""
    return Vector(map(math.ceil, self))
  
  def trunc(self):
    """Get vector with truncated components (see help(math.trunc))"""
    return Vector(map(math.trunc, self))
  
  def normalize(self):
    """Get normalized vector"""
    return self/self.magnitude
  
  
  #=================
  #  Representation 
  #=================
  
  def __str__(self):
    """Get string to print vector by str()"""
    return ", ".join(map(str, self))
  
  def __repr__(self):
    """Get string to represent vector by repr()"""
    return "Vector(" + repr(self._vals) + ")"
  
  
  #===============
  #  Items access 
  #===============
  
  def __len__(self):
    """Get vector size by len()"""
    return len(self._vals)
  
  def __iter__(self):
    """Get iterator over the components"""
    return iter(self._vals)
  
  def __getitem__(self, key):
    """Get component by index or Vector by slice"""
    if isinstance(key, slice):
      return Vector(self._vals[key])
    else:
      return self._vals[key]
  
  def __setitem__(self, key, value):
    """Modify component by index"""
    if isinstance(key, slice):
      raise TypeError("Can't modify vector by slice")
    else:
      self._vals[key] = float(value)
  
  
  #============
  #  Operators 
  #============
  
  def __eq__(self, other):
    """Check for equality"""
    if other is None:
      return False
    if not isinstance(other, Vector):
      if isinstance(other, (int, float)) and other == 0:
        return all(x==0 for x in self)
      else:
        raise ValueError("Can't compare vector and '{0.__name__}'".format(type(other)))
    return other._vals == self._vals
  
  def __ne__(self, other):
    """Check for non-equality"""
    return not self.__eq__(other)
  
  def __pos__(self):
    """Get positive Vector"""
    return Vector(self)
  
  def __neg__(self):
    """Get negative Vector"""
    return Vector([-x for x in self])
  
  def __add__(self, other):
    """Add vector to vector"""
    if not isinstance(other, Vector):
      return NotImplemented
    if len(self) != len(other):
      raise VectorError("Can't add vectors of different size")
    return Vector([sum(pair) for pair in zip(self, other)])
  
  def __sub__(self, other):
    """Substract vector from vector"""
    if not isinstance(other, Vector):
      return NotImplemented
    if len(self) != len(other):
      raise VectorError("Can't subtract vectors of different size")
    return self + -other
  
  def __mul__(self, other):
    """Multiply vector to scalar or vector to vector (dot product)"""
    if isinstance(other, Vector):
      if len(self) != len(other):
        raise VectorError("Can't multiply (dot product) vectors of different size")
      return sum(pair[0]*pair[1] for pair in zip(self, other))
    try:
      factor = float(other)
      return Vector([x*factor for x in self])
    except:
      return NotImplemented
  
  def __rmul__(self, other):
    """Multiply scalar to vector"""
    try:
      return self*float(other)
    except:
      return NotImplemented
  
  def __div__(self, other):
    """Divide vector to scalar"""
    try:
      return self*(1./float(other))
    except ZeroDivisionError:
      raise
    except:
      return NotImplemented

class Matrix(object):
  """
    class Matrix(object):

    A simple matrix calss with basic operations and operator overloading.

    Constructors:
      Matrix(int, int) -> zero Matrix with specified number of rows and columns
      Matrix(iterable) -> Matrix with rows form any iterable object, i.e. list
      Matrix(str) not implemented yet
      
      Matrix.Zero(int, int) <==> Matrix(int, int)
      Matrix.Identity(int) -> identity square Matrix with specified size
      Matrix.Diagonal(iterable) -> diagonal square Matrix with diagonal components form any iterable object, i.e. list
      Matrix.FromListOfRows(iterable) <==> Matrix(iterable)
      Matrix.FromListOfCols(iterable) -> Matrix with columns form any iterable object, i.e. list
      Matrix.Parse(str) <==> Matrix(str)
      Matrix.RowFromVector(iterable) -> single-row Matrix with components form any iterable object, i.e. list
      Matrix.ColFromVector(iterable) -> single-column Matrix with components form any iterable object, i.e. list
  """
  
  def __init__(self, *args):
    """
      Matrix constructor

      Matrix(int, int) -> zero Matrix with specified number of rows and columns
      Matrix(iterable) -> Matrix with rows form any iterable object, i.e. list
      Matrix(str) not implemented yet
    """
    if len(args) == 2:
      if (isinstance(args[0], numbers.Integral) and args[0] > 0 and
          isinstance(args[1], numbers.Integral) and args[1] > 0):
        self._rowsCount = args[0]
        self._columnsCount = args[1]
        self._vals = [[0.]*self._columnsCount for x in xrange(self._rowsCount)]
      else:
        raise ValueError("Two arguments passed. Both should be an int > 0. {0} and {1} passed instead".format(arg[0], arg[1]))
    elif len(args) == 1:
      if isinstance(arg, (str, unicode)):
        raise NotImplementedError
      else:
        try:
          self._rowsCount = len(args[0])
          self._columnsCount = len(args[0][0])
          self._vals = [[float(x) for x in row] for row in args[0]]
        except:
          raise MatrixError("Can't create matrix.")
        for row in self._vals:
          if len(row) != self._columnsCount:
            raise MatrixError("Can't create matrix.")
    else:
      raise TypeError("Wrong numbers of arguments. Should be 1 or 2. {0} passed".format(len(args)))
  
  #=============
  #  Properties 
  #=============
  
  @property
  def size(self):
    """tuple: read-only matrix size (number_of_rows, number_of_columns)"""
    return (self.m, self.n)
  
  @property
  def m(self):
    """int: read-only number of rows"""
    return self._rowsCount
  
  @property
  def n(self):
    """int: read-only number of columns"""
    return self._columnsCount
  
  @property
  def rows(self):
    """list: read-only list of rows. Each row is a Vector"""
    return [Vector(row) for row in self._vals]
  
  @property
  def cols(self):
    """list: read-only list of columns. Each column is a Vector"""
    return self.transpose().rows
  
  
  #=================
  #  Static methods 
  #=================
  
  @staticmethod
  def Zero(self, m, n):
    """Matrix.Zero(int, int) -> zero Matrix with specified number of rows and columns"""
    if isinstance(m, numbers.Integral) and isinstance(n, numbers.Integral):
      if m > 0 and n > 0:
        return Matrix(m, n)
      else:
        raise ValueError("Arguments should be an int > 0. {0} and {1} passed instead".format(m, n))
    else:
      raise TypeError("Arguments should be an int > 0. {0} and {1} passed instead".format(m, n))

  @staticmethod
  def Identity(n):
    """Matrix.Identity(int) -> identity square Matrix with specified size"""
    if isinstance(n, numbers.Integral):
      if n > 0:
        res = Matrix(n, n)
        for i in range(n):
          res[i,i] = 1.0
        return res
      else:
        raise ValueError("Argument should be an int > 0. {0} passed instead".format(n))
    else:
      raise TypeError("Argument should be an int > 0. {0} passed instead".format(n))
  
  @staticmethod
  def FromListOfRows(x):
    """Matrix.FromListOfRows(iterable) -> Matrix with rows form any iterable object, i.e. list"""
    return Matrix(x)
  
  @staticmethod
  def FromListOfCols(x):
    """Matrix.FromListOfCols(iterable) -> Matrix with columns form any iterable object, i.e. list"""
    return Matrix(x).transpose()
  
  @staticmethod
  def RowFromVector(x):
    """Matrix.RowFromVector(iterable) -> single-row Matrix with components form any iterable object, i.e. list"""
    return Matrix.FromListOfRows([x])
  
  @staticmethod
  def ColFromVector(x):
    """Matrix.ColFromVector(iterable) -> single-column Matrix with components form any iterable object, i.e. list"""
    return Matrix.FromListOfCols([x])
  
  @staticmethod
  def Diagonal(x):
    """Matrix.Diagonal(iterable) -> diagonal square Matrix with diagonal components form any iterable object, i.e. list"""
    return Matrix([[(x[i] if i == j else 0) for j in range(len(x))] for i in range(len(x))])

  @staticmethod
  def Parse(value):
    """Matrix.Parse(str) -> Matrix"""
    if isinstance(value, (str, unicode)):
      return NotImplemented
    else:
      raise TypeError("Argument should be a string. {0} passed instead".format((type(value))))
  
  
  #========
  #  Tests 
  #========
  
  def isZero(self):
    """Check if all components are zero"""
    return self == 0
  
  def isIdentity(self):
    """Check if all components are zero, except of diagonal (all componants = 1)"""
    return self == 1
  
  def isScalar(self):
    """Check if matrix size is 1x1"""
    return self.size == (1,1)
  
  def isVector(self):
    """Check if matrix is single-row or single-column"""
    return 1 in self.size
  
  def isSquare(self):
    """Check if matrix number of rows = number of columns"""
    return self.m == self.n
  
  def isDiagonal(self):
    """Check if matrix is square and all non-diagonal elements are zero"""
    if not self.isSquare():
      return False
    for i in range(0, self.m-1):
      for j in range(i+1, self.m):
        if self._vals[i][j] != 0 or self._vals[j][i] != 0:
          return False
    return True
  
  def isSymmetric(self):
    """Check if matrix is square and symmetric"""
    if not self.isSquare():
      return False
    for i in range(0, self.m-1):
      for j in range(i+1, self.m):
        if self._vals[i][j] != self._vals[j][i]:
          return False
    return True
  
  
  #============
  #  Get parts 
  #============
  
  def asList(self):
    """Get list of rows, where each row is list of components"""
    return [row[:] for row in self._vals]
  
  def getRow(self, n):
    """Get Vector with components from specified row"""
    return Vector(self._vals[n])
  
  def getCol(self, n):
    """Get Vector with components from specified column"""
    return self.transpose().getRow(n)
  
  def getDiagonal(self):
    """Get Vector with components from main diagonal"""
    return Vector([self._vals[i][i] for i in range(min(self.size))])
  
  def asScalar(self):
    """Convert matrix to float if possible"""
    if not self.isScalar():
      raise MatrixError("Matrix is not a scalar. Size is {0}".format(self.size))
    return self._vals[0][0]
  
  def asVector(self):
    """Convert matrix to Vector if possible"""
    if not self.isVector():
      raise MatrixError("Matrix is not a vector. Size is {0}".format(self.size))
    if self.m == 1:
      return self.getRow(0)
    else:
      return self.getCol(0)
  
  
  #===============
  #  Get modified 
  #===============
  
  def transpose(self):
    """Get transposed matrix"""
    return Matrix(zip(*self._vals))
  
  def round(self, n=0):
    """Get matrix with rounded components (see help(round))"""
    res = self.zero()
    for i in xrange(res.m):
      for j in xrange(res.n):
        res[i,j] = round(self[i,j], n)
    return res
  
  def floor(self):
    """Get matrix with floored components (see help(math.floor))"""
    return Matrix(map(lambda row: map(math.floor, row), self._vals))
  
  def ceil(self):
    """Get matrix with ceiled components (see help(math.ceil))"""
    return Matrix(map(lambda row: map(math.ceil, row), self._vals))
  
  def trunc(self):
    """Get vector with truncated components (see help(math.trunc))"""
    return Matrix(map(lambda row: map(math.trunc, row), self._vals))
  
  
  #=================
  #  Linear algebra 
  #=================
  
  def trace(self):
    """Get trace of matrix (sum of diagonal elements)"""
    return sum(self.getDiagonal())
  
  def det(self):
    """Get determinant of matrix"""
    if not self.isSquare():
      raise NotImplementedError("Determinant can't be calculated for non-square matrix")
    
    if self.isDiagonal():
      return reduce(lambda x, y: x*y, self.getDiagonal())
    
    if self.m == 2:
      return self._vals[0][0] * self._vals[1][1] - self._vals[0][1] * self._vals[1][0]
    
    res = 0.
    for i, a in enumerate(self._vals[0]):
      m = Matrix([self._vals[j][:i] + self._vals[j][(i+1):] for j in range(1, self.m)])
      if i % 2 == 0:
        res += a * m.det()
      else:
        res -= a * m.det()
    return res
  
  def eigenvalues(self):
    """Get sorted list of eigenvalues of matrix"""
    if not self.isSquare():
      raise NotImplementedError("Eigen values can't be calculated for non-square matrix")
    
    if self.isDiagonal():
      return sorted(list(self.getDiagonal()), reverse=True)
    
    if self.m == 2:
      a, b = self._vals[0]
      c, d = self._vals[1]
      sss = math.sqrt((a-d)**2 + 4.*b*c)
      return sorted([0.5*(a+d+sss), 0.5*(a+d-sss)], reverse=True)
    
    if self.m == 3 and self.isSymmetric():
      p1 = self._vals[0][1]**2 + self._vals[0][2]**2 + self._vals[1][2]**2
      q = self.trace()/3
      p2 = 2.*p1 + (self._vals[0][0]-q)**2 + (self._vals[1][1]-q)**2 + (self._vals[2][2]-q)**2
      p = math.sqrt(p2/6)
      B = (self - q * Matrix.Identity(3)) / p
      r = B.det() / 2
      
      # In exact arithmetic for a symmetric matrix  -1 <= r <= 1
      # but computation error can leave it slightly outside this range.
      if r <= -1:
        phi = math.pi / 3
      elif r >= 1:
        phi = 0.
      else:
        phi = math.acos(r) / 3
      
      # the eigenvalues satisfy eig3 <= eig2 <= eig1
      eig1 = q + 2 * p * math.cos(phi)
      eig3 = q + 2 * p * math.cos(phi + (2*math.pi/3))
      eig2 = 3 * q - eig1 - eig3
      return [eig1, eig2, eig3]
    
    raise NotImplementedError("eigenvalues() implemented for: diagonal matrix, square matrix size of 2, symmetric matrix size of 3")
  
  
  #=================
  #  Representation 
  #=================
  
  def __str__(self):
    """Get string to print metrix by str()"""
    return repr(self._vals)
  
  def __repr__(self):
    """Get string to represent matrix by repr()"""
    return "Matrix(" + repr(self._vals) + ")"
  
  
  #===============
  #  Items access 
  #===============
  
  def __getitem__(self, key):
    """Get component by index (tuple)"""
    if isinstance(key, slice):
      raise TypeError("Can't get item by slice")
    elif isinstance(key, tuple):
      if len(key) == 2:
        return self._vals[key[0]][key[1]]
      else:
        raise ValueError("Tuple length should be 2. {0} passed instead".format(len(key)))
    else:
      raise TypeError("Index should be a tuple")
  
  def __setitem__(self, key, value):
    """Modify component by index (tuple)"""
    if isinstance(key, slice):
      raise TypeError("Can't modify by slice")
    elif isinstance(key, tuple):
      if len(key) == 2:
        self._vals[key[0]][key[1]] = float(value)
      else:
        raise ValueError("Tuple length should be 2. {0} passed instead".format(len(key)))
    else:
      raise TypeError("Index should be a tuple")
  
  
  #============
  #  Operators 
  #============
  
  def __eq__(self, other):
    """Check for equality"""
    if other is None:
      return False
    if not isinstance(other, Matrix):
      if isinstance(other, int):
        if other == 0:
          return all(x==0 for x in sum(zip(*self._vals),()))
        elif other == 1:
          if self.m != self.n:
            return False
          for i in range(self.m):
            for j in range(self.n):
              if i == j:
                if self[(i,j)] != 1:
                  return False
              else:
                if self[(i,j)] != 0:
                  return False
          return True
      return NotImplemented
    return other._vals == self._vals
  
  def __ne__(self, other):
    """Check for non-equality"""
    return not self.__eq__(other)
  
  def __pos__(self):
    """Get positive Matrix"""
    return Matrix(self._vals)
  
  def __neg__(self):
    """Get negative Matrix"""
    return Matrix([[-x for x in row] for row in self._vals])
  
  def __add__(self, other):
    """Add matrix to matrix"""
    if not isinstance(other, Matrix):
      other = Matrix(other)
    if self.size != other.size:
      raise MatrixError("Trying to add matrixes of different size")
    return Matrix([[sum(pair) for pair in zip(self._vals[x], other._vals[x])] for x in xrange(self.m)])
  
  def __sub__(self, other):
    """Subtract matrix from matrix"""
    if not isinstance(other, Matrix):
      other = Matrix(other)
    if self.size != other.size:
      raise MatrixError("Trying to substract matrixes of different size")
    return self+(-other)
  
  def __mul__(self, other):
    """Multiply matrix to scalar or matrix to matrix or matrix to vector"""
    if isinstance(other, Matrix):
      if self.n != other.m:
        raise MatrixError("Matrices cannot be multipled. Sizes are inconsistent")
      res = Matrix(self.m, other.n)
      for x in range(res.m):
        for y in range(res.n):
          res[x,y] = sum([self[x,z]*other[z,y] for z in range(self.n)])
      return res
    if isinstance(other, Vector):
      if self.n != other.size:
        raise MatrixError("Matrices cannot be multipled. Sizes are inconsistent")
      return self*Matrix.ColFromVector(other)
    factor = float(other)
    return Matrix([[x*factor for x in row] for row in self._vals])
  
  def __rmul__(self, other):
    """Multiply scalar to matrix or vector to matrix"""
    if isinstance(other, Vector):
      if self.m != other.size:
        raise MatrixError("Matrices cannot be multipled. Sizes are inconsistent")
      return Matrix.RowFromVector(other)*self
    return self*float(other)
  
  def __div__(self, other):
    """Divide matrix to scalar"""
    if isinstance(other, Matrix):
      raise MatrixError("Can't divide matrises")
    return self*(1.0/other)