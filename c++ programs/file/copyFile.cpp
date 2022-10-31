#include <iostream>
#include <fstream>
#include <string>
using namespace std;
int main( ){
    //enter a source file
    cout<<"Enter a source file name : ";
    string inputFilename;
    cin>>inputFilename;

    //Enter a target file
    cout<<"Enter a target file name : ";
    string outputFilename;
    cin>>outputFilename;

    //create input and output stream
    ifstream input(inputFilename.c_str());
    ofstream output(outputFilename.c_str());

    //check if the file exist
    if (input.fail()){
        cout<<inputFilename<<" does not exist"<<endl;
        cout<<"Exit program"<<endl;
        return 0;
    }

    char ch = input.get();   //reads the current character
    while(!input.eof()){
        output.put(ch);
        ch = input.get();  //read next character
    }

    input.close();
    output.close();

    cout<<"\nCopy done!"<<endl;

    return 0;
}