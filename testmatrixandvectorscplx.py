# Test Calculadora de Matrices y Vectores de Numeros Complejos
# Por Santiago Sánchez Monroy
# Febrero 2023

import matrixandvectorscplx
import math
import unittest
class Testmatrixandvectorscplx(unittest.TestCase):
    
    def test_suma_Vector(self):
        v1 = [[[10,4]],[[-2,-5]],[[0,-9]]]
        v2 = [[[8,-4]],[[3,6]],[[3,0]]]

        self.assertEqual(matrixandvectorscplx.sum_vex(v1,v2), [[[18,0]],[[1,1]],[[3,-9]]])

    def test_resta_Vector(self):
        v1 = [[[8, 3]], [[-1, -4]], [[0, -9]]]
        v2 = [[[8, -3]], [[2, 5]], [[3, 0]]]

        self.assertEqual(matrixandvectorscplx.resta_Vex(v1,v2),[[[0,6]],[[-3,-9]],[[-3,-9]]])

    def test_inversoAditivo_Vector(self):
        v1 = [[[-6,3]],[[4,1]],[[1,0]]]

        self.assertEqual(matrixandvectorscplx.inverseAditive_Vex(v1),[[[6,-3]],[[-4,-1]],[[-1,0]]])

    def test_prodcutoEscalar_Vector(self):
        v1 = [[[-2,5]],[[-1,-1]],[[2,-9]]]
        v2 = [-1,1]

        self.assertEqual(matrixandvectorscplx.productEscalar_Vex(v1,v2),[[[-3,-7]],[[2,0]],[[7,11]]])

    def test_suma_Matriz(self):
        v1 = [[[-8,-3],[-6,-4],[0,-4]],
          [[-1,8],[6,-10],[8,-5]],
          [[4,0],[8,5],[-7,-9]]]

        v2 = [[[-7,-2],[-4,-2],[7,7]],
          [[5,9],[0,3],[6,-5]],
          [[1,5],[-6,-6],[5,8]]]

        self.assertEqual(matrixandvectorscplx.sum_Matrix(v1,v2),[[[-15,-5],[-10,-6],[7,3]],[[4,17],[6,-7],[14,-10]],[[5,5],[2,-1],[-2,-1]]])

    def test_inversoAditivo_Matriz(self):
        v1 = [[[7,3],[-1,7]],[[-9,-4],[-7,-9]]]

        self.assertEqual(matrixandvectorscplx.inverseAditive_Matrix(v1),[[[-7,-3],[1,-7]],[[9,4],[7,9]]])

    def test_productoEscalar_Matriz(self):
        v1 = [[[3,-2],[8,-4]],[[4,-10],[-2,-8]]]
        v2 = [-2,3]

        self.assertEqual(matrixandvectorscplx.productEscalar_Matrix(v1,v2),[[[0,13],[-4,32]],[[22,32],[28,10]]])

    def test_transpuesta_Matriz_Vector(self):
        v1 = [[[5,9],[-7,-5],[-1,-4]],[[8,2],[-3,-7],[7,-8]]]

        self.assertEqual(matrixandvectorscplx.trans_Matrix_Vex(v1),[[[5,9],[8,2]],[[-7,-5],[-3,-7]],[[-1,-4],[7,-8]]])

    def test_Conjugado_Matriz_Vector(self):
        v1 = [[[-6,1],[3,8]],[[2,-6],[3,0]]]

        self.assertEqual(matrixandvectorscplx.conjug_Matrix_Vex(v1),[[[-6,-1],[3,-8]],[[2,6],[3,0]]])

    def test_adjunta_Matriz_Vector(self):
        v1 = [[[7,7],[3,8],[8,4]],[[5,0],[8,-6],[-10,-1]]]

        self.assertEqual(matrixandvectorscplx.adj_Matrix_Vex(v1),[[[7,-7],[5,0]],[[3,-8],[8,6]],[[8,-4],[-10,1]]])

    def test_Producto_Matriz(self):
        v1 = [[[-6,2],[0,6],[7,2]],
              [[6,9],[7,7],[-6,-6]],
              [[5,8],[-6,8],[6,9]]]

        v2 = [[[9,-6],[-3,-4],[5,-2]],
              [[3,6],[-1,-5],[0,-5]],
              [[9,9],[8,-4],[-8,-4]]]

        self.assertEqual(matrixandvectorscplx.product_Matrix(v1,v2),[[[-33,153],[120,0],[-44,-22]],[[87,0],[-26,-117],[107,70]],[[0,165],[147,26],[69,-36]]])

    def test_accion_MatrizSobreVector(self):
        v1 = [[[-1,5],[1,-7],[-6,3]],
              [[-3,-9],[2,-5],[1,-10]],
              [[-6,5],[6,-5],[3,-2]]]

        v2 = [[[1,-3]],
              [[4,3]],
              [[-3,1]]]

        self.assertEqual(matrixandvectorscplx.accion_MatrixSobreVex(v1,v2),[[[54,-32]],[[0,17]],[[41,30]]])

    def test_productoInterno_Vector(self):
        v1 = [[[2,-1]],
              [[-8,-5]],
              [[-2,-6]]]

        v2 = [[[6,-3]],
              [[5,-1]],
              [[-6,-2]]]

        self.assertEqual(matrixandvectorscplx.productIntern_Vex(v1,v2),[[[4,1]]])

    def test_normaVector(self):
        v1 = [[[4,5]],[[3,1]],[[0,-7]]]

        self.assertEqual(matrixandvectorscplx.normaVex(v1),10)

    def test_distanciaVector(self):
        v1 = [[[2,7]],[[4,-1]],[[2,-4]]]
        v2 = [[[7,8]],[[2,-8]],[[1,4]]]

        self.assertEqual(matrixandvectorscplx.distanceVex(v1,v2),12)

    def test_matrizUnitaria(self):
        a = math.sqrt(2)

        v1 = [[[1/a,0],[0,1/a]],
              [[0,1/a],[1/a,0]]]

        v2 = [[[0,1],[1,0],[0,0]],
              [[0,0],[0,1],[1,0]],
              [[1,0],[0,0],[0,1]]]

        self.assertEqual(matrixandvectorscplx.matrixUnit(v1),True)
        self.assertEqual(matrixandvectorscplx.matrixUnit(v2),False)

    def test_productoTensorial_Matriz_Vector(self):
        v1 = [[[1,1],[0,0]],
              [[1,0],[0,1]]]

        v2 = [[[-1,2],[-2,-2],[0,2]],
              [[2,3],[3,1],[2,2]],
              [[-2,1],[1,-1],[2,1]]]

        v3 = [[[-3,1],[0,-4],[-2,2],[0,0],[0,0],[0,0]],
              [[-1,5],[2,4],[0,4],[0,0],[0,0],[0,0]],
              [[-3,-1],[2,0],[1,3],[0,0],[0,0],[0,0]],
              [[-1,2],[-2,-2],[0,2],[-2,-1],[2,-2],[-2,0]],
              [[2,3],[3,1],[2,2],[-3,2],[-1,3],[-2,2]],
              [[-2,1],[1,-1],[2,1],[-1,-2],[1,1],[-1,2]]]

        self.assertEqual(matrixandvectorscplx.productTensor_Matrix_Vex(v1,v2),v3)


if __name__=="__main__":
    unittest.main()