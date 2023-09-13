#include <Python.h>
#include <object.h>
#include <listobject.h>

void print_python_list_info(PyObject *p)
{
	long int size = PyList_Size(p);
	unsigned int count;
	PyListObject *obj = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", obj->allocated);
	for (count = 0; count < size; count++)
		printf("Element %u: %s\n", count, Py_TYPE(obj->ob_item[count])->tp_name);
}
