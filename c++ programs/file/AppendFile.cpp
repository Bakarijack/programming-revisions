#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main( ){
    fstream inout;

    //create a file
    inout.open("city.txt",ios::out);

    //write cities
    string inputC;
    for (int i=0; i<5;i++){
        cout<<"Enter the name of any city : ";
        getline(cin,inputC);
        inout<<inputC;
        inout<<" ";
        system("clear");
    }
    inout.close();

    //Append to the file
    inout.open("city.txt",ios::out | ios::app);

    //write cities
    inout<<"Savannah"<<" "<<"Austin"<<" "<<"Chicago";
    inout.close();

    string outC;
    //open the file 
    inout.open("city.txt",ios::in);
    while(!inout.eof()){
        inout>>outC;
        cout<<outC<<"  ";
    } 
    inout.close();

    return 0;
}