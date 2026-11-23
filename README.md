# NuvioTV-Roku

Cliente comunitário **não oficial** do Nuvio para Roku OS, desenvolvido com **BrightScript e SceneGraph**.

> **Estado atual:** repositório público em preparação. O código-fonte da Build 87 ainda **não foi enviado para esta branch**; não há release homologada. O projeto precisa ser testado no Roku físico antes de disponibilização para usuários.

## Objetivo

Adaptar uma experiência de navegação para Roku com Home, busca, biblioteca, detalhes de títulos, fontes, TV/IPTV e player Roku, preservando uma identidade própria para o login por QR e a escolha de perfis.

## Origem e créditos

A base da implementação experimental é [Esmequiinn/NuvioTVSmart-Roku](https://github.com/Esmequiinn/NuvioTVSmart-Roku). O [NuvioTVSmart](https://github.com/NuvioMedia/NuvioTVSmart) integra a linhagem indicada pelo projeto de origem. O [Nuvio Native Legacy](https://github.com/iqui27/nuvio-native-legacy) foi uma referência visual. A colaboração e o endosso desses mantenedores **não são presumidos**.

Leia [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) antes de reutilizar ou publicar código e recursos.

## Publicação do código

Existe uma exportação preparada da **Build 87** para colaboração, mas o conteúdo dela precisa ser importado e revisado neste repositório antes de qualquer release. Veja [docs/PUBLICACAO-BUILD87.md](docs/PUBLICACAO-BUILD87.md).

Um ZIP de instalação Roku e um ZIP do código-fonte não são a mesma coisa. O código final deverá conter `manifest`, `source/`, `components/`, `images/`, `locale/` e demais arquivos necessários, mantendo os avisos de terceiros.

## Segurança e testes

Não compartilhe tokens, cookies de sessão, PINs, QR Codes válidos, credenciais, chaves privadas ou playlists privadas em commits e Issues. Faça primeiro uma revisão completa dos materiais incorporados e confirme os direitos de distribuição das artes e logos. Testes em simulador não substituem testes no hardware Roku.

## Colaboração

Issues e Pull Requests são bem-vindos! Consulte [CONTRIBUTING.md](CONTRIBUTING.md).

## Licença

Código derivado distribuído sob a [GNU GPL-3.0](LICENSE), sujeito à preservação de avisos e direitos de terceiros. Nuvio, Roku e marcas de serviços pertencem aos seus respectivos titulares. Este projeto não é oficial.
