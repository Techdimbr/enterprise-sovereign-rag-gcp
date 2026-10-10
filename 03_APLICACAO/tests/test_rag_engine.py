#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Testes unitários para o motor do Enterprise Sovereign RAG GCP.
"""

import unittest
import sys
from pathlib import Path

SRC_DIR = Path(__file__).resolve().parent.parent / "src"
sys.path.insert(0, str(SRC_DIR))

from rag_engine import SovereignRAGEngine

class TestSovereignRAGEngine(unittest.TestCase):
    def setUp(self):
        self.rag = SovereignRAGEngine()

    def test_similaridade_cosseno_identicos(self):
        v1 = [1.0, 0.0, 0.0]
        v2 = [1.0, 0.0, 0.0]
        self.assertAlmostEqual(self.rag.similaridade_cosseno(v1, v2), 1.0)

    def test_similaridade_cosseno_ortogonais(self):
        v1 = [1.0, 0.0]
        v2 = [0.0, 1.0]
        self.assertAlmostEqual(self.rag.similaridade_cosseno(v1, v2), 0.0)

    def test_recuperacao_ranqueada(self):
        self.rag.adicionar_documento("A", "Doc A", [1.0, 0.0])
        self.rag.adicionar_documento("B", "Doc B", [0.0, 1.0])
        
        # Busca mais próxima de A
        resultados = self.rag.buscar_contexto([0.9, 0.1], top_k=1)
        self.assertEqual(len(resultados), 1)
        self.assertEqual(resultados[0][1]["id"], "A")

if __name__ == "__main__":
    unittest.main()
