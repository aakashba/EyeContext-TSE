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
	fixate = list()
	for fixation in main[sample]:
		if fixation['duration'] > 60000: #discard longer than 1 minute fixation on one word
			continue
		fixate.append(fixation['duration'])

	fduration = mean(fixate)

	if sample in lowcomplete:
		lowcompletecounts.append(fduration)
	elif sample in highcomplete:
		highcompletecounts.append(fduration)
	if sample in lowconcise:
		lowconcisecounts.append(fduration)
	elif sample in highconcise:
		highconcisecounts.append(fduration)




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
