import pickle
from statistics import mean
from statistics import median

main = pickle.load(open("java_fixations.pkl","rb"))

lcount = {1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[]}



for session in main:

	if len(main[session]) <10:
		continue
	
	lines = [] 
	sid = int(session.split(".")[-1])  #session number from 1 to 8

	for fixation in main[session]:
		lines.append(fixation['fixation_target']+str(fixation['source_file_line']))  #file+line number makes unique line
	
	lines = list(set(lines))
	lcount[sid].append(len(lines))



for sid in lcount:
	print("--------------------- Method Position:{} --------------------".format(sid))
	print("min:{}".format(min(lcount[sid])))
	print("max:{}".format(max(lcount[sid])))
	print("mean:{}".format(mean(lcount[sid])))
	print("median:{}".format(median(lcount[sid])))



from scipy.stats import mannwhitneyu as mannu

x = lcount[1] + lcount[2]
y = lcount[7] + lcount[8]

U1,p = mannu(x,y)
U2 = (len(x)*len(y)) - U1

print("U1:{}, U2:{}, p:{}".format(U1,U2,p))
