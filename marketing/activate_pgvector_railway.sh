#!/bin/bash
# Script pour activer pgvector sur Railway via CLI

echo "🚀 Activation de pgvector sur Railway..."
echo ""

# Vérifier que Railway CLI est installé
if ! command -v railway &> /dev/null; then
    echo "❌ Railway CLI n'est pas installé."
    echo "💡 Installe-le avec: npm install -g @railway/cli"
    exit 1
fi

# Vérifier que l'utilisateur est connecté
if ! railway whoami &> /dev/null; then
    echo "❌ Tu n'es pas connecté à Railway."
    echo "💡 Connecte-toi avec: railway login"
    exit 1
fi

echo "✅ Railway CLI détecté"
echo ""

# Exécuter la commande SQL pour activer pgvector
echo "📦 Activation de l'extension pgvector..."
railway run psql -c "CREATE EXTENSION IF NOT EXISTS vector;"

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ pgvector activé avec succès!"
    echo ""
    echo "💡 Vérification:"
    railway run psql -c "SELECT * FROM pg_extension WHERE extname = 'vector';"
else
    echo ""
    echo "❌ Erreur lors de l'activation de pgvector"
    exit 1
fi
