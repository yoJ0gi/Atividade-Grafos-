def criar_grafo():
    vertices = []
    arestas = []
    return vertices, arestas


def inserir_vertice(vertices, vertice):
    if vertice in vertices:
        print(f"Erro: o vértice {vertice} já existe.")
        return
    vertices.append(vertice)
    print(f"Vértice {vertice} inserido.")


def inserir_aresta(vertices, arestas, origem, destino, nao_direcionado=False):
    if origem == destino:
        print("Erro: laços (aresta de um vértice para ele mesmo) não são permitidos.")
        return
    if origem not in vertices:
        inserir_vertice(vertices, origem)
    if destino not in vertices:
        inserir_vertice(vertices, destino)
    if existe_aresta(arestas, origem, destino):
        print(f"Erro: a aresta {origem} -> {destino} já existe.")
        return
    arestas.append([origem, destino])
    if nao_direcionado:
        arestas.append([destino, origem])
    print(f"Aresta {origem} -> {destino} inserida.")


def remover_aresta(arestas, origem, destino, nao_direcionado=False):
    if not existe_aresta(arestas, origem, destino):
        print(f"Erro: a aresta {origem} -> {destino} não existe.")
        return
    for aresta in arestas:
        if aresta == [origem, destino]:
            arestas.remove(aresta)
            break
    if nao_direcionado:
        for aresta in arestas:
            if aresta == [destino, origem]:
                arestas.remove(aresta)
                break
    print(f"Aresta {origem} -> {destino} removida.")


def remover_vertice(vertices, arestas, vertice):
    if vertice not in vertices:
        print(f"Erro: o vértice {vertice} não existe.")
        return
    vertices.remove(vertice)
    for aresta in arestas[:]:
        if aresta[0] == vertice or aresta[1] == vertice:
            arestas.remove(aresta)
    print(f"Vértice {vertice} removido (junto com suas arestas).")


def existe_aresta(arestas, origem, destino):
    for aresta in arestas:
        if aresta == [origem, destino]:
            return True
    return False


def vizinhos(vertices, arestas, vertice):
    vizinhos = []
    for aresta in arestas:
        if aresta[0] == vertice:
            vizinhos.append(aresta[1])
    return vizinhos


def grau_vertices(vertices, arestas, nao_direcionado=False):
    graus = {}
    for vertice in vertices:
        if nao_direcionado:
            graus[vertice] = 0
        else:
            graus[vertice] = {"saida": 0, "entrada": 0, "total": 0}
    for aresta in arestas:
        origem = aresta[0]
        destino = aresta[1]
        if nao_direcionado:
            graus[origem] += 1
        else:
            graus[origem]["saida"] += 1
            graus[destino]["entrada"] += 1
            graus[origem]["total"] += 1
            graus[destino]["total"] += 1
    return graus


def percurso_valido(arestas, caminho):
    for i in range(len(caminho) - 1):
        u = caminho[i]
        v = caminho[i + 1]
        if not existe_aresta(arestas, u, v):
            return False
    return True


def listar_vizinhos(vertices, arestas, vertice):
    if vertice not in vertices:
        print(f"Erro: o vértice {vertice} não existe.")
        return
    lista = vizinhos(vertices, arestas, vertice)
    print(f"Vizinhos de {vertice}: {lista}")


def exibir_grafo(vertices, arestas):
    print(f"Vértices: {vertices}")
    print("Arestas:")
    for aresta in arestas:
        print(f"({aresta[0]} -> {aresta[1]})")


def ler_vertice(mensagem):
    vertice = input(mensagem).strip().upper()
    while vertice == "":
        print("Erro: o nome do vértice não pode ser vazio.")
        vertice = input(mensagem).strip().upper()
    return vertice


def main():
    print("Tipo de grafo:")
    print("1 - Não direcionado")
    print("2 - Direcionado")
    tipo = input("Escolha o tipo: ").strip()
    while tipo != "1" and tipo != "2":
        print("Opção inválida. Digite 1 ou 2.")
        tipo = input("Escolha o tipo: ").strip()
    nao_direcionado = tipo == "1"

    vertices, arestas = criar_grafo()
    for origem, destino in [["A", "B"], ["A", "C"], ["B", "C"], ["C", "D"]]:
        inserir_aresta(vertices, arestas, origem, destino, nao_direcionado)

    while True:
        print("\n========== MENU - LISTA DE ARESTAS ==========")
        print("1 - Mostrar o Grafo")
        print("2 - Inserir vértice")
        print("3 - Inserir aresta")
        print("4 - Remover vértice")
        print("5 - Remover aresta")
        print("6 - Verificar se existe aresta")
        print("7 - Listar vizinhos de um vértice")
        print("8 - Exibir grau de cada vértice")
        print("9 - Verificar se um percurso é válido")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            exibir_grafo(vertices, arestas)

        elif opcao == "2":
            vertice = ler_vertice("Nome do vértice: ")
            inserir_vertice(vertices, vertice)

        elif opcao == "3":
            origem = ler_vertice("Vértice de origem: ")
            destino = ler_vertice("Vértice de destino: ")
            inserir_aresta(vertices, arestas, origem, destino, nao_direcionado)

        elif opcao == "4":
            vertice = ler_vertice("Nome do vértice: ")
            remover_vertice(vertices, arestas, vertice)

        elif opcao == "5":
            origem = ler_vertice("Vértice de origem: ")
            destino = ler_vertice("Vértice de destino: ")
            remover_aresta(arestas, origem, destino, nao_direcionado)

        elif opcao == "6":
            origem = ler_vertice("Vértice de origem: ")
            destino = ler_vertice("Vértice de destino: ")
            if existe_aresta(arestas, origem, destino):
                print(f"Sim, existe aresta de {origem} para {destino}.")
            else:
                print(f"Não existe aresta de {origem} para {destino}.")

        elif opcao == "7":
            vertice = ler_vertice("Nome do vértice: ")
            listar_vizinhos(vertices, arestas, vertice)

        elif opcao == "8":
            graus = grau_vertices(vertices, arestas, nao_direcionado)
            for vertice in graus:
                if nao_direcionado:
                    print(f"grau({vertice}) = {graus[vertice]}")
                else:
                    print(f"{vertice}: entrada = {graus[vertice]['entrada']}, "
                          f"saída = {graus[vertice]['saida']}, "
                          f"total = {graus[vertice]['total']}")

        elif opcao == "9":
            texto = input("Digite o percurso separado por espaços (ex: A B C D): ")
            caminho = texto.upper().split()
            inexistentes = []
            for vertice in caminho:
                if vertice not in vertices:
                    inexistentes.append(vertice)
            if len(caminho) == 0:
                print("Erro: percurso vazio.")
            elif len(inexistentes) > 0:
                print(f"Percurso inválido: vértices inexistentes: {inexistentes}")
            elif percurso_valido(arestas, caminho):
                print(f"Percurso {' -> '.join(caminho)} é válido.")
            else:
                print(f"Percurso {' -> '.join(caminho)} é inválido.")

        elif opcao == "0":
            print("Encerrando o programa.")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
