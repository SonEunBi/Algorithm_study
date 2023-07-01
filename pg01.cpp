#include <string>
#include <vector>

using namespace std;

string solution(string phone_number) {
    string answer = phone_number;
    string add = "";
    add.append(phone_number.length()-4, '*');
    answer.replace(0,phone_number.length()-4, add);
   
    return answer;
}
