# two-sum

**Link:** https://leetcode.com/problems/two-sum/
**Dificuldade:** Easy
**Tags:** Array, Hash Table

## Enunciado (resumo)

Dado um array de inteiros `nums` e um inteiro `target`, retornar os índices dos dois números que somam `target`. Assume-se exatamente uma solução, e o mesmo elemento não pode ser usado duas vezes.

## Abordagem

Força bruta seria O(n²): comparar todo par. A abordagem eficiente usa um hash map (`map[int]int` em Go / `dict` em Python) guardando `valor -> índice` conforme percorre o array. Para cada número, verifica se `target - numero` já existe no map antes de inserir o número atual. Isso resolve em uma única passada.

## Complexidade

- **Tempo:** O(n) — uma passada pelo array, lookup O(1) no hash map
- **Espaço:** O(n) — no pior caso, guarda todos os elementos no map

## Aprendizados

- Trocar espaço por tempo é o padrão clássico pra sair de O(n²) pra O(n) em problemas de "encontrar par que satisfaz condição"
- Verificar o complemento *antes* de inserir o elemento atual evita usar o mesmo índice duas vezes
