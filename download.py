import urllib.request
urls = ['https://gobiernoabierto.corrientes.gob.ar/AWS/', 'https://aws.corrientes.gob.ar/']
for url in urls:
    try:
        with urllib.request.urlopen(url) as response:
            html = response.read().decode('utf-8')
            with open(f"corrientes_{url.replace('https://', '').replace('/', '_')}.html", 'w', encoding='utf-8') as f:
                f.write(html)
            print(f"Downloaded {url}")
    except Exception as e:
        print(f"Error for {url}:", e)
