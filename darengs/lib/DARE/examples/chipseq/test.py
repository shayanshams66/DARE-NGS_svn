import sys
input = sys.argv[1]
output = sys.argv[2]
testf = open(input,'r')
lines = testf.readlines()
outf = open(output,'w')
for line in lines:
    new_line = line.replace('CHROMOSOME_','')
    outf.write(new_line)
outf.close()
testf.close()
