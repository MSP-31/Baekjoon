#include <stdio.h>
#include <math.h>
#include <string>
using namespace std;

int main(){
    int num;
    int sum = 0;
    string temp, str;
    
    scanf("%d",&num);

    temp = to_string(num);
    
    for(int i=0; i<temp.size();i++){
        str = temp[i];
        sum += pow(stoi(str),5);
    }

    printf("%d\n",sum);

    return 0;
}