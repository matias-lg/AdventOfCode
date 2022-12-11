import { readFileSync } from "fs";

const inp = readFileSync("./input", "utf8")
  .split("\n")
  .slice(0, -1)
  .map((row) => row.split("").map(Number));

let ans = 2 * inp.length + 2 * inp[0].length - 4;

for (let r = 1; r < inp.length - 1; r++) {
  for (let c = 1; c < inp[r].length - 1; c++) {
    const thisN = inp[r][c];
    if (c > 0) {
      let left = inp[r].slice(0, c).every((num) => num < thisN);
      if (left) {
        ans++;
        continue;
      }
    }
    if (c < inp.length - 1) {
      let right = inp[r]
        .slice(c + 1, inp[r].length)
        .every((num) => num < thisN);
      if (right) {
        ans++;
        continue;
      }
    }

    if (r > 0) {
      let up = [...Array(r).keys()]
        .map((idx) => inp[idx][c])
        .every((num) => num < thisN);
      if (up) {
        ans++;
        continue;
      }
    }

    if (r < inp.length - 1) {
      let down = [...Array(inp.length).keys()]
        .slice(r + 1, inp.length)
        .map((idx) => inp[idx][c])
        .every((num) => num < thisN);
      if (down) {
        ans++;
        continue;
      }
    }
  }
}

console.log(ans);
