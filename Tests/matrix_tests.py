import unittest
import sys
import os
import random
import math
sys.path.append(os.path.abspath(".."))
from linear_algebra import *

class TestMatrixConstructor(unittest.TestCase):

  def test_int_int(self):
    for i in xrange(100):
      for j in xrange(100):
        with self.assertRaises(ValueError):
            Matrix(-i, -j)
        with self.assertRaises(ValueError):
            Matrix(-i, j)
        with self.assertRaises(ValueError):
            Matrix(i, -j)
    for i in xrange(1, 100):
      for j in xrange(1, 100):
        self.assertEqual(Matrix(i,j).asList(), [[0]*j]*i)

  def test_long_long(self):
    for i in xrange(100):
      for j in xrange(100):
        with self.assertRaises(ValueError):
            Matrix(-long(i), -long(j))
        with self.assertRaises(ValueError):
            Matrix(-long(i), long(j))
        with self.assertRaises(ValueError):
            Matrix(long(i), -long(j))
    for i in xrange(1, 100):
      for j in xrange(1, 100):
        self.assertEqual(Matrix(long(i),long(j)).asList(), [[0]*j]*i)

  def test_list(self):
    self.assertEqual(Matrix([[1,2,3], [4,5,6]]).asList(), [[1,2,3], [4,5,6]])
    with self.assertRaises(MatrixError):
      Matrix([])
    with self.assertRaises(MatrixError):
      Matrix([[]])
    with self.assertRaises(MatrixError):
      Matrix([[1,2],[3,4,5]])
    with self.assertRaises(MatrixError):
      Matrix([[1,2],[]])

  def test_str(self):
    with self.assertRaises(NotImplementedError):
      Matrix("")
    with self.assertRaises(NotImplementedError):
      Matrix("1,2,3;4,5,6")

  def test_unicode(self):
    with self.assertRaises(NotImplementedError):
      Matrix(u"")
    with self.assertRaises(NotImplementedError):
      Matrix(u"1,2,3;4,5,6")

  def test_float(self):
    with self.assertRaises(ValueError):
      Matrix(0., 0.)
    with self.assertRaises(ValueError):
      Matrix(10., 10.)
    with self.assertRaises(ValueError):
      Matrix(-10., 10.)


class TestMatrixFactories(unittest.TestCase):

  def test_Zero(self):
    for i in xrange(1, 100):
      for j in xrange(1, 100):
        self.assertEqual(Matrix.Zero(i,j).asList(), [[0]*j]*i)

  def test_Identity(self):
    self.assertEqual(Matrix.Identity(1).asList(), [[1]])
    self.assertEqual(Matrix.Identity(2).asList(), [[1,0], [0,1]])
    self.assertEqual(Matrix.Identity(3).asList(), [[1,0,0], [0,1,0], [0,0,1]])

  def test_FromListOfRows(self):
    self.assertEqual(Matrix.FromListOfRows([[1,2,3], [4,5,6]]).asList(), [[1,2,3], [4,5,6]])
  
  def test_FromListOfCols(self):
    self.assertEqual(Matrix.FromListOfCols([[1,2,3], [4,5,6]]).asList(), [[1,4], [2,5], [3,6]])
  
  def test_RowFromVector(self):
    self.assertEqual(Matrix.RowFromVector([1,2,3]).asList(), [[1,2,3]])
  
  def test_ColFromVector(self):
    self.assertEqual(Matrix.ColFromVector([1,2,3]).asList(), [[1], [2], [3]])
  
  def test_Diagonal(self):
    self.assertEqual(Matrix.Diagonal([3]).asList(), [[3]])
    self.assertEqual(Matrix.Diagonal([5,6]).asList(), [[5,0], [0,6]])
    self.assertEqual(Matrix.Diagonal([4,7,8]).asList(), [[4,0,0], [0,7,0], [0,0,8]])

  def test_Parse(self):
    self.assertEqual(Matrix.Parse(""), NotImplemented)
    self.assertEqual(Matrix.Parse("1,2,3;4,5,6"), NotImplemented)
    self.assertEqual(Matrix.Parse(u""), NotImplemented)
    self.assertEqual(Matrix.Parse(u"1,2,3;4,5,6"), NotImplemented)


