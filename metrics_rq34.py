import pickle
from statistics import  mean

dats = pickle.load(open("separated_context.pkl","rb"))

projects = {'scrimage':[],'mltk':[],'mallet':[],'openaudible':[],'freecol':[]}

sessions = {1:[],2:[],3:[],4:[],5:[]}

methods = {1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[]}

participants = {1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[],10:[]}

#offset participant id by -2




def getavgs(allvals):
	norm_class=list() 
	norm_decl=list()
	norm_call=list()
	norm_file=list()
	norm_project=list()
	for session in allvals:		
		cl=sum(session['duration_class'])
		decl=sum(session['duration_class_decl'])
		call=sum(session['duration_call'])
		file=sum(session['duration_file'])
		project=sum(session['duration_project'])

		total = cl+decl+call+file+project	
		if cl != 0:
			norm_class.append(cl/total)
		else:
			norm_class.append(0)
		if decl != 0:
			norm_decl.append(decl/total)
		else:
			norm_decl.append(0)
		if call != 0:
			norm_call.append(call/total)
		else:
			norm_call.append(0)
		if file != 0:
			norm_file.append(file/total)
		else:
			norm_file.append(0)
		if project != 0:
			norm_project.append(project/total)
		else:
			norm_project.append(0)
		
	print(mean(norm_class))
	print(mean(norm_decl))
	print(mean(norm_call))
	print(mean(norm_file))
	print(mean(norm_project))
				


for sample in dats:
	if sample['project'] == 'srcimage':
		sample['project'] = 'scrimage'

	projects[sample['project']].append({key:value for key,value in sample.items() if 'duration_' in key})
	sessions[int(sample['session'])].append({key:value for key,value in sample.items() if 'duration_' in key})
	methods[int(sample['method'])].append({key:value for key,value in sample.items() if 'duration_' in key})
	participants[int(sample['participant'])-2].append({key:value for key,value in sample.items() if 'duration_' in key})


for project in projects:
	print("--------------------Project-wise----------------------")
	print(project)
	getavgs(projects[project])
	print("---------------------------")


for method in methods:
	print("-------------------Method-wise------------------------")
	print(method)
	getavgs(methods[method])
	print("---------------------------")


for participant in participants:
	print("-------------------Participant-wise-------------------")
	print(participant)
	getavgs(participants[participant])
	print("---------------------------")

for session in sessions:
	print("-----------------Session-wise----------------------")
	print(session)
	getavgs(sessions[session])
	print("----------------------------")
