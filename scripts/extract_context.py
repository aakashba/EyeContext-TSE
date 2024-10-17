import pickle

main = pickle.load(open("java_fixations.pkl","rb"))
map = pickle.load(open("summaries.pkl","rb"))
new = list()

for key in main:
	participant = key.split("-")[0].replace("P","")
	session = key.split("-")[1].split(".")[0].replace("T","")
	method = key.split(".")[1]
	count = 0
	for sample in map:
		
		if sample['participant'] == participant and sample['session']==session and sample['method']==method:
			sample['fixations'] = main[key]
			new.append(sample)
			count += 1
	if count==0:
		print(key)

print(len(new))

pickle.dump(new,open("rq34.pkl","wb"))