class TestMatrixProperties(unittest.TestCase):

  def test_size(self):
    for i in range(1, 100):
      for j in range(1, 100):
        self.assertEqual(Matrix(i,j).size, (i,j))

    with self.assertRaises(AttributeError):
      Matrix(5,3).size = None
    with self.assertRaises(AttributeError):
      Matrix(5,3).size = 5
    with self.assertRaises(AttributeError):
      del Matrix(5,3).size

  def test_m(self):
    for i in range(1, 100):
      for j in range(1, 100):
        self.assertEqual(Matrix(i,j).m, i)

    with self.assertRaises(AttributeError):
      Matrix(5,3).m = None
    with self.assertRaises(AttributeError):
      Matrix(5,3).m = 5
    with self.assertRaises(AttributeError):
      del Matrix(5,3).m

  def test_n(self):
    for i in range(1, 100):
      for j in range(1, 100):
        self.assertEqual(Matrix(i,j).n, j)

    with self.assertRaises(AttributeError):
      Matrix(5,3).n = None
    with self.assertRaises(AttributeError):
      Matrix(5,3).n = 5
    with self.assertRaises(AttributeError):
      del Matrix(5,3).n

  def test_rows(self):
    self.assertEqual(Matrix([[1,2,3], [4,5,6]]).rows, [Vector([1,2,3]), Vector([4,5,6])])

    with self.assertRaises(AttributeError):
      Matrix(5,3).rows = None
    with self.assertRaises(AttributeError):
      Matrix(5,3).rows = 5
    with self.assertRaises(AttributeError):
      del Matrix(5,3).rows

  def test_cols(self):
    self.assertEqual(Matrix([[1,2,3], [4,5,6]]).cols, [Vector([1,4]), Vector([2,5]), Vector([3,6])])

    with self.assertRaises(AttributeError):
      Matrix(5,3).cols = None
    with self.assertRaises(AttributeError):
      Matrix(5,3).cols = 5
    with self.assertRaises(AttributeError):
      del Matrix(5,3).cols


class TestMatrixTestingMethods(unittest.TestCase):

  def test_isZero(self):
    for i in range(1, 100):
      for j in range(1, 100):
        self.assertTrue(Matrix(i,j).isZero())
    self.assertFalse(Matrix([[1,2], [3,4]]).isZero())

  def test_isIdentity(self):
    for i in range(1, 100):
      self.assertTrue(Matrix.Identity(i).isIdentity())
    self.assertFalse(Matrix([[1,2], [3,4]]).isIdentity())
  
  def test_isScalar(self):
    self.assertTrue(Matrix(1,1).isScalar())
    self.assertFalse(Matrix(3,3).isScalar())
    self.assertFalse(Matrix(1,3).isScalar())
    self.assertFalse(Matrix(3,1).isScalar())
  
  def test_isVector(self):
    self.assertTrue(Matrix(1,1).isVector())
    self.assertTrue(Matrix(1,3).isVector())
    self.assertTrue(Matrix(3,1).isVector())
    self.assertFalse(Matrix(3,3).isVector())
  
  def test_isSquare(self):
    self.assertTrue(Matrix(1,1).isSquare())
    self.assertTrue(Matrix(3,3).isSquare())
    self.assertFalse(Matrix(1,3).isSquare())
    self.assertFalse(Matrix(3,1).isSquare())
  
  def test_isDiagonal(self):
    self.assertTrue(Matrix(1,1).isDiagonal())
    self.assertTrue(Matrix(3,3).isDiagonal())
    self.assertTrue(Matrix.Identity(1).isDiagonal())
    self.assertTrue(Matrix.Identity(3).isDiagonal())
    self.assertTrue(Matrix([[2,0], [0,4]]).isDiagonal())
    self.assertTrue(Matrix([[2]]).isDiagonal())
    self.assertFalse(Matrix(3,2).isDiagonal())
    self.assertFalse(Matrix([[2,1], [0,4]]).isDiagonal())
  
  def test_isSymmetric(self):
    self.assertTrue(Matrix(1,1).isSymmetric())
    self.assertTrue(Matrix(3,3).isSymmetric())
    self.assertTrue(Matrix.Identity(1).isSymmetric())
    self.assertTrue(Matrix.Identity(3).isSymmetric())
    self.assertTrue(Matrix([[2]]).isSymmetric())
    self.assertTrue(Matrix([[2,3], [3,4]]).isSymmetric())
    self.assertTrue(Matrix([[2,3,4], [3,5,6], [4,6,7]]).isSymmetric())
    self.assertFalse(Matrix(3,2).isSymmetric())
    self.assertFalse(Matrix([[2,1], [0,4]]).isSymmetric())


