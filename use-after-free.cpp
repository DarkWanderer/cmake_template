#include <iostream>
#include <string>

using namespace std;

int main(int argc, char* argv[])
{
	int* i = new int;
	delete i;
	*i = 5;
	return 0;
}
