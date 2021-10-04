""" 성적 낮은 순으로 학생 출력
입력예시:
 2
 홍길동 95
 이순신 77
출력예시:
 이순신 홍길동
"""

def setting(data):
  return data[1]

def ascending():
  # 입력 받기
  n = int(input())
  students = []
  for i in range(n):
    name,score = input().split()
    score = int(score)
    students.append((name, score)) # tuple 형
   
  # value에 따라 오름차순 
  result = sorted(students, key=setting)
  for i in range(n):
    print(result[i][0], end =' ')
  

ascending()
