# Revisão estática — Build 87

Data: 2026-11-23. Fonte: ZIP de sideload da Build 87 fornecido pelo mantenedor.

## Alterações feitas para preparar o código público

1. Mantida a estrutura Roku `manifest`, `source/`, `components/`, `images/`, `locale/` e `web/`.
2. Retirados dois arquivos de mosaico antigos não referenciados pelo código: `images/nuvio_profiles_mosaic_user.jpg` e `images/legacy_profiles_collage.jpg`. O fundo atualmente referenciado em login/perfis (`images/legacy_original_login_bg.jpg`) foi mantido.
3. Retirado o valor literal de uma chave fixa de fallback do YouTube em `components/tasks/TrailerTask.brs`. A rotina já buscava a configuração do YouTube em tempo de execução; adicionada uma saída segura quando nenhuma chave é encontrada.
4. Adicionados README, créditos, segurança, instruções de colaboração, scripts e CI de checagem estática.
5. Mantida a licença GPL-3.0 recebida no pacote.

## Verificações e limites

- O script `tools/check_source.py` verifica XMLs, JSONs, arquivos essenciais, caminhos de recursos literais e padrões típicos de segredos embutidos.
- A inspeção do ZIP recebido não encontrou sessões reais, e-mails ou IPs privados em arquivos de texto, com base em padrões automatizados. **Isso não é garantia absoluta de ausência de segredos**.
- Imagens, logos, ícones e fontes **não foram auditados quanto a direitos autorais**. A presença de um recurso não prova que ele possa ser redistribuído.
- Não foi executado o fluxo real de login, sincronização, catálogo, IPTV, player ou instalação no Roku físico.
- Não foi executado compilador BrightScript ou teste completo de SceneGraph; XML válido não garante canal funcional.

## Recomendações antes de divulgar a usuários finais

- Testar em Roku físico: QR, retomada de sessão, seleção de perfis, Home, Busca, Biblioteca, abertura de detalhes e player.
- Testar a seleção de fontes, canais de TV com fontes autorizadas, troca de perfil e logout.
- Revisar cada imagem/logotipo e seus direitos de redistribuição.
- Verificar licenças de dependências incorporadas e preservar os avisos de autores.
- Revisar se existe algum segredo adicional incluído indiretamente, por exemplo em imagens, metadados, endpoints e histórico Git.
