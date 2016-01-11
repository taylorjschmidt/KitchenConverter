from fractions import Fraction

def teaspoon():
	print """
	Now, please select the unit to convert to:
	1. Tablespoons
	2. Cups
	3. Ounces
	
	Type 'b' to go back.
	Type 'q' to quit.
	"""
	unitTo = raw_input("Convert to: ")
	
	if unitTo == '1':
		tspToTbsp()
	elif unitTo == '2':
		tspToCup()
	elif unitTo == '3':
		tspToOunce()
	else:
		fail(unitTo)
	
def tablespoon():
	print """
	Now, please select the unit to convert to:
	1. Teaspoons
	2. Cups
	3. Ounces
	
	Type 'b' to go back.
	Type 'q' to quit.
	"""
	unitTo = raw_input("Convert to: ")
	
	if unitTo == '1':
		tbspToTsp()
	elif unitTo == '2':
		tbspToCup()
	elif unitTo == '3':
		tbspToOunce()
	else:
		fail(unitTo)
	
def cup():
	print """
	Now, please select the unit to convert to:
	1. Teaspoons
	2. Tablespoons
	3. Ounces
	
	Type 'b' to go back.
	Type 'q' to quit.
	"""	
	unitTo = raw_input("Convert to: ")
	
	if unitTo == '1':
		cupToTsp()
	elif unitTo == '2':
		cupToTbsp()
	elif unitTo == '3':
		cupToOunce()
	else:
		fail(unitTo)
	
def ounces():
	print """
	Now, please select the unit to convert to:
	1. Teaspoons
	2. Tablespoons
	3. Cups
	
	Type 'b' to go back.
	Type 'q' to quit.
	"""
	unitTo = raw_input("Convert to: ")
	
	if unitTo == '1':
		ounceToTsp()
	elif unitTo == '2':
		ounceToTbsp()
	elif unitTo == '3':
		ounceToCup()
	else:
		fail(unitTo)
		
def tspToTbsp():
	tsp = float(Fraction(raw_input("How many teaspoons?   ")))
	tbsp = int(tsp / 3)
	remainder = tsp % 3
	
	if remainder == 0:
		print "That is equal to %d tablespoons." % tbsp
	else:
		print "That is equal to %d %d/3" % (tbsp, remainder)
		
def tspToCup():
	tsp = float(Fraction(raw_input("How many teaspoons?   ")))
	cup = int(tsp / 48)
	remainder = tsp % 48
	
	if remainder == 0:
		print "That is equal to %d cups." % cup
	else:
		output = float(remainder / 48)
		print "That is equal to %d %s cups." % (cup, Fraction(output).limit_denominator())
	
def tspToOunce():
	tsp = float(Fraction(raw_input("How many teaspoons?   ")))
	ounce = int(tsp / 6)
	remainder = tsp % 6
	
	if remainder == 0:
		print "That is equal to %d ounces." % ounce
	else:
		output = float(remainder / 6)
		print "That is equal to %d %s cups." % (ounce, Fraction(output).limit_denominator())
	
def tbspToTsp():
	tbsp = float(Fraction(raw_input("How many tablespoons?   ")))
	tsp = int(tbsp / 3)
	remainder = tbsp % 3
	
	if remainder == 0:
		print "That is equal to %d Teaspoons." % tsp
	else:
		print "That is equal to %d %d/3 Teaspoons." % (tsp, remainder)
	
def tbspToCup():
	tbsp = float(Fraction(raw_input("How many tablespoons?   ")))	
	cup = int(tbsp / 16)
	remainder = tbsp % 16
	
	if remainder == 0:
		print "That is equal to %d cups." % cup
	else:
		output = Fraction(float(remainder / 16)).limit_denominator()
		print "That is equal to %d %s cups." % (cup, output)

def tbspToOunce():
	tbsp = float(Fraction(raw_input("How many tablespoons?   ")))
	ounce = int(tbsp / 2)
	
	if remainder == 0:
		print "That is equal to %d ounces." % ounce
	else:
		output = Fraction(float(remainder / 2)).limit_denominator()
		print "That is equal to %d %s ounces." % (ounce, output)		

def cupToTsp():
	cup = float(Fraction(raw_input("How many cups?   ")))
	tsp = cup * 48
	remainder = tsp % 1
	
	if remainder == 0:
		print "That is equal to %d teaspoons." % tsp
	else:
		output = Fraction(remainder).limit_denominator()
		print "That is equal to %d %s teaspoons." % (tsp, output)

def cupToTbsp():
	cup = float(Fraction(raw_input("How many cups?   ")))
	tbsp = cup * 16
	remainder = tbsp % 1
	
	if remainder == 0:
		print "That is equal to %d tablespoons." % tbsp
	else:
		output = Fraction(remainder).limit_denominator()
		print "That is equal to %d %s tablespoons." % (tbsp, output)
	
def cupToOunce():
	cup = float(Fraction(raw_input("How many cups?   ")))
	ounce = cup * 8
	remainder = cup % 1
	
	if remainder == 0: 
		print "That is equal to %d ounces." % ounce
	else:
		output = Fraction(remainder).limit_denominator()
		print "That is equal to %d %s ounces." % (ounce, output)
	
def ounceToTsp():
	ounce = float(Fraction(raw_input("How many ounces?   ")))
	tsp = ounce * 6
	remainder = ounce % 6
	
	if remainder == 0:
		print "That is equal to %d teaspoons." % tsp
	else:
		output = Fraction(remainder).limit_denominator()
		print "That is equal to %d %s teaspoons." % (tsp, output)

def ounceToTbsp():
	ounce = float(Fraction(raw_input("How many ounces?   ")))
	tbsp = ounce * 2
	remainder = tbsp % 1
	
	if remainder == 0:
		print "That is equal to %d tablespoons." % tbsp
	else:
		output = Fraction(remainder.limit_denominator())
		print "That is equal to %d %s tablespoons." % (tbsp, output)
	
def ounceToCup():
	ounce = float(Fraction(raw_input("How many ounces?   ")))
	cup = int(ounce / 8)
	remainder = cup % 8
	
	if remainder == 0:
		print "That is equal to %d cups." % cup
	else:
		output = Fraction(float(remainder / 8)).limit_denominator()
		print "That is equal to %d %s cups." % (cup, output)	
		
def fail(entry):
	if entry == 'b':
		start()
	elif entry == 'q':
		quit()
	else:
		print "Sorry, I didn't get that. Let's start again.\n"
		start()
	
def start():
	print """
	Please select the unit you would like to convert from:
	1. Teaspoons
	2. Tablespoons
	3. Cups
	4. Ounces
	"""
	unitFrom = raw_input("Convert from: ")
	
	if unitFrom == '1':
		teaspoon()
	elif unitFrom == '2':
		tablespoon()
	elif unitFrom == '3':
		cup()
	elif unitFrom == '4':
		ounces()
	else:
		print "Oops. I didn't understand that selection. Let's try again.\n"
		start()

start()
