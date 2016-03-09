// Simple test program

#include "vector.h"
#include <iostream>

int main()
{
	mymatrix M(2,2);
	M.set_val(0,0,3.14);
	M.set_val(0,1,25.);
	M.set_val(1,0,7.);
	M.set_val(1,1,1);
	std::cout << "Value test:" <<std::endl;
	std::cout << M.get_val(0,0) <<std::endl;
	std::cout << M.get_val(0,1) <<std::endl;
	std::cout << M.get_val(1,0) <<std::endl;
	std::cout << M.get_val(1,1) <<std::endl;
	mymatrix N(M);
	std::cout << "Copy test:" <<std::endl;
	std::cout << N.get_row_size() << std::endl;
	std::cout << N.get_col_size() << std::endl;
	std::cout << N.get_val(0,0) <<std::endl;
	std::cout << N.get_val(0,1) <<std::endl;
	std::cout << N.get_val(1,0) <<std::endl;
	std::cout << N.get_val(1,1) <<std::endl;
	mymatrix X(2,2),Y(2,2);
	std::cout << "Equal test: " <<std::endl;
	X=Y=M;
	std::cout << X.get_row_size() << std::endl;
	std::cout << X.get_col_size() << std::endl;
	std::cout << X.get_val(0,0) <<std::endl;
	std::cout << X.get_val(0,1) <<std::endl;
	std::cout << X.get_val(1,0) <<std::endl;
	std::cout << X.get_val(1,1) <<std::endl;
	std::cout << Y.get_row_size() << std::endl;
	std::cout << Y.get_col_size() << std::endl;
	std::cout << Y.get_val(0,0) <<std::endl;
	std::cout << Y.get_val(0,1) <<std::endl;
	std::cout << Y.get_val(1,0) <<std::endl;
	std::cout << Y.get_val(1,1) <<std::endl;
	std::cout << "Multiplication test:" <<std::endl;
        mymatrix A(2,2), B(2,2), C(2,2);
	A.set_val(0,0,1);
	A.set_val(0,1,2);
	A.set_val(1,0,3);
	A.set_val(1,1,4);
	B.set_val(0,0,5);
	B.set_val(0,1,6);
	B.set_val(1,0,7);
	B.set_val(1,1,8);
	C = A*B;
	std::cout << C.get_val(0,0) <<std::endl;
	std::cout << C.get_val(0,1) <<std::endl;
	std::cout << C.get_val(1,0) <<std::endl;
	std::cout << C.get_val(1,1) <<std::endl;
	std::cout << "END OF MATRIX TEST. VECTOR TEST BEGINS" << std::endl;
	return 0;
}
