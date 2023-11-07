#include "iostream"
using namespace  std;

int pta(int n){
    if(n){
        pta(n/8);
        cout << n % 8;
    }
}

int main(){
    int val;
    cin>>val;
    pta(val);
}