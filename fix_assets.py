import re

with open('aws_corrientes.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace asset URLs
content = content.replace('gobiernoabierto.corrientes.gob.ar/wp-', 'gobiernoabierto.chaco.gob.ar/wp-')
content = content.replace('gobiernoabierto.corrientes.gob.ar\/wp-', 'gobiernoabierto.chaco.gob.ar\/wp-')
# Fonts, JS, etc that might not be under /wp-
content = content.replace('gobiernoabierto.corrientes.gob.ar/wp-includes', 'gobiernoabierto.chaco.gob.ar/wp-includes')
content = content.replace('gobiernoabierto.corrientes.gob.ar/wp-content', 'gobiernoabierto.chaco.gob.ar/wp-content')

# Re-save
with open('aws_corrientes.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Assets fixed.")
