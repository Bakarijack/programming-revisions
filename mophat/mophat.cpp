
#include<iostream>
#include<ctime>
#include<cstdlib>
#include<string>
using namespace std;
int main ()
{
srand(time(0));
int lottery=rand()%91+10;
cout<<"lottery="<<lottery<<endl;
int lottery1=lottery%10;
int lottery2=lottery/10;
cout<<"user enter a two digit guess"<<endl;
int guess;
cin>>guess;
int guess1=guess%10;
int guess2=guess/10;

if(guess==lottery){

    cout<<"you win 10000"<<endl;
}
else if(lottery1==guess1||lottery1==guess2||lottery2==guess1||lottery2==guess2){
    cout<<"you win 5000 for matching atleast a digit"<<endl;
    {
        cout<<"you win 1000 for matching all the digits in the lottery ticket"<<endl;
    }
    else
    cout<<"you loose"<<endl;
    return 0;
}
