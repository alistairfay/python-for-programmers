#lettergrade

pointspossible=99
score=74
studentname="Nick"

'''
A - 100-90%
B - 89-80%
C - 79-70%
D - 69-60%
F - 59-0%
'''

#print the studentname and what grade they got
percent=score/pointspossible*100
print(percent)
print(round(percent))
if 90<=percent<=100:
    grade="A"
elif 80<=percent<=89:
    grade="B"
elif 70<=percent<=79:
    grade="C"
elif 60<=percent<=69:
    grade="D"
elif 0<=percent<=59:
    grade="F"
else:
    grade="BORK"

print("{} - {}".format(studentname, grade))
