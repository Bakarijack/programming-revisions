#include <iostream>
#include <string>
#include <fstream>
using namespace std;
int main( ){
    ofstream input;
    input.open("state.txt");
    
    string name;
    for (int i=0;i<5;i++){
    cout<<"Enter the names : ";
    getline(cin,name);
    input<<name;
    input<<"#";
    system("clear");
    }

    input.close();

    cout<<"done!"<<endl;
    return 0;
}