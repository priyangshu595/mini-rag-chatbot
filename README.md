# 🏗️ Mini RAG Chatbot for Construction Assistant

## 🚀 Live Demo
🔗 Frontend: https://mini-rag-chatbot.vercel.app/  
🔗 Backend API: https://mini-rag-chatbot-5n1r.onrender.com/

---

## 📌 Overview

This project implements a **Retrieval-Augmented Generation (RAG)** system that answers user queries using internal construction-related documents (policies, FAQs, specifications).

Instead of relying on general knowledge, the system retrieves relevant document chunks and generates **grounded, explainable answers**.

---

## 🧠 Key Features

- 🔍 Semantic search using embeddings
- 📚 Context-aware answer generation
- 🚫 Hallucination control ("I don't know" fallback)
- 📊 Transparent output (context + answer)
- 💬 ChatGPT-style interactive UI
- 🔄 Supports both API-based and local LLMs

---

## 🏗️ System Architecture

### 🔹 Offline Phase (Indexing)

1. Documents are loaded from the `data/` directory  
2. Text is split into chunks (~200 words)  
3. Each chunk is converted into embeddings  
4. Embeddings are stored in a FAISS vector index  

---

### 🔹 Online Phase (Query Handling)

1. User submits a query  
2. Query is converted into embedding  
3. FAISS retrieves top-k relevant chunks  
4. Retrieved chunks are passed as context to LLM  
5. LLM generates grounded answer  

---

## ⚙️ Tech Stack

- **Embedding Model:** `all-MiniLM-L6-v2` (Sentence Transformers)  
  - Lightweight, fast, and effective for semantic similarity  

- **Vector Database:** FAISS  
  - Efficient similarity search over embeddings  

- **LLM (Primary):** OpenRouter (`openai/gpt-3.5-turbo`)  
  - High-quality, fast, and reliable  

- **LLM (Bonus - Local):** Ollama (`phi3`)  
  - Runs locally without API usage  

- **Backend:** FastAPI  
- **Frontend:** HTML, CSS, JavaScript (custom chat UI)  

---

## 🧩 Document Processing

- Documents are chunked into meaningful segments (~200 words)
- Chunking ensures:
  - Better retrieval accuracy  
  - Efficient use of LLM context window  

---

## 🔍 Retrieval Mechanism

- Query is embedded using Sentence Transformers  
- FAISS performs similarity search  
- Top-k (k=3) relevant chunks are retrieved  

---

## 🤖 Grounded Answer Generation

- LLM is strictly instructed to:
  - Answer only from retrieved context  
  - Avoid adding external knowledge  
  - Respond with **"I don't know"** if answer is missing  

- Prompt engineering ensures:
  - Structured output  
  - Bullet-point formatting  
  - Clarity and conciseness  

---

## 🔎 Transparency & Explainability

The system explicitly displays:

- 📄 Retrieved document chunks  
- 💡 Final generated answer  

This ensures:
- Trustworthiness  
- Explainability  
- Debuggability  

---

## 🎨 UI Features

- ChatGPT-style interface  
- Chat bubbles (user + assistant)  
- Auto-scroll and typing indicator  
- Structured answer formatting (bullet points)  

---

## 🧪 Quality Analysis (Bonus)

The system was evaluated using 10+ queries derived from the provided documents, covering factual, reasoning-based, and out-of-scope scenarios.

---

### 📋 Test Questions

1. What is escrow-based payment?
2. How are contractor payments released?
3. What mechanisms are used to prevent delays?
4. How does the system ensure quality?
5. What are the critical checkpoints?
6. How does daily tracking help?
7. Why is penalisation used?
8. How does the system ensure transparency?
9. What materials are used in construction? *(out-of-scope)*
10. What is the cost of construction? *(out-of-scope)*

---

### 📊 Evaluation Results

| Query | Retrieval Relevance | Answer Quality | Hallucination | Completeness |
|------|-------------------|---------------|--------------|-------------|
| Escrow payment | High | High | No | Complete |
| Delay management | High | High | No | Complete |
| Quality system | High | High | No | Complete |
| Materials used | Low | Correct fallback | No | N/A |

---

### 🔍 Observations

- Retrieved chunks were highly relevant for most queries.
- The system successfully avoided hallucinations by responding **"I don't know"** for out-of-scope questions.
- Answer quality was strongly dependent on retrieval accuracy.
- Responses were clear, structured, and easy to understand.

---

## 🔄 LLM Comparison (Bonus)

| Metric | OpenRouter (GPT-3.5) | Local (Phi-3 via Ollama) |
|--------|---------------------|--------------------------|
| Answer Quality | High | Moderate |
| Latency | Fast | Slower |
| Cost | Paid | Free |
| Groundedness | Strong | Slightly weaker |

---