# add-two-numbers

**Link:** https://leetcode.com/problems/add-two-numbers/
**Dificuldade:** Medium
**Tags:** Linked List, Math, Recursion

## Enunciado (resumo)

Duas listas encadeadas não-vazias representam dois inteiros não-negativos, com os
dígitos armazenados em **ordem reversa** (a cabeça é a unidade). Somar os dois
números e retornar o resultado como uma nova lista encadeada, também em ordem
reversa. Não há zeros à esquerda, exceto o próprio número `0`.

## Abordagem

Como os dígitos já vêm em ordem reversa, eles estão alinhados exatamente na ordem
em que a **soma escrita à mão** acontece: unidade com unidade, dezena com dezena,
etc. Basta percorrer as duas listas em paralelo somando dígito a dígito e
propagando o "vai-um" (`carry`).

1. Uso um nó **sentinela** (`dummy`) para não tratar a criação da cabeça como caso
   especial; `tail` aponta sempre para o último nó do resultado.
2. A cada passo somo `l1->val + l2->val + carry`. O dígito gravado é `sum % 10` e
   o novo carry é `sum / 10` (sempre 0 ou 1).
3. A condição do laço é `l1 || l2 || carry`: continua enquanto sobrar dígito em
   qualquer lista **ou** ainda houver vai-um pendente. Isso cobre listas de
   tamanhos diferentes e o carry final (ex.: `[9,9] + [1] = [0,0,1]`).

## Complexidade

- **Tempo:** O(max(n, m)) — uma passada única pela lista mais longa
- **Espaço:** O(max(n, m)) — a lista de saída (o `dummy`/ponteiros são O(1))

## Aprendizados

- Guardar dígitos em **ordem reversa** é o que torna a soma trivial: elimina a
  necessidade de inverter listas ou usar pilha para alinhar as unidades
- O **nó sentinela** (`dummy`) remove o `if` de "primeiro nó" — padrão recorrente
  em construção de listas encadeadas
- Incluir `carry` na condição de parada evita esquecer o vai-um final, o bug mais
  comum nesse problema (ex.: `999 + 1`)
- Em C++, `11`/`12` (números) e `l1`/`l2` (letra L) são visualmente parecidos em
  algumas fontes — um typo assim gera dezenas de erros de compilação em cascata,
  já que o identificador `11` nem é válido

