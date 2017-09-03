import glob
import json

for f in glob.glob("*") :
	if "json" in  f or "JSON" in f or "Json" in f:
		with open(f) as fhandle:
			try:
				print f
				fp = fhandle.read()
				json.loads(fp)
				print "Valid JSON !!"
			except Exception as e:
				print e
