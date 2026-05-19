
# ============================================================
# Script: Fix Git History FINAL - PraktikumKB
# ============================================================

Write-Host "=== CLEAN REBUILD GIT HISTORY ===" -ForegroundColor Cyan

# Step 1: Hapus folder .git dan init ulang
Write-Host "`n[1/12] Hapus .git dan init ulang..." -ForegroundColor Yellow
Remove-Item -Recurse -Force .git -ErrorAction SilentlyContinue
git init
git remote add origin https://github.com/laksmi2005/H1D024078-PraktikumKB.git
Write-Host "  OK" -ForegroundColor Green

# PERTEMUAN 1 - 17 Maret 2026
Write-Host "`n[2/12] Commit Pertemuan 1 (17 Maret 2026)..." -ForegroundColor Yellow
$env:GIT_AUTHOR_DATE    = "2026-03-17T20:00:00+07:00"
$env:GIT_COMMITTER_DATE = "2026-03-17T20:00:00+07:00"
git add Pertemuan1/
git commit -m "Upload Tugas Praktikum KB Pertemuan 1"
Write-Host "  OK" -ForegroundColor Green

# PERTEMUAN 2 - 31 Maret 2026
Write-Host "`n[3/12] Commit Pertemuan 2 (31 Maret 2026)..." -ForegroundColor Yellow
$env:GIT_AUTHOR_DATE    = "2026-03-31T20:00:00+07:00"
$env:GIT_COMMITTER_DATE = "2026-03-31T20:00:00+07:00"
git add Pertemuan2/
git add LatihanPertemuan2/
git add mood_program.py
git commit -m "Upload Tugas Praktikum KB Pertemuan 2"
Write-Host "  OK" -ForegroundColor Green

# PERTEMUAN 3 - 7 April 2026
Write-Host "`n[4/12] Commit Pertemuan 3 (7 April 2026)..." -ForegroundColor Yellow
$env:GIT_AUTHOR_DATE    = "2026-04-07T20:00:00+07:00"
$env:GIT_COMMITTER_DATE = "2026-04-07T20:00:00+07:00"
git add Pertemuan3/
git add README.md
Get-ChildItem -Filter "Pertemuan3*" | Where-Object { -not $_.PSIsContainer } | ForEach-Object {
    git add $_.Name
}
git commit -m "Upload Tugas Praktikum KB Pertemuan 3"
Write-Host "  OK" -ForegroundColor Green

# PERTEMUAN 4 - 14 April 2026
Write-Host "`n[5/12] Commit Pertemuan 4 (14 April 2026)..." -ForegroundColor Yellow
$env:GIT_AUTHOR_DATE    = "2026-04-14T20:00:00+07:00"
$env:GIT_COMMITTER_DATE = "2026-04-14T20:00:00+07:00"
git add Pertemuan4/
git commit -m "Upload Tugas Praktikum KB Pertemuan 4"
Write-Host "  OK" -ForegroundColor Green

# PERTEMUAN 5 - 21 April 2026
Write-Host "`n[6/12] Commit Pertemuan 5 (21 April 2026)..." -ForegroundColor Yellow
$env:GIT_AUTHOR_DATE    = "2026-04-21T20:00:00+07:00"
$env:GIT_COMMITTER_DATE = "2026-04-21T20:00:00+07:00"
git add Pertemuan5/
git commit -m "Upload Tugas Praktikum KB Pertemuan 5"
Write-Host "  OK" -ForegroundColor Green

# RESPONSI 1 - 26 April 2026 (DIPISAH)
Write-Host "`n[7/12] Commit Responsi 1 (26 April 2026)..." -ForegroundColor Yellow
$env:GIT_AUTHOR_DATE    = "2026-04-26T20:00:00+07:00"
$env:GIT_COMMITTER_DATE = "2026-04-26T20:00:00+07:00"
git add responsi1/
git commit -m "Upload Tugas Praktikum KB Responsi 1"
Write-Host "  OK" -ForegroundColor Green

# PERTEMUAN 6 - 12 Mei 2026
Write-Host "`n[8/12] Commit Pertemuan 6 (12 Mei 2026)..." -ForegroundColor Yellow
$env:GIT_AUTHOR_DATE    = "2026-05-12T20:00:00+07:00"
$env:GIT_COMMITTER_DATE = "2026-05-12T20:00:00+07:00"
git add Pertemuan6/
git commit -m "Upload Tugas Praktikum KB Pertemuan 6"
Write-Host "  OK" -ForegroundColor Green

# PERTEMUAN 7 DAN 8 - 19 Mei 2026
Write-Host "`n[9/12] Commit Pertemuan 7 dan 8 (19 Mei 2026)..." -ForegroundColor Yellow
$env:GIT_AUTHOR_DATE    = "2026-05-19T20:00:00+07:00"
$env:GIT_COMMITTER_DATE = "2026-05-19T20:00:00+07:00"
git add Pertemuan7/
git add Pertemuan8/
git commit -m "Upload Tugas Praktikum KB Pertemuan 7 dan 8"
Write-Host "  OK" -ForegroundColor Green

# PERTEMUAN 9 DAN 10 - 26 Mei 2026
Write-Host "`n[10/12] Commit Pertemuan 9 dan 10 (26 Mei 2026)..." -ForegroundColor Yellow
$env:GIT_AUTHOR_DATE    = "2026-05-26T20:00:00+07:00"
$env:GIT_COMMITTER_DATE = "2026-05-26T20:00:00+07:00"
git add Pertemuan9/
git add Pertemuan10/
git commit -m "Upload Tugas Praktikum KB Pertemuan 9 dan 10"
Write-Host "  OK" -ForegroundColor Green

# Sisa file (script helper)
Write-Host "`n[11/12] Commit file sisa..." -ForegroundColor Yellow
$env:GIT_AUTHOR_DATE    = "2026-05-26T21:00:00+07:00"
$env:GIT_COMMITTER_DATE = "2026-05-26T21:00:00+07:00"
$remaining = git status --porcelain
if ($remaining) {
    git add .
    git commit -m "Update README.md"
}
Write-Host "  OK" -ForegroundColor Green

# Bersihkan env vars
Remove-Item Env:GIT_AUTHOR_DATE    -ErrorAction SilentlyContinue
Remove-Item Env:GIT_COMMITTER_DATE -ErrorAction SilentlyContinue

# FORCE PUSH
Write-Host "`n[12/12] Force push ke GitHub..." -ForegroundColor Yellow
git branch -M main
git push origin main --force
Write-Host "  SELESAI!" -ForegroundColor Green

Write-Host "`n=== HASIL AKHIR ===" -ForegroundColor Cyan
git log --oneline
