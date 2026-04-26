import re

with open('/Users/boscojfrancisco/AWS/AWS/aws_chaco.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace Chaco with Corrientes
content = content.replace('Chaco', 'Corrientes')
content = content.replace('CHACO', 'CORRIENTES')
content = content.replace('chaco.gob.ar', 'corrientes.gob.ar')
content = content.replace('chaco', 'corrientes')

# Content replacements:
# Title update
content = content.replace('<title>Amazon entrena Argentina &#8211; Gobierno Abierto.</title>', '<title>AWS Desarrolla Argentina &#8211; Gobierno Abierto Corrientes.</title>')

# Update CTA Link
# The CTA is Postulate aquí
content = re.sub(r'href="https://argentina\.awsentrena\.com/[^"]*"', 'href="https://argentina.awsentrena.com/#/libraries?id=772a7a2d-10f3-4e7f-981c-cdd5a981af26"', content)

# Check if AWS Entrena is still there, replace it to AWS Desarrolla if it's the main header, but in menus maybe leave it?
# The task says: "3- el conitenido del programa cambiar a AWS Desarrolla, texto del body del html debe ser lo que tiene  este sitio, como ser que es aws desarrolla, como participar, obejetivos del programa, etc https://gobiernoabierto.chaco.gob.ar/aws-desarrolla/"
# But aws_chaco.html already has "¿Qué es AWS Desarrolla?", "¿CÓMO PARTICIPAR?", etc. (see line 336, 355). 
# Wait, did I look at aws_chaco.html and see it already has that? Yes, my view_file showed it!
# Wait, let me check the title tag and other occurrences of AWS Entrena.

with open('/Users/boscojfrancisco/AWS/AWS/aws_chaco.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated text.")
