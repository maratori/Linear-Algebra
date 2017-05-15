import unittest
import sys
import os
import random
sys.path.append(os.path.abspath(".."))
from linear_algebra import *

class TestVectorConstructor(unittest.TestCase):

  def test_int(self):
    for i in xrange(1000):
      with self.assertRaises(ValueError):
        Vector(-i)
    for i in xrange(1, 1000):
      self.assertEqual(Vector(i).values, [0]*i)

  def test_long(self):
    for i in xrange(1000):
      with self.assertRaises(ValueError):
        Vector(long(-i))
    for i in xrange(1, 1000):
      self.assertEqual(Vector(long(i)).values, [0]*i)

  def test_list(self):
    with self.assertRaises(VectorError):
      Vector([])
    self.assertEqual(Vector([1,2,3]).values, [1,2,3])

  def test_iter(self):
    with self.assertRaises(VectorError):
      Vector(iter([]))
    with self.assertRaises(VectorError):
      Vector(iter("1,2,3"))
    self.assertEqual(Vector(iter([1,2,3])).values, [1,2,3])

  def test_str(self):
    with self.assertRaises(TypeError):
      Vector("")
    with self.assertRaises(TypeError):
      Vector("1,2,3")

  def test_unicode(self):
    with self.assertRaises(TypeError):
      Vector(u"")
    with self.assertRaises(TypeError):
      Vector(u"1,2,3")

  def test_float(self):
    with self.assertRaises(VectorError):
      Vector(0.)
    with self.assertRaises(VectorError):
      Vector(10.)
    with self.assertRaises(VectorError):
      Vector(-10.)


class TestVectorFactories(unittest.TestCase):

  def test_Zero(self):
    for i in xrange(1000):
      with self.assertRaises(ValueError):
        Vector.Zero(-i)
    for i in xrange(1, 1000):
      self.assertEqual(Vector.Zero(i).values, [0]*i)

    for i in xrange(1000):
      with self.assertRaises(ValueError):
        Vector.Zero(long(-i))
    for i in xrange(1, 1000):
      self.assertEqual(Vector.Zero(long(i)).values, [0]*i)

    with self.assertRaises(TypeError):
      Vector.Zero(0.)
    with self.assertRaises(TypeError):
      Vector.Zero(1.)
    with self.assertRaises(TypeError):
      Vector.Zero(-1.)
    with self.assertRaises(TypeError):
      Vector.Zero("")
    with self.assertRaises(TypeError):
      Vector.Zero("1,2,3")
    with self.assertRaises(TypeError):
      Vector.Zero(u"")
    with self.assertRaises(TypeError):
      Vector.Zero(u"1,2,3")
    with self.assertRaises(TypeError):
      Vector.Zero([])
    with self.assertRaises(TypeError):
      Vector.Zero([1,2,3])

  def test_FromList(self):
    with self.assertRaises(VectorError):
      Vector.FromList([])
    self.assertEqual(Vector.FromList([1,2,3]).values, [1,2,3])

    with self.assertRaises(VectorError):
      Vector.FromList(iter([]))
    with self.assertRaises(VectorError):
      Vector.FromList(iter("1,2,3"))
    self.assertEqual(Vector.FromList(iter([1,2,3])).values, [1,2,3])

    with self.assertRaises(TypeError):
      Vector.FromList(0)
    with self.assertRaises(TypeError):
      Vector.FromList(1)
    with self.assertRaises(TypeError):
      Vector.FromList(-1)
    with self.assertRaises(TypeError):
      Vector.FromList(0.)
    with self.assertRaises(TypeError):
      Vector.FromList(1.)
    with self.assertRaises(TypeError):
      Vector.FromList(-1.)
    with self.assertRaises(TypeError):
      Vector.FromList("")
    with self.assertRaises(TypeError):
      Vector.FromList("1,2,3")
    with self.assertRaises(TypeError):
      Vector.FromList(u"")
    with self.assertRaises(TypeError):
      Vector.FromList(u"1,2,3")

  def test_Parse(self):
    self.assertEqual(Vector.Parse(""), NotImplemented)
    self.assertEqual(Vector.Parse("1,2,3"), NotImplemented)
    self.assertEqual(Vector.Parse(u""), NotImplemented)
    self.assertEqual(Vector.Parse(u"1,2,3"), NotImplemented)

    with self.assertRaises(TypeError):
      Vector.Parse(0)
    with self.assertRaises(TypeError):
      Vector.Parse(1)
    with self.assertRaises(TypeError):
      Vector.Parse(-1)
    with self.assertRaises(TypeError):
      Vector.Parse(0.)
    with self.assertRaises(TypeError):
      Vector.Parse(1.)
    with self.assertRaises(TypeError):
      Vector.Parse(-1.)
    with self.assertRaises(TypeError):
      Vector.Parse([])
    with self.assertRaises(TypeError):
      Vector.Parse([1,2,3])
    with self.assertRaises(TypeError):
      Vector.Parse(iter(""))
    with self.assertRaises(TypeError):
      Vector.Parse(iter([1,2,3]))