class TestMatrixGetPartsMethods(unittest.TestCase):

  def test_asList(self):
    self.assertEqual(Matrix([[1,2,3], [4,5,6]]).asList(), [[1,2,3], [4,5,6]])
    
  def test_getRow(self):
    self.assertEqual(Matrix([[1,2,3], [4,5,6]]).getRow(0), Vector([1,2,3]))
    self.assertEqual(Matrix([[1,2,3], [4,5,6]]).getRow(1), Vector([4,5,6]))
    self.assertEqual(Matrix([[1,2,3], [4,5,6]]).getRow(-1), Vector([4,5,6]))
    with self.assertRaises(IndexError):
      Matrix([[1,2,3], [4,5,6]]).getRow(2)

  def test_getCol(self):
    self.assertEqual(Matrix([[1,2,3], [4,5,6]]).getCol(0), Vector([1,4]))
    self.assertEqual(Matrix([[1,2,3], [4,5,6]]).getCol(1), Vector([2,5]))
    self.assertEqual(Matrix([[1,2,3], [4,5,6]]).getCol(2), Vector([3,6]))
    self.assertEqual(Matrix([[1,2,3], [4,5,6]]).getCol(-1), Vector([3,6]))
    with self.assertRaises(IndexError):
      Matrix([[1,2,3], [4,5,6]]).getCol(3)
  
  def test_getDiagonal(self):
    self.assertEqual(Matrix([[1,2,3], [4,5,6]]).getDiagonal(), Vector([1,5]))
  
  def test_asScalar(self):
    with self.assertRaises(MatrixError):
      Matrix([[1,2,3], [4,5,6]]).asScalar()
    self.assertEqual(Matrix([[5]]).asScalar(), 5)
  
  def test_asVector(self):
    with self.assertRaises(MatrixError):
      Matrix([[1,2,3], [4,5,6]]).asVector()
    self.assertEqual(Matrix([[1,2,3]]).asVector(), Vector([1,2,3]))
    self.assertEqual(Matrix([[1],[2],[3]]).asVector(), Vector([1,2,3]))


class TestMatrixGetModifiedMethods(unittest.TestCase):

  def test_transpose(self):
    self.assertEqual(Matrix([[1,2,3], [4,5,6]]).transpose().asList(), [[1,4], [2,5], [3,6]])
  
  def test_round(self):
    self.assertEqual(Matrix([[1.34, 4.56, -3.89]]).round().asList(), [[1, 5, -4]])
    self.assertEqual(Matrix([[1.34, 4.56, -3.89]]).round(1).asList(), [[1.3, 4.6, -3.9]])
    self.assertEqual(Matrix([[1.34, 4.56, -3.89]]).round(2).asList(), [[1.34, 4.56, -3.89]])
    self.assertEqual(Matrix([[1.34, 4.56, -3.89]]).round(3).asList(), [[1.34, 4.56, -3.89]])
    self.assertEqual(Matrix([[1.34, 54.56, -23.89]]).round(-1).asList(), [[0, 50, -20]])
  
  def test_floor(self):
    self.assertEqual(Matrix([[1.34, 4.56, -3.89]]).floor().asList(), [[1, 4, -4]])
  
  def test_ceil(self):
    self.assertEqual(Matrix([[1.34, 4.56, -3.89]]).ceil().asList(), [[2, 5, -3]])
  
  def test_trunc(self):
    self.assertEqual(Matrix([[1.34, 4.56, -3.89]]).trunc().asList(), [[1, 4, -3]])


