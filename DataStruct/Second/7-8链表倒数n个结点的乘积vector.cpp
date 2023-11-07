#include "algorithm"
#include "iostream"
#include "vector"

using namespace std;

int main(){

    vector<int> v;
    int tmp,m,n;
    cin>>m;
    cin>>n;
    if(m == 0 || n==0){
        cout<<"0";
        return 0;
    }

    for (int i = 0; i < m; ++i){
        cin>>tmp;
        v.push_back(tmp);
    }

    auto it = v.end()-n;
    int sum = 1;

    while (it != v.end()){
        sum *= *it;
        it++;
    }
    cout << sum;
    return 0;
}


