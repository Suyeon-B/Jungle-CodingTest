/**
 * @param {number[]} nums 
 * @return {number[]}
 */
var productExceptSelf = function (nums) {
  let p = 1;
  answer = [];
  nums.map((el) => {
    answer.push(p);
    p *= el;
  });
  p = 1;
  for (let i = answer.length - 1; i > -1; i--) {
    answer[i] = p * answer[i];
    p *= nums[i];
  }
  return(answer);
};