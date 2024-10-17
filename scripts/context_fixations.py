import pickle

import copy

def startend(xpath,struct):
	s = xpath.split(struct)[-1].split("/")[0]
	s_start = int(s.split("and")[0].split("='")[-1].split(":")[0])
	s_end = int(s.split("and")[-1].split("='")[-1].split(":")[0])
	return s_start,s_end


old = pickle.load(open("rq34.pkl","rb"))
new = list()
for sample in old:
	newsample = copy.deepcopy(sample)
	new.append(newsample)
	new[-1]['fixations'] = list()
	tempdur = list()
	for fixation in sample['fixations']:
		xpath = fixation['xpath']
		file = fixation['fixation_target']
		func_start = 0
		func_end = 0
		class_start = 0
		class_end = 0
		
		if "src:class" in xpath:
			class_start,class_end = startend(xpath,"src:class")
		

		if "src:func" in xpath:
			func_start,func_end = startend(xpath,"src:func")
		elif "src:function" in xpath:
			func_start,func_end = startend(xpath,"src:function")


		duration = fixation['duration']
		record = {'file':file,'class_start':class_start,'class_end':class_end,'func_start':func_start,'func_end':func_end}
		
		if len(new[-1]['fixations']) == 0:
			new[-1]['fixations'].append(record)
			tempdur.append(duration)
			continue

		if new[-1]['fixations'][-1] == record:
			tempdur.append(duration)
		else:                             #accumulate duration till record changes then dump in last one
			new[-1]['fixations'][-1]['duration'] = tempdur
			tempdur = list()
			tempdur.append(duration)
			new[-1]['fixations'].append(record)

	if len(new[-1]['fixations']) > 0:
		if 'duration' not in new[-1]['fixations'][-1].keys():
			new[-1]['fixations'][-1]['duration'] = tempdur    

pickle.dump(new,open("intermediate_context.pkl","wb"))

callcontext = pickle.load(open("callgraph_context.pkl","rb"))

for sample in new:
	path = sample['path'].replace("srcimage","scrimage")
	project = sample['project'].replace("srcimage","scrimage")
	calls = list()
	calls = callcontext[project+"_caller"][path] 
	callee = callcontext[project+"_callee"][path]
	calls.extend(callee)
	call_files = dict()
	for item in calls:
		call_files[item.split(">")[0]] = list()
		call_files[item.split(">")[0]].append(int(item.split(">")[-1]))
	target_file = path.split(">")[-2]
	target_line = int(path.split(">")[-1].split("line")[-1].replace("]",""))
	sample['duration_target'] = list()
	sample['duration_class'] =  list()
	sample['duration_class_decl'] = list()
	sample['duration_file'] = list()
	sample['duration_call'] = list()
	sample['duration_project'] = list()

	for fixation in sample['fixations']:
		if target_file == fixation['file']:
			if fixation['func_start'] <= target_line and fixation['func_end'] >= target_line: # if inside target method
				sample['duration_target'].extend(fixation['duration'])
				continue

			if fixation['class_start'] <= target_line and fixation['class_end'] >= target_line:  #if inside same class
				if fixation['func_end'] != 0:
					sample['duration_class'].extend(fixation['duration'])
				else:
					sample['duration_class_decl'].extend(fixation['duration'])	
			else: 																		 # anything in same file but not in the class is file context
				sample['duration_file'].extend(fixation['duration'])
			
			if fixation['file'] in call_files.keys() and fixation['func_start'] != 0:
				if fixation['func_start'] in call_files[fixation['file']]:
					sample['duration_call'].extend(fixation['duration'])
		
		elif fixation['file'] in call_files.keys() and fixation['func_start'] != 0:
			if fixation['func_start'] in call_files[fixation['file']]:
				sample['duration_call'].extend(fixation['duration'])
		else:
			sample['duration_project'].extend(fixation['duration']) 
			

pickle.dump(new,open("separated_context.pkl","wb"))
