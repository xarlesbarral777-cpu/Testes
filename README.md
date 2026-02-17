# Multi Stream View (iniciante)

Projeto simples para estudar HTML, CSS e JavaScript criando um site que mostra várias lives ao mesmo tempo.

## Como usar

1. Abra o arquivo `index.html` no navegador.
2. Adicione um título opcional e uma URL de embed.
3. Clique em **Adicionar live**.
4. Para remover, clique em **Remover** no card.

## Como testar

### Teste rápido manual

1. Inicie um servidor local:

   ```bash
   python3 -m http.server 8000 --bind 127.0.0.1
   ```

2. Abra no navegador:

   ```
   http://127.0.0.1:8000/index.html
   ```

3. Teste o fluxo:
   - adicionar uma live com URL embed;
   - recarregar a página (deve continuar salva no `localStorage`);
   - remover a live.

### Teste automatizado

Execute:

```bash
python3 -m unittest -v tests/test_app.py
```

Esse teste valida:
- se a página principal responde `200`;
- se os elementos principais do app existem no HTML;
- se os arquivos essenciais do projeto estão presentes.

## Observações importantes

- Nem toda URL normal funciona em `iframe`.
- Em geral, você deve usar links de **embed** (incorporação).
- No Twitch, lembre-se de configurar o parâmetro `parent` com o domínio correto.

## Próximos passos (ideias)

- Escolher layouts (2x2, 3x3, foco em 1 live).
- Ajustar volume por live.
- Salvar perfis de streams favoritos.
- Adicionar autenticação para ter conta de usuário.
