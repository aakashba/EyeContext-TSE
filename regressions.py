import pickle
from statistics import mean
from statistics import median

main = pickle.load(open("java_fixations.pkl","rb"))

rcount = {1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[]}



for session in main:

	if len(main[session]) <10:
		continue
	
	words = []
	sid = int(session.split(".")[-1])  #session number from 1 to 8

	for fixation in main[session]:
		words.append(fixation['fixation_target']+str(fixation['source_file_line'])+fixation['token']) #unique words


	swords = list(set(words))

	r = ((len(words)-len(swords))*100)/len(words)
	
	rcount[sid].append(r)



for sid in rcount:
	print("--------------------- Method Position:{} --------------------".format(sid))
	print("min:{}".format(min(rcount[sid])))
	print("max:{}".format(max(rcount[sid])))
	print("mean:{}".format(mean(rcount[sid])))
	print("median:{}".format(median(rcount[sid])))

from scipy.stats import mannwhitneyu as mannu

x = rcount[1] + rcount[2]
y = rcount[7] + rcount[8]

U1,p = mannu(x,y)
U2 = (len(x)*len(y)) - U1

print("U1:{}, U2:{}, p:{}".format(U1,U2,p))
