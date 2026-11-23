# Preparação para publicar o código da Build 87

A Build 87 experimental foi preparada localmente como dois artefatos distintos:

- **Código-fonte:** `NuvioTV-Roku-Codigo-Fonte-Build87-GitHub.zip`
- **Canal de teste:** `NuvioTV-Roku-Build87-Sideload-Sanitizado.zip`

**Esses ZIPs ainda não estão anexados a este repositório.** A integração GitHub foi verificada, mas o arquivo ZIP local não pode ser transferido diretamente para o serviço por esta operação de edição de texto.

## Antes de importar

- Preserve `LICENSE`, `THIRD_PARTY_NOTICES.md` e informações de autoria.
- Verifique a origem das artes e logos, e não inclua recursos para os quais não haja direito de redistribuição.
- Revise credenciais e dados privados nos arquivos e no histórico que será publicado.
- Use a pasta extraída do **código-fonte**, não um ZIP instalável como se fosse árvore Git.
- Confirme `manifest`, `source/main.brs`, `components/MainScene.xml` e os caminhos `images/`, `locale/`, `web/` quando aplicáveis.
- Execute os testes estáticos e de empacotamento disponíveis no pacote do código, depois valide autenticação, perfis, navegação e playback em Roku físico.

## Fluxo recomendado

1. Abra um clone local de `barrospxpb/NuvioTV-Roku` com GitHub Desktop.
2. Extraia o ZIP do código-fonte e copie os arquivos para o clone (sem sobrescrever inadvertidamente mudanças posteriores).
3. Revise as diferenças no GitHub Desktop, especialmente em `images/`, configurações e arquivos sensíveis.
4. Faça commit numa branch de importação e envie um Pull Request para `main`.
5. Só publique um Release após revisão e testes. Não trate a presença de uma Build 87 como aprovação para usuários finais.

## Observações sobre o snapshot

A documentação preparada localmente registra a remoção de dois mosaicos antigos não referenciados e de uma chave fixa de fallback do YouTube, que pode afetar a obtenção de trailers se a configuração dinâmica falhar. A auditoria automatizada não garante que todos os recursos tenham licenciamento adequado nem que não existam segredos fora dos padrões pesquisados.
