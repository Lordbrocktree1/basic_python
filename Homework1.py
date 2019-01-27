import numpy as np


def transform2D(dx,dy,R):
    T = np.array([ [    R[0,0] ,  R[0,1] ,  dx ],
                   [	R[1,0] ,  R[1,1] ,  dy ],
                   [	0.0	   ,	0.0	 , 1.0 ]]);
    return T;

# Rotation about x axis
def rotX(angle):
    m = np.array([ [	1.0, 		0.0	  ,       0.0     ],
                   [	0.0, np.cos(angle), -np.sin(angle)],
                   [	0.0, np.sin(angle),  np.cos(angle)]]);
    return m;


# Rotation about y axis
def rotY(angle):
    m = np.array([ [ np.cos(angle), 0.0, np.sin(angle)],
                   [   0.0		  , 1.0, 	0.0		  ],
                   [-np.sin(angle), 0.0, np.cos(angle)]]);
    return m;

# Rotation about z axis
def rotZ(angle):
    m = np.array([ [np.cos(angle), -np.sin(angle), 0.0],
                   [np.sin(angle),  np.cos(angle), 0.0],
                   [    0.0		 , 		0.0		 , 1.0]]);
    return m


# convert rotation matrix to normalized quaternion
def M2Q(rot):
    m00 = rot[0,0]
    m01 = rot[0,1]
    m02 = rot[0,2]
    m10 = rot[1,0]
    m11 = rot[1,1]
    m12 = rot[1,2]
    m20 = rot[2,0]
    m21 = rot[2,1]
    m22 = rot[2,2]

    qw = np.sqrt(1 + m00 + m11 + m22)/2.0
    qx = (m21 - m12)/(4*qw)
    qy = (m02 - m20)/(4*qw)
    qz = (m10 - m01)/(4*qw)

    return np.array([qw, qx, qy, qz])

def q1(idMat):
    print("Q1:")
    print("WTA: ")
    move1 = transform2D(2, 0, idMat)
    print(move1)
    print("ATB: ")
    ang = rotZ(np.radians(45))
    move2 = transform2D(0, 0, ang)
    print(move2)
    print("BTC")
    move3 = transform2D(.5, 0, idMat)
    print(move3)
    print("CTD")
    ang = rotZ(np.radians(-30))
    move4 = transform2D(0, 0, ang)
    print(move4)
    print("DTE")
    move5 = transform2D(.25, 0, idMat)
    print(move5)
    print("WTE")
    endval = np.dot(np.dot(np.dot(move1, move2), np.dot(move3, move4)), move5)
    print(endval)

def q2(idMat):
    print("Q2:")
    print("WTR: ")
    ang = rotZ(np.pi/6)
    move1 = transform2D(3.5, -.25, ang)
    print(move1)
    print("RTL: ")
    ang = rotZ(np.pi/10)
    move2 = transform2D(0.1, 0.0, ang)
    print(move2)
    print("LTO: ")
    move3 = transform2D(0.5, 0.0, idMat)
    print(move3)
    print("WTO: ")
    endval = np.dot(np.dot(move1, move2), move3)
    print(endval)

def q3help(num, ang, xyz):
    print()
    print(num, ".)")
    print("Rotation Matrix: ")

    if xyz == "x":
        rotmat = rotX(ang)
        print(rotmat)
        print("Quaternion: ")
        print(M2Q(rotmat))

    elif xyz == "y":
        rotmat = rotY(ang)
        print(rotmat)
        print("Quaternion: ")
        print(M2Q(rotmat))

    else:
        if xyz == "z":
            rotmat = rotZ(ang)
            print(rotmat)
            print("Quaternion: ")
            print(M2Q(rotmat))


def q3(idMat):
    print("Q3:")
    q3help("a", 0, "z")
    q3help("b", np.pi / 2, "x")
    q3help("c", np.pi / 2, "y")
    q3help("d", np.pi / 2, "z")
    q3help("e", np.pi / 3, "x")
    q3help("f", np.pi / 3, "y")
    q3help("g", np.pi / 3, "z")
    q3help("h", np.pi / 4, "x")
    q3help("i", np.pi / 4, "y")
    q3help("j", np.pi / 4, "z")
    q3help("k", np.pi / 6, "x")
    q3help("l", np.pi / 6, "y")
    q3help("m", np.pi / 6, "z")
    q3help("n", -np.pi / 3, "x")
    q3help("o", -np.pi / 3, "y")
    q3help("p", -np.pi / 3, "z")
    q3help("q", -np.pi / 6, "x")
    q3help("r", -np.pi / 6, "y")
    q3help("s", -np.pi / 6, "z")


def q4():
    print("Q4:")
    m = np.array([[0.747, 0.5430, 0.3826, 0.2528],
                  [0.2936, 0.7867, -0.5430, -0.8787],
                  [0.5960, 0.2936, 0.7474, -0.4321]])
    print(M2Q(m))

# Convert normalized quaternion to rotation matrix
def Q2M(quat):
    qw = quat[0]
    qx = quat[1]
    qy = quat[2]
    qz = quat[3]

    m00 = 1-2*qy*qy - 2*qz*qz
    m01 = 2.0*(qx*qy - qz*qw)
    m02 = 2.0*(qx*qz + qy*qw)

    m10 = 2.0*(qx*qy + qz*qw)
    m11 = 1-2*qx*qx - 2*qz*qz
    m12 = 2.0*(qy*qz - qx*qw)

    m20 = 2.0*(qx*qz - qy*qw)
    m21 = 2.0*(qy*qz + qx*qw)
    m22 =  1-2*qx*qx - 2*qy*qy

    return np.array([[ m00, m01, m02], [ m10, m11, m12], [ m20, m21, m22] ])


def q5():
    print("Q5:")
    q = np.array([0.74846, 0.13062, 0.50764, 0.40626])
    print(Q2M(q))

def q7():
    print("Q7:")
    print("A)")


    print("B)")
    r = .25 * 10
    c = .258 / 2
    leftR = r + c
    rightR = r - c
    tanSpeedLeft = leftR * .1
    tanSpeedRight = rightR * .1

    wheelRad = .0645 / 2
    velLeft = tanSpeedLeft / wheelRad
    velRight = tanSpeedRight / wheelRad
    print("Left Speed:", velLeft)
    print("Right Speed:", velRight)


if __name__ == '__main__':
    m = np.array(   [[  1.0, 0.0,   0.0],
                    [   0.0, 1.0,   0.0],
                    [	0.0, 0.0,   1.0]])
    identityMat = np.array([[1.0, 0.0], [0.0, 1.0]])
    # q1(identityMat)
    # q2(identityMat)
    # q3(identityMat)
    # q4()
    # q5()
    # q6 on hw2_6.py
    q7()









