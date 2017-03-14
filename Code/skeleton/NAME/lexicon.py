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
		if i in directions:
			direct=('direction',i)
			result.append(direct)	
		elif i in verbs:
			verb=('verb',i)
			result.append(verb)
		elif i in stops:
			stop=('stop',i)
			result.append(stop)
		elif i in nouns:
			noun=('noun',i)
			result.append(noun)
		elif convert_number(i):
			number=('number',convert_number(i))
			result.append(number)

		else:
			error=('error',i)
			result.append(error)
	return result


