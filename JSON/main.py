with open("comprar.html", "w") as compra:
    compra.write("<body> <h1> Fiz essa lista para comprar coisas pra casa, fique a vontade para adicionar</h1>")
    compra.write("<br><h2> Lembrando que só podemos levar 7 itens </h2>")
    compra.write("<br><h2> Lista: </h2>")
    compra.write("<h3>")
    item=""
    while item!="SAIR":
        item = input("Digite algo para comprar ou SAIR: ").upper()
        if item!="SAIR":
            compra.write("<br>"+f'<li>{item}</li>')
                
    compra.write("<br> <h3>Esses são todos os itens </h3>")    
    compra.write("</h3></body>")

with open("comprar.css","w") as pagina:
  pagina.write("body{color:#301868;}")