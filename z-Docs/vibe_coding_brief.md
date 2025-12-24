# Project Brief: Vibe-Coding AI Agents (The Antigravity Workflow)

## 1. Overview
This project establishes a collaborative workflow between **You (The User)** and **Antigravity (The AI Agent)**. The goal is to build sophisticated AI Agents from scratch, leveraging your Python knowledge while bypassing the steep learning curve of advanced AI engineering. We call this "Vibe-Coding": you provide the *vibe* (intent, logic, and creative direction), and Antigravity handles the heavy lifting, explaining the *how* and *why* along the way.

## 2. The Core Philosophy
- **Vibe-Coding**: You don't need to know the syntax for every LLM API or vector database. You need to know *what* you want to build. You drive the car; Antigravity builds the engine.
- **Just-in-Time Learning**: We won't start with a textbook. We start building immediately. When we hit a concept (e.g., "Embeddings," "Tool Use," "RAG"), we pause, explain it in context, implement it, and move on.
- **Iterative Refinement**: Code is never perfect on the first draft. We embrace a cycle of *Prompt -> Prototype -> Critique -> Refine*.

## 3. The Roles
*   **The User (Architect & Supervisor)**:
    *   Provides high-level prompts and business logic.
    *   Reviews the "Implementation Plan" proposed by Antigravity.
    *   Tests the agents and provides feedback on "vibes" (e.g., "Make it sassier," "It's hallucinating too much," "It needs access to my calendar").
*   **Antigravity (Lead Engineer & Mentor)**:
    *   translates prompts into production-grade Python code.
    *   Manages environments, dependencies (`uv`), and file structures.
    *   Explains *crucial* implementation details to upskill the User.
    *   Ensures code quality, testing, and scalability.

## 4. The Workflow Cycle
This process repeats for every new agent or feature.

### Phase 1: The "Vibe" (Ideation)
*   **Action**: User allows their imagination to run wild.
*   **Input**: "I want an agent that reads my emails and summarizes the drama."
*   **Antigravity Response**: Break down the technical requirements (Gmail API, LLM summarization, secure auth) and propose a roadmap.

### Phase 2: The Blueprint (Planning)
*   **Action**: Antigravity creates an `implementation_plan.md`.
*   **Content**:
    *   Folder structure changes.
    *   New libraries needed.
    *   Step-by-step logic.
*   **User Action**: Review and Approve (or ask for changes).

### Phase 3: The Build (Execution)
*   **Action**: Antigravity writes the code.
*   **Learning Moment**: Antigravity stops to explain key concepts.
    *   *Example*: "Here is why we are using a 'System Prompt' vs a 'User Prompt'..."
    *   *Example*: "We are using Pydantic here to ensure the agent returns structured JSON..."

### Phase 4: Vibe Check (Verification)
*   **Action**: User runs the agent.
*   **Feedback**: "It works, but it's too formal." or "It crashed when I sent an empty email."
*   **Refinement**: We loop back to Phase 3 to tweak and polish.

## 5. Getting Started
To begin, you only need to provide a single prompt in our chat.
**Example Starting Prompts:**
*   "Let's build a simple CLI chatbot that roasts my code."
*   "I want an agent that searches the web and plans my weekend."
*   "Build a RAG agent that answers questions about my PDF documents."

## 6. Goal
By the end of this journey, you will have:
1.  A portfolio of working AI Agents.
2.  Deep understanding of AI Engineering concepts (RAG, Function Calling, Agents, Memory).
3.  A robust, reusable codebase for future ideas.
