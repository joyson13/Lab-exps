# <linkageDistances name="Joyson" rollNo=8390 />

import math

l3=[]
l4=[]
l5=[]
l6=[]

def singleLinkage(x,y,m,n):
	l5=[]
	for i in range(m):
		for j in range(n):
			distance1 = math.sqrt(sum([(a-b)**2 for a,b in zip(x[i], y[j])]))
			l5.append(distance1)
		
	distance = min(l5)
	l5=[]
	print("Single linkage distance between the two clusters is ",distance)

def completeLinkage(x,y,m,n):
	l5=[]
	for i in range(m):
		for j in range(n):
			distance1 = math.sqrt(sum([(a-b)**2 for a,b in zip(x[i], y[j])]))
			l5.append(distance1)
		
	distance = max(l5)
	l5=[]
	print("Complete linkage distance between the two clusters is ",distance)
	
def avgLinkage(x,y,m,n):
	sum1=0
	sum2=0
	for i in x:
		for j in y:
			sum1 += abs(i[0]-j[0])
			sum2 += abs(i[1]-j[1])
	
	sum = math.sqrt(sum1**2+sum2**2)			
	sum = sum/(m*n)
	print("Average linkage distance between the two clusters is ",sum)
	
def centroidLinkage(x,y,m,n):
	sum=0
	sum1=0
	sum2=0
	sum3=0
	sum4=0
	for i in x:
		sum1+=i[0]
		sum2+=i[1]
	sum1=sum1/m
	sum2=sum2/m
		
	for j in y:
		sum3+=j[0]
		sum4+=j[1]
	sum3=sum3/n
	sum4=sum4/n
	sum5 = abs(sum1-sum3)
	sum6 = abs(sum2-sum4)
	sum = math.sqrt(sum5**2+sum6**2)
	print("Centroid linkage distance between the two clusters is ",sum)
	
	
while(1) :
	print("roll no 8390, name = Joyson Gaurea\n1) Enter data clusters\n2) Calculate linkage distances\n3) Exit");
	choice = int(input())
	if choice == 1 :
		print("Enter first cluster")
		u=int(input("Enter number of data points\n"))
		for g in range(u):
			print("Enter data point")
			l1 = [int (a) for a in input().strip().split(",")]
			l3.append(l1)
		print("Enter second cluster")
		v=int(input("Enter number of data points\n"))
		for g in range(v):
			print("Enter data point")
			l2 = [int (a) for a in input().strip().split(",")]
			l4.append(l2)
	elif choice == 2 :
		m = len(l3)
		n = len(l4)
		print("Clusters are ",l3," ",l4)
		singleLinkage(l3,l4,m,n)
		completeLinkage(l3,l4,m,n)
		avgLinkage(l3,l4,m,n)
		centroidLinkage(l3,l4,m,n)									
	elif choice == 3 :
		break
	else : print("Invalid choice, enter again\n")
	
	
	
	
'''
Output1

λ python linkageDistances.py
roll no 8390, name = Joyson Gaurea
1) Enter data clusters
2) Calculate linkage distances
3) Exit
1
Enter first cluster
Enter number of data points
2
Enter data point
1,0
Enter data point
2,0
Enter second cluster
Enter number of data points
3
Enter data point
3,0
Enter data point
4,0
Enter data point
5,0
roll no 8390, name = Joyson Gaurea
1) Enter data clusters
2) Calculate linkage distances
3) Exit
2
Clusters are  [[1, 0], [2, 0]]   [[3, 0], [4, 0], [5, 0]]
Single linkage distance between the two clusters is  1.0
Complete linkage distance between the two clusters is  4.0
Average linkage distance between the two clusters is  2.5
Centroid linkage distance between the two clusters is  2.5


Output2
λ python linkageDistances.py
roll no 8390, name = Joyson Gaurea
1) Enter data clusters
2) Calculate linkage distances
3) Exit
1
Enter first cluster
Enter number of data points
2
Enter data point
1,2
Enter data point
2,3
Enter second cluster
Enter number of data points
3
Enter data point
3,4
Enter data point
4,5
Enter data point
5,6
roll no 8390, name = Joyson Gaurea
1) Enter data clusters
2) Calculate linkage distances
3) Exit
2
Clusters are  [[1, 2], [2, 3]]   [[3, 4], [4, 5], [5, 6]]
Single linkage distance between the two clusters is  1.4142135623730951
Complete linkage distance between the two clusters is  5.656854249492381
Average linkage distance between the two clusters is  3.5355339059327378
Centroid linkage distance between the two clusters is  3.5355339059327378
'''