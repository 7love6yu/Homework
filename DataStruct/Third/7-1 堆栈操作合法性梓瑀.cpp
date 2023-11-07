# include "iostream"
# include "string"
using namespace std;

int main(){
    int n, m,cnt = 0;
    string str,tmp;
    cin >> n >> m;
    for (int i = 0; i < n; ++i) {
        cin >> str;
        tmp = "YES";
        for (auto c : str) {
            if (c == 'S')
                cnt++;
            else if(c == 'X')
                cnt--;

            if (cnt < 0 || cnt > m){  //多出栈或者溢栈
                tmp = "NO";
                break;
            }
        }

        if (cnt)  tmp = "NO";    //栈没空
        cout << tmp << endl;
        cnt = 0; //reset
    }
    return 0;
}