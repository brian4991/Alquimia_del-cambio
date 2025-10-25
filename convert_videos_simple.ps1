$publicDir = "frontend\public"

Write-Host "Conversion video 1..." -ForegroundColor Cyan
ffmpeg -i "$publicDir\video-para-ti.mov" -vcodec libx264 -acodec aac -movflags +faststart -crf 23 -preset medium "$publicDir\video-para-ti.mp4" -y

Write-Host "Conversion video 2..." -ForegroundColor Cyan
ffmpeg -i "$publicDir\video-retiro-1.mov" -vcodec libx264 -acodec aac -movflags +faststart -crf 23 -preset medium "$publicDir\video-retiro-1.mp4" -y

Write-Host "Conversion video 3..." -ForegroundColor Cyan
ffmpeg -i "$publicDir\video-retiro-2.mov" -vcodec libx264 -acodec aac -movflags +faststart -crf 23 -preset medium "$publicDir\video-retiro-2.mp4" -y

Write-Host "Termine!" -ForegroundColor Green

