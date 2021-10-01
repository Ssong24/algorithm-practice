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
