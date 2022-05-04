# 100점 코드
# if 문 검사가 시간에 영향을 얼마나 주는지는 정확히 모르지만
# if oil == 1 이 때의 경우를 for문 밖으로 빼니 58점에서 100점이 나옴 // 수연) 헉 if문인데도 ?!?!?!
import sys
sys.stdin = open("input_py.txt", "r")
input = sys.stdin.readline

def main():
  n = int(input())
  road = [0] + list(map(int, input().split()))
  gas_station = list(map(int, input().split()))

  answer = 0
  oil = gas_station[0]
  length = 0
  # 첫 주유소가 1이면 첫 주유소에서 다 넣으면 됨 기름이 제일 쌈
  if oil == 1:
    answer = sum(road)
    print(answer)
    return 

  # 현재보다 값이 싼 주유소가 나올때 까지 거리를 저장
  # 현재보다 싼 주유소가 나오면 answer에 거리* 현재 주유소 값을 더함
  for i in range(1, n):
    # 마지막 주유소는 기름을 넣지 않아도 되니 결과 계산
    if i == n-1:
      length += road[-1]
      answer += oil * length
      break
    
    if oil >= gas_station[i]:
      length += road[i]
      answer += oil * length
      oil = gas_station[i]
      length = 0
    elif oil < gas_station[i]:
      length += road[i]

  print(answer)
main()

###########################################
# 58점 코드
import sys
input = sys.stdin.readline

def main():
  n = int(input())
  road = [0] + list(map(int, input().split()))
  gas_station = list(map(int, input().split()))

  answer = 0
  oil = gas_station[0]
  length = 0
  for i in range(1, n):
    if oil == 1:
      answer = sum(road)
      break
    
    if i == n-1:
      length += road[-1]
      answer += oil * length
      break
    if oil >= gas_station[i]:
      length += road[i]
      answer += oil * length
      oil = gas_station[i]
      length = 0
    elif oil < gas_station[i]:
      length += road[i]

  print(answer)
main()