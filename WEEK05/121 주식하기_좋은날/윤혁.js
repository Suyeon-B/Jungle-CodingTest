const prices = [7, 1, 5, 3, 6, 4];

const lengthP = prices.length;

let i;

let answer = 0;

let stand, maxV;

for (i = 0; i < lengthP - 1; i++) {
  if (stand < prices[i]) {
    continue;
  }
  stand = prices[i]; // Number
  maxV = Math.max(...prices.slice(i + 1));
  if (stand < maxV) {
    answer = Math.max(maxV - stand, answer);
  }
}
console.log(answer);
