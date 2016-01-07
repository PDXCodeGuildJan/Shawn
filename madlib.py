#Make a madlib that promts the user for 5 words/phrases
#These are then added to a silly story

madlib = "The forest floor is covered in "

plural_noun = input("Please give a plural noun: ")

madlib = madlib + plural_noun+ " ,which, although sticky, \n "

plural_verb = input("Please give plural verb: ")

madlib = madlib +plural_verb+ " constantly. "

name = input("Please enter a proper noun: ")

madlib = madlib + name + " waits patiently under the soft duff for "

time_frame = input("Please enter a period in time: ")

madlib = madlib + time_frame+". \n"

onomonopea = input("Please enter onomonopea: ")

madlib = madlib + onomonopea + " is the only sound the " + plural_noun + " can hear in these woods."
print(madlib)