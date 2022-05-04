# 아이디어 : 리스트에 있는 문자열을 쪼개고 정렬후 check 리스트 앞부분에 저장
# 맨 앞부분과 쪼개고 정렬한 값이 같으면 동일한 애너그램이므로 그 리스트에 넣어줌
# 출력할 때는 맨 앞 문자열을 지우고 출력

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs.sort()

        check = []
        answer = []

        for i in strs:
            temp = list(i)
            temp.sort()
            temp = ''.join(temp)

            for j in range(len(answer)):
                if answer[j][0] == temp:
                    answer[j].append(i)
                    break # 수연) 한 수 배워갑니다?
            else:
                answer.append([temp])
                answer[-1].append(i)


        for i in range(len(answer)):
            answer[i] = answer[i][1:]

        return answer
