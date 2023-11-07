#include "iostream"
using namespace  std;

int pta(int n){
    if(n){
        pta(n/2);
        cout<<n%2;
    }
}

int main(){
    int val;
    cin>>val;
    pta(val);
    return 0;
}