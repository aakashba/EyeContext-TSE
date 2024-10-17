import pickle
import random
import os
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-path", "--path", dest = "path")

args = parser.parse_args()

path = args.path

master = pickle.load(open("master.pkl","rb"))

def rfile(x,xnew,project):
	with open(xnew,"w") as newf:
		lines = x.readlines()

		#randomizing order from the 2nd method
		samples = master[project]
		newsam = samples[1:]
		random.shuffle(newsam)
		samples[1:] = newsam

		for line in lines:
			if "Method" in line and ":" in line:
				n = int(line.split(":")[0].split(" ")[1])
				newf.write("\tMethod {}: {}\n".format(n,samples[n-1]))
			
			else:
				newf.write(line)


flist = ["mallet.txt","freecol.txt","scrimage.txt","mltk.txt","openaudible.txt"]


for fl in flist:
	new = os.path.join(path,fl)
	project = fl.split(".")[0]
	with open(fl) as f:
		rfile(f,new,project)


