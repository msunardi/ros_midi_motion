#!/usr/bin/env python

from midi_motion.srv import *
import rospy, rospkg

import numpy as np
from readmidi import Readmidi
import analyzer as az

def extract(service_request):
    # rospy.loginfo(filename)
    # if not filename:
    # 	return MidiInfoResponse("fubar" ,"456")
    # return MidiInfoResponse("barfoo", "123")
    path = service_request.source
    if not path:
        return False

    print "Extract: %s" % path

    r = Readmidi()
    rm = r.openfile(path)
    events = r.parseevents(ret=2)
    nopb = az.analyzeNoteOnPerBeat(events)
    t, m = az.analyzePhrase3(nopb)
    return MidiInfoResponse(str(t), str(m))
    # return MidiInfoResponse("foo", "bar")


def mm_server():
    rospy.init_node('midi_motion_server')
    s = rospy.Service('midi_motion_server', MidiInfo, extract)
    print "Ready to extract MIDI"
    rospy.spin()

if __name__ == "__main__":
    mm_server()