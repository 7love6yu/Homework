#include <iostream>
#include <string>
#include <queue>
using namespace std;

int main() {
   int n,flag,val;
   queue <int> qee;
   cin >> n;
    for (int i = 0; i < n; ++i) {
        cin >> flag;
        if (flag == 1){
            cin >> val;
            qee.push(val);
        }
        if (flag == 2)
        {
            if (qee.empty()){
                cout <<"Invalid"<<endl;
            }
            else{
                cout << qee.front()<<endl;
                qee.pop();
            }
        }
        if (flag == 3){
            cout << qee.size()<<endl;
        }
    }
}
