#include<cstring>
#include<iostream>
#include<cstddef>
#include "/usr/include/python3.4m/Python.h"
using namespace std;
int fac(int n){
	if (n<2){
		return 1;
	}
	return (n)*fac(n-1);
}
char* rex(char *str){
	char *sp = str;		
	size_t len = strlen(str);
	char *ep = sp+len-1;
	while(sp<ep){
		char *tmp = sp;
		*sp = *ep;
		*ep = *tmp;
		ep--;;
		sp++;
	}
	return str;
}
int main(){
	char strs[] = "abcde";
	char back[strlen(strs)+1];
	strcpy(back,strs);
	cout<<fac(5)<<endl;	
	cout<<rex(strs)<<"\t"<<back<<endl;	
	return 0;
}
