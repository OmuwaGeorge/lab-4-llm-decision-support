# Lab 4: LLMs and Prompt Engineering for Decision Support
Duration: 2 weeks [30 Jul - 13 Aug, 2026] Due Date: 13th August, 2026 Format: Jupyter Notebook / Google Colab + external APIs + GitHub version control Grading: This is a graded lab.

Student Name: Omuwa George Student ID: 53362027

# Objective
In the previous labs you trained models. In this lab you will use a model that someone else spent millions of dollars training — a Large Language Model (LLM) — and learn that getting good results out of one is an engineering discipline of its own: prompt engineering.

You will build a decision support system for a microfinance loan officer. Given a pile of free-text loan application letters, your system will:

Summarize each application into a short, factual brief,
Extract specific structured data points (JSON) that a downstream system could store,
Produce a decision-support recommendation — while keeping the human firmly in the loop.
Just as importantly, you will evaluate the LLM's output for quality, reliability, and appropriateness: Does it hallucinate? Is it consistent across runs? Should it be trusted to make the final call?

# AI-Use Decleration: https://claude.ai/share/1e76d6db-f86d-4a80-a3d4-f0f7ce74db98
