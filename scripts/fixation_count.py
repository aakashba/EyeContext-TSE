import pickle
from statistics import mean
from statistics import median
from scipy.stats import mannwhitneyu as mannu


main = pickle.load(open("java_fixations.pkl","rb"))

fcount = {1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[]}



for session in main:
	sid = int(session.split(".")[-1])  #session number from 1 to 8
	if len(main[session])<10:
		continue
	fcount[sid].append(len(main[session]))



for sid in fcount:
	print("--------------------- Method Position:{} --------------------".format(sid))
	print("min:{}".format(min(fcount[sid])))
	print("max:{}".format(max(fcount[sid])))
	print("mean:{}".format(mean(fcount[sid])))
	print("median:{}".format(median(fcount[sid])))

x = fcount[1] + fcount[2]
y = fcount[7] + fcount[8]

U1,p = mannu(x,y)
U2 = (len(x)*len(y)) - U1

print("U1:{}, U2:{}, p:{}".format(U1,U2,p))
