import roboticstoolbox as rtb
import numpy as np
from spatialmath import *
from spatialmath.base import *
from spatialmath.base.symbolic import *
from matplotlib import pyplot as plt


def main():
    th1, l1, th2, l2, d3 = symbol('th1, l1, th2, l2, d3')

    robot = rtb.DHRobot(
        [
            rtb.RevoluteDH(d=l1, alpha=pi() / 2),
            rtb.RevoluteDH(offset=pi()/2, alpha=pi()/2),
            rtb.PrismaticDH(offset=l2)
        ], name="My_Robot")
    for link in robot.links:
        print(link)

    print(robot.fkine([th1, th2, d3]))

    J = simplify(robot.jacob0([th1, th2, d3]))
    for x in J:
        print(x)


if __name__ == '__main__':
    main()
