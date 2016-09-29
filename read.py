from collections import defaultdict

def url():
	counts = [0 for x in range(15)]
	count = 0
	inp = "paths.txt"
	with open(inp) as f:
		for line in f:
			count += 1
			i,temp = 0,0
			while i < len(line):
				if line[i] == "/":
					temp += 1
				i += 1
			counts[temp] += 1		

	print count
	print counts
	print sum(j for j in counts)

def UniqueCourse():
	courses = set()
	inp = "course_id.txt"
	with open(inp) as f:
		for line in f:
			courses.add(line)
	print len(courses)

	out = "new.txt"
	f = open(out, 'w')
	for i in courses:
		f.write(i)

def courseCount():
	courses = defaultdict(int)
	inp = "course_id.txt"
	with open(inp) as f:
		for line in f:
			courses[line] += 1
	out = "Course_Frequency.txt"
	out_f = open(out,'w')
	out_f.seek(0)
	for k,v in courses.iteritems():
		final = str(k).rstrip("\n") + " ----> " + str(v) + '\n'
		out_f.write(final) 

def url2():
	courses = set()
	internal = set()
	misc = set()
	inp = "paths.txt"
	with open(inp) as f:
		for line in f:
			if line[1] == "c":
				courses.add(line)
			elif line[1] =="i":
				internal.add(line)

	print "Course Content: ", len(courses)
	print "Internal - Attachements: ", len(internal)
	print "Total Unique: ", len(courses) + len(internal) 

def url3():
	prepArea = set()
	copyCourses = set()
	inp = "paths.txt"
	with open(inp) as f:
		for line in f:
			if "Prep" in line:
				prepArea.add(line)
			if "COPY" in line:
				copyCourses.add(line)
	print "Prep Areas Videos", len(prepArea)
	print "Copy Courses Videos", len (copyCourses)

def urlID():
	blogs = set()
	studentAttempts = set()
	db = set()
	wikis = set()
	inp = "paths.txt"
	with open(inp) as f:
		for line in f:
			if "blog" in line:
				blogs.add(line)
			elif "attempt" in line:
				studentAttempts.add(line)
			elif "db" in line:
				db.add(line)
			elif "wikis" in line:
				wikis.add(line)

	print "Blogs:", len(blogs)
	print "Attempts:", len(studentAttempts)
	print "In DB", len(db)
	print "Wikis", len(wikis)

	print "Wrting to file"

	out = "Blogs.txt"
	out_f = open(out,'w')
	for i in blogs:
		out_f.write(i)

	out2 = "Attemps.txt"
	out2_f = open(out2,'w')
	for i in blogs:
		out2_f.write(i)



url()
UniqueCourse()
courseCount()
url2()
url3()
urlID()