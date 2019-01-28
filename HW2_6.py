''' HW2.6 data'''
'''  by David Conner CPSC 495/595 Spring 2017 '''

import numpy as np

#Homework Hw2.6



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

# convert x,y,z displacements and rotation matrix into homogeneous transform
def transform3D(dx,dy,dz,R):
    T = np.array([ [    R[0,0] ,  R[0,1] , R[0,2],  dx ],
                   [	R[1,0] ,  R[1,1] , R[1,2],  dy ],
                   [    R[2,0] ,  R[2,1] , R[2,2],  dz ],
                   [	0.0	   ,	0.0	 ,   0.0 , 1.0 ]]);
    return T;

def help1(arr):
    return arr[0]

def help2(arr):
    return arr[1]

def help3(arr):
    return arr[2]
#RESULTS: for pelvis to r_palm
#Chain is: r_palm -> r_hand -> r_arm_wrist_roll -> r_arm_wrist_yaw -> r_arm_elbow -> r_arm_shoulder_yaw -> r_arm_shoulder_roll -> r_arm_shoulder_pitch -> utorso -> waist -> pelvis
# plm-hnd-wr-wy-el-shy-shr-shp-tor-wst-pel
t_pel_wst = np.array([0.000, 0.000, 0.137])
q_pel_wst = np.array([1.000, 0.000, 0.000, -0.000]) # [w, (x,y,z)] form

t_wst_tor = np.array([0.000, 0.000, 0.000])
q_wst_tor= np.array([1.000, 0.000, 0.003, 0.000])# [w, (x,y,z)] form

t_tor_shp = np.array([0.000, -0.234, 0.165])
q_tor_shp = np.array([0.851, 0.000, -0.525, 0.000]) # [w, (x,y,z)] form

t_shp_shr = np.array([0.000, 0.000, 0.000])
q_shp_shr = np.array([0.960, -0.279, 0.000, 0.000])# [w, (x,y,z)] form

t_shr_shy = np.array([0.000, 0.000, 0.000])
q_shr_shy = np.array([0.842, 0.000, 0.000, 0.540])# [w, (x,y,z)] form

t_shy_el = np.array([0.030, 0.000, -0.246])
q_shy_el = np.array([0.863, 0.000, -0.506, 0.000])# [w, (x,y,z)] form

t_el_wy = np.array([-0.030, 0.000, -0.186])
q_el_wy = np.array([0.566, 0.000, 0.000, 0.824])# [w, (x,y,z)] form

t_wy_wr = np.array([0.000, 0.000, 0.000])
q_wy_wr = np.array([0.904, -0.428, 0.000, 0.000])# [w, (x,y,z)] form

t_wr_hnd = np.array([0.000, 0.000, 0.000])
q_wr_hnd = np.array([0.797, 0.000, 0.000, -0.605])# [w, (x,y,z)] form

t_hnd_plm = np.array([0.000, 0.000, -0.160])
q_hnd_plm = np.array([0.000, 0.707, 0.707, 0.000])# [w, (x,y,z)] form

print("palmThand -> handTarmwristroll -> armwristrollTarmwristyaw -> "
      "armwristyawTarmelbow -> armelbowTshoulderyaw -> shoulderyawTshoulderroll "
      "-> shoulderrollTshoulderpitch -> shoulderpitchTutorso -> utorsoTwaist -> "
      "waistTpelvis")


print("palmThand: ")
move1 = transform3D(t_hnd_plm[0], t_hnd_plm[1], t_hnd_plm[2])
print(move1)
print("handTarmwristroll: ")
move2 = transform3D(t_wr_hnd[0], t_wr_hnd[1], t_wr_hnd[2])
print(move2)
print("armwristrollTarmwristyaw: ")
move3 = transform3D(t_wy_wr[0], t_wy_wr[1], t_wy_wr[2])
print(move3)
print("armwristyawTarmelbow: ")
move4 = transform3D(t_el_wy[0], t_el_wy[1], t_el_wy[2])
print(move4)
print("armelbowTshoulderyaw: ")
move5 = transform3D(t_shy_el[0], t_shy_el[1], t_shy_el[2])
print(move5)
print("shoulderyawTshoulderroll: ")
move6 = transform3D(t_shr_shy[0], t_shr_shy[1], t_shr_shy[2])
print(move6)
print("shoulderrollTshoulderpitch: ")
move7 = transform3D(t_shp_shr[0], t_shp_shr[1], t_shp_shr[2])
print(move7)
print("shoulderpitchTutorso: ")
move8 = transform3D(t_tor_shp[0], t_tor_shp[1], t_tor_shp[2])
print(move8)
print("utorsoTwaist: ")
move9 = transform3D(t_wst_tor[0], t_wst_tor[1], t_wst_tor[2])
print(move9)
print("waistTpelvis: ")
move10 = transform3D(t_pel_wst[0], t_pel_wst[1], t_pel_wst[2])
print(move10)
# this should be the palm and pelvis .dot
print("B)")
endval = np.dot(np.dot(np.dot(np.dot(np.dot(move1, move2), np.dot(move3, move4)),
                    np.dot(move5, move6)), np.dot(move7, move8)), move9)
print(endval)

print("C)")
m = np.array([[1.0, 0.0, 0.0],
              [0.0, 1.0, 0.0],
              [0.0, 0.0, 1.0]])
# this is just the transform3D(0,0,.2, identityMatrix)
print(np.dot(endval, transform3D(0, 0, 0.2, m)))




