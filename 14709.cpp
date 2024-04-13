#include <iostream>
#include <vector>
using namespace std;

int num,a,b;
int s = 0;

int main(){
    
    cin >> num;
    vector<pair<int,int>> finger;
    
    for(int i = 0; i < num; i++){
        cin >> a >> b;
        finger.push_back({a,b});
    }

    for(int i = 0; i < num; i++){
        a = finger.at(i).first;
        b = finger.at(i).second;

        if(((a == 1 || a == 3) && (b == 3 || b == 1)) || 
           ((a == 1 || a == 4) && (b == 4 || b == 1)) ||
           ((a == 3 || a == 4) && (b == 4 || b == 3)) ) {
            s++;
        }
        else { 
            s--;
        }
    }

    if(s == 3){ printf("Wa-pa-pa-pa-pa-pa-pow!\n");}
    else      { printf("Woof-meow-tweet-squeek\n");}
    
    return 0;
}