#include <iostream>
#include <string>
using namespace std;
int main(){
    string city;
    cout<<"Enter a city : ";
    getline(cin,city,'\n');
    cout<<"You entered : "<<city<<endl;
    return 0;
}