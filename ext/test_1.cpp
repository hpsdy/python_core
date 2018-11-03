#include<iostream>
#include<typeinfo>
#include<cstring>
using namespace std;
int main(){
	char p[] = "abc";
	unsigned len = strlen(p);
	cout<<"len:"<<len<<endl;
	char b[len];
	b[0] = 'a';
	cout<<"b:"<<b<<endl;
	return 0;
}
