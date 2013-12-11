import numpy
import tf
import geometry_msgs

from geometry_msgs.msg import Pose, PoseStamped, Transform, TransformStamped


def homogeneous_product_pose_transform(pose, transform):
    """
     pose should be Pose() msg
     transform is Transform()
    """
    # 1. Get the transform homogenous matrix.
    Ht = tf.transformations.quaternion_matrix([transform.rotation.x, transform.rotation.y,
                                             transform.rotation.z, transform.rotation.w])

    Tt = [transform.translation.x, transform.translation.y, transform.translation.z]

    Ht[:3,3] = Tt

    # 2.Original pose to homogenous matrix
    H0 = tf.transformations.quaternion_matrix([pose.orientation.x, pose.orientation.y,
                                               pose.orientation.z, pose.orientation.w])

    T0 = [pose.position.x, pose.position.y, pose.position.z]
    H0[:3,3] = T0

    H1 = numpy.dot(H0, Ht)

    # Get results from matrix
    result_position = H1[:3,3].T
    result_position = geometry_msgs.msg.Vector3(result_position[0], result_position[1], result_position[2])
    result_quat     = tf.transformations.quaternion_from_matrix(H1)
    result_quat     = geometry_msgs.msg.Quaternion(result_quat[0], result_quat[1], result_quat[2], result_quat[3])
    result_pose             = Pose()
    result_pose.position    = result_position
    result_pose.orientation = result_quat
    return result_pose
