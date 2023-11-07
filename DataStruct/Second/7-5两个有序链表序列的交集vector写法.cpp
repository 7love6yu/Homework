#include <algorithm>
#include "iostream"
#include "vector"

using namespace std;

int main(){
	vector<int> l1,l2,target;
    int tmp;
    while(cin>>tmp && tmp!= -1){
        l1.push_back(tmp);
    }

    while(cin>>tmp && tmp!= -1){
        l2.push_back(tmp);
    }
    target.resize(min(l1.size(),l2.size()));

    auto  last=
            set_intersection(l1.begin(),l1.end(),l2.begin(),l2.end(),target.begin());
    auto it =target.begin();
    if (last == it ) cout<<"NULL";
    else{
        for(;it!= last-1;it++)
            cout << *it <<" ";
        cout << *it;
    }

	return 0;
}

 
