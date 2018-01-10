/*
Implement a class for rational numbers(defined as the ratio between two integers)
need following members:
+
-
*
/
>>
<<
*/
//http://en.cppreference.com/w/cpp/language/operators
#include <iostream>
#include <string>
#include <cstring>
class Rational
{
private:
	int num;
	int div;
public:
	/*basic initialization methods*/
	Rational():num(0), div(1){std::cout<<"basic@1"<<std::endl;};
	Rational(int x):num(x), div(1){std::cout<<"basic@2"<<std::endl;};
	Rational(int x, int y):num(x), div(y){std::cout<<"basic@3"<<std::endl;};
	/*constructors*/
	/*copy constructor*/
	Rational(const Rational &other);
	/*move constructor*/
	Rational(Rational &&other);
	~Rational(){
		std::cout<<"Destructor"<<std::endl;
	}
	bool operator ==(const Rational &other) const;
	bool operator >(const Rational &other) const;
	bool operator <(const Rational &other) const;
	/*no-init equalization
	no need for rval ref here
	interpreter will automatically move with rvalue and copy with lvalue
	*/
	Rational & operator=(Rational other);
	friend std::ostream & operator << (std::ostream &os, const Rational &r);
};
Rational::Rational(const Rational &other){
	std::cout<<"copy constructor"<<std::endl;
	num = other.num;
	div = other.div;
}
Rational::Rational(Rational &&other){
	std::cout<<"move constructor"<<std::endl;
	num = other.num;
	div = other.div;
}
Rational & Rational::operator =(Rational other){
	std::cout<<"operator ="<<std::endl;
	std::swap(other.num, num);
	std::swap(other.div, div);
	return *this;
}
bool Rational::operator ==(const Rational &other) const{
	return num*other.div == div*other.num;
}
bool Rational::operator >(const Rational &other) const{
	return num*other.div > div*other.num;
};
bool Rational::operator <(const Rational &other) const{
	return num*other.div < div*other.num;
};
std::ostream & operator << (std::ostream &os, const Rational &r){
	os<<"Rational"<<"("<<r.num<<'/'<<r.div<<")";
	return os;
}

Rational temporaryRational(){
	return Rational(9,8);
}
int main(){
	std::cout<<"----constructer----"<<std::endl;
	Rational A;
	std::cout<<A<<std::endl;
	Rational B(1);
	std::cout<<B<<std::endl;
	Rational C(3,2);
	std::cout<<C<<std::endl;
	std::cout<<"----copy constructer----"<<std::endl;
	Rational D(C);
	std::cout<<D<<std::endl;
	Rational E = B;
	std::cout<<E<<std::endl;
	std::cout<<"----move constructer----"<<std::endl;
	// Rational F(temporaryRational());
	Rational F(temporaryRational());
	std::cout<<F<<std::endl;
	std::cout<<"----operators----"<<std::endl;
	F = A;
	std::cout<<F<<std::endl;

	return 0;
}