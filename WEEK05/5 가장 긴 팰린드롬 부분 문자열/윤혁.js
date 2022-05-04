// 수연) JS 풀이 진짜 쩐다고 생각합니다. @))))) 김밥 한 줄 놓고 가요
s = s.split("");
lengthS = s.length;
let dp = Array.from(Array(lengthS), () => new Array(lengthS));

let answer = "";
for (let slength = 0; slength < lengthS; slength++) {
  for (let start = 0; start < lengthS - slength; start++) {
    end = start + slength;
    if (start === end) {
      dp[start][end] = 1;
      if (answer === "") {
        answer = s[start];
      }
    } else if (s[start] === s[end]) {
      // console.log(dp[start][end - 1]);
      if (start + 1 === end) {
        dp[start][end] = end - start + 1;
        if (answer.length < end - start + 1) {
          answer = s.slice(start, end + 1).join("");
        }
      } else if (dp[start + 1][end - 1] !== undefined) {
        if (answer.length < end - start + 1) {
          answer = s.slice(start, end + 1).join("");
        }
        dp[start][end] = end - start + 1;
      }
    }
  }
}
console.log(answer);

// 개쩌는 풀이
// (1) for each 1 unit or 2 units, we expand
// (2) we judge whether the expanded two chars are the same
// (3) if the expanded chars are the same, we expand again
// (4) else we calculate the length by (right - left - 1), and compare it with the current max
var str = '';
  for (let i = 0; i < s.length; i++) {
      for (let j = 0; j < 2; j++) {
          var left = i;
          var right = left + j;
          while (s[left] && s[left] === s[right]) {
              left--;
              right++;
          }
          if (right - left - 1 > str.length) {
              str = s.slice(left + 1, right);
          }
      }
  }
  return str;
