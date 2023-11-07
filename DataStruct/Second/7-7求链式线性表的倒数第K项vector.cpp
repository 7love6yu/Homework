#include <algorithm>
#include "iostream"
#include "vector"

using namespace std;

int main(){
    vector<int> l1;
    int tmp,k;
    cin>>k;
    //负数退出
    while(cin>>tmp && tmp >= 0){
        l1.push_back(tmp);
    }

    auto it =l1.end()-k;
    if (it <l1.cbegin() || it >= l1.cend())
        cout<<"NULL";
    else
        cout<<*it;

    return 0;
}


