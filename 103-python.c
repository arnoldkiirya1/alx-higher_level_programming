#include <Python.h>

void print_python_list(PyObject *p) {
    Py_ssize_t size, i;
    PyListObject *list;

    if (!PyList_Check(p)) {
        printf("[.] Invalid List Object\n");
        return;
    }

    size = PyList_Size(p);
    list = (PyListObject *)p;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", list->allocated);

    for (i = 0; i < size; i++) {
        PyObject *element = PyList_GetItem(p, i);
        const char *type = Py_TYPE(element)->tp_name;

        printf("Element %ld: %s\n", i, type);
    }
}

void print_python_bytes(PyObject *p) {
    Py_ssize_t size, i;
    PyBytesObject *bytes;

    if (!PyBytes_Check(p)) {
        printf("[.] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_Size(p);
    bytes = (PyBytesObject *)p;

    printf("[.] bytes object info\n");
    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", PyBytes_AsString(p));

    printf("  first %ld bytes:", size + 1);
    for (i = 0; i <= size; i++) {
        printf(" %.2x", bytes->ob_sval[i] & 0xff);
    }
    printf("\n");
}
void print_python_float(PyObject *p) {
    PyFloatObject *float_obj;

    if (!PyFloat_Check(p)) {
        printf("[.] Invalid Float Object\n");
        return;
    }

    float_obj = (PyFloatObject *)p;

    printf("[.] float object info\n");
    printf("  value: %f\n", float_obj->ob_fval);
}
