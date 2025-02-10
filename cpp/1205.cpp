#include <iostream>
#include <vector>
using namespace std;

int main(){
    int n,score,p;
    int result;

    freopen("input.txt", "r", stdin);

    scanf("%d %d %d",&n,&score,&p);
    
    if (n != 0){
        vector<int> num(n);
        for(int i=0;i<n;i++){
            scanf("%d",&num[i]);
        }

        // 연산
        for(int i=0;i<p;i++){
            // num이 score랑 같고 랭킹내 일때
            if(num[i] == score && i<n){
                result = i+1;
                for(i;i<p;i++){
                    // 마지막까지 같다면
                    if(num[i] == score && i+1 == n){
                        result = -1;
                        break;
                    }
                }
            }
            // score가 num보다 크고 랭킹내일때
            else if(num[i] < score && i<n){
                result = i+1;
                break;
            }
            else{
                result = -1;
            }
        }
    }
    // n이 0일때
    else {
        result = 1;
    }

    printf("%d\n",result);

    return 0;
}