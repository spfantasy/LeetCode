#include <cstring>
#include <vector>
#include <iostream>
#include <string>
#include <memory>
class MyString{
private:
	std::unique_ptr<char> _data;
	size_t _len;
	void _init_data(const char *s){
		_len = strlen(s);
		_data = std::unique_ptr<char>(new char[_len+1]);
		memcpy(_data.get(), s, _len);
		_data.get()[_len] = '\0';
	}
public:
	MyString():_data(nullptr), _len(0){std::cout<<"basic constructer"<<std::endl;}
	MyString(const char *p){
		_init_data(p);
		std::cout<<"basic constructor"<<std::endl;
	}
	MyString(const MyString &str){
		_init_data(str._data.get());
		std::cout<<"copy constructor"<<std::endl;
	}
	MyString(MyString &&str){
		std::swap(_data, str._data);
		std::swap(_len, str._len);
		std::cout<<"move constructor"<<std::endl;
	}
	MyString & operator=(const MyString &str){
		if(this != &str){
			_init_data(str._data.get());
		}
		std::cout<<"copy assignment"<<std::endl;
		return *this;
	}
	MyString & operator=(MyString &&str){
		if(this != &str){
			std::swap(_data, str._data);
			std::swap(_len, str._len);
		}
		std::cout<<"move assignment"<<std::endl;
		return *this;
	}
	~MyString(){
		std::cout<<"destructor"<<std::endl;		
		if(_data) 
			_data.reset();
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
	std::cout<<"----swaps----"<<std::endl;
	Lswap(a,b);
	Rswap(a,b);
	return 0;
}