#include <iostream>
#include <bits/stdc++.h> 
using namespace std; 
  
int main() 
{ 
	int i,j,n,t,flag,c1,c2;
	cin>>t;
	char c;
	string s;
	for(i=0; i<t ; i++) {
		flag=0;
		c1=0;
		c2=0;
		n=0;
		cin>>s;
		for(j=0;j<s.length()-1;j++) {
			if(s[j]==(1-(s[j+1]-'0'))+'0') {
				n++;
			}
		}
		if(n<3)
			cout<<"0"<<endl;
		else {
			for(j=0;j<s.length();j++) {
				if(s[j]=='0')
					c1++;
				else c2++;
			}
			if(c1>c2) {
				for(j=1;j<s.length()-1;j++) {
					if(s[j]=='1' && s[j-1]=='0' && s[j+1]=='0')
						flag++;
				}
			}
			else {
				for(j=1;j<s.length()-1;j++) {
					if(s[j]=='0' && s[j-1]=='1' && s[j+1]=='1')
						flag++;
				}
			}
			cout<<flag<<" "<<c1<<" "<<c2<<endl;
		}
	}	
    return 0; 
}