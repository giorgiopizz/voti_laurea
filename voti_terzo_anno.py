from time import sleep
#possible grades for exam in order to graduate with laude
exams={'quantistica':12, 'elettronica':6,'astrofisica':6,'lab particelle':8,
'particelle':8,'struttura':8}
#number of steps
n=0
#bound
s=28.8163*120
#define some reasonable bounds for each exams
exams_bounds=[[25,30],[20,28],[23,30],[28,30],[28,30],[24,30]]
#exams_bounds=[[29,30],[29,30],[29,30],[29,30],[29,30],[29,30]]
#exams_bounds=[[25,30],[25,30],[25,30]]


difficulties=[5,6,5,3,3,6]

rank_min=10**10

def bound(grades):
    sum=s
    global n
    global rank_min
    #rank indicates how difficult the strike is, lower is better
    rank=0
    for i in range(len(exams.values())):
        sum+=exams.values()[i]*grades[i]
        rank+=difficulties[i]*grades[i]
    sum/=168
    sum*=11
    sum/=3
    sum+=6
    n+=1
    sum=round(sum)
    if(sum>110):
        if(rank<rank_min):
            rank_min=rank
            #save in the file
            with open("voti.txt","w") as file:
                file.write("{}\n{}\nVoto:{}\nRank:{}".format(n,grades,sum,rank))
        
        print("{}\n{}\nVoto:{}\nRank:{}".format(n,grades,sum,rank))
        return True
    else:
        return False

def recursive(grades,i):
    #grades is the list of grades and i is the i-th element that will be changed
    for j in range(exams_bounds[i][0],exams_bounds[i][1]+1):
        #sleep(0.1)
        
        grades[i]=j
        if i!=len(grades)-1:
            recursive(grades,i+1)
        else:
            bound(grades)

if __name__=='__main__':
    #grades=[30,23,30,30,30,28]
    #print(bound(grades))
    #grades basis
    #lets set the initial grades
    grades_b=[]
    for i in exams_bounds:
        grades_b.append(i[0])
    #grades_b=[exams_bounds[0][0],exams_bounds[1][0],exams_bounds[2][0]]   
    recursive(grades_b,0)
    print("\n\nFinito\n\n")
    with open("voti.txt","r") as file:
        print(file.read())
    #how to calculate every possible combination?
    #6 loop is too long to write
    #using an iterative function
