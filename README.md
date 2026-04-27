# 🌳 Daily Reflection Tree (Deterministic Decision Tree)

This project is a Python implementation of a **Deterministic Decision Tree** designed to organize and categorize daily reflections. Developed as part of the DeepThought Recruitment Assignment.

## 🚀 Project Overview
The goal is to move away from unstructured journaling and use a structured Data Structure (Tree) to map daily experiences. It uses a deterministic approach to ensure that every reflection is categorized logically without AI hallucination.

## 🛠️ Features
- **Deterministic Logic:** Uses a keyword-based classification system to filter reflections into Positive, Challenges, or General categories.
- **Tree Data Structure:** Implements an N-ary tree where each reflection is a node, allowing for organized visualization.
- **Recursive Rendering:** A custom recursive function to display the tree hierarchy in the console.

## 🧩 Technical Approach
1. **Node Class:** Created a `ReflectionNode` class to store the category, the reflection text, and a list of children.
2. **Logic Engine:** Built a `categorize_reflection` function that acts as the "Decision" part of the tree.
3. **Guardrails:** To prevent AI Hallucination (as per guidelines), I strictly defined the categories and restricted the logic to Python's core string methods instead of unpredictable NLP models.

## 💻 How to Run
1. Clone this repository.
2. Open your terminal/command prompt.
3. Run the script:
   ```bash
   python main.py
