import sys
import io

# Read the file
with open('create_exercises_module4_all.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace problematic characters
# Replace straight quotes with curly quotes or escape them
content = content.replace('"Debo', '"Debo')
content = content.replace('"Si exp', '"Si exp')
content = content.replace('"No soy', '"No soy')
content = content.replace('"Siempre', '"Siempre')
content = content.replace('"Soy', '"Soy')
content = content.replace('"Estoy', '"Estoy')
content = content.replace('"Cada', '"Cada')
content = content.replace('"Los', '"Los')
content = content.replace('"Confío', '"Confío')
content = content.replace('"Hoy', '"Hoy')

# Write back
with open('create_exercises_module4_all.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fichier corrigé!")

