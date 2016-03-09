#Import the actual data files
piplusfile = open('pip_p.dat','r')
piminusfile = open('pim_p.dat','r')
#Create a file for output
piplusoutputfile = open('pip_output.dat','w')
piminusoutputfile = open('pim_output.dat','w')

def writeOutput(infile, outfile):
    for line in infile:
         line = line.split()
         ymin = float(line[4]) - float(line[5]) - float(line[7])
         ymax = float(line[4]) + float(line[6]) + float(line[8])
         linestring = "%s %s %s %s %f %f %s" % (line[1], line[4], line[2], line[3], ymin, ymax, "\n")
         outfile.write(linestring)

writeOutput(piplusfile, piplusoutputfile)
writeOutput(piminusfile, piminusoutputfile) 

piplusfile.close()
piminusfile.close()
piplusoutputfile.close()
piminusoutputfile.close()
