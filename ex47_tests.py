from nose.tools import *
from ex47.game import Room

def test_room():
    gold = Room("GoldRoom", """This room has gold you can forcibly acquire. There's a door to the north""")
    assert_equal(gold.name,"GoldRoom")
    assert_equal(gold.paths,{})

def test_room_paths():
    center = Room("Center", "Test room in the center")
    north  = Room("North", "Test room in the north")
    south  = Room("North", "Test room in the south")
    
    center.add_paths({'north': north, 'south': south})

    assert_equal(center.go('north'), north)
    assert_equal(center.go('south'), south)
    
def test_map():
    start = Room("Start location.", "Can go left or right.",)
    left = Room("Left location.","Can go right.")
    right = Room("Right location", "Can go left")

    start.add_paths({"left": left, "right": right})
    left.add_paths({"right": start})
    right.add_paths({"left": start})

    assert_equal(start.go("left"), left)
    assert_equal(start.go("left").go("right"), start)
    assert_equal(start.go("right").go("left"), start)



def setup():
    print("SETUP")

def teardown():
    print("++UNSETUP")

def test_basic():
    print("TEST FUNCTION EXECUTED")