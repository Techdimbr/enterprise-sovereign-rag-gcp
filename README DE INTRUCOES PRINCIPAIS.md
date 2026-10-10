# 🏛️ README DE INSTRUÇÕES PRINCIPAIS — Enterprise Sovereign RAG GCP

**Repositório Oficial:** `https://github.com/Techdimbr/enterprise-sovereign-rag-gcp`  
**Classificação:** Projeto de Referência Técnica Corporativa (Padrão Open-Core)  
**Doutrina de Engenharia:** Kether_1 · Central de Tecnologia TECHDIM  
**Status Atual:** Estrutura Base Canônica Homologada — Aguardando Desenvolvimento da Função  
**Website Institucional:** https://techdimbr.github.io/techdimbr/  
**Licença:** MIT Corporate  

---

## 1. Identificação e Propósito do Projeto
- **Nome Comercial:** Enterprise Sovereign RAG GCP
- **Identificador (Slug):** `enterprise-sovereign-rag-gcp`
- **Categoria:** IA Generativa Corporativa & Busca Semântica Soberana
- **Stack Tecnológica:** Python, Cloud Run, Vertex AI, Cloud Storage, Vector Search
- **Objetivo Central:** Pipeline de Retrieval-Augmented Generation (RAG) soberano e seguro no Google Cloud. Garante que os dados corporativos indexados não sejam utilizados para treinamento de modelos públicos, operando com governança de IAM e encriptação ponta a ponta.

### Principais Casos de Uso Previstos
- Consulta semântica sobre bases documentais corporativas confidenciais via Vertex AI
- Isolamento criptográfico total de embeddings vetoriais com controle estrito de acesso IAM
- Integração com aplicações internas mantendo conformidade e sigilo empresarial irrestrito

---

## 2. Estrutura Operacional Canônica
Este repositório foi construído sobre a arquitetura canônica **PRJ-TECHDIM-PUBLIC-v1.0.0**:
- `00_AUDITORIA/`: Verificação criptográfica de integridade SHA-256 (`./00_AUDITORIA/verificar_integridade.sh`).
- `01_SOBRE_O_PROJETO/`: Documentação de requisitos, casos de uso e roadmap de desenvolvimento.
- `02_COMO_USAR/`: Procedimentos operacionais padrão (SOP), pré-requisitos e configurações.
- `03_APLICACAO/`: Núcleo de código (`src/`) e suite de testes automatizados (`tests/`).
- `04_INTELIGENCIA_DE_DESENVOLVIMENTO/`: Decisões de arquitetura (ADRs) e regras de contexto para agentes de IA.
- `05_VERSOES/`: Controle semântico de versões (`CHANGELOG.md`).
- `06_MIDIA/`: Material de apresentação executiva e ficha técnica.

---

## 3. Instruções Iniciais para Início do Desenvolvimento
Quando for iniciar o desenvolvimento da função específica:
1. **Ativação e Validação Inicial:**
   ```bash
   ./iniciar.sh
   ```
   *O bootstrap verificará o ambiente Debian/Linux, dependências e ativará os pre-commit hooks de proteção Zero Leaks.*

2. **Implementação do Core:**
   - Codifique a lógica da solução dentro do diretório `03_APLICACAO/src/`.
   - Mantenha o código modular, desacoplado e documentado.

3. **Criação e Execução de Testes:**
   - Escreva testes unitários e de integração em `03_APLICACAO/tests/`.
   - Valide a execução com:
     ```bash
     python3 -m unittest discover 03_APLICACAO/tests
     ```

4. **Auditoria de Integridade Criptográfica:**
   - Antes de efetuar novos commits de versão, atualize o manifesto SHA-256 executando:
     ```bash
     ./00_AUDITORIA/verificar_integridade.sh --gerar
     ```

---

## 4. Diretrizes e Regras de Negócio a Preencher
<!-- PREENCHA ESTA SEÇÃO COM AS DIRETRIZES ESPECÍFICAS DA FUNÇÃO QUANDO FOR INICIAR O DESENVOLVIMENTO -->
> **[ESPAÇO RESERVADO PARA DETALHAMENTO DA FUNÇÃO]**
> - Inserir aqui os casos de uso detalhados;
> - Inserir aqui parâmetros de entrada, saída e esquemas de dados;
> - Inserir requisitos específicos de bibliotecas e integração de APIs externas;
> - Inserir regras de segurança específicas para o ambiente de execução.
