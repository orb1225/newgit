def convert_number(s):
	try:
		return int(s)
	except ValueError:
		return None	

directions=('north','south','east','west','down','up','left','right','back')
verbs=('go','stop','kill','eat')
stops=('the','in','of','from','at','it')
nouns=('door','bear','princess','cabinet')


		
def scan(stuff):
	result=[]
	words=stuff.split()
	for i in words:
		for j in directions:
			if i==j:
				direct=('direction',i)
				result.append(direct)	
				words.remove(i)
	for o in words:
		for k in verbs:
			if o==k:
				verb=('verb',o)
				result.append(verb)
				words.remove(o)

	for p in words:
		for l in stops:
			if p==l:
				stop=('stop',p)
				result.append(stop)
				words.remove(p)

	for u in words:
		for t in nouns:
			if u==t:
				noun=('noun',u)
				result.append(noun)
				words.remove(u)

	for q in words:
		qm=convert_number(q)
		if qm:
			number=('numbers',qm)
			result.append(number)
			words.remove(q)

	for r in words:
		error=('error',r)
		result.append(error)
	return result
a=scan("south east")
print "south east"
print a
b=scan("north east  eat bear south down")
print "north east  eat bear south down"
print b	
