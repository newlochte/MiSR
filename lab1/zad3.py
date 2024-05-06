import roboticstoolbox as rtb
import numpy as np
from spatialmath import *
from spatialmath.base import *
from spatialmath.base.symbolic import *
from matplotlib import pyplot as plt
from sympy import symbols


def main():
    pD = np.array([1, -2, 2])
    t_PS = np.array([3, -6, 4])
    R_PS = SO3(np.array([[-1, 0, 0], [0, 1, 0], [0, 0, -1]]))
    pTs = SE3.Rt(R_PS, t_PS)
    t_BS = np.array([2, 5, 0])
    R_BS = SO3(np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]]))
    bTs = SE3.Rt(R_BS, t_BS)
    sD = pTs.inv() * pD
    bD = bTs * sD

    sD = sD[:, 0]
    bD = bD[:, 0]

    print(f'pTs:\n{pTs}\nbTs:\n{bTs}\nsD:\n{sD}\nbD:\n{bD}')

    t_BS = np.array([2, 5, 0])
    t_PS = np.array([3, -6, 4])
    R_BS = SO3(np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]]))
    R_PS = SO3(np.array([[-1, 0, 0], [0, 1, 0], [0, 0, -1]]))
    T_BS = SE3.Rt(R_BS, t_BS)
    T_PS = SE3.Rt(R_PS, t_PS)
    B = SE3.Rt(SO3(np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])), np.array([0, 0, 0]))
    T_SP = T_PS.inv()
    T_BP = T_BS * T_SP
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    trplot(T_BS.A, color='green', frame='S')
    trplot(T_BP.A, color='green', frame='P')
    trplot(B.A, color='green', frame='B')
    ax.quiver(0, 0, 0, -2, 7, 2, color='black')
    plt.show()


if __name__ == '__main__':
    main()