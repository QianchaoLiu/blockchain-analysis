towrite = []
with open('./block.csv', 'r') as f:
    for line_index, line in enumerate(f):
	line = line.strip('\n')
    	line_split = line.split(',')
    	towrite.append(line_split)

oldheight_newheight = []
towrite.sort(key=lambda x:x[4])
with open('./block_reviesd.csv', 'w') as wf:
	for index, item in enumerate(towrite):
		wf.write(','.join([str(index)]+item[1:])+'\n')
		oldheight_newheight.append([item[0],str(index),item[4]])

with open('./oldheight_newheight.csv','w') as wf:
	for item in oldheight_newheight:
		wf.write(','.join(item)+'\n')
