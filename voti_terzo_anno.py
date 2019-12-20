#possible grades for exam in order to graduate with laude
exams={'quantistica':12, 'elettronica':6,'astrofisica':6,'lab particelle':8,
'particelle':8,'struttura':8}
#bound
s=28.8163*120
def bound(grades):
    sum=s
    for i in range(len(exams.values())):
        sum+=exams.values()[i]*grades[i]
    sum/=168
    sum*=11
    sum/=3
    sum+=6
    sum=round(sum)
    print(sum)
    print(grades)
    if(sum>110):
        return True
    else:
        return False

"""if __name__=='__main__':
    grades=[30,23,30,30,30,28]
    print(bound(grades))

    #grades basis
    grades_b=[18,18,18,18,18,18]
    i=0
    while(not bound(grades_b)):
        grades_b[i]+=1
        if i!=5:
            i+=1
        else:
            i=0"""

#how to calculate every possible combination?
#6 loop is too long to write
#using an iterative function

def b(grades):
    s=0
    for i in grades:
        s+=i
    print(s)

def recursive(grades,i):
    #grades is the list of grades and i is the i-th element that will be changed
    for j in range(18,31):
        grades[i]=j
        b(grades)
        if i!=len(grades)-1:
            recursive(grades,i+1)

g=[18,18,18]
i=0
recursive(g,i)

"""#let each grade vary from 18 to 30
for i in range(18,30):
    for """
