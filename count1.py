
#for most artest that has more oscars
import csv
from collections import Counter
older = 0 
array = [] 
with open('oscar.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    for line in csv_reader:
            array.append(line[3])
            count = Counter(array) 
csv_file.close()




counter = 0
actor_name = ""
for name , num in count.items():
    if counter < int(num):
        counter = num
        actor_name = name



print(actor_name + " takes oscardddd " +   str(counter) +" times \n\n") 
    
#for oldest  artest 

older=3000
with open ('oscar.csv','r') as f:
    r=csv.reader(f)
    for i in r:
        if older > int(i[1]):
            older =int(i[1])
            w=older
            w2=i[4]
            r=i[3]

print("the mr."+r+"has oldest oscar in year :" +str(w)+" to filme called :"+str(w2))          

f.close()
    

    
              
              
input("press any key to exit")
            
             
        
