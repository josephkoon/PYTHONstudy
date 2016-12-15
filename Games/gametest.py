from sys import exit
from random import randint


class Scene(object):
	def enter(self):
		print "This scene is not yet configured. Subclass it and implement enter()."
		exit(1)
		
		
class Engine(object):
	
	#initialize with scene_map
	def __init__(self, scene_map):
		self.scene_map = scene_map
		
	#playing the game
	def play(self):
		
		#access the map opening scene and next scene
		current_scene = self.scene_map.opening_scene()
		last_scene = self.scene_map.next_scene('finished')
		
		#as long as you aren't on the last scene - enter
		while current_scene != last_scene :
			next_scene_name = current_scene.enter()
			current_scene = self.scene_map.next_scene(next_scene_name)
			
		#print out the last scene
		current_scene.enter()
		
		
class Death(Scene):

	quips = [
	'You died. Idiot',
	'loser',
	'you are a cow',
	'you suck'
	]
	
	#acces the quips 
	def enter(self):
		print Death.quips[randint(0,len(self.quips)-1)]


class CentralCorridor(Scene):
	def enter(self):
		pass
		
		
class LaserWeaponArmory(Scene):
	def enter(self):
		pass
		
		
class TheBridge(Scene):
	def enter(self):
		pass
		
		
class EscapePod(Scene):
	def enter(self):
		pass
		
		
class Map(object):
	def __init__(self, start_scene):
		pass
		
	def next_scene(self, scene_name):
		pass
		
	def opening_scene(self):
		pass

a_map = Map('central corridor')
a_game = Engine(a_map)
a_game.play()	