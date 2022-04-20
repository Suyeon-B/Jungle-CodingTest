"""
모든 테트로미노의 모양별로 모두 배치해본 뒤 최댓값을 구한다.
인간승리 ><
"""
import sys
input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    table = []
    for i in range(n):
        table.append(list(map(int, input().split())))

    # ---- 모양
    # 가로
    SUM = []
    if m >= 4: # M < 4이면 불가능함
        for i in range(n):
            for j in range(m-4+1):
                SUM.append(sum(table[i][j:j+4]))
    # 세로
    if m >= 1:
        temp = 0
        for i in range(n-4+1):
            for j in range(m):
                for z in range(4):
                    temp += table[i+z][j]
                SUM.append(temp)
                temp = 0

    # ㅁ 모양
    if m >= 2:
        temp = 0
        for i in range(n-1):
            for j in range(m-1):
                temp += table[i][j]
                temp += table[i][j+1]
                temp += table[i+1][j]
                temp += table[i+1][j+1]
                SUM.append(temp)
                temp = 0

    # L 모양 & ㅗ모양
    # 가로
    if m >= 3:
        temp = 0
        for i in range(n):
            for z in range(6):
                for j in range(m-3+1):
                    temp = sum(table[i][j:j+3])
                    # L
                    if z == 0: # L중 튀어나온 부분이 위의 오른쪽에 달렸을 때
                        if i == 0: # 위에 달린 애 두려면 i=1부터
                            temp = 0
                            break
                        temp += table[i-1][j+2]
                    elif z == 1: # L중 튀어나온 부분이 위의 왼쪽에 달렸을 때
                        if i == 0: # 위에 달린 애 두려면 i=1부터
                            temp = 0
                            break
                        temp += table[i-1][j]
                    elif z == 2: # L중 튀어나온 부분이 아래의 왼쪽에 달렸을 때
                        if i == n-1:
                            temp = 0
                            break
                        temp += table[i+1][j]
                    elif z == 3: # L중 튀어나온 부분이 아래의 오른쪽에 달렸을 때
                        if i == n-1:
                            temp = 0
                            break
                        temp += table[i+1][j+2]
                    # ㅗ
                    elif z == 4: # ㅗ 모양
                        if i == 0:
                            temp = 0
                            break
                        temp += table[i-1][j+1]
                    elif z == 5: # ㅜ 모양
                        if i == n-1:
                            temp = 0
                            break
                        temp += table[i+1][j+1]
                    SUM.append(temp)
                    temp = 0
    # 세로
    if m>=2:
        temp = 0
        for i in range(n-3+1):
            for z in range(6):
                for j in range(m):
                    for w in range(3):
                        temp += table[i+w][j]
                        if w == 2: # 세로 막대기 다 뒀으면 
                            # L
                            if z == 0: # L중 튀어나온 부분이 위의 왼쪽에 달렸을 때
                                if j == 0: # 왼쪽에 달린 애 두려면 j=1부터
                                    temp = 0
                                    break
                                temp += table[i][j-1]
                            elif z == 1: # L중 튀어나온 부분이 위의 오른쪽에 달렸을 때
                                if j == m-1: # 오른쪽에 달린 애 두려면 j=m-2까지만
                                    temp = 0
                                    break
                                temp += table[i][j+1]
                            elif z == 2: # L 모양으로 딱 생겼을 때
                                if j == m-1: # 오른쪽에 달린 애 두려면 j=m-2까지만
                                    temp = 0
                                    break
                                temp += table[i+w][j+1]
                            elif z == 3: # L중 튀어나온 부분이 왼쪽 아래에 달렸을 때
                                if j == 0: # 왼쪽에 달린 애 두려면 j=1부터
                                    temp = 0
                                    break
                                temp += table[i+w][j-1]
                            # ㅗ
                            elif z == 4: # ㅓ 모양
                                if j == 0: 
                                    temp = 0
                                    break
                                temp += table[i+1][j-1]
                            elif z == 5: # ㅏ 모양
                                if j == m-1: 
                                    temp = 0
                                    break
                                temp += table[i+w-1][j+1]
                            SUM.append(temp)
                            temp = 0

    # ㄱㄴ 이렇게 생긴 애
    # 가로
    if m >= 3:
        temp = 0
        for i in range(n-1):
            for j in range(m-2):
                # _|-
                temp += table[i+1][j]
                temp += table[i+1][j+1]
                temp += table[i][j+1]
                temp += table[i][j+2]
                SUM.append(temp)
                temp = 0
                # ㄱㄴ
                temp += table[i][j]
                temp += table[i][j+1]
                temp += table[i+1][j+1]
                temp += table[i+1][j+2]
                SUM.append(temp)
                temp = 0
    # 세로
    if m>=2:
        temp = 0
        for i in range(1, n-1):
            for j in range(m-1):
                # 오른쪽
                temp += table[i][j]
                temp += table[i][j+1]
                temp += table[i-1][j+1]
                temp += table[i+1][j]
                SUM.append(temp)
                temp = 0
                # 왼쪽
                temp += table[i-1][j]
                temp += table[i][j]
                temp += table[i][j+1]
                temp += table[i+1][j+1]
                SUM.append(temp)
                temp = 0
    if m==0:
        print(0)
    else:
        print(max(SUM))

main()



# 170줄 ㄷㄷ 진정한 구현이네요