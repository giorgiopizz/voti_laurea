from time import sleep
#possible grades for exam in order to graduate with laude
exams={'quantistica':12, 'elettronica':6,'astrofisica':6,'lab particelle':8,
'particelle':8,'struttura':8}
#number of steps
n=0
#bound
s=28.8163*120
#define some reasonable bounds for each exams
#exams_bounds=[[25,30],[20,30],[23,30],[25,30],[25,30],[24,30]]
exams_bounds=[[29,30],[29,30],[29,30],[29,30],[29,30],[29,30]]

difficulties=[6,2,5,3,2,6]

def bound(grades):
    sum=s
    #rank indicates how difficult the strike is, lower is better
    rank=0
    for i in range(len(exams.values())):
        sum+=exams.values()[i]*grades[i]
        rank+=difficulties[i]*grades[i]
    sum/=168
    sum*=11
    sum/=3
    sum+=6
    sum=round(sum)
    n+=1
    if(sum>110):
        print("{}\n{}\nVoto:{}\nRank:{}".format(n,grades,sum,rank))
        return True
    else:
        return False

def recursive(grades,i):
    global n
    #grades is the list of grades and i is the i-th element that will be changed
    for j in range(exams_bounds[i][0],exams_bounds[i][1]+1):
        sleep(1)

        grades[i]=j
        bound(grades)
        if i!=len(grades)-1:
            recursive(grades,i+1)

if __name__=='__main__':
    grades=[30,23,30,30,30,28]
    print(bound(grades))

    #grades basis
    grades_b=[18,18,18,18,18,18]
    recursive(grades_b,0)

    #how to calculate every possible combination?
    #6 loop is too long to write
    #using an iterative function
