#include <iostream>
using namespace std;
int main()
{
    int num;
    //Input the number
    cout<<"Enter an integer: ";
    cin>>num;
    if (num % 2 == 0)//check its divisibility with 2
         cout<< num << " is even.";
    else
        cout<< num <<" is odd.";
    return 0;
}