class TestMatrixGetModifiedMethods(unittest.TestCase):

  def test_trace(self):
    self.assertEqual(Matrix([[2,4,6], [4,7,9]]).trace(), 9)
    
  def test_det(self):
    with self.assertRaises(NotImplementedError):
      Matrix(2,3).det()
    
    self.assertEqual(Matrix.Diagonal([3]).det(), 3)
    self.assertEqual(Matrix.Diagonal([3,4]).det(), 12)
    self.assertEqual(Matrix.Diagonal([3,4,2]).det(), 24)
    self.assertEqual(Matrix.Diagonal([3,4,2,5]).det(), 120)
    self.assertEqual(Matrix.Diagonal([3,4,2,5,-4]).det(), -480)
    self.assertEqual(Matrix([[3,6], [2,5]]).det(), 3)
    self.assertEqual(Matrix([[3,6,2], [1,0,5], [7,2,1]]).det(), 178)
    self.assertEqual(Matrix([[3,6,2,1], [1,0,5,3], [7,2,1,4], [1,2,3,4]]).det(), 452)
  
  def test_eigenvalues(self):
    with self.assertRaises(NotImplementedError):
      Matrix(2,3).eigenvalues()
    
    self.assertEqual(Matrix.Diagonal([3]).eigenvalues(), [3])
    self.assertEqual(Matrix.Diagonal([3,4]).eigenvalues(), [4,3])
    self.assertEqual(Matrix.Diagonal([3,4,2]).eigenvalues(), [4,3,2])
    self.assertEqual(Matrix.Diagonal([3,4,2,5]).eigenvalues(), [5,4,3,2])
    self.assertEqual(Matrix.Diagonal([3,4,2,5,-4]).eigenvalues(), [5,4,3,2,-4])
    
    self.assertEqual(Matrix([[3,4], [2,5]]).eigenvalues(), [7,1])
    vals = Matrix([[3,6,2], [6,0,5], [2,5,1]]).eigenvalues()
    self.assertAlmostEqual(vals[0], 10.178278302361)
    self.assertAlmostEqual(vals[1], -0.14659863242975)
    self.assertAlmostEqual(vals[2], -6.0316796699311)

    with self.assertRaises(NotImplementedError):
      Matrix([[3,6,2], [6,0,7], [2,5,1]]).eigenvalues()
    with self.assertRaises(NotImplementedError):
      Matrix([[3,6,2,4], [6,0,7,1], [2,5,1,3], [7,3,2,1]]).eigenvalues()


class TestMatrixBuiltinFunctions(unittest.TestCase):

  def test_str(self):
    self.assertEqual(str(Matrix(2,3)), "[[0.0, 0.0, 0.0], [0.0, 0.0, 0.0]]")
    self.assertEqual(str(Matrix([[1.1, 2.2, 3.3], [4.4, 5.5, 6.6]])), "[[1.1, 2.2, 3.3], [4.4, 5.5, 6.6]]")

  def test_repr(self):
    self.assertEqual(repr(Matrix(2,3)), "Matrix([[0.0, 0.0, 0.0], [0.0, 0.0, 0.0]])")
    self.assertEqual(repr(Matrix([[1.1, 2.2, 3.3], [4.4, 5.5, 6.6]])), "Matrix([[1.1, 2.2, 3.3], [4.4, 5.5, 6.6]])")

  def test_getitem(self):
    myList = [[random.uniform(-50, 50) for j in xrange(10)] for i in xrange(10)]
    m = Matrix(myList)
    for i, row in enumerate(myList):
      for j, v in enumerate(row):
        self.assertEqual(m[(i,j)], v)
        self.assertEqual(m[i,j], v)
    self.assertEqual(m[-5,-3], myList[-5][-3])
    with self.assertRaises(IndexError):
      m[100,20]
    with self.assertRaises(TypeError):
      m[5]
    with self.assertRaises(TypeError):
      m[5:]
    with self.assertRaises(ValueError):
      m[(1,)]
    with self.assertRaises(ValueError):
      m[(1,2,3)]

  def test_setitem(self):
    m = Matrix(5,3)
    m[0,0] = 14
    self.assertEqual(m.asList(), [[14,0,0], [0,0,0], [0,0,0], [0,0,0], [0,0,0]])
    m[4,1] = 65
    self.assertEqual(m.asList(), [[14,0,0], [0,0,0], [0,0,0], [0,0,0], [0,65,0]])
    m[-3,-2] = 10
    self.assertEqual(m.asList(), [[14,0,0], [0,0,0], [0,10,0], [0,0,0], [0,65,0]])
    with self.assertRaises(IndexError):
      m[6,7] = 10
    with self.assertRaises(TypeError):
      m[5]
    with self.assertRaises(TypeError):
      m[5:]
    with self.assertRaises(ValueError):
      m[(1,)]
    with self.assertRaises(ValueError):
      m[(1,2,3)]
    m[1,2] = 98
    self.assertEqual(m.asList(), [[14,0,0], [0,0,98], [0,10,0], [0,0,0], [0,65,0]])

  def test_sum(self):
    self.assertEqual(sum([Matrix([[4,5],[3,2]]), Matrix([[1,2],[7,6]]), Matrix([[7,1],[5,9]])]), Matrix([[12,8],[15,17]]))
    with self.assertRaises(TypeError):
      sum(Matrix([[4,5],[3,2]]))
    with self.assertRaises(TypeError):
      sum([Matrix([[4,5],[3,2]]), 3, Matrix([[7,1],[5,9]])])
    with self.assertRaises(TypeError):
      sum([Matrix([[4,5],[3,2]]), [[1,2],[7,6]], Matrix([[7,1],[5,9]])])
    with self.assertRaises(TypeError):
      sum([Matrix([[4,5],[3,2]]), "123", Matrix([[7,1],[5,9]])])
    with self.assertRaises(MatrixError):
      sum([Matrix([[4,5],[3,2]]), Matrix([[1,2],[7,6],[5,6]]), Matrix([[7,1],[5,9]])])


