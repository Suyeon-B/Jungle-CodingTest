/**
 * @param {number[]} nums
 * @return {number[][]}
 */
// 파이썬으로 하다가 js로 하니깐 못 하겠네요 js 개 어려움
// 	1428 ms	62.2 MB 시간은 더 빠르네요
var threeSum = function (nums) {
  nums.sort((a, b) => {
    return a - b;
  });
  let answer = [];
  const ans_set = new Set();

  nums.map((el, i) => {
    let left = i + 1;
    let right = nums.length - 1;

    while (left < right) {
      let temp = nums[left] + nums[right] + el;
      if (temp > 0) right--;
      else if (temp < 0) left++;
      else {
        ans_set.add(JSON.stringify([el, nums[left], nums[right]]));

        left++;
        right--;
      }
    }
  });

  // 중복제거 코드
  answer.push(...ans_set);
  answer = answer.map((el) => {
    return JSON.parse(el);
  });

  return answer;
};
