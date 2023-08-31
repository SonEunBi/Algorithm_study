import sys
input = sys.stdin.readline

def check_cheating(task_answer):
    n = len(task_answer)
    
    for i in range(1, n // 2 + 1):
        front_candidate = task_answer[:i]
        back_candidate = task_answer[i:2*i]
        repeated_candidate = front_candidate + back_candidate

        if repeated_candidate * (n // i) == task_answer:
            original_answer = front_candidate
            cheating_answer = repeated_candidate
            return True, original_answer, cheating_answer
    
    return False, "", ""

# 과제 답안을 입력 받습니다.
task_answer = input().strip()

cheating, original, cheated = check_cheating(task_answer)

if cheating:
    print("Cheating Detected!")
    print("Original Answer:", original)
    print("Cheated Answer:", cheated)
else:
    print("No Cheating Detected.")