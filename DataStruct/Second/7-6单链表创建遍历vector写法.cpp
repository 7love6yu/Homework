#include "iostream"
#include "algorithm"
#include "vector"

using namespace std;

int main(){
    vector<int> v;
    int n,val;
    cin >> n;
    if (n==0) return 0;
    for(int i = 0;i<n;i++){
        cin >> val;
        v.push_back(val);
    }
    int i;
    for(i=0;i<v.size()-1;i++)
        cout <<v[i] <<" ";
    cout << v[i];

}
