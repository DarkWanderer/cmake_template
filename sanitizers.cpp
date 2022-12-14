#include <iostream>
#include <string>
#include <climits>

using namespace std;

void use_after_free() {
    int* i = new int;
    delete i;
    *i = 5;
}

void leak() {
    int* i = new int;
    *i = 5;
}

void overflow() {
    signed char a = SCHAR_MAX;
    a++;
}

void bounds() {
    char c[2];
    char d[3]; // padding to avoid triggering stack smashing detection
    c[0] = 0;
    c[1] = 1;
    c[2] = 2;
}

int main(int argc, char* argv[])
{
    use_after_free();
    leak();
    overflow();
    bounds();
	return 0;
}
