import csv

def criar_planilha_livros():
    livros = [
        {"Título": "1984", "Autor": "George Orwell", "Ano de publicação": 1949, "Número de páginas": 328},
        {"Título": "To Kill a Mockingbird", "Autor": "Harper Lee", "Ano de publicação": 1960, "Número de páginas": 281},
        {"Título": "The Great Gatsby", "Autor": "F. Scott Fitzgerald", "Ano de publicação": 1925, "Número de páginas": 180},
        {"Título": "Pride and Prejudice", "Autor": "Jane Austen", "Ano de publicação": 1813, "Número de páginas": 279},
        {"Título": "Moby-Dick", "Autor": "Herman Melville", "Ano de publicação": 1851, "Número de páginas": 585},
        {"Título": "War and Peace", "Autor": "Leo Tolstoy", "Ano de publicação": 1869, "Número de páginas": 1225},
        {"Título": "The Catcher in the Rye", "Autor": "J.D. Salinger", "Ano de publicação": 1951, "Número de páginas": 277},
        {"Título": "The Lord of the Rings", "Autor": "J.R.R. Tolkien", "Ano de publicação": 1954, "Número de páginas": 1216},
        {"Título": "Brave New World", "Autor": "Aldous Huxley", "Ano de publicação": 1932, "Número de páginas": 268},
        {"Título": "One Hundred Years of Solitude", "Autor": "Gabriel García Márquez", "Ano de publicação": 1967, "Número de páginas": 417}
]
    with open("meus_livros.csv", "w", newline='') as csvfile:
        fieldnames = ["Título", "Autor", "Ano de publicação", "Número de páginas"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for livro in livros:
            writer.writerow(livro)

criar_planilha_livros()
