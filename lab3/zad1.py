import roboticstoolbox as rtb
import numpy as np
from spatialmath import *
from spatialmath.base import *
from spatialmath.base.symbolic import *
from matplotlib import pyplot as plt
from sympy import symbols



def main():
    robot = rtb.models.Puma560()


    T_start = robot.fkine(robot.qz)
    print(T_start)
    T_end = T_start * SE3(0, 0, -0.2) * SE3.Rz(90,'deg') * SE3.Ry(90,'deg')
    solution = robot.ikine_LM(T_end)
    print(T_end)

    traj = rtb.jtraj(robot.qz, solution.q, 50)
    robot.plot(traj.q, loop=True)


if __name__ == '__main__':
    main()