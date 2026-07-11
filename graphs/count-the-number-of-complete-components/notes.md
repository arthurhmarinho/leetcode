# count-the-number-of-complete-components

**Link:** https://leetcode.com/problems/count-the-number-of-complete-components/
**Dificuldade:** Medium
**Tags:** Graph, DFS, BFS, Union-Find

## Enunciado (resumo)

Dado um inteiro `n` (vértices numerados de `0` a `n-1`) e uma lista de arestas
não-direcionadas `edges`, retornar o número de **componentes conexas completas**.
Uma componente é **completa** quando existe aresta entre todo par dos seus vértices.

## Abordagem

Duas observações resolvem o problema:

1. **Componente conexa** — um "pedaço" do grafo onde todo vértice alcança todo
   outro. Encontramos cada uma com uma travessia (DFS/BFS) a partir de vértices
   ainda não visitados.
2. **Teste de completude (chave do problema)** — uma componente com `k` vértices
   é completa se, e somente se, tem exatamente `k·(k-1)/2` arestas (todo par
   conectado, dividido por 2 porque o grafo é não-direcionado).

Montamos uma lista de adjacência. Para cada componente, a DFS coleta os vértices
e soma os graus. Como a soma dos graus conta cada aresta **duas vezes**,
comparamos direto `soma_graus == k·(k-1)` (equivalente a `arestas == k·(k-1)/2`
sem precisar dividir).

## Complexidade

- **Tempo:** O(n + e) — cada vértice e cada aresta são visitados uma única vez
- **Espaço:** O(n + e) — lista de adjacência + array `visited` + pilha da DFS

## Aprendizados

- Reduzir "é completo?" a uma contagem de arestas (`k·(k-1)/2`) evita ter que
  checar cada par de vértices explicitamente — troca um teste O(k²) por O(1)
- Somar graus conta cada aresta 2x; comparar com `k·(k-1)` dispensa a divisão e
  evita erros de arredondamento/paridade
- DFS **iterativa com pilha** é preferível à recursiva em grafos grandes para não
  estourar o limite de recursão
- Padrão reaproveitável: "varrer todos os vértices + marcar visitados" garante
  cobrir todas as componentes, inclusive vértices isolados (que são triviamente
  completos: `k=1`, `0` arestas → `0 == 0`)
