// 백준 2562번 최대값
#include <iostream>
using namespace std;

int main(){
    int max = 0;
    int maxi = 0;
    int n[9];
    
    for(int i=0; i<9; i++){
        cin >> n[i];
        if(max <= n[i]){
            max = n[i];
            maxi = i+1;
        }
    }
    cout << max << endl;
    cout << maxi << endl;
    
    return 0;
}