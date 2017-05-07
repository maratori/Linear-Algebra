import math

class MatrixError(Exception):
  """ An exception class for Matrix """
  pass

class Matrix(object):
  """
    A simple Python matrix class with basic operations and operator overloading.
    m = Matrix(3,4) # zero matrix with 3 rows and 4 columns
    m = Matrix([[1,2],[3,4],[5,6]]) # matrix from list (3 rows and 2 columns)
    m = Matrix.Identity(4) # identity matrix 4x4
    m = Matrix.FromListOfRows(myList)
    m = Matrix.FromListOfCols(myList)
    m = Matrix.RowFromVector(myVectorOrList)
    m = Matrix.ColFromVector(myVectorOrList)
    m = Matrix.Diagonal(myVectorOrList)
  """
  
  def __init__(self, *args):
    if len(args) == 2:
      if isinstance(args[0], int) and isinstance(args[1], int):
        self._rowsCount = args[0]
        self._columnsCount = args[1]
        self._vals = [[0.]*self._columnsCount for x in xrange(self._rowsCount)]
    elif len(args) == 1:
      try:
        self._rowsCount = len(args[0])
        self._columnsCount = len(args[0][0])
        self._vals = [[float(x) for x in row] for row in args[0]]
      except:
        raise MatrixError("Can't create matrix.")
    else:
      raise MatrixError("Wrong numbers of arguments")
    for row in self._vals:
      if len(row) != self._columnsCount:
        raise MatrixError("Can't create matrix.")
  
  #=============
  #  Properties 
  #=============
  
  @property
  def size(self):
    return (self.m, self.n)
  
  @property
  def m(self):
    return self._rowsCount
  
  @property
  def n(self):
    return self._columnsCount
  
  @property
  def rows(self):
    return [Vector(row) for row in self._vals]
  
  @property
  def cols(self):
    return self.transpose().rows
  
  
  #=================
  #  Static methods 
  #=================
  
  @staticmethod
  def Identity(n):
    res = Matrix(n, n)
    for i in range(n):
      res[i,i] = 1.0
    return res
  
  @staticmethod
  def FromListOfRows(x):
    return Matrix(x)
  
  @staticmethod
  def FromListOfCols(x):
    return Matrix(x).transpose()
  
  @staticmethod
  def RowFromVector(x):
    return Matrix.FromListOfRows([x])
  
  @staticmethod
  def ColFromVector(x):
    return Matrix.FromListOfCols([x])
  
  @staticmethod
  def Diagonal(x):
    return Matrix([[(x[i] if i == j else 0) for j in range(len(x))] for i in range(len(x))])
  
  
  #========
  #  Tests 
  #========
  
  def isZero(self):
    return self == 0
  
  def isIdentity(self):
    return self == 1
  
  def isScalar(self):
    return self.size == (1,1)
  
  def isVector(self):
    return 1 in self.size
  
  def isSquare(self):
    return self.m == self.n
  
  def isDiagonal(self):
    if not self.isSquare():
      return False
    for i in range(0, self.m-1):
      for j in range(i+1, self.m):
        if self._vals[i][j] != 0 or self._vals[j][i] != 0:
          return False
    return True
  
  def isSymmetric(self):
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
    return [row[:] for row in self._vals]
  
  def getRow(self, n):
    return Vector(self._vals[n])
  
  def getCol(self, n):
    return self.transpose().getRow(n)
  
  def getDiagonal(self):
    return Vector([self._vals[i][i] for i in range(min(self.size))])
  
  def asScalar(self):
    if not self.isScalar():
      raise MatrixError, "Matrix is not a scalar. Size is "+str(self.size)
    return self._vals[0][0]
  
  def asVector(self):
    if not self.isVector():
      raise MatrixError, "Matrix is not a vector. Size is "+str(self.size)
    if self.m == 1:
      return self.getRow(0)
    else:
      return self.getCol(0)
  
  
  #===============
  #  Get modified 
  #===============
  
  def transpose(self):
    return Matrix(zip(*self._vals))
  
  def zero(self):
    return Matrix(*self.size)
  
  def round(self, n=0):
    res = self.zero()
    for i in xrange(res.m):
      for j in xrange(res.n):
        res[i,j] = round(self[i,j], n)
    return res
  
  def floor(self):
    return Matrix(map(lambda row: map(math.floor, row), self._vals))
  
  def ceil(self):
    return Matrix(map(lambda row: map(math.ceil, row), self._vals))
  
  def trunc(self):
    return Matrix(map(lambda row: map(math.trunc, row), self._vals))
  
  
  #=================
  #  Linear algebra 
  #=================
  
  def trace(self):
    return sum(self.getDiagonal())
  
  def det(self):
    if not self.isSquare():
      raise MatrixError, "Determinant can't be calculated for non-square matrix."
    
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
    
  #def inverse(self):
  
  def eigenvalues(self):
    if not self.isSquare():
      raise MatrixError, "Eigen values can't be calculated for non-square matrix."
    
    if self.isDiagonal():
      return sorted(list(self.getDiagonal()), reverse=True)
    
    if self.m == 2:
      a, b = self._vals[0]
      c, d = self._vals[1]
      sss = math.sqrt((a-d)**2 + 4.*b*c)
      return sorted([0.5*(a+d+sss), 0.5*(a+d-sss)], reverse=True)
    
    if self.m == 3:
      if not self.isSymmetric():
        raise NotImplemented
      
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
    
    raise NotImplemented
  
  
  #=================
  #  Representation 
  #=================
  
  def __str__(self):
    return repr(self._vals)
  
  def __repr__(self):
    return "Matrix(" + repr(self._vals) + ")"
  
  
  #===============
  #  Items access 
  #===============
  
  def __getitem__(self, key):
    if isinstance(key, slice):
      raise MatrixError, "Can't get by slice."
    elif isinstance(key, tuple) and len(key) == 2:
      return self._vals[key[0]][key[1]]
    else:
      raise MatrixError, "Error while getting item."
  
  def __setitem__(self, key, value):
    if isinstance(key, slice):
      raise MatrixError, "Can't modify by slice."
    elif isinstance(key, tuple) and len(key) == 2:
      self._vals[key[0]][key[1]] = float(value)
    else:
      raise MatrixError, "Error while setting item."
  
  
  #============
  #  Operators 
  #============
  
  def __eq__(self, other):
    """ Test equality """
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
      raise NotImplemented
    return other._vals == self._vals
  
  def __ne__(self, other):
    """ Define a non-equality test """
    return not self.__eq__(other)
  
  def __pos__(self):
    return Matrix(self._vals)
  
  def __neg__(self):
    return Matrix([[-x for x in row] for row in self._vals])
  
  def __add__(self, other):
    """ Add a matrix to this matrix and return the new matrix. Doesn't modify the current matrix """
    if not isinstance(other, Matrix):
      other = Matrix(other)
    if self.size != other.size:
      raise MatrixError, "Trying to add matrixes of different size."
    return Matrix([[sum(pair) for pair in zip(self._vals[x], other._vals[x])] for x in xrange(self.m)])
  
  def __sub__(self, other):
    """ Subtract a matrix from this matrix and return the new matrix. Doesn't modify the current matrix """
    if not isinstance(other, Matrix):
      other = Matrix(other)
    if self.size != other.size:
      raise MatrixError, "Trying to substract matrixes of different size."
    return self+(-other)
  
  def __mul__(self, other):
    """ Multiple a matrix with this matrix and return the new matrix. Doesn't modify the current matrix """
    if isinstance(other, Matrix):
      if self.n != other.m:
        raise MatrixError, "Matrices cannot be multipled. Sizes are inconsistent."
      res = Matrix(self.m, other.n)
      for x in range(res.m):
        for y in range(res.n):
          res[x,y] = sum([self[x,z]*other[z,y] for z in range(self.n)])
      return res
    if isinstance(other, Vector):
      if self.n != other.size:
        raise MatrixError, "Matrices cannot be multipled. Sizes are inconsistent."
      return self*Matrix.ColFromVector(other)
    factor = float(other)
    return Matrix([[x*factor for x in row] for row in self._vals])
  
  def __rmul__(self, other):
    """ Multiply this matrix to a scalar and return the new matrix. Doesn't modify the current matrix """
    if isinstance(other, Vector):
      if self.m != other.size:
        raise MatrixError, "Matrices cannot be multipled. Sizes are inconsistent."
      return Matrix.RowFromVector(other)*self
    return self*float(other)
  
  def __div__(self, other):
    if isinstance(other, Matrix):
      raise MatrixError, "Can't divide matrises."
    return self*(1.0/other)