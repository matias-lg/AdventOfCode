import { readFileSync } from "fs";

const wins = {
  X: "C",
  Y: "A",
  Z: "B",
};

const eq = {
  X: "A",
  Y: "B",
  Z: "C",
};

const inp = readFileSync("./input", "utf8");
const pairs = inp.split("\n").slice(0, -1);

console.log(
  pairs
    .map((x) => x.split(" "))
    .map(([op, me]) => {
      if (op == wins[me]) return [6, me];
      else if (op == eq[me]) return [3, me];
      return [0, me];
    })
    .reduce(
      (acc, [n, me]) =>
        acc + Number(n) + String(me).charCodeAt(0) - "X".charCodeAt(0) + 1,
      0
    )
);
