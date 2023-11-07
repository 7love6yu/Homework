#include <iostream>
#include <string>
#include "algorithm"
using namespace std;

int main() {
    string str,result;
    cin >> str;
    result = str;
    reverse(result.begin(), result.end());

    if (result == str) 
        cout << "yes" << endl;
    else 
        cout << "no" << endl;
    
}
