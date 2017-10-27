#!/usr/bin/env python

import sys
import rospy, rospkg
from midi_motion.srv import *

rospack = rospkg.RosPack()

def mm_client(filename):
    rospy.wait_for_service('midi_motion_server')
    try:
        mm = rospy.ServiceProxy('midi_motion_server', MidiInfo)
        r = mm(filename)
        return r.events, r.timing
    except rospy.ServiceException, e:
        print "Service call failed: %s" % e

def usage():
    return "Either give a path to .med file or a default will be given."

if __name__ == "__main__":
    filename = None
    if len(sys.argv) == 2:
        filename = str(sys.argv[1])
    else:
        print usage()
        filename = "lullaby_of_birdland.med"
    path = '%s/src/%s' % (rospack.get_path('midi_motion'), filename)
    print path
    print "Requesting MIDI information ... %s" % path
    timing, accent = mm_client(path)
    print timing