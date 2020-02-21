# <kMeansClustering name="Joyson" rollNo=8390 />

import math
l=[]
c1=[]
c2=[]
while(1) :
	print("1) Enter data point \n2) Calculate clusters\n3) Exit");
	choice = int(input())
	if choice == 1 :
		l1 = [int (a) for a in input().strip().split(",")]
		l.append(l1)
	elif choice == 2 :
		l = sorted(l, key = lambda k : [k[0], k[1]])
		#print(l)
		curr_diff=[]
		cc1 = l[0]
		cc2 = l[-1]
		while(1):
			c1_new = []
			c2_new = []
			for i in range (len(l)) :
				distance1 = math.sqrt(sum([(a-b)**2 for a,b in zip(cc1, l[i])]))
				distance2 = math.sqrt(sum([(a-b)**2 for a,b in zip(cc2, l[i])]))
				if distance1 <= distance2 :
					c1_new.append(l[i])
				else : 
					c2_new.append(l[i])
			if c1_new==c1 and c2_new==c2 :
				print("Cluster centres are ",cc1," and ",cc2,"\nClusters are", c1," and ",c2,"\n")
				break
			else :
				c1=c1_new
				c2=c2_new
				sum1 = 0
				sum2 = 0
				ele = 0
				for j in c1:
					sum1 = sum1+j[0]
					sum2 = sum2+j[1]
					ele = ele + 1
				cc1 = [sum1/ele, sum2/ele]
				sum1 = 0
				sum2 = 0
				ele = 0
				for j in c2:
					sum1 = sum1+j[0]
					sum2 = sum2+j[1]
					ele = ele + 1
				cc2 = [sum1/ele, sum2/ele]
					
				
	elif choice == 3 :
		break
	else : print("Invalid choice, enter again\n")

'''	
1) Enter data point
2) Calculate clusters
3) Exit
1
11,11
1) Enter data point
2) Calculate clusters
3) Exit
1
3,1
1) Enter data point
2) Calculate clusters
3) Exit
1
11,12
1) Enter data point
2) Calculate clusters
3) Exit
1
10,10
1) Enter data point
2) Calculate clusters
3) Exit
1
8,9
1) Enter data point
2) Calculate clusters
3) Exit
1
2,2
1) Enter data point
2) Calculate clusters
3) Exit
1
2,3
1) Enter data point
2) Calculate clusters
3) Exit
1
1,1
1) Enter data point
2) Calculate clusters
3) Exit
2
Cluster centres are  [2.0, 1.75]  and  [10.0, 10.5]
Clusters are [[1, 1], [2, 2], [2, 3], [3, 1]]  and  [[8, 9], [10, 10], [11, 11], [11, 12]]
'''