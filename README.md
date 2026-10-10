# 🧠 Enterprise Sovereign RAG GCP
## Arquitetura de IA Generativa Soberana e Busca Semântica Empresarial no Google Cloud

![Enterprise Sovereign RAG GCP](06_MIDIA/banner_oficial.png)

[![Padrão](https://img.shields.io/badge/Padr%C3%A3o-PRJ--TECHDIM--PUBLIC--v1.0.0-00E5FF.svg)](https://techdimbr.github.io/techdimbr/)
[![Doutrina](https://img.shields.io/badge/Doutrina-KETHER__1-7C4DFF.svg)](https://www.techdim.com.br)
[![IA Engine](https://img.shields.io/badge/Vertex%20AI-Vector%20Search%20%7C%20Gemini-4285F4.svg)](https://cloud.google.com/vertex-ai)
[![Privacidade](https://img.shields.io/badge/Zero%20Training%20Leak-Data%20Sovereignty-00C853.svg)](README.md)
[![Computação](https://img.shields.io/badge/Runtime-Cloud%20Run%20Serverless-FF6F00.svg)](https://cloud.google.com/run)
[![Licença](https://img.shields.io/badge/Licen%C3%A7a-MIT%20Corporate-green.svg)](LICENSE)

> **Pipeline de Retrieval-Augmented Generation (RAG) soberano para dados corporativos confidenciais. Garante que nenhum documento interno seja utilizado para retreinamento de modelos de terceiros, com encriptação de ponta a ponta e controle estrito de acesso via Cloud IAM.**

---

## 🏛️ Visão Geral & Proposta de Valor

Empresas enfrentam um dilema crítico: como permitir que colaboradores usem Inteligência Artificial Generativa para consultar documentos internos (estratégias, contratos, código proprietário) sem correr o risco de exfiltração de dados ou de alimentar o treinamento de LLMs comerciais abertas?

O **Enterprise Sovereign RAG GCP** resolve essa barreira com uma infraestrutura corporativa soberana:
1. **Zero Data Training Guarantee:** Utiliza contratos corporativos da Vertex AI e APIs do Google Cloud onde os dados nunca saem do tenant seguro do cliente e não são retidos para treinamento de modelos fundacionais.
2. **Busca Vetorial em Milissegundos:** Indexa bases documentais com `text-embedding-004` e gerencia consultas semânticas no Vertex AI Vector Search com suporte a bilhões de vetores.
3. **Governança Granular de Acesso:** Cada consulta ao RAG valida as permissões de acesso do colaborador, garantindo que um analista não receba resumos de documentos restritos à diretoria.

---

## 🏗️ Topologia da Arquitetura RAG Soberana

```mermaid
graph TD
    User["Colaborador / Aplicação Interna"] -->|Pergunta em Linguagem Natural| Gateway["API Gateway / Cloud Run (Auth IAM)"]
    Gateway -->|Validação de Permissão & Token| Embed["Vertex AI text-embedding-004"]
    Embed -->|Vetor de Consulta| VectorDB["Vertex AI Vector Search (Índice Isolado)"]
    VectorDB -->|Trechos Mais Relevantes| Rerank["Filtro Soberano & Re-ranking"]
    Rerank -->|Contexto Enriquecido + Prompt Blindado| Gemini["Google Gemini 2.5 Pro (Tenant Privado)"]
    Gemini -->|Resposta Precisa com Citações| User
```

---

## ⚡ Início Rápido

### Comandos de Operação
```bash
# 1. Clonar o repositório
git clone https://github.com/Techdimbr/enterprise-sovereign-rag-gcp.git
cd enterprise-sovereign-rag-gcp

# 2. Inicializar o ambiente
./iniciar.sh

# 3. Testar a busca semântica em memória governada
python3 03_APLICACAO/src/rag_engine.py --demo
```

---

## 🛡️ Governança & Contato Corporativo
- **Autor:** Deivis Írio Mayer (Kether_1)
- **Entidade:** TECHDIM INOVA SIMPLES (I.S.) - ME · CNPJ 61.933.926/0001-24
- **Website Oficial:** [https://www.techdim.com.br](https://www.techdim.com.br)
- **Portal de Soluções:** [https://techdimbr.github.io/techdimbr/](https://techdimbr.github.io/techdimbr/)
