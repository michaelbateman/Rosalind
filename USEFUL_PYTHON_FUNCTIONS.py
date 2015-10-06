
def make_dict(s):
    try:
        input_file = open(s, "r")
        print "input file is", input_file.name
    except IOError:
        print "Oh no, we couldn't open our file!"

    dict = {}
    for line in input_file:
	temp = line.split()
	dict.update(  {temp[0]:float(temp[1])}  )
	
    return dict	

