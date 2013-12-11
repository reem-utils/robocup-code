all: ehbsw_if_py.i ehbsw_if_py.cpp ehbsw.hpp
	swig -c++ -python -o ehbsw_if_py_wrap.cpp ehbsw_if_py.i
	g++ -shared -fPIC -O3 -o _ehbsw.so ehbsw_if_py.cpp ehbsw_if_py_wrap.cpp -I/usr/include/python2.7 -L/usr/lib/python2.7/config -lm #-lpthread -ldl -lutil -lm -lpython2.7
