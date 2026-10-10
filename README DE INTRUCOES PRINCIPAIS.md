# 🏛️ README DE INSTRUÇÕES PRINCIPAIS — Enterprise Sovereign RAG GCP

**Repositório Oficial:** `https://github.com/Techdimbr/enterprise-sovereign-rag-gcp`  
**Classificação:** Projeto de Referência Técnica Corporativa (Padrão Open-Core)  
**Doutrina de Engenharia:** Kether_1 · Central de Tecnologia TECHDIM  
**Status Atual:** Base Canônica Homologada — Pronto para Expansão de Funções  
**Website Institucional:** https://techdimbr.github.io/techdimbr/  
**Licença:** MIT Corporate  

---

## 1. Identificação e Propósito do Projeto
- **Nome Comercial:** Enterprise Sovereign RAG GCP
- **Identificador (Slug):** `enterprise-sovereign-rag-gcp`
- **Categoria:** IA Generativa Corporativa & Busca Semântica Soberana
- **Stack Tecnológica:** Python 3.11+, Google Cloud Vertex AI, Cloud Run, Cloud Storage, Vector Search, Gemini 2.5
- **Objetivo Central:** Implementar um pipeline de ponta a ponta de RAG soberano para ambientes corporativos no Google Cloud, com ingestão automatizada de PDFs e documentos técnicos, busca vetorial em escala e geração fundamentada com Gemini sem vazamento de dados.

### Casos de Uso Reais
1. **Chat Corporativo com Documentação Técnica:** Respostas imediatas para engenheiros com citação direta de parágrafos e manuais.
2. **Análise de Contratos Jurídicos e Compliance:** Busca semântica sobre cláusulas confidenciais com preservação de sigilo.
3. **Assistente de Políticas Internas de RH:** Atendimento a dúvidas de funcionários baseado nas normas vigentes da empresa.

---

## 2. Estrutura dos Módulos em `03_APLICACAO/src/`

```text
03_APLICACAO/src/
├── rag_engine.py                      # Motor de busca semântica, cálculo de similaridade e prompt augmentation
├── ingestion.py                       # Pipeline de chunking inteligente e extração de metadados de documentos
├── vector_client.py                   # Integração com Vertex AI Vector Search / índice de embeddings
└── server.py                          # Endpoint HTTP FastAPI / Cloud Run para integração com frontends
```

---

## 3. Guia Operacional para o Desenvolvedor

1. **Bootstrap do Ambiente:**
   ```bash
   ./iniciar.sh
   ```
2. **Executar Testes Unitários:**
   ```bash
   python3 -m unittest discover 03_APLICACAO/tests
   ```
3. **Auditar Integridade Criptográfica dos Arquivos:**
   ```bash
   ./00_AUDITORIA/verificar_integridade.sh --gerar
   ```

---

## 4. Diretrizes e Regras de Negócio da Função (Para Preenchimento)
<!-- ÁREA DESTINADA À ESPECIFICAÇÃO DE NOVOS RECURSOS DO PIPELINE RAG -->
- [x] Motor matemático de similaridade de cosseno para busca de embeddings;
- [x] Sanitização de contexto com remoção de dados que infrinjam políticas de DLP;
- [ ] Integração com Vertex AI Matching Engine SDK para índices distribuídos em nuvem;
- [ ] Sistema de cache semântico de respostas para redução de latência e consumo de tokens.
