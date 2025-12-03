import fs from "fs";

const banks: string[] = fs
  .readFileSync("day3_input.csv", "utf-8")
  .trim()
  .split("\n");

// PART ONE
let sum = 0;
for (const bank of banks) {
  //   console.log(bank);

  let best = ((bank.at(-2) as string) + bank.at(-1)) as string;
  //   console.log(` Starting best: ${best}`);

  for (let i = bank.length - 3; i >= 0; i--) {
    const candidate1 = bank[i] + best[0];
    const candidate2 = bank[i] + best[1];
    if (candidate1 > best && candidate1 >= candidate2) {
      best = candidate1;
      //   console.log(`  New best: ${best}`);
    } else if (candidate2 > best && candidate2 >= candidate1) {
      best = candidate2;
      //   console.log(`  New best: ${best}`);
    }
  }

  //   console.log(` Final best: ${best}`);
  sum += parseInt(best);
}
console.log(`Sum of bests: ${sum}`);

// PART TWO

const numBatteries = 12;
sum = 0;
for (const bank of banks) {
  console.log(bank);

  let best = bank.substring(bank.length - numBatteries);
  console.log(` Starting best: ${best}`);

  let nextBest = best;
  for (let i = bank.length - numBatteries - 1; i >= 0; i--) {
    const nextBattery = bank[i];
    for (let j = 0; j < numBatteries; j++) {
      const candidate =
        nextBattery + best.substring(0, j) + best.substring(j + 1);
      console.log(` Considering candidate: ${candidate} (dropping ${best[j]})`);
      if (candidate > nextBest) {
        nextBest = candidate;
        console.log(`  New best: ${nextBest}`);
      }
    }
    best = nextBest;
  }

  console.log(` Final best: ${nextBest}`);
  sum += parseInt(nextBest);
}
console.log(`Sum of bests: ${sum}`);
