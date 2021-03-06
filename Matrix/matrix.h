// Header file for custom matrix class

class mymatrix
{
	public:
        void set_val(int, int, float);
	float get_val(int, int);
	int get_row_size();
	int get_col_size();
	mymatrix(int, int);
	~mymatrix();
	mymatrix(const mymatrix&);
	mymatrix& operator=(const mymatrix&);
	mymatrix& operator*(const mymatrix&);

	//private:
	//mymatrix();

        protected:
	int nrows, ncols;
	float *data;
};
