import pickle
from statistics import mean
from statistics import median
from scipy.stats import mannwhitneyu as mannu
import csv


rfile = open('summaries_ratings.csv','r')
reader = csv.DictReader(rfile)

ratings = list()

for dict in reader:
	ratings.append(dict)


lowcomplete = list()
highcomplete = list()
lowconcise = list()
highconcise = list()



for sample in ratings:
	print(sample)
	sid = "P{}-T{}.{}".format(sample['participant'],sample['session'],sample['method'])
	if int(sample['Completeness']) <= 3:
		lowcomplete.append(sid)	
	elif int(sample['Completeness']) == 5:
		highcomplete.append(sid)

	if int(sample['Conciseness']) <= 3:
		lowconcise.append(sid)
	elif int(sample['Conciseness']) == 5:
		highconcise.append(sid)




main = pickle.load(open("java_fixations.pkl","rb"))

lowcompletecounts= list()
highcompletecounts = list()

lowconcisecounts = list()
highconcisecounts = list()



for sample in main:
	if len(main[sample])<10:
		continue
	methods = []

	for fixation in main[sample]:
		astpath = fixation['xpath'].split("/")
		methodpos = ""
		for ast in astpath:
			if "src:function" in ast or "src:constructor" in ast:
				methodpos = ast

		if methodpos == "":
			continue            # not inside a function

		methods.append(fixation['fixation_target']+methodpos)  #file name + method location makes unique method string

	methods = list(set(methods))
	mcount = len(methods)


	if sample in lowcomplete:
		lowcompletecounts.append(mcount)
	elif sample in highcomplete:
		highcompletecounts.append(mcount)
	if sample in lowconcise:
		lowconcisecounts.append(mcount)
	elif sample in highconcise:
		highconcisecounts.append(mcount)




print("low complete:{}".format(mean(lowcompletecounts)))
print("high complete:{}".format(mean(highcompletecounts)))


x = lowcompletecounts
y = highcompletecounts
U1,p = mannu(x,y)
U2 = (len(x)*len(y)) - U1

print("U1:{}, U2:{}, p:{}".format(U1,U2,p))


print("low concise:{}".format(mean(lowconcisecounts)))
print("high concise:{}".format(mean(highconcisecounts)))

x = lowconcisecounts
y = highconcisecounts
U1,p = mannu(x,y)
U2 = (len(x)*len(y)) - U1

print("U1:{}, U2:{}, p:{}".format(U1,U2,p))