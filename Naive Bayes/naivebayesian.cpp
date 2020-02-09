// <NaiveBayes rollNo=8390 name='Joyson' /> 

#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <iterator>
#include <map>

using namespace std;

auto countFreq(vector<string> vect, int n) {
	map<string, float> mp;
	
	for(auto x : vect)
		mp[x]++;

	return mp;
}

int main() {
	int n,m,i,j,e;
	string temp,temp1,temp2;
	cout<<"Enter number of tuples\n";
	cin>>n;
	cout<<"Enter number of attributes\n";
	cin>>m;
	
	vector<string> b, newtuple, classes, raw_list;
	vector<float> probabilities;
	map<string, float> frequency, prob_match;
	vector<vector<string>> a;
	a.resize(n);
	for(i=0; i<a.size(); i++)
		a[i].resize(m);
	
	cout<<"Enter attribute labels (Restrict label names within 7 alphabets)\n";
	for(i=0;i<m;i++) {
		cin>>temp;
		b.push_back(temp);
	}
	
	
	for(i=0;i<n;i++) {
		cout<<"Enter tuple "<<i+1<<" (Restrict attribute values within 7 alphabets) \n";
		for(j=0;j<m;j++) {
			cin>>temp;
			a[i][j]=temp;
		}
	}
	
	cout<<"\n\n||\t\t||";
	for(i=0;i<m;i++) {
		cout<<"\t"<<b[i]<<"\t||";
	}
	cout<<"\n";
	for(i=0;i<20*m;i++)
		cout<<"_";
	cout<<"\n";
	
	for(i=0;i<n;i++) {
		cout<<"||\t"<<i+1<<"\t||";
		for(j=0;j<m;j++) {
			cout<<"\t"<<a[i][j]<<"\t||";
		}
		cout<<"\n";
	}
	
	cout<<"\n\nEnter new tuple to be classified (Restrict attribute values within 7 alphabets) \n";
	for(i=0;i<m-1;i++) {
		cin>>temp;
		newtuple.push_back(temp);
	}
	
	for(i=0;i<n;i++) {
		temp = a[i][n-1];
		bool present = binary_search(classes.begin(), classes.end(), temp);
		if(!present)
			classes.push_back(temp);
	}
	
	for(i=0;i<n;i++) {
		for(j=0;j<m;j++) {
			raw_list.push_back(a[i][j]);
		}
	}
	
	e = sizeof(raw_list)/sizeof(raw_list[0]);
	frequency = countFreq(raw_list, e);
	
	for(auto x : classes) {
		float prod = 1;
		for(auto y : newtuple) {
			float count = 0;
			for( auto z : a) {
				bool contains1 = 0, contains2 = 0;
				if(std::find(z.begin(), z.end(), x)!=z.end())
					contains1 = 1;
				if(std::find(z.begin(), z.end(), y)!=z.end())
					contains2 = 1;
				if(contains1 && contains2)
				{
					count++;
				}
			}
			prod = prod * ((float)count/(float)frequency[x]);
		}
		prod = prod * ((float)frequency[x]/(float)n);
		prob_match[x]=prod;
	}
	
	float sum = 0;
	for (auto x : prob_match)
		sum+=x.second;
	
	for (auto &x : prob_match)
		x.second = x.second/sum;
	
	for(auto x : prob_match)
		cout<<"\n"<<x.first<<" : "<<x.second*100<<"%"<<endl;
	
	return 0;
}



/*
Enter number of tuples                                                                            
5                                                                                                 
Enter number of attributes                                                                        
5                                                                                                 
Enter attribute labels (Restrict label names within 7 alphabets)                                  
Outlook Temp Humidty Windy Play                                                                   
Enter tuple 1 (Restrict attribute values within 7 alphabets)                                      
Rainy Hot High False No                                                                           
Enter tuple 2 (Restrict attribute values within 7 alphabets)                                      
Rainy Hot High True No                                                                            
Enter tuple 3 (Restrict attribute values within 7 alphabets)                                      
Ovrcast Hot High False Yes                                                                        
Enter tuple 4 (Restrict attribute values within 7 alphabets)                                      
Sunny Mild High False Yes                                                                         
Enter tuple 5 (Restrict attribute values within 7 alphabets)                                      
Sunny Cool Normal False Yes                                                                       
                                                                                                  
                                                                                                  
||      ||  Outlook ||  Temp  ||  Humidty ||  Windy  ||  Play  ||
_________________________________________________________________
||  1   ||  Rainy   ||  Hot   ||  High    ||  False  ||  No    ||
||  2   ||  Rainy   ||  Hot   ||  High    ||  True   ||  No    ||
||  3   ||  Ovrcast ||  Hot   ||  High    ||  False  ||  Yes   ||
||  4   ||  Sunny   ||  Mild  ||  High    ||  False  ||  Yes   ||
||  5   ||  Sunny   ||  Cool  ||  Normal  ||  False  ||  Yes   ||
                                                                                                  
                                                                                                  
Enter new tuple to be classified (Restrict attribute values within 7 alphabets)                   
Rainy Hot High True                                                                               
                                                                                                  
No : 100%                                                                                         
                                                                                                  
Yes : 0% 
*/                                                                                         