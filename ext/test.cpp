#include<iostream>
#include<typeinfo>
#include<cstring>
using namespace std;
char* ret(char p[]){
	unsigned len = strlen(p);
	return p;
}
int main(){
	char p[] = "abc";
	cout<<ret(p)<<endl;
	return 0;
}
