from bs4 import BeautifulSoup
import json

with open('aws_corrientes.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

print("Extracting...")
