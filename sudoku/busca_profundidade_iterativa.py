from arvore import Nodo as Node


def buscar(node: Node, target, limit, atual):
    if atual > limit:
        return False

    if node is None:
        return None

    if node.objeto == target:
        return node

    for child in node.children:
        result = buscar(child, target, limit, atual + 1)
        if result is not None:
            return result

    return None


# Exemplo de uso
if __name__ == "__main__":
    # Criando uma árvore simples
    root = Node(1)
    root.add_child(Node(2))
    root.add_child(Node(3))
    root.children[0].add_child(Node(4))
    root.children[0].add_child(Node(5))
    root.children[1].add_child(Node(6))

    target_value = 5
    result = buscar(root, target_value)

    if result:
        print(f"Encontrado o nó com valor {target_value}")
    else:
        print(f"Nó com valor {target_value} não encontrado na árvore")
