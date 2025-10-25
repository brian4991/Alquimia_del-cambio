# Script pour convertir les vidéos MOV en MP4 compatible mobile
# Nécessite ffmpeg installé

$publicDir = "frontend\public"

Write-Host "Conversion des videos pour compatibilite mobile..." -ForegroundColor Green

# Verifier si ffmpeg est installe
try {
    ffmpeg -version | Out-Null
    Write-Host "FFmpeg trouve!" -ForegroundColor Green
} catch {
    Write-Host "ERREUR: FFmpeg n'est pas installe." -ForegroundColor Red
    Write-Host "Telechargez-le depuis: https://ffmpeg.org/download.html" -ForegroundColor Yellow
    Write-Host "Ou installez avec: winget install ffmpeg" -ForegroundColor Yellow
    exit 1
}

# Liste des videos a convertir
$videos = @(
    "video-para-ti",
    "video-retiro-1", 
    "video-retiro-2"
)

foreach ($video in $videos) {
    $input = "$publicDir\$video.mov"
    $output = "$publicDir\$video.mp4"
    
    Write-Host "`nConversion de $video.mov..." -ForegroundColor Cyan
    
    # Convertir avec codec H.264 et AAC, optimise pour mobile
    ffmpeg -i $input -vcodec libx264 -acodec aac -movflags +faststart -crf 23 -preset medium -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" $output -y
    
    if ($LASTEXITCODE -eq 0) {
        Write-Host "✓ $video.mp4 cree avec succes" -ForegroundColor Green
        
        # Afficher les tailles
        $origSize = (Get-Item $input).Length / 1MB
        $newSize = (Get-Item $output).Length / 1MB
        Write-Host "  Taille originale: $([math]::Round($origSize, 2)) MB" -ForegroundColor Gray
        Write-Host "  Nouvelle taille: $([math]::Round($newSize, 2)) MB" -ForegroundColor Gray
    } else {
        Write-Host "✗ Erreur lors de la conversion de $video" -ForegroundColor Red
    }
}

Write-Host "Conversion terminee!" -ForegroundColor Green
Write-Host "N'oubliez pas de mettre a jour les chemins dans le code JSX (.mov -> .mp4)" -ForegroundColor Yellow

