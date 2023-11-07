#include <algorithm>
#include "iostream"
#include "vector"

using namespace std;

int main(){
    vector<int> l1,l2,result;
    int tmp;
    while(cin>>tmp && tmp!= -1){
        l1.push_back(tmp);
    }

    while(cin>>tmp && tmp!= -1){
        l2.push_back(tmp);
    }
    result.insert(result.end(),l1.begin(),l1.end());
    result.insert(result.end(),l2.begin(),l2.end());
    sort(result.begin(), result.end());

    if (result.empty()) cout<<"NULL";
    else{
        int i;
        for ( i = 0 ; i<result.size()-1;++i)
            cout<<result[i]<<" ";
        cout<<result[i]<<endl;
    }

}


