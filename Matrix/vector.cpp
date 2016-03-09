// Implement vector 

#include "vector.h"
#include <iostream>

myvector::myvector(int rows)
{
  nrows = rows;
  ncols = 1;
  data = new float [nrows];
}
