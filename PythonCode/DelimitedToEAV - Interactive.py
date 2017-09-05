#!/usr/bin/python3
import os.path
import sys
# if linux/unix - might work with OS X too dont know
if not sys.platform.startswith("win"):
    pathSeparator = "/"
# if windows   
else:
    pathSeparator = "\\"

print('Platform is:' + str(sys.platform))
print('Enter the common working path:')
commonPath = input() 
print('Enter the source folder:')
sourceFolder = pathSeparator + input() 
print('Enter the output folder:')
outputFolder = pathSeparator + input()
print('Enter the source file delimiter:')
srcDelimiter = input()
print('Enter the destination file delimiter:')
destDelimiter = input()
print('Use CR/LF for new line? Otherwise LF only will be used: (y/n)')
if input() == 'y':
    newLinechars = "\n\r"
else:
    newLinechars = "\n"
print('Working, please wait...')
for filename in os.listdir(commonPath + sourceFolder):
    if filename.endswith('.txt'):
        with open(commonPath + outputFolder + pathSeparator + "EAV_" + filename, mode="w") as dest:
            dest.write("SchemaKey" + destDelimiter + "SourceFilename" + destDelimiter
                       + "RecordID" + destDelimiter + "ColumnID"
                       + destDelimiter + "HeaderColumnName" + destDelimiter + "Value"
                       + newLinechars)
            fullPathFileName = commonPath + sourceFolder + pathSeparator + filename
            with open(fullPathFileName) as f:
                linenum = 0
                for line in f:
                    line = line.strip()
                    colnum = 0
                    columnList = line.split(srcDelimiter)
                    if linenum == 0:
                        schemaKey = ""
                        headers = columnList
                        for hcol in headers:
                            schemaKey = schemaKey + "[" + hcol + "]"
                    for col in columnList:
                        if linenum != 0:
                            columnName = headers[colnum]
                            colnum += 1
                            outstr = (schemaKey + destDelimiter + fullPathFileName.rstrip() + destDelimiter
                                      + str(linenum).strip() + destDelimiter
                                      + str(colnum).strip() + destDelimiter
                                      + columnName.replace(" ", "")
                                      + destDelimiter + (str(col)).rstrip() + newLinechars)
                            dest.write(outstr)
                    linenum += 1
        continue
    else:
        continue
print('Complete')
