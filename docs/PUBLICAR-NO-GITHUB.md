# Como colocar a Build 87 no GitHub público

Repositório criado: https://github.com/barrospxpb/NuvioTV-Roku

**Atenção:** o ZIP de código-fonte que você recebeu precisa ser **extraído** antes do envio ao GitHub. Não envie apenas o ZIP como se ele fosse o projeto: isso dificultaria muito a colaboração.

## Método mais fácil no Windows — GitHub Desktop

1. Instale [GitHub Desktop](https://desktop.github.com/) e entre com sua conta GitHub.
2. Escolha **File → Clone repository** e selecione `barrospxpb/NuvioTV-Roku`.
3. Clique em **Show in Explorer** para abrir a pasta do repositório clonado.
4. **Extraia** o pacote `NuvioTV-Roku-Codigo-Fonte-Build87-GitHub.zip` para uma pasta temporária.
5. Copie **todo o conteúdo de dentro do ZIP** (incluindo `manifest`, pastas `components`, `images`, `source`, `locale`, `web`, `tools`, `docs`, `.github`, `.gitignore` etc.) para **dentro da pasta clonada**, substituindo o `README.md` e `LICENSE` existentes. Não apague a pasta oculta `.git` do clone.
6. No GitHub Desktop, revise a lista de alterações e confirme que não há tokens, chaves, playlists privadas ou arquivos pessoais.
7. Informe um resumo de commit, por exemplo `Add Roku Build 87 community source`, e clique **Commit to main**.
8. Clique **Push origin**. O código ficará público imediatamente.

## Usando Git pelo terminal (alternativa)

```bash
git clone https://github.com/barrospxpb/NuvioTV-Roku.git
cd NuvioTV-Roku
# Copie aqui os arquivos EXTRAÍDOS do ZIP preparado; preserve .git/
python tools/check_source.py
git add .
git commit -m "Add Roku Build 87 community source"
git push origin main
```

## Antes de clicar em Push origin

- Leia `docs/BUILD87-AUDITORIA.md` e `THIRD_PARTY_NOTICES.md`.
- Verifique a procedência dos recursos visuais e o uso de marcas de terceiros.
- Confirme que o código não contém segredos ou informações pessoais.
- Não confunda o ZIP de **código-fonte** com o ZIP do **canal Roku** para sideload.
- Para gerar o ZIP de sideload a partir do código publicado, execute `python tools/package_roku.py`.

## Compartilhar com os desenvolvedores

Envie o link do GitHub para @Esmequiinn e @iqui27 e diga que é um fork/adaptação experimental e que sugestões e pull requests são bem-vindos. Peça que revisem os componentes reutilizados e os termos de contribuição.
