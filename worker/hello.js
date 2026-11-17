// Worker contoh: benchmark CPU sederhana (gratis via GitHub Actions).
// Repo publik = menit gratis tanpa batas, 4 vCPU per job, maks 20 job paralel.
const os = require('node:os');

const cpus = os.cpus().length;
console.log(`CPU: ${cpus} core, platform: ${os.platform()} ${os.arch()}, RAM: ${(os.totalmem() / 2 ** 30).toFixed(1)} GB`);

function countPrimes(limit) {
  const sieve = new Uint8Array(limit + 1);
  let count = 0;
  for (let i = 2; i <= limit; i++) {
    if (!sieve[i]) {
      count++;
      for (let j = i * i; j <= limit; j += i) sieve[j] = 1;
    }
  }
  return count;
}

const t0 = Date.now();
let total = 0;
let rounds = 0;
while (Date.now() - t0 < 10000) {
  total += countPrimes(200000);
  rounds++;
}
console.log(`Selesai: ${rounds} ronde sieve 200k dalam ${((Date.now() - t0) / 1000).toFixed(1)} detik, total prima terhitung: ${total}`);
