from __future__ import print_function
import re

# Guarantee python 2 and 3 compatibility.
try: input = raw_input
except NameError: pass

#String for each madlib. [] denotes an input
mad_libs = ["I spent last summer on my grandfather's [adjective] farm. He raises [plural noun] for local food [plural noun]. He also grows corn on the [noun], [adjective] lettuce and lima [plural noun]. My favorite place to [verb] on the farm is the [adjective] house where grandfather keeps his [plural noun]. But when I visit in November, there are no [plural noun]! They are all gone! I anxiously await at the table that Thanksgiving. I see the corn on the [noun] and even the lima [plural noun]. I am relieved when grandma brings out a [noun] for Thanksgiving dinner!",
		   "Today we are celebrating [holiday] dinner at [name of person]'s house. When we arrived, my [name of family member] greeted us with a big, [adjective] kiss. Kisses are so [adjective]! Now we're just waiting for the [animal] to come out of the oven. My dad is watching [sport] on TV. He always shouts, \"[exclamation]\" when his team scores a [noun]. Yesss!!! Only [number] more minutes until the [animal] will be ready to eat. I wonder if my mom will let me try the [food] first. My grandma makes the best [flavor] pie! It smells like [noun]. (Much better than my [name of family member]. He/She smells like [noun]!) Happy [holiday]!",
		   "It all began way back in 1621. The [adjective] pilgrims set sail from (the) [place] in hopes of starting new lives in the \"New World\" that we now call The [adjective] States of America. The first Plymouth colonists needed help adjusting to the new land. Fortunately, a Native American named Squanto (which means \"To [present tense verb] a/an [object]\") was glad to help. He taught them how to grow tall stalks of [food], make maple syrup from [type of plant] sap, and catch [living creature] from the river. He even advised them as to which plants were edibly [adjective] and which were poisonous. That first autumn harvest celebration actually lasted [number] whole days! We're pretty sure that lots of [food] and [food] were on the menu! President Lincoln made Thanksgiving an official natiional holiday in 1863. And we've been stuffing our grateful faces with [food] ever since!"]
print("Welcome to the Thanksgiving Mad Lib Generator!")

BOLD_MARKER = '\033[1m'
NORMAL_MARKER = '\033[0m'

#for each madlib
for mad_lib in mad_libs:
	#set the pattern to search for []
	bracket_pattern = re.compile('\[.*?\]')
	#for each match found
	for field in bracket_pattern.finditer(mad_lib):
		#value found
		value = field.group()
		#user's input
		user_input = input(BOLD_MARKER + "Enter a " + value[1:-1] + ": " + NORMAL_MARKER)
		#replace the match found with the user input. Uses the first found so it does not replace more than one.
		mad_lib = mad_lib.replace(value, user_input, 1)
	#prints the mad lib generated
	print(mad_lib)