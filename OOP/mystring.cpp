#include <cstring>
#include <vector>
#include <iostream>
#include <string>
class MyString{
private:
	char *_data;
	size_t _len;
	void _init_data(const char *s){
		_len = strlen(s);
		_data = new char[_len+1];
		memcpy(_data, s, _len);
		_data[_len] = '\0';
	}
public:
	MyString():_data(nullptr), _len(0){std::cout<<"basic constructor"<<std::endl;};
	MyString(const char *p){
		std::cout<<"basic constructor"<<std::endl;
		_init_data(p);
	}
	MyString(const MyString &p){
		std::cout<<"copy constructor"<<std::endl;
		_init_data(p._data);
	}
	MyString(MyString &&p){
		std::cout<<"move constructor"<<std::endl;
		_len = p._len;
		_data = p._data;
		_len = 0;
		_data = nullptr;
	}
	MyString & operator=(const MyString &str){
		if(this != &str){
			_init_data(str._data);
		}
		std::cout<<"copy assignment"<<std::endl;
		return *this;
	}
	MyString & operator=(MyString &&str){
		if(this != &str){
			_len = str._len;
			_data = str._data;
			str._len = 0;
			str._data = nullptr;
		}
		std::cout<<"move assignment"<<std::endl;
		return *this;
	}
	virtual ~MyString(){
		if(_data) free(_data);
		std::cout<<"destructor"<<std::endl;
	}
};
template <typename T> void Lswap(T &a, T &b){
	T tmp(a);
	a = b;
	b = tmp;
}
template <typename T> void Rswap(T &a, T &b){
	T tmp(std::move(a));
	a = std::move(b);
	b = std::move(tmp);
}
int main() { 
	std::cout<<"----move assignment----"<<std::endl;
	MyString a; 
	a = MyString("Hello"); 
	std::cout<<"----move constructor----"<<std::endl;
	MyString b(MyString("World"));
	std::vector<MyString> vec; 
	vec.push_back(MyString("World")); 
	std::cout<<"----move assignment----"<<std::endl;
	Lswap(a,b);
	Rswap(a,b);
	return 0;
}