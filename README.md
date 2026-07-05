# LeetCode

Repositório de estudo contínuo para manter a lógica de programação afiada. Soluções organizadas por tópico, com anotações de complexidade e abordagem para revisão futura.

## Progresso

| # | Problema | Tópico | Dificuldade | Linguagem | Status |
|---|----------|--------|-------------|-----------|--------|
| 1 | [Two Sum](arrays/two-sum) | Arrays | Easy | Go, Python | ✅ |

## Estrutura

```
leetcode/
├── arrays/
│   └── two-sum/
│       ├── solution.go
│       ├── solution.py
│       └── notes.md
├── strings/
├── linked-lists/
├── trees/
├── graphs/
├── dynamic-programming/
├── greedy/
├── backtracking/
├── sorting-searching/
├── stack-queue/
├── heap/
├── bit-manipulation/
├── math/
├── two-pointers/
├── sliding-window/
└── scripts/
    └── new_problem.sh
```

Cada problema tem sua própria pasta contendo:
- **solution.{ext}** — implementação da solução
- **notes.md** — enunciado resumido, abordagem, complexidade (tempo/espaço) e aprendizados

## Novo problema

Use o script para criar a estrutura automaticamente:

```bash
./scripts/new_problem.sh <topico> <nome-do-problema>
# exemplo:
./scripts/new_problem.sh dynamic-programming climbing-stairs
```

## Convenções

- Nomes de pasta em `kebab-case`, iguais ao slug do LeetCode (ex: `two-sum`, `longest-substring-without-repeating-characters`)
- `notes.md` sempre preenchido com complexidade Big O e a intuição da solução — é o que mais vale para revisão antes de entrevistas
- Commits atômicos: um problema por commit, com mensagem no padrão `feat(topico): nome-do-problema`

## Estatísticas

- Total resolvido: **1**
- Easy: 1 | Medium: 0 | Hard: 0
