import roboticstoolbox as rtb
import numpy as np
from spatialmath import *
from spatialmath.base import *
from spatialmath.base.symbolic import *
from matplotlib import pyplot as plt


def main():
    l1, l2, l3 = symbol('l1, l2, l3')
    d1, theta2, theta3 = symbol('d1, theta2, theta3')
    px, py, pz = symbol('px, py, pz')

    A01 = SE3.Trans(0, 0, l1+d1)
    print(A01)

    A12 = SE3.Rz(theta2) * SE3.Trans(l2, 0, 0)
    print(A12)

    A23 = SE3.Rz(theta3) * SE3.Trans(l3, 0, 0) * SE3.Rx(pi())
    print(A23)

    print(A01*A12*A23)

    th3 = np.arccos((l2**2 + l3**2 - px**2 - py**2)/(2*l2*l3))
    print(th3)
    print(np.sin(th3))


if __name__ == '__main__':
    main()
