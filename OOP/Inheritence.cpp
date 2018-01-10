#include <stdio.h>

class Base
{
public:
	void print() {
		printf("Base: print\n");
	}
	
	void callPrint() {
		print();
	}

	virtual void vPrint() {
		printf("Base: virtual print\n");
	}

	virtual void vPrintNotOverride() {
		printf("Base: virtual print not override\n");
	}

	void vCallPrint() {
		vPrint();
		vPrintNotOverride();
	}
};

class Derived : public Base
{
public:
	void print() {
		printf("Derived: print\n");
	}
	
	void vPrint() override {
		printf("Derived: virtual print\n");
	}
};

int main(int argc, char const *argv[])
{
	Base b;
	Derived d1;
	Derived d2;

	Base    *pb_d1 = &d1;
	Derived *pd_d2 = &d2;

	b.callPrint();		// Base:    print
	b.vCallPrint();		// Base:    virtual print
	               		// Base:    virtual print not override

	d1.callPrint();		// Base:    print
	d1.vCallPrint();	// Derived: virtual print
	                	// Base:    virtual print not override

	pb_d1->print();		// Base:    print
	pb_d1->callPrint(); 	// Base:    print
	pb_d1->vCallPrint();	// Derived: virtual print
	               	     	// Base:    virtual print not override

	pd_d2->print();		// Derived: print
	pd_d2->callPrint(); 	// Base:    print
	pd_d2->vCallPrint(); 	// Derived: virtual print
				// Base:    virtual print not override
	return 0;
}