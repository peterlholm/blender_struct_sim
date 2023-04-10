#
# makefile for blender execution
#

run:
	blender -b -o output  analog_sim.blend -f 1 

testing:
	blender -b -o output analog_sim.blend -f 1
