oldheight_newheight = {}
with open('./oldheight_newheight.csv', 'r') as f:
	for line in f:
		line=line.strip('\n')
		oldheight_newheight[line.split(',')[0]] = [line.split(',')[1],''.join(line.split(',')[2][0:10].split('-'))]

print oldheight_newheight.keys()[:30]
import sys
filename =sys.argv[1]
print filename
to_write = []
with open('./'+filename,'r') as f, open('/mnt/revised_'+filename,'w') as wf:
	for line in f:
                line = line.strip('\n')
		line = line.split(',')
		wf.write(','.join([oldheight_newheight[line[0]][0]]+ line[1:]+[oldheight_newheight[line[0]][1]])+'\n')

print 'finished' + filename
