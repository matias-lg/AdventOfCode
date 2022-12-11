import { readFileSync } from "fs";

const inp = readFileSync("./input", "utf8")
  .split("\n")
  .slice(0, -1)
  .map((row) => row.split("").map(Number));

let ans = -1;

for (let r = 1; r < inp.length - 1; r++) {
  for (let c = 1; c < inp[r].length - 1; c++) {
    const thisN = inp[r][c];
    let thisScore = 1;

    let larr = inp[r].slice(0, c).reverse();
    let lvd = 0;
    for (let e of larr) {
      lvd++;
      if (e >= thisN) break;
    }
    thisScore *= lvd;

    let rarr = inp[r].slice(c + 1, inp[r].length);
    let rvd = 0;
    for (let e of rarr) {
      rvd++;
      if (e >= thisN) break;
    }
    thisScore *= rvd;

    let uarr = [...Array(r).keys()].map((idx) => inp[idx][c]).reverse();
    let uvd = 0;
    for (let e of uarr) {
      uvd++;
      if (e >= thisN) break;
    }
    thisScore *= uvd;

    let darr = [...Array(inp.length).keys()]
      .slice(r + 1, inp.length)
      .map((idx) => inp[idx][c]);
    let dvd = 0;
    for (let e of darr) {
      dvd++;
      if (e >= thisN) break;
    }
    thisScore *= dvd;

    ans = Math.max(thisScore, ans);
  }
}

console.log(ans);
