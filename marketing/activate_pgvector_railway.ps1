# Script PowerShell pour activer pgvector sur Railway via CLI

Write-Host "🚀 Activation de pgvector sur Railway..." -ForegroundColor Cyan
Write-Host ""

# Vérifier que Railway CLI est installé
try {
    $null = railway --version 2>$null
    Write-Host "✅ Railway CLI détecté" -ForegroundColor Green
} catch {
    Write-Host "❌ Railway CLI n'est pas installé." -ForegroundColor Red
    Write-Host "💡 Installe-le avec: npm install -g @railway/cli" -ForegroundColor Yellow
    exit 1
}

# Vérifier que l'utilisateur est connecté
try {
    $null = railway whoami 2>$null
} catch {
    Write-Host "❌ Tu n'es pas connecté à Railway." -ForegroundColor Red
    Write-Host "💡 Connecte-toi avec: railway login" -ForegroundColor Yellow
    exit 1
}

Write-Host ""

# Exécuter la commande SQL pour activer pgvector
Write-Host "📦 Activation de l'extension pgvector..." -ForegroundColor Cyan
railway run psql -c "CREATE EXTENSION IF NOT EXISTS vector;"

if ($LASTEXITCODE -eq 0) {
    Write-Host ""
    Write-Host "✅ pgvector activé avec succès!" -ForegroundColor Green
    Write-Host ""
    Write-Host "💡 Vérification:" -ForegroundColor Yellow
    railway run psql -c "SELECT * FROM pg_extension WHERE extname = 'vector';"
} else {
    Write-Host ""
    Write-Host "❌ Erreur lors de l'activation de pgvector" -ForegroundColor Red
    exit 1
}
