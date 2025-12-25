# Capstone 1: AI Test Case Generator using RAG

## Problem
Manual test case design from requirement documents is time-consuming and error-prone.

## Solution
An AI-powered pipeline that ingests requirement documents, retrieves relevant context using RAG,
and generates structured test cases and Playwright-ready automation skeletons.

## Architecture
PDF → Text Extraction → Chunking → Embeddings → Semantic Retrieval → LLM-based Test Generation

## Key Capabilities
- Requirement document ingestion (PDF)
- Text chunking with overlap for RAG
- Embedding generation using SentenceTransformers
- Semantic retrieval via cosine similarity
- LLM-driven test case generation
- Playwright automation-ready output

## Tech Stack
- Python
- SentenceTransformers
- Retrieval-Augmented Generation (RAG)
- Agent-based orchestration
- Playwright (output)

## Status
Completed core pipeline. LLM integration can be swapped with OpenAI / Azure / local models.
