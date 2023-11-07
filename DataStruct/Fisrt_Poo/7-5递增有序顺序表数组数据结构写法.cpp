#include "iostream"
#define  max 100
using namespace std;

typedef struct {
    int *pBase;
    int cnt;
}sqList;

int init(sqList& l){
    l.pBase = new  int[max];
    if(l.pBase == nullptr) return 0;
    l.cnt =0;
    return  1;
}
void createList(sqList& l,int n){
    int val;
    for (int i = 0; i < n; ++i) {
        cin>>val;
        l.pBase[i] = val;
    }
    l.cnt = n;
}

int insertList(sqList& l,int pos,int val){
    if(pos <1 || pos > l.cnt + 1) return 0;
    for (int i = l.cnt-1; i >= pos-1 ; --i) {
        l.pBase[i+1] = l.pBase[i];
    }
    l.pBase[pos-1] = val;
    l.cnt++;
    return  1;
}

void disList(sqList& l){
    for (int i = 0; i < l.cnt; ++i) {
        cout << l.pBase[i]<<",";
    }
}
int main(){
    sqList l;
    init(l);
    int n;
    cin >> n;
    createList(l,n);
    int cnt = 0, elem;
    cin >> elem;
    for (int i = 0; i < n; ++i) {
        if (l.pBase[i] < elem)
            cnt++;
    }
    int pos = cnt+1;
    insertList(l,pos,elem);
    disList(l);




    return 0;
}