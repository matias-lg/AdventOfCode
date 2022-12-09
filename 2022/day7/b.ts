import { readFileSync } from "fs";

type DirNode = {
  dirname: string;
  childrenDir: { [dirname: string]: DirNode };
  files: { [filename: string]: number };
  parent?: DirNode;
};

const root: DirNode = {
  dirname: "\\",
  childrenDir: {},
  files: {},
};

let cwd = root;

const inp = readFileSync("./input", "utf8").split("\n").slice(1, -1);

const getTokens = (idx: number): string[] => inp[idx].split(" ");

let idx = 0;
while (idx < inp.length) {
  let tokens = getTokens(idx);
  // user input
  if (tokens[0] == "$") {
    switch (tokens[1]) {
      case "ls":
        idx++;
        while (idx < inp.length && getTokens(idx)[0] != "$") {
          let childTokens = getTokens(idx);
          if (childTokens[0] == "dir") {
            if (!cwd.childrenDir[childTokens[1]])
              cwd.childrenDir[childTokens[1]] = {
                parent: cwd,
                dirname: childTokens[1],
                childrenDir: {},
                files: {},
              };
          } else {
            if (!cwd.files[childTokens[1]])
              cwd.files[childTokens[1]] = parseInt(childTokens[0]);
          }
          idx++;
        }
        break;

      case "cd":
        let targetDir = tokens[2];
        if (targetDir == "..") {
          if (cwd.parent) cwd = cwd.parent;
        } else cwd = cwd.childrenDir[tokens[2]];
        idx++;
        break;

      default:
        console.error(`Unexpected keyword ${tokens[0]}`);
        idx++;
    }
  }
}

let sizes: number[] = [];
const getDirSizes = (dir: DirNode): number => {
  let totalSize = Object.values(dir.files).reduce((acc, x) => acc + x, 0);
  let childrens = Object.keys(dir.childrenDir);
  if (childrens.length > 0) {
    totalSize += childrens
      .map((child) => getDirSizes(dir.childrenDir[child]))
      .reduce((acc, v) => acc + v, 0);
  }
  sizes.push(totalSize);
  return totalSize;
};

const TOTAL_SPACE = 70000000;
const NEED = 30000000;
const UNUSED_SPACE = TOTAL_SPACE - getDirSizes(root);

let closest = Infinity;
for (let sz of sizes) {
  if (UNUSED_SPACE + sz >= NEED) {
    closest = Math.min(closest, sz);
  }
}

console.log(`Smallest dir that frees up needed space is ${closest}`);
