import pickle

old = pickle.load(open("fixations.pkl","rb"))

new = dict()

for session in old:
	new[session] = list()
	for fixation in old[session]:
		if fixation['token'] != None:
			new[session].append(fixation)


pickle.dump(new, open("java_fixations.pkl","wb"))
			
	