class TestVectorProperties(unittest.TestCase):

  def test_size(self):
    for i in range(1, 1000):
      self.assertEqual(Vector(i).size, i)
      self.assertEqual(Vector([1]*i).size, i)
    with self.assertRaises(AttributeError):
      Vector(5).size = None
    with self.assertRaises(AttributeError):
      Vector(5).size = 5
    with self.assertRaises(AttributeError):
      del Vector(5).size

  def test_values(self):
    self.assertEqual(Vector([1,2,3]).values, [1,2,3])
    self.assertEqual(Vector([1,2,3,4]).values, [1,2,3,4])
    with self.assertRaises(AttributeError):
      Vector(5).values = None
    with self.assertRaises(AttributeError):
      Vector(5).values = [1,2,3]
    with self.assertRaises(AttributeError):
      del Vector(5).values

  def test_magnitude(self):
    self.assertEqual(Vector([3, 4]).magnitude, 5)
    self.assertEqual(Vector([3, 4, 3.3166247903553998491149327366707]).magnitude, 6)
    for i in range(1, 100):
      self.assertEqual(Vector(i).magnitude, 0)
    for i in range(-100, 100):
      for j in range(1, 10):
        for k in range(j):
          myList = [0]*j
          myList[k] = i
          self.assertEqual(Vector(myList).magnitude, abs(i))
    for i in range(-100, 100):
      for j in range(1, 10):
        self.assertAlmostEqual(Vector([i]*j).magnitude, abs(math.sqrt(j)*i))
    with self.assertRaises(AttributeError):
      Vector(5).magnitude = None
    with self.assertRaises(AttributeError):
      Vector(5).magnitude = 5
    with self.assertRaises(AttributeError):
      del Vector(5).magnitude


class TestVectorTestingMethods(unittest.TestCase):

  def test_isZero(self):
    for i in range(1, 100):
      self.assertTrue(Vector(i).isZero())
    self.assertFalse(Vector([1,2,3]).isZero())

  def test_isNormalized(self):
    for i in range(1, 10):
      for j in range(i):
        myList = [0]*i
        myList[j] = 1
        self.assertTrue(Vector(myList).isNormalized())
    for i in range(1, 100):
      self.assertFalse(Vector(i).isNormalized())
    self.assertFalse(Vector([1,2,3]).isNormalized())
    self.assertFalse(Vector([1./math.sqrt(2)]*2).isNormalized())


