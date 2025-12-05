import fs from "fs";

const lines: string[] = fs
  .readFileSync("day5_input.csv", "utf-8")
  .trim()
  .split("\n");

let availableIngredients: number[] = [];
let freshRanges: [number, number][] = [];
for (const line of lines) {
  if (line === "") continue;
  if (line.includes("-")) {
    const [start, end] = line.split("-").map(Number);
    freshRanges.push([start, end]);
  } else {
    const num = Number(line);
    availableIngredients.push(num);
  }
}

// Optimize ranges
freshRanges.sort((a, b) => a[0] - b[0]);
for (let i = 1; i < freshRanges.length; i++) {
  const [start0, end0] = freshRanges[i - 1];
  const [start1, end1] = freshRanges[i];

  if (start1 >= start0 && start1 <= end0) {
    // Overlap detected, merge ranges
    freshRanges[i - 1][1] = Math.max(end0, end1);
    freshRanges.splice(i, 1);
    i--; // Stay at the same index for next iteration
  }
}

// PART ONE
let numFresh = 0;
for (const ingredient of availableIngredients) {
  for (const [start, end] of freshRanges) {
    if (ingredient >= start && ingredient <= end) {
      numFresh++;
      break;
    }
  }
}
console.log(`Number of fresh ingredients: ${numFresh}`);

// PART TWO
let numFreshIds = 0;
for (const [start, end] of freshRanges) {
  numFreshIds += end - start + 1;
}
console.log(`Total number of fresh ingredient IDs: ${numFreshIds}`);