class TestMatrixOperators(unittest.TestCase):
  
  def test_eq(self):
    self.assertTrue(Matrix(5,4) == Matrix(5,4))
    self.assertFalse(Matrix(5,6) == None)
    self.assertTrue(Matrix(5,4) == 0)
    self.assertTrue(Matrix(2,4) == 0.0)
    self.assertFalse(Matrix(2,4) == 1)
    self.assertTrue(Matrix.Identity(2) == 1)
    self.assertTrue(Matrix.Identity(4) == 1.0)
    self.assertFalse(Matrix.Identity(4) == 0)
    with self.assertRaises(ValueError):
      Matrix(5,5) == 10
    with self.assertRaises(ValueError):
      Matrix(5,5) == -1.6
    self.assertTrue(Matrix([[4,5,6], [1,2,3]]) == Matrix([[4,5,6], [1,2,3]]))
    self.assertFalse(Matrix([[4,5,6], [1,2,3]]) == Matrix([[10,5,6], [1,2,3]]))
  
  def test_ne(self):
    self.assertFalse(Matrix(5,4) != Matrix(5,4))
    self.assertTrue(Matrix(5,6) != None)
    self.assertFalse(Matrix(5,4) != 0)
    self.assertFalse(Matrix(2,4) != 0.0)
    self.assertTrue(Matrix(2,4) != 1)
    self.assertFalse(Matrix.Identity(2) != 1)
    self.assertFalse(Matrix.Identity(4) != 1.0)
    self.assertTrue(Matrix.Identity(4) != 0)
    with self.assertRaises(ValueError):
      Matrix(5,5) != 10
    with self.assertRaises(ValueError):
      Matrix(5,5) != -1.6
    self.assertFalse(Matrix([[4,5,6], [1,2,3]]) != Matrix([[4,5,6], [1,2,3]]))
    self.assertTrue(Matrix([[4,5,6], [1,2,3]]) != Matrix([[10,5,6], [1,2,3]]))
  
  def test_pos(self):
    self.assertEqual((+Matrix([[4,5,-6], [1,-2,3]])).asList(), [[4,5,-6], [1,-2,3]])
  
  def test_neg(self):
    self.assertEqual((-Matrix([[4,5,-6], [1,-2,3]])).asList(), [[-4,-5,6], [-1,2,-3]])
  
  def test_add(self):
    with self.assertRaises(TypeError):
      Matrix(3,3) + None
    with self.assertRaises(TypeError):
      Matrix(3,3) + 4
    with self.assertRaises(TypeError):
      Matrix(3,3) + "asd"
    with self.assertRaises(TypeError):
      Matrix(3,3) + [1,2,3]
    with self.assertRaises(MatrixError):
      Matrix(3,3) + Matrix(3,4)
    self.assertEqual((Matrix([[1,2,3], [4,5,6]])+Matrix([[4,-5,6], [-1,2,-3]])).asList(), [[5,-3,9], [3,7,3]])
  
  def test_sub(self):
    with self.assertRaises(TypeError):
      Matrix(3,3) - None
    with self.assertRaises(TypeError):
      Matrix(3,3) - 4
    with self.assertRaises(TypeError):
      Matrix(3,3) - "asd"
    with self.assertRaises(TypeError):
      Matrix(3,3) - [1,2,3]
    with self.assertRaises(MatrixError):
      Matrix(3,3) - Matrix(3,4)
    self.assertEqual((Matrix([[1,2,3], [4,5,6]])-Matrix([[4,-5,6], [-1,2,-3]])).asList(), [[-3,7,-3], [5,3,9]])
  
  def test_mul(self):
    self.assertEqual((Matrix([[2]]) * Matrix([[4]])).asList(), [[8]])
    self.assertEqual((Matrix([[2,5]]) * Matrix([[4],[7]])).asList(), [[43]])
    self.assertEqual((Matrix([[4],[7]]) * Matrix([[2,5]])).asList(), [[8, 20], [14, 35]])
    self.assertEqual((Matrix([[1,2,3]]) * Matrix([[4],[5],[6]])).asList(), [[32]])
    self.assertEqual((Matrix([[1,2,3], [4,5,6]]) * Matrix([[4,7], [5,8], [6,9]])).asList(), [[32, 50], [77, 122]])

    self.assertEqual((Matrix([[2],[5]]) * Vector([4])).asList(), [[8],[20]])
    self.assertEqual((Matrix([[2,5]]) * Vector([4,7])).asList(), [[43]])
    self.assertEqual((Matrix([[1,2,3]]) * Vector([4,5,6])).asList(), [[32]])
    self.assertEqual((Matrix([[4,3],[7,1]]) * Vector([2,5])).asList(), [[23],[19]])
    self.assertEqual((Matrix([[4,3,1],[7,1,4]]) * Vector([2,5,3])).asList(), [[26],[31]])

    self.assertEqual((Matrix([[1,2,3], [4,5,6]]) * 5).asList(), [[5,10,15], [20,25,30]])
    self.assertEqual((Matrix([[1,0,-3], [2,-1,0]]) * -7.8).asList(), [[-7.8,0,23.4], [-15.6,7.8,0]])

    with self.assertRaises(MatrixError):
      Matrix(4,6) * Matrix(7,5)
    with self.assertRaises(MatrixError):
      Matrix(4,6) * Vector(3)
    with self.assertRaises(TypeError):
      Matrix(5,3) * None
    with self.assertRaises(TypeError):
      Matrix(5,3) * "asd"
    with self.assertRaises(TypeError):
      Matrix(5,3) * [1,2,3]
  
  def test_rmul(self):
    self.assertEqual((Vector([2]) * Matrix([[4,8]])).asList(), [[8,16]])
    self.assertEqual((Vector([2,5]) * Matrix([[4],[7]])).asList(), [[43]])
    self.assertEqual((Vector([1,2,3]) * Matrix([[4],[5],[6]])).asList(), [[32]])
    self.assertEqual((Vector([2,5]) * Matrix([[4,3],[7,1]])).asList(), [[43,11]])
    self.assertEqual((Vector([2,5]) * Matrix([[4,3],[7,1]])).asList(), [[43,11]])

    self.assertEqual((5 * Matrix([[1,2,3], [4,5,6]])).asList(), [[5,10,15], [20,25,30]])
    self.assertEqual((-7.8 * Matrix([[1,0,-3], [2,-1,0]])).asList(), [[-7.8,0,23.4], [-15.6,7.8,0]])

    with self.assertRaises(MatrixError):
      Vector(3) * Matrix(4,5)
    with self.assertRaises(TypeError):
      None * Matrix(4,5)
    with self.assertRaises(TypeError):
      "asd" * Matrix(4,5)
    with self.assertRaises(TypeError):
      [1,2,3] * Matrix(4,5)
  
  def test_div(self):
    self.assertEqual((Matrix([[1,2,5]]) / 5).asList(), [[0.2,0.4,1]])

    with self.assertRaises(ZeroDivisionError):
      Matrix(5,4) / 0
    with self.assertRaises(ZeroDivisionError):
      Matrix(5,4) / 0.0

    with self.assertRaises(TypeError):
      Matrix(5,4) / Matrix(5,4)
    with self.assertRaises(TypeError):
      Matrix(5,4) / None
    with self.assertRaises(TypeError):
      Matrix(5,4) / "asd"
    with self.assertRaises(TypeError):
      Matrix(5,4) / [1,2,3]
  
  def test_rdiv(self):
    with self.assertRaises(TypeError):
      5 / Matrix(5,4)
    with self.assertRaises(TypeError):
      None / Matrix(5,4)
    with self.assertRaises(TypeError):
      "asd" / Matrix(5,4)
    with self.assertRaises(TypeError):
      [1,2,3] / Matrix(5,4)

if __name__ == '__main__':
  unittest.main()