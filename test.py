import random

numbers = [1,2,3,4,5,6,7,8,9]
array = []
col1 = []
col2 = []
col3 = []
row1 = []

#while len(row1) < 9:

while len(col1) < 9:
row = []
c1 = []
c2 = []
c3 = []
while len(c1) < 3:
     r = []
     while len(r) < 3:
               generate = random.choice(numbers)
               if generate not in r and generate not in c1 and generate not in c2 and generate not in c3:
                    r.append(generate)
                    row.append(generate)
     if r not in row:
          if r[0] not in col1 and r[1] not in col2 and r[2] not in col3:
               c1.append(r[0])
               c2.append(r[1])
               c3.append(r[2])

for i,value in enumerate(c1):
     col1.append(c1[i])  
     col2.append(c2[i])     
     col3.append(c3[i])

                                   
for i,value in enumerate(col1):
     print(f"{col1[i]} {col2[i]} {col3[i]}")

     


