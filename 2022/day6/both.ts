import { readFileSync } from "fs";

const inp = readFileSync("./input", "utf8").slice(0, -1);

const solve = (inp: string, window_size: number) => {
  const windowSet: { [key: string]: number } = {};

  for (let i = 0; i < window_size; i++) {
    let c = inp.charAt(i);
    if (windowSet[c]) {
      windowSet[c] = windowSet[c] + 1;
    } else {
      windowSet[c] = 1;
    }
  }

  for (let i = window_size; i < inp.length; i++) {
    let currlen = Object.keys(windowSet)
      .map((key) => windowSet[key])
      .filter((x) => x > 0).length;
    if (currlen >= window_size) {
      console.log(i);
      break;
    }
    let l = inp.charAt(i - window_size);
    let r = inp.charAt(i);
    windowSet[l] = Math.max(0, windowSet[l] - 1);
    if (windowSet[r]) {
      windowSet[r] = windowSet[r] + 1;
    } else windowSet[r] = 1;
  }
};

console.log("Part One: ");
solve(inp, 4);
console.log("Part Two: ");
solve(inp, 14);
