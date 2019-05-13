
# function that takes 2 strings s1 and s2
# and returns the longest common sequence
# Ex: "'AGGTAB','GXTXAYB'" -> GTAB
def find_com(x,y):
    word=""
    for i in x:
        if i in y:
            word=word+i
    return(word)

def comp(s1,s2):
    sequence=""
    s1_comm=find_com(s1,s2)
    s2_comm=find_com(s2,s1)
    if len(s1_comm)>len(s2_comm):
        s1_comm,s2_comm=s2_comm,s1_comm
    i=0
    j=0
    print(s1_comm)
    print(s2_comm)
    while(i<len(s1_comm) and j<len(s2_comm)):
        if s1_comm[i] is s2_comm[j]:
            sequence=sequence+s2_comm[j]
            i=i+1
        j=j+1
    print("The largest common string is: {} ".format(sequence))


comp("AGGTAB","GXTXAYB")
comp("ABAZDC","BACBAD")
comp("AAAA","AA")
