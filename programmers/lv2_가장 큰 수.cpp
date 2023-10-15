#include <string>
#include <vector>
#include <queue>
#include <set>
#include <iostream>
#include <algorithm>
using namespace std;

string solution(vector<int> numbers) {
    string answer = "";
    vector<int> num(numbers.size(), 0);
    for(int i=0; i<numbers.size(); i++){
        num[i] = numbers[i];
    }
    sort(num.begin(), num.end());
    int l = numbers.size();

    do{
        for(auto i= num.begin(); i != num.end(); ++i){
            cout << *i;
            
        }

    }while(next_permutation(numbers.begin(), numbers.end()))

    for(int i =0; i<l ; i++){

    }




    return answer;
}