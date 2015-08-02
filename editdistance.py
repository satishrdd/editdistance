import sys
#global etdistance


s1 = raw_input().lower();
s2 = raw_input().lower();



#etdistance=0;
i = len(s1)-1;
j= len(s2)-1;

def substr(string):
    j=1
    a=set()
   # b=set()
    while True:
        for i in range(len(string)-j+1):
            a.add(string[i:i+j])
        
            
        if j==len(string):
            break
        j+=1
        
        #string=string[1:]
    return a






def etd(i,j,etdistance):
        

        if (i+1)==0 or (j+1)==0:
             return(etdistance+ i+j+2);
        elif (i+1)==0 and (j+1)==0:
             return etdistance;
        elif s1[i]== s2[j]:
             return etd(i-1,j-1,etdistance);
        elif s1[i]!=s2[j]:
             l1  = etd(i-1,j,etdistance);
             l2 = etd(i,j-1,etdistance);
             l3 = etd(i-1,j-1,etdistance);
             return 1+min(l1,l2,l3);

       # return(etdistance);


etdistance = etd(i,j,0);











counter = 0;


#print(s1);
print(etdistance);


a= substr(s1);
b = substr(s2);
c= tuple(a)
d= tuple(b)








    
    



