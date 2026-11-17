# Compute Worker — gratis, tanpa kartu

Repo ini dipakai sebagai "mesin compute gratis" untuk Boone (agen AI milik Senjas).
Semua yang di sini gratis dan tidak butuh kartu kredit.

## Yang terpasang

### 1. GitHub Actions — worker CPU (utama)
- File: `.github/workflows/compute-worker.yml`
- Repo **publik** = menit Actions gratis **tanpa batas**, 4 vCPU per job, maks 20 job paralel.
- Cara menjalankan:
  1. Buka tab **Actions** di repo ini.
  2. Pilih workflow **Compute Worker** → **Run workflow**.
  3. Isi nama script (default `worker/hello.js`) → **Run workflow**.
  4. Hasilnya terlihat di log job itu.
- Untuk job sendiri: taruh script Node.js di folder `worker/`, lalu jalankan lewat workflow dengan nama file-nya.
- Batas: ini CI, bukan server 24/7. Satu job maks 6 jam. Cocok untuk kerja yang bisa dipecah jadi banyak job paralel.

### 2. GitHub Codespaces — mesin interaktif (burst pendek)
- File: `.devcontainer/devcontainer.json` (Node 22).
- Kuota gratis: **120 core-hours/bulan** (mis. 3,75 jam/bulan di mesin 32 core, 15 jam/bulan di 8 core).
- Cara menjalankan: tombol **Code → Codespaces → Create codespace on main**.
- Tanpa kartu, pemakaian berhenti sendiri saat kuota habis (tidak ditagih).

## Yang TIDAK dipasang (dan kenapa)
- **Kaggle TPU 96 core** — angkanya benar, tapi aturannya melarang worker non-ML ("server farming"); akun bisa disuspend. Tidak dipakai.
- **Oracle Always Free (2 OCPU ARM, selamanya)** — satu-satunya VPS gratis 24/7, tapi pendaftaran butuh identitas + kartu Senjas sendiri. Boone tidak bisa daftarkan. Kalau Senjas mau, daftar di cloud.oracle.com (pilih Always Free, Ampere A1).
- **Modal / DigitalOcean / Google Cloud / Linode / Kamatera** — semuanya butuh kartu kredit untuk daftar (trial sekali pakai). GCP paling aman soal tagihan (tidak pernah auto-charge), tapi tetap butuh kartu.

## Catatan
- Verifikasi lengkap semua klaim: `~/workspace/research_notes/free-compute-20261117/report.md` (dicek 17 Nov 2026).
- Repo ini sebelumnya dibuat untuk entri make.fun github-core-clone-01, tapi entri itu dikirim lewat source bundle dan repo ini tetap kosong — jadi dipakai untuk compute worker.
