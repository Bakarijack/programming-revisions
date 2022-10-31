#include <iostream>
#include <fstream>
#include <string>
using namespace std;

class employee{                                        //class difinition
    private: 
       string emp_name;
       int emp_number;
       float emp_compension;
    public: 
       employee(): emp_number(0),emp_compension(0) //constructor
       {/*constructor body*/}

       void getData(){
           cout<<"Enter the employee name : ";            getline(cin,emp_name); 
           cout<<"Enter the employee number : ";          cin>>emp_number;  
           cout<<"Enter the employee compensation : ";    cin>>emp_compension;  
       }

       void displayData(){
           cout<<emp_name<<"\t\t\t\t"<<emp_number<<"\t\t\t\t"<<emp_compension<<endl;
       }
};

//main fuction
int main( ){
    employee emp1,emp2,emp3;

    //setting employee data
    emp1.getData();
    system("clear");
    emp2.getData();
    system("clear");
    emp3.getData();
    system("clear");


    //display the data
    cout<<"Employee Profile "<<endl;
    cout<<"Name                 employeeNumber              Compensation \n";
    emp1.displayData();
    emp2.displayData();
    emp3.displayData();

    return 0;
}