from Vector3n import Vector3n
#from Matrix3n import Matrix3n
#from Quaternion import Quaternion

vect1 = Vector3n(0, 4, 0)
axis = Vector3n(0, 0, 1)
rotatedVector = Vector3n(0, 0, 0)

#regualar quaternion rotation
#rotatedVector = vect1.rotateVector(-90, axis)

#t is the time varible of the rotation

#quaternion rotation using LERP interpolation and t = 1
#rotatedVectorL = vect1.rotateVectorLERP(-90, axis, 1)

#quaternion rotation using SLERP interpolation and t = 1
#rotatedVectorS = vect1.rotateVectorSLERP(-90, axis, 1)

#quaternion rotation using SLERP No Invert interpolation and t = 1
#rotatedVectorN = vect1.rotateVectorSLERPNoInvert(-90, axis, 1)

#progression of rotations using SQUAD and inputs of t = 0, 0.25, 0.75, and 1
rotatedVectorSQ25 = vect1.rotateVectorSQUAD(-90, axis, 0.25)
rotatedVectorSQ50 = vect1.rotateVectorSQUAD(-90, axis, 0.5)
rotatedVectorSQ75 = vect1.rotateVectorSQUAD(-90, axis, 0.75)
rotatedVectorSQLast = vect1.rotateVectorSQUAD(-90, axis, 1)

#print staring vector
print("Starting Vector")
vect1.show()

#print the progression of vector positions of SQUAD interpolation
print("SQUAD 0.25")
rotatedVectorSQ25.show()
print("SQUAD 0.50")
rotatedVectorSQ50.show()
print("SQUAD 0.75")
rotatedVectorSQ75.show()
print("SQUAD Final:")
rotatedVectorSQLast.show()


#print()

#print finished rotations of different interpolations
#print("SLERP No Invert")
#rotatedVectorN.show()
#print("SLERP:")
#rotatedVectorS.show()
#print("LERP:")
#rotatedVectorL.show()
#print("Regular:")
#rotatedVector.show()




