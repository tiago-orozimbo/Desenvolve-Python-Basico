URLs = ["www.google.com", "www.gmail.com", "www.github.com", "www.reddit.com", "www.yahoo.com"]
dominios = []
for i in URLs:
    dominio = i[4:-4]
    dominios.append(dominio)
print(dominios)
