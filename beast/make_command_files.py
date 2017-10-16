import glob

cmdfiles = ['beastjob{}.sh'.format(i) for i in range(1,17)]

xmlfiles = [f for f in glob.glob('*.xml')]

beast_calls = []
for i in range(1,5):
    for xml in xmlfiles:
        command = "beast -overwrite -prefix chain{} {}".format(i,xml)
        beast_calls.append(command)

for cmdfile,call in zip(cmdfiles,beast_calls):
    with open(cmdfile, 'w') as file:
        file.write('#!/bin/bash' + '\n\n')
        file.write(call)
