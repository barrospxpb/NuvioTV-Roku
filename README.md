# NuvioTV-Roku

Cliente **não oficial** do Nuvio para Roku OS, desenvolvido com **BrightScript e SceneGraph**.

> **Status: versão experimental (Build 87).** Este repositório é um snapshot de código para colaboração e testes. A validação em um dispositivo Roku físico e os testes de integração da sessão com a conta Nuvio precisam ser feitos antes de qualquer lançamento público para usuários finais.

## Projeto e origem

Este código foi derivado principalmente de **[Esmequiinn/NuvioTVSmart-Roku](https://github.com/Esmequiinn/NuvioTVSmart-Roku)**, versão 0.1.8 IPTV, com adaptações locais na identidade visual da autenticação por QR e da seleção de perfis. A implementação do Esmequiinn deriva de iniciativas do [NuvioTVSmart](https://github.com/NuvioMedia/NuvioTVSmart) da equipe Nuvio. O projeto [Nuvio Native Legacy](https://github.com/iqui27/nuvio-native-legacy) serviu de referência visual durante o desenvolvimento; isso **não significa** que os autores dos projetos originais endossam este repositório.

Os créditos e observações de licença estão detalhados em [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) e [SOURCE-AND-LICENSE.txt](SOURCE-AND-LICENSE.txt).

## Funcionalidades presentes no código

- Interface para TV com navegação por controle remoto, Home, Busca e Biblioteca.
- Detalhes de filmes e séries, temporadas e episódios.
- Login Nuvio por QR Code e escolha de perfis.
- Seleção de fontes de vídeo e interface de reprodução Roku.
- Área de Canais de TV / IPTV, condicionada à configuração de fontes autorizadas pelo usuário.
- Interface traduzida em múltiplos idiomas.

A presença de um módulo no código **não garante** que a função esteja homologada ou operacional em todas as TVs. **Nenhuma lista IPTV, vídeo ou conta de terceiros é fornecida neste repositório.**

## Instalar para teste (modo desenvolvedor)

O Roku instala um **ZIP de canal**, diferente do ZIP de *código-fonte* disponibilizado para colaboração.

1. Instale Python 3 em seu computador.
2. Na raiz deste repositório, execute:

   ```bash
   python tools/check_source.py
   python tools/package_roku.py
   ```

3. O pacote para sideload ficará em `dist/NuvioTV-Roku-build87-sideload.zip`.
4. Ative o modo de desenvolvedor no seu Roku e faça o sideload pelo endereço de desenvolvedor do aparelho. Use apenas um dispositivo e uma conta que você tem permissão para testar.

O `package_roku.py` seleciona apenas `manifest`, `source/`, `components/`, `images/`, `web/`, `locale/` e os avisos de licença exigidos; **não** empacota documentação, scripts nem a pasta `.git`.

## Ambiente de desenvolvimento

- Roku OS com suporte a SceneGraph.
- BrightScript / SceneGraph (código em `source/` e `components/`).
- Editor de texto ou VS Code; o simulador BrightScript pode ajudar no desenvolvimento, mas **não substitui** testes no hardware real.
- Sem etapa de compilação tradicional: o canal é instalado como um ZIP com os arquivos na raiz.

## Estrutura

| Caminho | Conteúdo |
| --- | --- |
| `manifest` | Metadados do canal Roku |
| `source/` | Inicialização BrightScript |
| `components/` | Interfaces SceneGraph, lógica e tasks |
| `images/` | Recursos visuais do aplicativo |
| `locale/` | Traduções |
| `web/` | Interface local auxiliar incorporada |
| `tools/` | Auditoria estática e empacotamento |
| `docs/` | Estado dos testes e orientações para publicação |

## Notas desta distribuição pública

Este snapshot foi preparado a partir da Build 87 enviada pelo mantenedor. Em comparação com o ZIP original, as duas imagens antigas de mosaico de perfis **não utilizadas no código** foram omitidas, e uma chave fixa de fallback da API interna do YouTube foi retirada. O módulo de trailers continua tentando obter a configuração dinamicamente e pode ficar indisponível se não conseguir fazê-lo. Consulte [docs/BUILD87-AUDITORIA.md](docs/BUILD87-AUDITORIA.md).

As imagens, marcas, pôsteres e logotipos de terceiros podem ter direitos separados do código. **Revise a procedência dos recursos antes de publicar ou redistribuir comercialmente.**

## Contribuições

Issues e Pull Requests são bem-vindos. Veja [CONTRIBUTING.md](CONTRIBUTING.md). Se encontrar uma vulnerabilidade ou exposição de credenciais, siga [SECURITY.md](SECURITY.md) em vez de publicar dados sensíveis em uma issue.

## Licença e marcas

O código derivado é disponibilizado sob os termos da **GNU General Public License v3.0**. Consulte [LICENSE](LICENSE).

O nome Nuvio, as marcas dos serviços e outros materiais identificáveis pertencem aos respectivos titulares. Este projeto comunitário **não é um produto oficial** do Nuvio, do Roku, do Esmequiinn ou do Nuvio Native Legacy.
