import math
import numbers

class VectorError(Exception):
  """An exception class for Vector"""
  pass

class Vector(object):
  """
    class Vector(object):

    A simple vector class with basic operations and operator overloading.

    Constructors:
      Vector(int) -> zero Vector with specified size
      Vector(iterable) -> Vector with components from any iterable object, i.e. list
      Vector.FromList(iterable) <==> Vector(iterable)
  """
  
  def __init__(self, arg):
    """
      Vector constructor

      Vector(int) -> zero Vector with specified size
      Vector(iterable) -> Vector with components from any iterable object, i.e. list
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
    if not isinstance(x, (numbers.Integral, str, unicode)):
      return Vector(x)
    else:
      raise ValueError("Argument should be an iterable. {0} passed instead".format(type(x)))

  @staticmethod
  def Parse(value):
    """Vector.Parse(str) -> Vector"""
    if isinstance(value, (str, unicode)):
      return NotImplemented
    else:
      raise: TypeError("Argument should be a string. {0} passed instead".format((type(value))))
  
  def asList(self):
    """Get list of components.\nvector.asList() <==> vector.values"""
    return self.values
  
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
  
  def round(self, ndigits=0):
    """Get vector with rounded components (see help(round))"""
    return Vector([round(x, ndigits) for x in self])
  
  def floor(self):
    """Get vector with floored components (see help(floor))"""
    return Vector(map(math.floor, self))
  
  def ceil(self):
    """Get vector with ceiled components (see help(ceil))"""
    return Vector(map(math.ceil, self))
  
  def trunc(self):
    """Get vector with truncated components (see help(trunc))"""
    return Vector(map(math.trunc, self))
  
  def zero(self):
    """Get zero vector of the same size"""
    return Vector(len(self))
  
  def isZero(self):
    """Check if all components are zero"""
    return self == 0
  
  def isNormalized(self):
    """Check if vector magnitude == 1"""
    return self.magnitude == 1
  
  def normalize(self):
    """Get normalized vector"""
    return self/self.magnitude
  
  def __str__(self):
    """Get string to print vector by str()"""
    return ", ".join(map(str, self))
  
  def __repr__(self):
    """Get string to represent vector by repr()"""
    return "Vector(" + repr(self._vals) + ")"
  
  def __iter__(self):
    """Get iterator over the components"""
    return iter(self._vals)
  
  def __len__(self):
    """Get vector size by len()"""
    return len(self._vals)
  
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
    return self*float(other)
  
  def __div__(self, other):
    """Divide vector to scalar"""
    try:
      return self*(1/float(other))
    except:
      return NotImplemented