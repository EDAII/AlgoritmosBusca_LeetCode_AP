## Alunos  
| Matrícula | Nome |  
|-----------------------|---------------------|  
| 20/2015868 | Alexandre Lema Xavier Júnior |  
| xx/xxxxxxx | xxxx xxxx xxxxx |  

## Sobre 
Resolução de questões do LeetCode (2 difíceis e 2 médias) pelos integrantes do grupo com o objetivo de demonstrar o conhecimento adquirido nesse módulo (Algoritmos de Busca) da disciplina.

## Questões

|Questão | Dificuldade |
| -- | -- |
| [1268. Search Suggestions System](https://leetcode.com/problems/search-suggestions-system/description/)| Média |
| [212. Word Search II](https://leetcode.com/problems/word-search-ii/description/)| Difícil |

### [1268 - Média](https://leetcode.com/problems/search-suggestions-system/description/) 

A questão pedia um sistema de sugestões de produtos a partir de uma lista de palavras que, a cada caractere digitado, mostrasse até três produtos com o mesmo prefixo em ordem lexicográfica. Para resolver, os produtos foram ordenados e, para cada prefixo, usou-se busca binária para encontrar rapidamente as sugestões corretas. Foram selecionados no máximo três produtos que começassem com o prefixo digitado. Assim, a solução combinou ordenação com busca binária, garantindo eficiência e atendendo aos requisitos da questão.

![Print da Resolução 1268](questoes\questao1268.jpg)