class TestVectorOtherMethods(unittest.TestCase):

  def test_asList(self):
    self.assertEqual(Vector([1,2,3]).asList(), [1,2,3])
    self.assertEqual(Vector([1,2,3,4]).asList(), [1,2,3,4])
  
  def test_dot(self):
    self.assertEqual(Vector([2]).dot(Vector([4])), 8)
    self.assertEqual(Vector([2,5]).dot(Vector([4,7])), 43)
    self.assertEqual(Vector([1,2,3]).dot(Vector([4,5,6])), 32)

    with self.assertRaises(VectorError):
      Vector([1,2,3]).dot(Vector([4,5]))
    with self.assertRaises(VectorError):
      Vector([1]).dot(Vector([4,5]))
    with self.assertRaises(VectorError):
      Vector([1]).dot(Vector([4,5,7]))
  
  def test_cross(self):
    self.assertEqual(Vector([1,2,3]).cross(Vector([4,5,6])).values, [-3, 6, -3])

    with self.assertRaises(NotImplementedError):
      Vector([5]).cross(None)
    with self.assertRaises(NotImplementedError):
      Vector([1,2]).cross(None)
    with self.assertRaises(NotImplementedError):
      Vector([1,2,3,4]).cross(None)
    with self.assertRaises(NotImplementedError):
      Vector([1,2,3,4,5]).cross(None)

    with self.assertRaises(TypeError):
      Vector([1,2,3]).cross(None)
    with self.assertRaises(TypeError):
      Vector([1,2,3]).cross(10)
    with self.assertRaises(TypeError):
      Vector([1,2,3]).cross(True)
    with self.assertRaises(TypeError):
      Vector([1,2,3]).cross([1,2,3])

    with self.assertRaises(ValueError):
      Vector([1,2,3]).cross(Vector([1]))
    with self.assertRaises(ValueError):
      Vector([1,2,3]).cross(Vector([1,2]))
    with self.assertRaises(ValueError):
      Vector([1,2,3]).cross(Vector([1,2,3,4]))
    with self.assertRaises(ValueError):
      Vector([1,2,3]).cross(Vector([1,2,3,4,5]))
  
  def test_round(self, ndigits=0):
    self.assertEqual(Vector([1.34, 4.56, -3.89]).round().values, [1, 5, -4])
    self.assertEqual(Vector([1.34, 4.56, -3.89]).round(1).values, [1.3, 4.6, -3.9])
    self.assertEqual(Vector([1.34, 4.56, -3.89]).round(2).values, [1.34, 4.56, -3.89])
    self.assertEqual(Vector([1.34, 4.56, -3.89]).round(3).values, [1.34, 4.56, -3.89])
    self.assertEqual(Vector([1.34, 54.56, -23.89]).round(-1).values, [0, 50, -20])
  
  def test_floor(self):
    self.assertEqual(Vector([1.34, 4.56, -3.89]).floor().values, [1, 4, -4])
  
  def test_ceil(self):
    self.assertEqual(Vector([1.34, 4.56, -3.89]).ceil().values, [2, 5, -3])
  
  def test_trunc(self):
    self.assertEqual(Vector([1.34, 4.56, -3.89]).trunc().values, [1, 4, -3])
  
  def test_normalize(self):
    self.assertEqual(Vector([1]).normalize().values, [1])
    self.assertEqual(Vector([35.456]).normalize().values, [1])
    self.assertAlmostEqual(Vector([-0.453]).normalize().values[0], -1)

    with self.assertRaises(ZeroDivisionError):
      Vector([0]).normalize()
    with self.assertRaises(ZeroDivisionError):
      Vector([0,0]).normalize()
    with self.assertRaises(ZeroDivisionError):
      Vector([0,0,0]).normalize()


class TestVectorBuiltinFunctions(unittest.TestCase):

  def test_len(self):
    for i in range(1, 1000):
      self.assertEqual(len(Vector(i)), i)
      self.assertEqual(len(Vector([1]*i)), i)

  def test_str(self):
    self.assertEqual(str(Vector(5)), "0.0, 0.0, 0.0, 0.0, 0.0")
    self.assertEqual(str(Vector([1.1, 2.2, 3.3])), "1.1, 2.2, 3.3")

  def test_repr(self):
    self.assertEqual(repr(Vector(5)), "Vector([0.0, 0.0, 0.0, 0.0, 0.0])")
    self.assertEqual(repr(Vector([1.1, 2.2, 3.3])), "Vector([1.1, 2.2, 3.3])")

  def test_iter(self):
    self.assertEqual(list(iter(Vector([1,2,3]))), [1,2,3])
    self.assertEqual(list(iter(Vector([1,2,3,4]))), [1,2,3,4])

  def test_getitem(self):
    myList = [random.uniform(-50, 50) for i in xrange(50)]
    vec = Vector(myList)
    for i, v in enumerate(myList):
      self.assertEqual(vec[i], v)
    self.assertEqual(vec[-5], myList[-5])
    with self.assertRaises(IndexError):
      vec[100]

  def test_setitem(self):
    v = Vector(5)
    v[0] = 14
    self.assertEqual(v.values, [14,0,0,0,0])
    v[4] = 65
    self.assertEqual(v.values, [14,0,0,0,65])
    v[-3] = 10
    self.assertEqual(v.values, [14,0,10,0,65])
    with self.assertRaises(IndexError):
      v[6] = 10
    v[3] = 98
    self.assertEqual(v.values, [14,0,10,98,65])


