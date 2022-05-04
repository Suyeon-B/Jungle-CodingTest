//진우) js 코드가 많이 복잡하네요 풀이 잘보고 갑니다
//수연) 나도 js 고수가 되고싶다.. 한 수 배워 갑니다

let nums = [1, 2, 3, 4];

var leftMultiple = [];
var rightMultiple = [];

let left, right;
let lengthN = nums.length;

for (left = 0, right = lengthN - 1; left < lengthN; left++, right--) {
  if (left === 0) {
    leftMultiple[left] = nums[left];
    rightMultiple[right] = nums[right];
    continue;
  }
  leftMultiple[left] = leftMultiple[left - 1] * nums[left];
  rightMultiple[right] = rightMultiple[right + 1] * nums[right];
}

let answer = [];
let i;
for (i = 0; i < lengthN; i++) {
  if (i === 0) {
    answer[i] = rightMultiple[i + 1];
    continue;
  } else if (i === lengthN - 1) {
    answer[i] = leftMultiple[i - 1];
  } else {
    answer[i] = leftMultiple[i - 1] * rightMultiple[i + 1];
  }
}
console.log(answer);
