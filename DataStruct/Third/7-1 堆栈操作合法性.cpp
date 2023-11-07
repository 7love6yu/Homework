# include "iostream"
# include "string"
using namespace std;

int main(){
    int n, m, tmp, cnt = 0;
    string str;
    cin >> n >> m;
    for (int i = 0; i < n; ++i) {
        cin >> str;
        for (auto c : str) {
            if (c == 'S')
                cnt++;
            else if(c == 'X')
                cnt--;
            if (cnt < 0 || cnt > m){
                tmp = -1;
                break;
            }
        }
        if(tmp == -1){
            cout <<"NO"<<endl;
            tmp = 1;
//            continue;
        }
        else if (cnt == 0) cout << "YES"<<endl;
        else cout << "NO" << endl;
        //reset
        cnt = 0;
    }
    return 0;
}