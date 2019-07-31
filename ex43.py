from sys import exit
from random import randint
from textwrap import dedent


class Scene(object):

    # this method would run if a inheriting class had yet not implemented a enter method
    def enter(self):
        print("Not yet implemented")
        exit(1)


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()


class Death(Scene):
    quips = [
        "You not only die. \nYou disappoint millions of galactic citizens with your mediocrity...",
        "You saaad bruh!",
        "You never learn",
        "Oh no you dedent!"
    ]

    def enter(self):

        print(Death.quips[randint(0, len(self.quips) - 1)])
        exit(1)


class CentralCorridor(Scene):

    def enter(self):
        print(dedent("""
            The Gothons have invaded your ship and destroyed your entire crew.
            You're the last surviving member and your last mission is to get the 
            neutron destruct bomb from the armory, put it in the bridge 
            and blow the ship up after getting in an escape pod.
            You are running down the central corridorto the weapons armory when a gothon jumps out.
            """))

        action = input("> ")

        if action == "shoot!":
            print(dedent("""
                Quick at the draw you yank out the blaster and fire it at the Gothon. 
                His clown costume is flowing around his body, which throws off your aim. 
                You completely miss his body and he kills you
                """))

            return 'death'

        elif action == 'dodge':
            print(dedent("""
                Your clumsy ass falls when trying to dodge.
                The Gothon kills you and stomps your corpse.
                """))

            return 'death'

        elif action == 'tell a joke' or action == 'godmode':
            print(dedent("""
                Fortunately for you the Gothon gets it, after a quick afterthinking.
                Laughter, as we all know paralyze the Gothons for hours.
                So you can pass his limp body without thing turning ugly.
                """))

            return 'laser_weapon_armory'

        else:
            print(dedent("""
                Didn't quite get that...
                Try one of these instead: 'shoot!', 'dodge', 'tell a joke'
                """))

            return 'central_corridor'


class LaserWeaponArmory(Scene):

    def enter(self):
        print(dedent("""
            You're in the armory, a code needs to be cracked,
            it's three digits and you have 10 tries.
            """))

        code = f"{randint(1,9)}{randint(1,9)}{randint(1,9)}"
        print(code)
        guess = input("[keypad]> ")
        guesses = 1

        while guess != code and guesses < 10 and guess != 'godmode':
            print("The lock goes: BZZzzZZTtt")
            guesses += 1
            guess = input("> ")

        if guess == code or guess == "godmode":
            print(dedent("""
                The container clicks open and the seal breaks, letting gas out.
                You grab the neutron bomb and run as fast as you can to the 
                bridge where you must place it in the right spot.
                """))
            return 'the_bridge'
        else:
            print(dedent("""
                The lock buzzes dissapproving one last time.
                The lock self-destucts and leaves you to think about
                your own mediocrity one last hour before 
                the Gothons blow the ship to atoms with their
                Ion-Bagel.
                """))
            return 'death'


class TheBridge(Scene):

    def enter(self):
        print(dedent("""
            You burst onto the bridge with the neutron destruct bomb 
            under your arm and surprise 5 Gothons who are trying to 
            take control of the ship.
            They haven't yet pulled out their weapons, because the sight of the bomb
            under your arm made them somewhat, hesitant...
            """))

        action = input("> ")

        if action == "throw the bomb":

            print(dedent("""
                In a panic you throw the bomb right at the group of Gothons
                and make a leap for the door. Right as you let go of the bomb,
                a Gothon shoots you in your face and you die...
                They go to disarm the bomb, but what do you care – you're dead af
                """))

            return 'death'

        elif action == "slowly place the bomb" or action == "godmode":

            print(dedent("""
                You point your blaster at the bomb under your arm
                and this way you convince the Gothons to raise their hands over
                their ugly mutt faces. You place the bomb right by the door, 
                still pointing your blaster at it, you jump through the door opening and 
                when you've swiftly shut the door you blast the lock to keep the Gothons
                from opening it. It works, yikes!
                You run for the escape pods to jump ship safely before the neutron bomb, well... ...bombs.
                """))

            return 'escape_pod'

        elif action == "tell a joke":

            print(dedent("""
                One would hope and maybe think this would work.
                But your nerves has your comedial timing well off, you ”bomb” the joke.
                The Gothons shoot you in a limb each, yes all five of them.
                Ouch, you die af...
                """))

            return 'death'

        else:

            print(dedent("""
                Didn't quite get that...
                Try one of these instead: 'throw the bomb', 'slowly place the bomb', 'tell a joke'
                """))

            return 'the_bridge'


class EscapePod(Scene):

    def enter(self):
        print(dedent("""
            You rush through the ship desperately trying to make it to 
            the escape pod before the whole ship explodes.
            It seems like hardly any Gothons are on the ship so your run is
            clear of interference. You get to the chamber with the escape pods,
            and now you need to choose which of the pods to take.
            Some do look damaged but you haven't got the time to check them.
            There are 5 pods, which one do you choose?
            """))
        good_pod = randint(1, 5)
        print({good_pod})
        guess = input("[pod #]> ")

        if int(guess) != good_pod and int(guess) != 666:
            print(dedent(f"""
                You jump into pod {guess} and hit the eject button.
                The pod escapes out into the void of space, 
                then implodes as the hull ruptures, 
                crushing your body into jam jelly
                """))
            return 'death'
        elif int(guess) == good_pod or int(guess) == 666:
            print(dedent(F"""
                You jump into pod {guess} and hit the eject button.
                The pod easily slides out into space heading to the
                planet below.  As it flies to the planet, you look
                back and see your ship implode then explode like a
                bright star, taking out the Gothon ship at the same
                time.  You won!
            """))
            return 'finished'


class Finished(Scene):

    def enter(self):
        print("You won, good job!")
        return 'finished'


class Map(object):

    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
