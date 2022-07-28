#include <string>
#include <vector>

using namespace std;

string solution(string phone_number) {
    string answer = phone_number;
    string add = "*";
    answer.replace(0,phone_number.length()-4, add);
    
   
    return answer;
}

//이게 실패한 이유 : replace 함수는 A 문자열을 B 문자열로 대체하는 역할을 함
// *가 들어갈 수 있는 정도를 정해준다면 *를 n번 곱해서 대체하는 식으로 구현할 수 있음
