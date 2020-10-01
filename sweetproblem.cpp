#include <iostream>
using namespace std;

int main() {
	int i,j;
	long int k,t;
	cin>>t;
	long long int temp,a[3],count=0,sum;
	for (k=0; k<t ;k++) {
		count=0,sum=0;
		for(j=0;j<3;j++) {
			cin>>a[j];
		}
		
		if(a[0] != 1 && a[1] != 1 && a[2] != 1) {
			sum = a[0]+a[1]+a[2];
			count=sum/2;
		}
		
		else {
		for(i=0;i<3;i++) {
			for(j=0;j<3;j++) {
				if(a[j]<a[i]) {
					temp=a[j];
					a[j]=a[i];
					a[i]=temp;
				}
			}
		}
		
		while(a[0]+a[1]!=0 && a[1]+a[2]!=0 && a[2]+a[0]!=0) {
			if(a[0]!=0 && a[1]!=0 && a[0]!=a[1]) {
				a[0]--;
				a[1]--;
				count++;
			}
			else if(a[1]!=0 && a[2]!=0 && a[1]!=a[2]) {
				a[1]--;
				a[2]--;
				count++;
			}
			else if(a[2]!=0 && a[0]!=0) {
				a[2]--;
				a[0]--;
				count++;
			}
			else break;
		}
		}
		cout<<count<<endl;
	}
	return 0;
}