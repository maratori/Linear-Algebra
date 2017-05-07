import math

class VectorError(Exception):
  """ An exception class for Vector """
  pass

class Vector(object):
  """
    A simple Python vector class with basic operations and operator overloading.
    v = Vector(5) # zero vector with size of 5
    v = Vector([1,4,5,6]) # vector from list
    v = Vector.FromList([1,4,5,6]) # vector from list
    v = Vector(myIterator) # vector from iterator
  """
  
  def __init__(self, arg):
    if isinstance(arg, int):
      self._vals = [0.]*arg
    else:
      try:
        self._vals = [float(x) for x in arg]
      except:
        raise VectorError("Can't create vector.")
    if len(self._vals) == 0:
      raise VectorError("Vector size should be positive.")
  
  @property
  def size(self):
    return len(self._vals)
  
  @property
  def values(self):
    return self._vals[:]
  
  @property
  def magnitude(self):
    return math.sqrt(self*self)
  
  @staticmethod
  def FromList(x):
    return Vector(x)
  
  def asList(self):
    return self.values
  
  def dot(self, other):
   """ Dot product a vector to this vector. """
   if not isinstance(other, Vector):
     raise VectorError, "Argument should be a Vector."
   return self*other
  
  def cross(self, other):
    """ Cross product a vector to this vector. """
    if not isinstance(other, Vector):
      if isinstance(other, int):
        raise VectorError, "Argument should be a Vector."
      other = Vector(other)
    if len(self) != 3 or len(other) != 3:
      raise VectorError, "Cross product is valid only for vectors of size 3."
    return Vector([self[1]*other[2]-self[2]*other[1], self[2]*other[0]-self[0]*other[2], self[0]*other[1]-self[1]*other[0]])
  
  def round(self, n=0):
    return Vector([round(x, n) for x in self])
  
  def floor(self):
    return Vector(map(math.floor, self))
  
  def ceil(self):
    return Vector(map(math.ceil, self))
  
  def trunc(self):
    return Vector(map(math.trunc, self))
  
  def zero(self):
    return Vector(len(self))
  
  def isZero(self):
    return self == 0
  
  def isNormalized(self):
    return self.magnitude == 1
  
  def normalize(self):
    return self/self.magnitude
  
  def __str__(self):
    return ", ".join(map(str, self))
  
  def __repr__(self):
    return "Vector(" + repr(self._vals) + ")"
  
  def __iter__(self):
    """ Get iterator """
    return iter(self._vals)
  
  def __len__(self):
    return self.size
  
  def __getitem__(self, key):
    if isinstance(key, slice):
      return Vector(self._vals[key])
    else:
      return self._vals[key]
  
  def __setitem__(self, key, value):
    if isinstance(key, slice):
      raise VectorError, "Can't modify vector by slice."
    else:
      self._vals[key] = float(value)
  
  def __eq__(self, other):
    """ Test equality """
    if other is None:
      return False
    if not isinstance(other, Vector):
      if isinstance(other, int) and other == 0:
        return all(x==0 for x in self)
      else:
        raise NotImplemented
    return other._vals == self._vals
  
  def __ne__(self, other):
    """ Define a non-equality test """
    return not self.__eq__(other)
  
  def __pos__(self):
    return Vector(self)
  
  def __neg__(self):
    return Vector([-x for x in self])
  
  def __add__(self, other):
    """ Add a vector to this vector and return the new vector. Doesn't modify the current vector """
    if not isinstance(other, Vector):
      if isinstance(other, int):
        raise VectorError, "Can't add int to Vector."
      other = Vector(other)
    if len(self) != len(other):
      raise VectorError, "Can't add vectors of different size."
    return Vector([sum(pair) for pair in zip(self, other)])
  
  def __sub__(self, other):
    """ Subtract a vector from this vector and return the new vector. Doesn't modify the current vector """
    if not isinstance(other, Vector):
      if isinstance(other, int):
        raise VectorError, "Can't subtract int from Vector."
      other = Vector(other)
    if len(self) != len(other):
      raise VectorError, "Can't subtract vectors of different size."
    return self+(-other)
  
  def __mul__(self, other):
    """ Multiply a scalar to this vector and return the new vector. Doesn't modify the current vector """
    if isinstance(other, Vector):
    #  raise VectorError, "Can't multiply vectors. Use cross or dot methods."
      if len(self) != len(other):
        raise VectorError, "Can't multiply (dot) vectors of different size."
      return sum(pair[0]*pair[1] for pair in zip(self, other))
    try:
      factor = float(other)
      return Vector([x*factor for x in self])
    except:
      return other.__rmul__(self)
  
  def __rmul__(self, other):
    """ Multiply this vector to a scalar and return the new vector. Doesn't modify the current vector """
    return self*float(other)
  
  def __div__(self, other):
    if isinstance(other, Vector):
      raise VectorError, "Can't divide vectors."
    return self*(1.0/other)