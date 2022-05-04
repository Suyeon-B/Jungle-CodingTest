/**
 * @param {number[]} prices
 * @return {number}
 */
// 찢었네
var maxProfit = function(prices) {
  let answer = 0;
  let min_day = prices[0];
  for (let i = 1; i < prices.length; i++) {
    if (min_day > prices[i]) {
      min_day = prices[i];
      continue;
    }
    if (min_day < prices[i]) {
      let cul = prices[i] - min_day;
      answer = Math.max(answer, cul);
    }
  }
  
  return answer;
};