#!/usr/bin/env  python
import rospy
from process.srv import behavior
from process.msg import BehaviorInfo

rospy.init_node('behavior_client')
rospy.wait_for_service('behavior_manager')
behavior_sender = rospy.ServiceProxy('behavior_manager', behavior)

# Behavior a envoyer
info0 = BehaviorInfo(behavior_id='000', type='limite',
                     xa=-50, ya=-70, xb=-50, yb=70, s=-1, r=30)
info1 = BehaviorInfo(behavior_id='001', type='ligne',
                     xa=-30, ya=-30, xb=70, yb=-20, s=-3, r=30)
info2 = BehaviorInfo(behavior_id='002', type='waypoint',
                     xa=30, ya=10, xb=20, yb=20, s=-1, r=10)
info3 = BehaviorInfo(behavior_id='003', type='patrol_circle',
                     xa=30, ya=10, xb=20, yb=20, s=1, r=30)

# Confirmation de la reception du behavior
rate = rospy.Rate(1)
for info in reversed([info0, info1, info3]):
    confirmation = behavior_sender(info)
    print confirmation
    rate.sleep()
