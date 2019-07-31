
from nose.tools import *
from ex47.game import Room


def test_room():
    gold = Room(
        "Gold room", """This room has gold wherever you look, there's a door to the north.""")
    assert_equal(gold.name, "Gold room")
    assert_equal(gold.paths, {})


def test_room_paths():
    north = Room("Test Room north", "This room is in the north")
    center = Room("Test Room center", "This room is in the center")
    south = Room("Test Room south", "This room is in the south")

    center.add_paths({'north': north, 'south': south})

    assert_equal(center.go('north'), north)
    assert_equal(center.go('south'), south)


def test_map():
    start = Room("start", "You can go west and down a hole")

    west = Room("west", "There are trees and you can go east.")
    down = Room("dungeon", "It's dark down here, you can go up")

    start.add_paths({"west": west, "down": down})
    west.add_paths({'east': start})
    down.add_paths({'up': start})

    assert_equal(start.go('west'), west)
    assert_equal(start.go('down').go('up'), start)
    assert_equal(start.go('west').go('east'), start)

# def test_basic():
#     print("I RAN")
