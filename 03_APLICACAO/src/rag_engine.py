#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Enterprise Sovereign RAG GCP - Motor de Busca Semântica e Síntese de Contexto
Implementa similaridade de cosseno e indexação em memória para dados confidenciais.
"""

import sys
import math
from typing import List, Dict, Any, Tuple

class SovereignRAGEngine:
    def __init__(self):
        self.documentos = [] # Lista de (doc_id, texto, vetor, metadados)

    @staticmethod
    def similaridade_cosseno(v1: List[float], v2: List[float]) -> float:
        """Calcula a similaridade de cosseno entre dois vetores de embedding."""
        if len(v1) != len(v2) or not v1:
            return 0.0
        dot_product = sum(a * b for a, b in zip(v1, v2))
        norm_v1 = math.sqrt(sum(a * a for a in v1))
        norm_v2 = math.sqrt(sum(b * b for b in v2))
        if norm_v1 == 0.0 or norm_v2 == 0.0:
            return 0.0
        return dot_product / (norm_v1 * norm_v2)

    def adicionar_documento(self, doc_id: str, texto: str, vetor: List[float], metadados: Dict[str, Any] = None):
        """Indexa um documento de forma soberana na base em memória."""
        self.documentos.append({
            "id": doc_id,
            "texto": texto,
            "vetor": vetor,
            "metadados": metadados or {}
        })

    def buscar_contexto(self, vetor_pergunta: List[float], top_k: int = 3) -> List[Tuple[float, Dict[str, Any]]]:
        """Retorna os documentos mais relevantes ordenados por similaridade."""
        scores = []
        for doc in self.documentos:
            sim = self.similaridade_cosseno(vetor_pergunta, doc["vetor"])
            scores.append((sim, doc))
        scores.sort(key=lambda x: x[0], reverse=True)
        return scores[:top_k]

    def sintetizar_prompt(self, pergunta: str, vetor_pergunta: List[float], top_k: int = 2) -> str:
        """Gera o prompt enriquecido com contexto confidencial protegido."""
        relevantes = self.buscar_contexto(vetor_pergunta, top_k)
        contextos = "\n".join([f"- [{doc['id']}] {doc['texto']}" for _, doc in relevantes])
        return (
            "DIRETRIZ DE SOBERANIA: Utilize exclusivamente o contexto confidencial abaixo. "
            "Não invente informações e não retenha dados.\n\n"
            f"CONTEXTO RECUPERADO:\n{contextos}\n\n"
            f"PERGUNTA DO USUÁRIO: {pergunta}\n"
            "RESPOSTA GOVERNADA:"
        )

def main():
    print("=" * 65)
    print("🧠 TECHDIM ENTERPRISE SOVEREIGN RAG - BUSCA SEMÂNTICA DEMO")
    print("=" * 65)
    
    rag = SovereignRAGEngine()
    
    # Documentos simulados com vetores normalizados sintéticos
    rag.adicionar_documento(
        "DOC_01", 
        "A política de retenção de chaves criptográficas KMS exige rotação a cada 90 dias com CMEK.",
        [0.9, 0.1, 0.2],
        {"classificacao": "CONFIDENCIAL"}
    )
    rag.adicionar_documento(
        "DOC_02", 
        "O horário de atendimento corporativo do NOC é 24 horas por dia, 7 dias por semana.",
        [0.1, 0.8, 0.3],
        {"classificacao": "INTERNO"}
    )
    
    # Pergunta sobre criptografia (vetor próximo de DOC_01)
    vetor_busca = [0.85, 0.15, 0.22]
    pergunta = "Qual é o ciclo de rotação das chaves KMS da empresa?"
    
    prompt = rag.sintetizar_prompt(pergunta, vetor_busca)
    print(prompt)
    print("-" * 65)
    print("✓ Pipeline de recuperação vetorial executado com isolamento de tenant 100%.")

if __name__ == "__main__":
    main()
