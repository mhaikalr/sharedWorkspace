import os
import Issue
import re

filenameNew = ""
filenameOld = "R22_internal_tracking.csv"
pwd = os.path.dirname(os.path.abspath(__file__))

# prepare list of new issues
issuesNew = []
fileNew = open(filenameNew, "r")
headerRow = fileNew.readline()
headerList = headerRow.split(",")
indices = []
indices.append(headerList.index("Issue key"))
indices.append(headerList.index("Summary"))
indices.append(headerList.index("Assignee"))
indices.append(headerList.index("Status"))
for x in fileNew:
	x.strip()
	detailList = x.split(",")
	if len(detailList) < 4:
		print("WRONG LENGTH")
		fileNew.close()
		exit()
	i = Issue.Issue(detailList[indices[0]], detailList[indices[1]], detailList[indices[2]], detailList[indices[3]])
	issuesNew.append(i)
fileNew.close()
issuesNew.pop(0)
# prepare list of new issues

# prepare list of old issues
issuesOld = []
fileOld = open(filenameOld, "r")
for x in fileOld:
	x.strip()
	detailList = x.split(",")
	if len(detailList) < 4:
		print("WRONG LENGTH")
		fileOld.close()
		exit()
	i = Issue.Issue(detailList[0], detailList[1], detailList[2], detailList[3])
	issuesOld.append(i)
fileOld.close()
issuesOld.pop(0)
# prepare list of old issues

