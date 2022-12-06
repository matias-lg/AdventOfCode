import { readFileSync } from "fs";

const inp = readFileSync("./input", "utf8");
console.log(
  inp
    .split("\n")
    .map((line) => line.split(","))
    .slice(0, -1)
    .map(([a, b]) => [a.split("-"), b.split("-")])
    .map(([[a1, a2], [b1, b2]]) => [
      [parseInt(a1), parseInt(a2)],
      [parseInt(b1), parseInt(b2)],
    ])
    .reduce((acc, [[a, b], [c, d]]) => acc + +!(b < c || a > d), 0)
);
