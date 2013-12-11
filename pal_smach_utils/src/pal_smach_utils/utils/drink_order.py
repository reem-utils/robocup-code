

class DrinkOrder:
    """DrinkOrder.

    Use this class to represent a drink order.
    """

    person_name = None
    drink = None

    def __init__(self, name, drink, person_pose=None):
        """Constructor for DrinkOrder.

        @type name: string
        @param name: The person name that want a drink.

        @type drink: string
        @param drink: The drink name requested by the person.

        @type person_pose: 'geometry_msgs/PoseStamped'
        @param person_pose: The person pose.
        If you use 'geometry_msgs/PoseStamped' don't forget to update header.stamp when sending the goal for some action.

        """
        self.person_name = name
        self.drink = drink
        self.person_pose = person_pose

# vim: expandtab ts=4 sw=4
