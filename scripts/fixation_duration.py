import pickle
from statistics import mean
from statistics import median

main = pickle.load(open("java_fixations.pkl","rb"))

fduration = {1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[]}



for session in main:
	if len(main[session]) < 10:
		continue
	sid = int(session.split(".")[-1])  #session number from 1 to 8
	fixate = list()
	for fixation in main[session]:
		if fixation['duration'] > 60000: #discard longer than 1 minute fixation on one word
			continue
		fixate.append(fixation['duration'])	
	
	fduration[sid].append(mean(fixate))



for sid in fduration:
	print("--------------------- Method Position:{} --------------------".format(sid))
	print("min:{}".format(min(fduration[sid])))
	print("max:{}".format(max(fduration[sid])))
	print("mean:{}".format(mean(fduration[sid])))
	print("median:{}".format(median(fduration[sid])))


from scipy.stats import mannwhitneyu as mannu

x = fduration[1] + fduration[2]
y = fduration[7] + fduration[8]

U1,p = mannu(x,y)
U2 = (len(x)*len(y)) - U1

print("U1:{}, U2:{}, p:{}".format(U1,U2,p))
