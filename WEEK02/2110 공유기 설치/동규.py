import sys
input = sys.stdin.readline # 수연: 이거 천잰데요? 나 이거 왜 생각 못했지
# sys.stdin = open('input.txt')

n, c = map(int, input().split())
array = []
for i in range(n):
    array.append(int(input()))
array.sort()

start= 1
end = array[-1] - array[0]
answer = 0

# def binary(array, start, end):
def binary(array, start, end):
    while start <= end:
        mid = (start + end) //2
        current = array[0]
        count = 1

        for i in range(1, len(array)):
            if array[i] >= current + mid:
                count += 1
                current = array[i]

        if count >= c:
            global answer
            start = mid +1
            answer = mid
        else:
            end = mid -1

binary(array, start, end)
print(answer)

