import pickle
from statistics import mean
from statistics import median

main = pickle.load(open("java_fixations.pkl","rb"))

mcount = {1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[]}



for session in main:

	if len(main[session]) <10:
		continue
	
	methods = [] 
	sid = int(session.split(".")[-1])  #session number from 1 to 8

	for fixation in main[session]:
		astpath = fixation['xpath'].split("/")
		methodpos = ""
		for ast in astpath:
			if "src:function" in ast or "src:constructor" in ast:
				methodpos = ast
		
		if methodpos == "":
			continue			# not inside a function

		methods.append(fixation['fixation_target']+methodpos)  #file name + method location makes unique method string
	
	methods = list(set(methods))
	mcount[sid].append(len(methods))



for sid in mcount:
	print("--------------------- Method Position:{} --------------------".format(sid))
	print("min:{}".format(min(mcount[sid])))
	print("max:{}".format(max(mcount[sid])))
	print("mean:{}".format(mean(mcount[sid])))
	print("median:{}".format(median(mcount[sid])))

from scipy.stats import mannwhitneyu as mannu

x = mcount[1] + mcount[2]
y = mcount[7] + mcount[8]

U1,p = mannu(x,y)
U2 = (len(x)*len(y)) - U1

print("U1:{}, U2:{}, p:{}".format(U1,U2,p))
