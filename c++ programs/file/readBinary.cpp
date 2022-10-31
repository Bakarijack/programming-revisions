#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main( ){
    cout<<"Enter the file name : ";
    string s;
    cin>>s;

    fstream binaryio(s.c_str(),ios::in | ios::binary);

    string z;
    while(!binaryio.eof()){
        binaryio>>z;
        cout<<z;
    }

    binaryio.close();
    cout<<endl;

    return 0;
}