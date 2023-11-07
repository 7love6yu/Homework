#include <iostream>
#include <string>
#include <stack>
using namespace std;

int main() {
    string str;
    getline(cin, str);
    stack<char> t1;
    int flag = 1,left = 0,right = 0;

    for (auto c : str) {
        if (c == '(' || c == '[' || c == '{') {
            left++;
            t1.push(c);
        } else if (c == ')' || c == ']' || c == '}') {
               right++;
                    if (t1.empty() || c - t1.top() > 2) 
                           flag = -1;   //40 41 91 93 122 125
             t1.pop();
          }
    }
    cout << left << " " << right << endl;
    if (flag!=-1 && t1.empty()) 
        cout << "YES" << endl;
    else 
        cout << "NO" << endl;

}
