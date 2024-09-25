import pickle
import sqlite3
import os

def fixations(fname):
	sqliteConnection = sqlite3.connect(fname)

	cursor = sqliteConnection.cursor()

	cursor.execute('SELECT * from fixation')

	desc = cursor.description

	col_names = [col[0] for col in desc]

	data = [dict(zip(col_names, row))for row in cursor]

	sqliteConnection.close()
	
	return data





alldb = [os.path.join(root, name)
             for root, dirs, files in os.walk(".")
             for name in files
             if name.endswith(".db3")]

final = dict()
for fname in alldb:
	sample = fname.split("/")[-1].replace(".db3","")
	try:
		final[sample] = fixations(fname)
	except:
		print(fname)

pickle.dump(final,open("fixations.pkl","wb"))
