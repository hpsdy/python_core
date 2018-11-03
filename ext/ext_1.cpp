#include<cstring>
#include<cctype>
#include<iostream>
#include "/usr/include/python3.4m/Python.h"
using namespace std;
int fac(int n){
	if (n<2){
		return 1;
	}
	return (n)*fac(n-1);
}
char* rex(char * str){
	unsigned len = strlen(str);
	char *ep = str+len-1;
	while(str<ep){
		char *tmp = str;
		*str = *ep;
		*ep = *tmp;
		str++;
		ep--;
	}
	return str;
}
static PyObject * ext_1_fac(PyObject *self,PyObject *args){
	int num;
	if(!PyArg_ParseTuple(args,"i",&num)){
		return NULL;
	}
	return (PyObject*)Py_BuildValue("i",fac(num));
}
static PyMethodDef ext_1_methods[] = {
	{"fac",(PyCFunction)ext_1_fac,METH_VARARGS},
	{NULL,NULL},
};

static int ext_1_traverse(PyObject *m, visitproc visit, void *arg) {
    return 0;
}

static int ext_1_clear(PyObject *m) {
    return 0;
}


static struct PyModuleDef moduledef = {
        PyModuleDef_HEAD_INIT,
        "ext_1",
        NULL,
        -1,
        ext_1_methods,
        NULL,
        ext_1_traverse,
        ext_1_clear,
        NULL
};


PyMODINIT_FUNC PyInit_ext_1(){
	PyObject *module = PyModule_Create(&moduledef);
	return module;
}
