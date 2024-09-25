import os
import csv
import pickle

calldir ="Callgraph/"

flist = os.listdir(calldir)

new = dict()

for f in flist:
	if f.split(".")[-1] != "csv":
		continue

	project = f.split(" ")[0]
	cgraph = f.split(" ")[-1].replace(".csv","")
	
	fname = calldir+f
	pname =project+"_"+cgraph
	new[pname] = list()
	with open(fname) as f:
		reader = csv.DictReader(f)
		records = [row for row in reader]
		paths = {a:[] for a in records[0].keys()}
		for row in records:
			for key,value in row.items():
				if value != "":
					paths[key].append(value)
		
		new[pname] = paths

pickle.dump(new,open("callgraph_context.pkl","wb"))
			
