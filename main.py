from Vector3n import Vector3n
#from Matrix3n import Matrix3n
#import Quaternion

vect1 = Vector3n(5, 5, 5)
axis = Vector3n(1, 0, 0)
rotatedVector = (0, 0, 0)

rotatedVector = vect1.rotateVector(90, axis)

rotatedVector.show()






