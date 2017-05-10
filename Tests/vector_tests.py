import unittest
import sys
import os
import random
sys.path.append(os.path.abspath(".."))
from Vector import *

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
    self.assertTrue(all(myList[i] == vec[i] for i in xrange(len(myList))))

if __name__ == '__main__':
  unittest.main()