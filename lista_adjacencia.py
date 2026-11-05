def criar_grafo():
    return {}


def inserir_vertice(grafo, vertice):
    if vertice in grafo:
        print(f"Erro: o vértice {vertice} já existe.")
        return
    grafo[vertice] = []
    print(f"Vértice {vertice} inserido.")


def inserir_aresta(grafo, origem, destino, nao_direcionado=False):
    if origem == destino:
        print("Erro: laços (aresta de um vértice para ele mesmo) não são permitidos.")
        return
    if origem not in grafo:
        inserir_vertice(grafo, origem)
    if destino not in grafo:
        inserir_vertice(grafo, destino)
    if existe_aresta(grafo, origem, destino):
        print(f"Erro: a aresta {origem} -> {destino} já existe.")
        return
    grafo[origem].append(destino)
    if nao_direcionado:
        grafo[destino].append(origem)
    print(f"Aresta {origem} -> {destino} inserida.")


def vizinhos(grafo, vertice):
    if vertice in grafo:
        return grafo[vertice]
    return []


def listar_vizinhos(grafo, vertice):
    if vertice not in grafo:
        print(f"Erro: o vértice {vertice} não existe.")
        return
    lista = vizinhos(grafo, vertice)
    print(f"Vizinhos de {vertice}: {lista}")


def exibir_grafo(grafo):
    if len(grafo) == 0:
        print("O grafo está vazio.")
        return
    for vertice in grafo:
        print(f"{vertice} -> {', '.join(grafo[vertice])}")


def remover_aresta(grafo, origem, destino, nao_direcionado=False):
    if origem not in grafo:
        print(f"Erro: o vértice {origem} não existe.")
        return
    if destino not in grafo[origem]:
        print(f"Erro: a aresta {origem} -> {destino} não existe.")
        return
    grafo[origem].remove(destino)
    if nao_direcionado:
        if destino in grafo and origem in grafo[destino]:
            grafo[destino].remove(origem)
    print(f"Aresta {origem} -> {destino} removida.")


def remover_vertice(grafo, vertice, nao_direcionado=True):
    if vertice not in grafo:
        print(f"Erro: o vértice {vertice} não existe.")
        return
    for outro in grafo:
        if vertice in grafo[outro]:
            grafo[outro].remove(vertice)
    del grafo[vertice]
    print(f"Vértice {vertice} removido (junto com suas arestas).")


def existe_aresta(grafo, origem, destino):
    if origem not in grafo:
        return False
    return destino in grafo[origem]


def grau_vertices(grafo):
    graus = {}
    for vertice in grafo:
        graus[vertice] = {"saida": 0, "entrada": 0, "total": 0}
    for u in grafo:
        graus[u]["saida"] = len(grafo[u])
        for v in grafo:
            if u in grafo[v]:
                graus[u]["entrada"] += 1
        graus[u]["total"] = graus[u]["entrada"] + graus[u]["saida"]
    return graus


def percurso_valido(grafo, caminho):
    if len(caminho) < 2:
        return True
    for i in range(len(caminho) - 1):
        origem = caminho[i]
        destino = caminho[i + 1]
        if not existe_aresta(grafo, origem, destino):
            return False
    return True


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

    grafo = criar_grafo()
    for origem, destino in [["A", "B"], ["A", "C"], ["B", "C"], ["C", "D"]]:
        inserir_aresta(grafo, origem, destino, nao_direcionado)

    while True:
        print("\n========== MENU - LISTA DE ADJACÊNCIA ==========")
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
            exibir_grafo(grafo)

        elif opcao == "2":
            vertice = ler_vertice("Nome do vértice: ")
            inserir_vertice(grafo, vertice)

        elif opcao == "3":
            origem = ler_vertice("Vértice de origem: ")
            destino = ler_vertice("Vértice de destino: ")
            inserir_aresta(grafo, origem, destino, nao_direcionado)

        elif opcao == "4":
            vertice = ler_vertice("Nome do vértice: ")
            remover_vertice(grafo, vertice, nao_direcionado)

        elif opcao == "5":
            origem = ler_vertice("Vértice de origem: ")
            destino = ler_vertice("Vértice de destino: ")
            remover_aresta(grafo, origem, destino, nao_direcionado)

        elif opcao == "6":
            origem = ler_vertice("Vértice de origem: ")
            destino = ler_vertice("Vértice de destino: ")
            if existe_aresta(grafo, origem, destino):
                print(f"Sim, existe aresta de {origem} para {destino}.")
            else:
                print(f"Não existe aresta de {origem} para {destino}.")

        elif opcao == "7":
            vertice = ler_vertice("Nome do vértice: ")
            listar_vizinhos(grafo, vertice)

        elif opcao == "8":
            graus = grau_vertices(grafo)
            for vertice in graus:
                if nao_direcionado:
                    print(f"grau({vertice}) = {graus[vertice]['saida']}")
                else:
                    print(f"{vertice}: entrada = {graus[vertice]['entrada']}, "
                          f"saída = {graus[vertice]['saida']}, "
                          f"total = {graus[vertice]['total']}")

        elif opcao == "9":
            texto = input("Digite o percurso separado por espaços (ex: A B C D): ")
            caminho = texto.upper().split()
            inexistentes = []
            for vertice in caminho:
                if vertice not in grafo:
                    inexistentes.append(vertice)
            if len(caminho) == 0:
                print("Erro: percurso vazio.")
            elif len(inexistentes) > 0:
                print(f"Percurso inválido: vértices inexistentes: {inexistentes}")
            elif percurso_valido(grafo, caminho):
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
