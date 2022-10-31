#include <iostream>
#include <fstream>
#include <string>
using namespace std;
int main( ){
    ifstream input("state.txt");

    if (input.fail()){
        cout<<"File does not exist"<<endl;
        cout<<"Exit program"<<endl;
        return 0;
    }
    
    string name;
    while(!input.eof()){
        getline(input,name,'#');
        cout<<name<<endl;
    }
    input.close();

    cout<<"Done!"<<endl;
    return 0;
}