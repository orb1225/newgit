from nose.tools import *
from gothonweb.map import Room



def test_room():
	gold= Room("GoldRoom",""" to the north""")
	assert_equal(gold.name,"GoldRoom")
	assert_equal(gold.paths,{})

def test_room_paths():
	center=Room("center","Test center")
	north=Room("north","Test north")
	south=Room("South","Test south")


	center.add_paths({'north':north,'south':south})
	assert_equal(center.go('north'),north)
	assert_equal(center.go('south'),south)
def test_map():
	start=Room("start","You can go west an down a hole")
	west=Room("Trees","There are trees here")
	down=Room("Dungeon","It's dark down here,you can go up")

	start.add_paths({'west':west,'down':down})
	west.add_paths({'east':start})
	down.add_paths({'up':start})

	assert_equal(start.go('west'),west)
	assert_equal(start.go('west').go('east'),start)
	assert_equal(start.go('down').go('up'),start)










