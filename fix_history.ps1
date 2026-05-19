
# ============================================================
# Script: Fix Git History - PraktikumKB
# Tujuan: Rewrite commit history per pertemuan dengan tanggal yang benar
# ============================================================

Write-Host "=== Memulai perbaikan git history ===" -ForegroundColor Cyan

# Step 1: Unstage semua commit (kembalikan ke working directory)
Write-Host "`n[1/10] Reset semua commit ke working directory..." -ForegroundColor Yellow
git reset --soft HEAD~2
git rm -r --cached . | Out-Null
Write-Host "  OK - Semua file sudah di-unstage" -ForegroundColor Green

# ============================================================
# PERTEMUAN 1 - 17 Maret 2026
# ============================================================
Write-Host "`n[2/10] Commit Pertemuan 1 (17 Maret 2026)..." -ForegroundColor Yellow
$env:GIT_AUTHOR_DATE    = "2026-03-17T20:00:00+07:00"
$env:GIT_COMMITTER_DATE = "2026-03-17T20:00:00+07:00"
git add Pertemuan1/
git commit -m "Upload Tugas Praktikum KB Pertemuan 1"
Write-Host "  OK" -ForegroundColor Green

# ============================================================
# PERTEMUAN 2 - 31 Maret 2026
# ============================================================
Write-Host "`n[3/10] Commit Pertemuan 2 (31 Maret 2026)..." -ForegroundColor Yellow
$env:GIT_AUTHOR_DATE    = "2026-03-31T20:00:00+07:00"
$env:GIT_COMMITTER_DATE = "2026-03-31T20:00:00+07:00"
git add Pertemuan2/
git add LatihanPertemuan2/
git add mood_program.py
git commit -m "Upload Tugas Praktikum KB Pertemuan 2"
Write-Host "  OK" -ForegroundColor Green

# ============================================================
# PERTEMUAN 3 - 7 April 2026
# ============================================================
Write-Host "`n[4/10] Commit Pertemuan 3 (7 April 2026)..." -ForegroundColor Yellow
$env:GIT_AUTHOR_DATE    = "2026-04-07T20:00:00+07:00"
$env:GIT_COMMITTER_DATE = "2026-04-07T20:00:00+07:00"
git add Pertemuan3/
git add "Pertemuan3?README.md" 2>$null
git add README.md
git commit -m "Upload Tugas Praktikum KB Pertemuan 3"
Write-Host "  OK" -ForegroundColor Green

# ============================================================
# PERTEMUAN 4 - 14 April 2026
# ============================================================
Write-Host "`n[5/10] Commit Pertemuan 4 (14 April 2026)..." -ForegroundColor Yellow
$env:GIT_AUTHOR_DATE    = "2026-04-14T20:00:00+07:00"
$env:GIT_COMMITTER_DATE = "2026-04-14T20:00:00+07:00"
git add Pertemuan4/
git commit -m "Upload Tugas Praktikum KB Pertemuan 4"
Write-Host "  OK" -ForegroundColor Green

# ============================================================
# PERTEMUAN 5 - 21 April 2026
# ============================================================
Write-Host "`n[6/10] Commit Pertemuan 5 (21 April 2026)..." -ForegroundColor Yellow
$env:GIT_AUTHOR_DATE    = "2026-04-21T20:00:00+07:00"
$env:GIT_COMMITTER_DATE = "2026-04-21T20:00:00+07:00"
git add Pertemuan5/
git add responsi1/
git commit -m "Upload Tugas Praktikum KB Pertemuan 5"
Write-Host "  OK" -ForegroundColor Green

# ============================================================
# PERTEMUAN 6 - 12 Mei 2026
# ============================================================
Write-Host "`n[7/10] Commit Pertemuan 6 (12 Mei 2026)..." -ForegroundColor Yellow
$env:GIT_AUTHOR_DATE    = "2026-05-12T20:00:00+07:00"
$env:GIT_COMMITTER_DATE = "2026-05-12T20:00:00+07:00"
git add Pertemuan6/
git commit -m "Upload Tugas Praktikum KB Pertemuan 6"
Write-Host "  OK" -ForegroundColor Green

# ============================================================
# PERTEMUAN 7 DAN 8 - 19 Mei 2026
# ============================================================
Write-Host "`n[8/10] Commit Pertemuan 7 dan 8 (19 Mei 2026)..." -ForegroundColor Yellow
$env:GIT_AUTHOR_DATE    = "2026-05-19T20:00:00+07:00"
$env:GIT_COMMITTER_DATE = "2026-05-19T20:00:00+07:00"
git add Pertemuan7/
git add Pertemuan8/
git commit -m "Upload Tugas Praktikum KB Pertemuan 7 dan 8"
Write-Host "  OK" -ForegroundColor Green

# ============================================================
# PERTEMUAN 9 DAN 10 - 26 Mei 2026
# ============================================================
Write-Host "`n[9/10] Commit Pertemuan 9 dan 10 (26 Mei 2026)..." -ForegroundColor Yellow
$env:GIT_AUTHOR_DATE    = "2026-05-26T20:00:00+07:00"
$env:GIT_COMMITTER_DATE = "2026-05-26T20:00:00+07:00"
git add Pertemuan9/
git add Pertemuan10/
git commit -m "Upload Tugas Praktikum KB Pertemuan 9 dan 10"
Write-Host "  OK" -ForegroundColor Green

# ============================================================
# Bersihkan environment variable tanggal
# ============================================================
Remove-Item Env:GIT_AUTHOR_DATE    -ErrorAction SilentlyContinue
Remove-Item Env:GIT_COMMITTER_DATE -ErrorAction SilentlyContinue

# ============================================================
# FORCE PUSH ke GitHub
# ============================================================
Write-Host "`n[10/10] Force push ke GitHub..." -ForegroundColor Yellow
git push origin main --force
Write-Host "  OK - Selesai!" -ForegroundColor Green

Write-Host "`n=== SELESAI! Cek GitHub kamu sekarang ===" -ForegroundColor Cyan
git log --oneline