class TestVectorOperators(unittest.TestCase):
  
  def test_eq(self):
    self.assertTrue(Vector(5) == Vector(5))
    self.assertFalse(Vector(5) == None)
    self.assertTrue(Vector(5) == 0)
    with self.assertRaises(ValueError):
      Vector(5) == 10
    with self.assertRaises(ValueError):
      Vector(5) == -1.6
    self.assertTrue(Vector([4,5,6]) == Vector([4,5,6]))
    self.assertFalse(Vector([4,5,6]) == Vector([4,5,6,3]))
  
  def test_ne(self):
    self.assertFalse(Vector(5) != Vector(5))
    self.assertTrue(Vector(5) != None)
    self.assertFalse(Vector(5) != 0)
    with self.assertRaises(ValueError):
      Vector(5) != 10
    with self.assertRaises(ValueError):
      Vector(5) != -1.6
    self.assertFalse(Vector([4,5,6]) != Vector([4,5,6]))
    self.assertTrue(Vector([4,5,6]) != Vector([4,5,6,3]))
  
  def test_pos(self):
    self.assertEqual((+Vector([4,-5,6])).values, [4,-5,6])
  
  def test_neg(self):
    self.assertEqual((-Vector([4,-5,6])).values, [-4,5,-6])
  
  def test_add(self):
    with self.assertRaises(TypeError):
      Vector(5) + None
    with self.assertRaises(TypeError):
      Vector(5) + 4
    with self.assertRaises(TypeError):
      Vector(5) + "asd"
    with self.assertRaises(TypeError):
      Vector(5) + [1,2,3]
    with self.assertRaises(VectorError):
      Vector(5) + Vector(3)
    self.assertEqual((Vector([1,2,3])+Vector([4,-5,6])).values, [5,-3,9])
  
  def test_sub(self):
    with self.assertRaises(TypeError):
      Vector(5) - None
    with self.assertRaises(TypeError):
      Vector(5) - 4
    with self.assertRaises(TypeError):
      Vector(5) - "asd"
    with self.assertRaises(TypeError):
      Vector(5) - [1,2,3]
    with self.assertRaises(VectorError):
      Vector(5) - Vector(3)
    self.assertEqual((Vector([1,2,3])-Vector([4,-5,6])).values, [-3,7,-3])
  
  def test_mul(self):
    self.assertEqual(Vector([2]) * Vector([4]), 8)
    self.assertEqual(Vector([2,5]) * Vector([4,7]), 43)
    self.assertEqual(Vector([1,2,3]) * Vector([4,5,6]), 32)
    self.assertEqual((Vector([1,2,3]) * 5).values, [5,10,15])
    self.assertEqual((Vector([1,0,-3]) * -7.8).values, [-7.8,0,23.4])

    with self.assertRaises(VectorError):
      Vector([1,2,3]) * Vector([4,5])
    with self.assertRaises(VectorError):
      Vector([1]) * Vector([4,5])
    with self.assertRaises(VectorError):
      Vector([1]) * Vector([4,5,7])
    with self.assertRaises(TypeError):
      Vector(5) * None
    with self.assertRaises(TypeError):
      Vector(5) * "asd"
    with self.assertRaises(TypeError):
      Vector(5) * [1,2,3]
  
  def test_rmul(self):
    self.assertEqual((5 * Vector([1,2,3])).values, [5,10,15])
    self.assertEqual((-7.8 * Vector([1,0,-3])).values, [-7.8,0,23.4])

    with self.assertRaises(TypeError):
      None * Vector(5)
    with self.assertRaises(TypeError):
      "asd" * Vector(5)
    with self.assertRaises(TypeError):
      [1,2,3] * Vector(5)
  
  def test_div(self):
    self.assertEqual((Vector([1,2,5]) / 5).values, [0.2,0.4,1])

    with self.assertRaises(ZeroDivisionError):
      Vector(5) / 0
    with self.assertRaises(ZeroDivisionError):
      Vector(5) / 0.0

    with self.assertRaises(TypeError):
      Vector([1,2,3]) / Vector([4,5])
    with self.assertRaises(TypeError):
      Vector(5) / None
    with self.assertRaises(TypeError):
      Vector(5) / "asd"
    with self.assertRaises(TypeError):
      Vector(5) / [1,2,3]
  
  def test_rdiv(self):
    with self.assertRaises(TypeError):
      5 / Vector(5)
    with self.assertRaises(TypeError):
      None / Vector(5)
    with self.assertRaises(TypeError):
      "asd" / Vector(5)
    with self.assertRaises(TypeError):
      [1,2,3] / Vector(5)

if __name__ == '__main__':
  unittest.main()