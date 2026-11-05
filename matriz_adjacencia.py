def criar_grafo():
    matriz = []
    vertices = []
    return matriz, vertices


def inserir_vertice(matriz, vertices, vertice):
    if vertice in vertices:
        print(f"Erro: o vértice {vertice} já existe.")
        return
    vertices.append(vertice)
    for linha in matriz:
        linha.append(0)
    matriz.append([0] * len(vertices))
    print(f"Vértice {vertice} inserido.")


def inserir_aresta(matriz, vertices, origem, destino, nao_direcionado=False):
    if origem == destino:
        print("Erro: laços (aresta de um vértice para ele mesmo) não são permitidos.")
        return
    if origem not in vertices:
        inserir_vertice(matriz, vertices, origem)
    if destino not in vertices:
        inserir_vertice(matriz, vertices, destino)
    i = vertices.index(origem)
    j = vertices.index(destino)
    if matriz[i][j] == 1:
        print(f"Erro: a aresta {origem} -> {destino} já existe.")
        return
    matriz[i][j] = 1
    if nao_direcionado:
        matriz[j][i] = 1
    print(f"Aresta {origem} -> {destino} inserida.")


def remover_vertice(matriz, vertices, vertice):
    if vertice not in vertices:
        print(f"Erro: o vértice {vertice} não existe.")
        return
    i = vertices.index(vertice)
    matriz.pop(i)
    for linha in matriz:
        linha.pop(i)
    vertices.remove(vertice)
    print(f"Vértice {vertice} removido (junto com suas arestas).")


def remover_aresta(matriz, vertices, origem, destino, nao_direcionado=False):
    if origem not in vertices or destino not in vertices:
        print(f"Erro: os vértices {origem} e {destino} precisam existir.")
        return
    i = vertices.index(origem)
    j = vertices.index(destino)
    if matriz[i][j] == 0:
        print(f"Erro: a aresta {origem} -> {destino} não existe.")
        return
    matriz[i][j] = 0
    if nao_direcionado:
        matriz[j][i] = 0
    print(f"Aresta {origem} -> {destino} removida.")


def existe_aresta(matriz, vertices, origem, destino):
    if origem not in vertices or destino not in vertices:
        return False
    i = vertices.index(origem)
    j = vertices.index(destino)
    return matriz[i][j] == 1


def vizinhos(matriz, vertices, vertice):
    if vertice not in vertices:
        return []
    i = vertices.index(vertice)
    lista = []
    for j in range(len(matriz[i])):
        if matriz[i][j] == 1:
            lista.append(vertices[j])
    return lista


def grau_vertices(matriz, vertices, nao_direcionado=False):
    graus = {}
    for i in range(len(vertices)):
        saida = sum(matriz[i])
        if nao_direcionado:
            graus[vertices[i]] = saida
        else:
            entrada = 0
            for linha in matriz:
                entrada += linha[i]
            graus[vertices[i]] = {"saida": saida, "entrada": entrada, "total": entrada + saida}
    return graus


def percurso_valido(matriz, vertices, caminho):
    for i in range(len(caminho) - 1):
        u = caminho[i]
        v = caminho[i + 1]
        if not existe_aresta(matriz, vertices, u, v):
            return False
    return True


def listar_vizinhos(matriz, vertices, vertice):
    if vertice not in vertices:
        print(f"Erro: o vértice {vertice} não existe.")
        return
    lista = vizinhos(matriz, vertices, vertice)
    print(f"Vizinhos de {vertice}: {lista}")


def exibir_grafo(matriz, vertices):
    if len(vertices) == 0:
        print("O grafo está vazio.")
        return
    print("  " + " ".join(vertices))
    for i in range(len(vertices)):
        valores = []
        for valor in matriz[i]:
            valores.append(str(valor))
        print(vertices[i] + " " + " ".join(valores))


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

    matriz, vertices = criar_grafo()
    for origem, destino in [["A", "B"], ["A", "C"], ["B", "C"], ["C", "D"]]:
        inserir_aresta(matriz, vertices, origem, destino, nao_direcionado)

    while True:
        print("\n========== MENU - MATRIZ DE ADJACÊNCIA ==========")
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
            exibir_grafo(matriz, vertices)

        elif opcao == "2":
            vertice = ler_vertice("Nome do vértice: ")
            inserir_vertice(matriz, vertices, vertice)

        elif opcao == "3":
            origem = ler_vertice("Vértice de origem: ")
            destino = ler_vertice("Vértice de destino: ")
            inserir_aresta(matriz, vertices, origem, destino, nao_direcionado)

        elif opcao == "4":
            vertice = ler_vertice("Nome do vértice: ")
            remover_vertice(matriz, vertices, vertice)

        elif opcao == "5":
            origem = ler_vertice("Vértice de origem: ")
            destino = ler_vertice("Vértice de destino: ")
            remover_aresta(matriz, vertices, origem, destino, nao_direcionado)

        elif opcao == "6":
            origem = ler_vertice("Vértice de origem: ")
            destino = ler_vertice("Vértice de destino: ")
            if existe_aresta(matriz, vertices, origem, destino):
                print(f"Sim, existe aresta de {origem} para {destino}.")
            else:
                print(f"Não existe aresta de {origem} para {destino}.")

        elif opcao == "7":
            vertice = ler_vertice("Nome do vértice: ")
            listar_vizinhos(matriz, vertices, vertice)

        elif opcao == "8":
            graus = grau_vertices(matriz, vertices, nao_direcionado)
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
            elif percurso_valido(matriz, vertices, caminho):
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
