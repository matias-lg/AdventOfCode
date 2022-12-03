import { readFileSync } from "fs";

const losesTo = {
  A: "B",
  B: "C",
  C: "A",
};

const scores = {
  A: 1,
  B: 2,
  C: 3,
};

const inp = readFileSync("./input", "utf8");
const pairs = inp.split("\n")
let score = 0;

for (let pair of pairs) {
  const [o, m] = pair.split(" ");
  if (m == "Y") score += scores[o] + 3;
  else if (m == "X") score += scores[losesTo[losesTo[o]]];
  else score += scores[losesTo[o]] + 6;
}

console.log(score);
