import numpy as np
class Quaternion(np.ndarray):

#creates the Quaternion class and defines some useful methods
    def __new__(cls, Re, Im):
        '''
        Re is an integer. 
        Im is a list or an array.
        '''
        obj = np.concat([np.array([Re]), np.array(Im)]).view(cls)
        return obj
    
    def __array_finalize__(self, obj):
        return super().__array_finalize__(obj)

    
    def __mul__(Q1, Q2):
        Re = Q1[0]*Q2[0] - np.dot(Q1[1:4], Q2[1:4])
        Im = Q1[0] * Q2[1:4] + Q2[0] * Q1[1:4] + np.cross(Q1[1:4], Q2[1:4])
        return  Quaternion(Re, Im)
   
    def conjug(Q1):
        return Quaternion(Q1[0], -Q1[1:4])
    
    def rotate(v, q, theta):
        #v is a vector, q is the axis of rotation, theta the amount to rotate by
        V = Quaternion(0, v)
        Q = Quaternion(np.cos(theta/2), np.sin(theta/2) * np.array(q))
        return (Q*V)*Quaternion.conjug(Q)
    
    def norm(Q1):
        return np.sqrt(np.dot(Q1, Q1))
    
    def inverse(Q1):
        return Quaternion.conjug(Q1)/(Quaternion.norm(Q1))**2