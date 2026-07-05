#!/usr/bin/env bash
# Gera a estrutura de pastas/arquivos para um novo problema de LeetCode.
#
# Uso:
#   ./scripts/new_problem.sh <topico> <nome-do-problema>
#
# Exemplo:
#   ./scripts/new_problem.sh dynamic-programming climbing-stairs

set -euo pipefail

if [ "$#" -ne 2 ]; then
  echo "Uso: $0 <topico> <nome-do-problema>"
  echo "Exemplo: $0 arrays two-sum"
  exit 1
fi

TOPIC="$1"
NAME="$2"
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PROBLEM_DIR="$ROOT_DIR/$TOPIC/$NAME"

if [ -d "$PROBLEM_DIR" ]; then
  echo "Erro: a pasta '$PROBLEM_DIR' já existe."
  exit 1
fi

mkdir -p "$PROBLEM_DIR"

cat > "$PROBLEM_DIR/notes.md" <<EOF
# $NAME

**Link:** https://leetcode.com/problems/$NAME/
**Dificuldade:**
**Tags:**

## Enunciado (resumo)



## Abordagem



## Complexidade

- **Tempo:** O(?)
- **Espaço:** O(?)

## Aprendizados


EOF

cat > "$PROBLEM_DIR/solution.go" <<EOF
package main

// $NAME
// https://leetcode.com/problems/$NAME/
EOF

cat > "$PROBLEM_DIR/solution.py" <<EOF
"""
$NAME
https://leetcode.com/problems/$NAME/
"""
EOF

echo "Estrutura criada em: $PROBLEM_DIR"
echo "Não esqueça de atualizar a tabela de progresso no README.md"
