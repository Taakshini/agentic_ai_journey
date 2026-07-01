import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
# ------------------------
# TOOL (simulated web search)
# ------------------------
def web_search(query):
    return f"""
    [Search Results for: {query}]  
    along from the web, here are some resources you might find useful: by requesting the question,you 
            1. AI Agents - beginner guide (example.com/agents)
    2. Building AI tools with Python (example.com/python-ai)
    3. Intro to LLM-based agents (example.com/llm-agents)
    """
# ------------------------
# LLM CALL
# ------------------------
def call_llm(prompt):
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )
    return response.json()["response"]

# ------------------------
# AGENT LOOP (1-step version first)
# ------------------------
user_input = input("Ask something: ")

# Step 1: give LLM tool context
prompt = f"""
You are an AI agent.

You have access to this tool:

Tool: web_search(query)
Returns: list of learning resources

User request:
{user_input}

Decide:
- Do you need the tool? (yes/no)
- If yes, give the search query
"""

decision = call_llm(prompt)

print("\n--- LLM DECISION ---\n")
print(decision)

# Step 2: simple manual tool trigger (we automate next step later)
query = input("\nEnter search query from LLM (copy it): ")

tool_result = web_search(query)

print("\n--- TOOL OUTPUT ---\n")
print(tool_result)

# Step 3: final LLM synthesis
final_prompt = f"""
You are a study assistant.

User asked:
{user_input}

Here are search results:
{tool_result}

Now give a structured learning plan.
"""

final_output = call_llm(final_prompt)

print("\n--- FINAL AGENT OUTPUT ---\n")
print(final_output)