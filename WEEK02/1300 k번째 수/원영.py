# 답봄
# 10^5 * 10^5 배열을 만들면 메모리 초과가 발생
import sys
sys.stdin = open("input_py.txt", "r")

n = int(input())
k = int(input())

start = 0
end = k

while start < end:
  mid = (start+end)//2
  
  temp = 0
  for i in range(1, n+1):
    temp += min(mid//i, n)
  
  if temp >= k:
    end = mid # 수연) 오 작은 수들이 k개 보다 많이 세어졌어도 end값 조정이 필요 없는건가?
  else:
    start = mid +1

print(start)

# 💩💩💩

# 잘 봤습니다!! 

# 수연) input값 file 읽어서 돌리시는 거 간zi라고 생각함 귯~ 