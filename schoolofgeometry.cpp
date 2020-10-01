#include <iostream>
#include <algorithm>
#include <vector>
#include <iterator>

using namespace std;

int main() {
	int i,t;
	long int n;
	long long int j,temp,d,sum;
	cin>>t;
	for (i=0;i<t;i++) {
		cin>>n;
		vector<long long int> a, b, t;
		sum=0;
		
		for(j=0;j<n;j++) {
			cin>>temp;
			a.push_back(temp);
		}
		
		for(j=0;j<n;j++) {
			cin>>temp;
			b.push_back(temp);
		}
		
		int k = sizeof(a)/sizeof(a[0]);
		
		sort(a.begin(), a.end());
		sort(b.begin(), b.end());
		
		if(b[n-1]>a[n-1]) {
			t=b;
			b=a;
			a=t;
		}
		
		auto it = lower_bound(a.begin(), a.end(), b[n-1]);
		temp=*it;
		
		reverse(a.begin(),a.end());
		reverse(b.begin(),b.end());
		
		auto it2 = find(a.begin(), a.end(), temp);

		d = distance(a.begin(), it2);
		//cout<<d<<endl;
		
		for( j=0;j<=d;j++)
			sum+=b[j];
		
		for(j=d+1;j<n;j++)
			sum += min(a[j], b[j]);
		
		cout<<sum<<"\n";
	
	}
	return 0;
}