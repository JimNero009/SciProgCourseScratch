// Implement matrix 

#include "matrix.h"
#include <iostream>

mymatrix::mymatrix(int rows, int cols)
{
	nrows = rows;
	ncols = cols;
        data = new float [nrows*ncols];
};

mymatrix::~mymatrix()
{
	delete [] data;
};


void mymatrix::set_val(int i, int j, float value)
{
  data[i*ncols + j] = value;
};

float mymatrix::get_val(int i, int j)
{
  return data[i*ncols + j];
};

int mymatrix::get_row_size()
{
  return nrows;
};

int mymatrix::get_col_size()
{
  return ncols;
};

// Copy constructor
mymatrix::mymatrix(const mymatrix &obj)
{
  ncols = obj.ncols;
  nrows = obj.nrows;
  data = new float [nrows*ncols];
  for(int i=0; i<nrows; i++){
    for(int j=0; j<ncols; j++){
      data[i*ncols + j] = obj.data[i*ncols + j];
    }
  }
};


mymatrix& mymatrix::operator=(const mymatrix& obj){
  ncols = obj.ncols;
  nrows = obj.nrows;
  data = new float [nrows*ncols];
  for(int i=0; i<nrows; i++){
    for(int j=0; j<ncols; j++){
      data[i*ncols + j] = obj.data[i*ncols + j];
    }
  }
  return *this;
};

mymatrix& mymatrix::operator*(const mymatrix& obj){
  if(ncols != obj.ncols || nrows != obj.nrows){
    std::cerr << "Incompatible matrix types!" << std::endl;
      }
  else{
    float sum=0;
    float temp[ncols*nrows];
    for(int i=0; i<nrows; i++){
      for(int k=0; k<ncols; k++){
	for(int j=0; j<ncols; j++){
	sum += data[i*ncols + j]*obj.data[j*ncols + k];
	}
	temp[i*ncols + k] = sum;
	sum = 0;
      }
    }

    for(int i=0; i<nrows; i++){
	for(int j=0; j<ncols; j++){
	  data[i*ncols + j] = temp[i*ncols + j];
	}
      }
    
    return *this;
  }
};
