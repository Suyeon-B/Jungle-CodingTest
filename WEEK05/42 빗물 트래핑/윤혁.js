// 정답 봄....
if (!height) return 0;
let left = 0,
  right = height.length - 1,
  maxLeft = height[left],
  maxRight = height[right],
  res = 0;

while (left < right) {
  if (maxLeft < maxRight) {
    left++;
    maxLeft = Math.max(maxLeft, height[left]);
    res += maxLeft - height[left];
  } else {
    right--;
    maxRight = Math.max(maxRight, height[right]);
    res += maxRight - height[right];
  }
}
return res;
