# AnimalisCare Backend

Backend Django do projeto AnimalisCare. Este repositório organiza a base de dados, autenticação e páginas principais através de uma estrutura modular de *apps*.

## Tecnologias Principais
- Python / Django 5
- SQLite (padrão de desenvolvimento)
- HTML, CSS e JavaScript (para templates e assets estáticos)
- Timezone configurado: `America/Recife`
- Idioma padrão: `pt-br`

## Estrutura Geral
O projeto segue a convenção Django: um módulo principal (`AnimalisCare_Backend`) com configurações globais e três apps registrados em `INSTALLED_APPS`:

| App | Função principal | Observação |
|-----|------------------|-----------|
| `account` | Gerenciamento de usuários | Define um modelo de usuário customizado (`AUTH_USER_MODEL = account.User`) |
| `blog` | Publicação de conteúdo informativo | Provável suporte a posts, categorias ou artigos (código de modelos não exibido aqui) |
| `homepage` | Página(s) iniciais / institucionais | Centraliza views públicas básicas |

Abaixo um resumo raso (superficial) de cada app, conforme solicitado:

### account
Responsável por autenticação e identidade. O fato de haver `AUTH_USER_MODEL = "account.User"` indica:
- Existe (ou existirá) um modelo customizado `User` substituindo o padrão do Django.
- Possibilita extensões como campos extras (ex: telefone, tipo de perfil, etc).
- Interage com permissões e sessões via os middlewares padrão.

### blog
Provê estrutura para conteúdos dinâmicos (ex.: notícias, artigos, atualizações). Em um cenário típico:
- Modelos para Post, possivelmente com título, conteúdo, autor, data de publicação.
- Views/listagens para exibir posts no site.
- Integração futura com a homepage ou páginas internas.

### homepage
App simples para renderizar páginas principais (landing, institucional, talvez contato).
- Centraliza templates iniciais.
- Facilita separar lógica pública de outros domínios (como blog ou conta).

## Organização de Configuração
Principais pontos do arquivo de configurações:
- `INSTALLED_APPS`: inclui os três apps internos (`account`, `blog`, `homepage`).
- `TEMPLATES`: diretório extra configurado em `core/templates` além dos diretórios dos apps.
- `STATIC_ROOT` definido para coleta de arquivos estáticos em produção.
- Segurança: chave secreta presente apenas para desenvolvimento (não usar em produção).

## Executando Localmente (Desenvolvimento)
1. Criar e ativar um ambiente virtual (opcional, mas recomendado).
2. Instalar dependências (criar `requirements.txt` se ainda não existir).
3. Rodar migrações:
   ```bash
   python manage.py migrate
   ```
4. Criar superusuário (se necessário):
   ```bash
   python manage.py createsuperuser
   ```
5. Iniciar o servidor:
   ```bash
   python manage.py runserver
   ```

## Estrutura de Pastas (Simplificada)
```
AnimalisCare_Backend/
  settings.py
account/
  apps.py
blog/
  apps.py
homepage/
  apps.py
```

Seção elaborada com base apenas nos arquivos de configuração e estrutura disponível até agora. Para aprofundar, basta adicionar detalhes dos modelos, views e rotas à medida que forem implementados.
