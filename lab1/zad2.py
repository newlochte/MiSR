import roboticstoolbox as rtb
import numpy as np
from spatialmath import *
from spatialmath.base import *
from spatialmath.base.symbolic import *
from matplotlib import pyplot as plt

def main():
    l1, l2, l3, l4 = symbol('l1, l2, l3, l4')
    theta1, d2, theta3 = symbol('theta1, d2, theta3')
    AB0 = SE3.Trans(0, 0, l1) * SE3.Rx(-pi()/2)
    A01 = SE3.Rz(-theta1)*SE3.Trans(0, 0, l2)*SE3.Rx(-pi()/2)
    A12 = SE3.Rz(-pi()/2)*SE3.Trans(l3, 0, d2)
    A23 = SE3.Rz(-theta3)*SE3.Trans(l4, 0, 0)
    A33p = SE3.Rz(pi()/2)*SE3.Rx(pi()/2)

    print(AB0*A01*A12*A23*A33p)
    print(AB0)


if __name__ == '__main__':
    main()
