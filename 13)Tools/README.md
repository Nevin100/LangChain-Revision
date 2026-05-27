# 📖 Folder 13: Tools & Agents

## 🎯 Objective

Provide external tools to AI agents. Give LLMs web search, calculations, and custom capabilities.

## 📚 Theory & Concepts

### **Agent vs Chain**

```
Chain:
├── Fixed workflow (Prompt → Model → Parser)
├── Predetermined steps
└── No decision making

Agent:
├── Dynamic decision making
├── Chooses which tool to use
├── Loops: Think → Choose Tool → Execute → Observe → Repeat
└── Based on intermediate results
```

### **Agent Decision Making**

```
Agent Loop:
┌─────────────────────────────┐
│ User Question              │
└────────────┬────────────────┘
             ↓
┌─────────────────────────────┐
│ LLM Thinks: What to do?     │
│ Options: Search / Calculate │
└────────────┬────────────────┘
             ↓
┌─────────────────────────────┐
│ Choose Tool: Web Search     │
└────────────┬────────────────┘
             ↓
┌─────────────────────────────┐
│ Execute Tool               │
│ Result: [Search results]   │
└────────────┬────────────────┘
             ↓
┌─────────────────────────────┐
│ Observe & Decide           │
│ Need more info? Use another?
└────────────┬────────────────┘
             ↓
┌─────────────────────────────┐
│ Final Answer               │
└─────────────────────────────┘
```

### **Tool Types**

```
Built-in Tools:
├── DuckDuckGoSearchRun - Web search
├── Calculator - Math operations
├── PythonREPL - Execute Python
└── Arxiv - Research papers

Custom Tools:
├── Database query
├── API calls
├── File operations
└── Any Python function
```

### **Tool Format**

```python
Tool = {
    "name": "tool_name",
    "description": "What it does",
    "input_schema": {...},
    "func": function_to_execute
}

Agent sees: Name + Description
Agent decides: Relevant for this task?
Agent uses: If relevant, calls func() with input
```

## 📁 Files Overview

### **Built/**
```
Purpose: Built-in tools (DuckDuckGoSearchRun)
Tool: Web search functionality
Use: Agent can search the web
```

### **custom/**
```
Purpose: Template for custom tools
Use: Extend with domain-specific tools
Examples: Database tools, API tools, etc.
```

## 🔑 Key Learning Points

### **1. Built-in Tools - DuckDuckGo Search**

```python
from langchain_community.tools import DuckDuckGoSearchRun

# Create search tool
search_tool = DuckDuckGoSearchRun()

# Use directly
result = search_tool.run("Python programming")
print(result)
```

### **2. Tool Description (Important for Agent)**

```python
from langchain.tools import Tool

def my_search(query: str) -> str:
    """Search the internet for information"""
    return search_tool.run(query)

search_tool = Tool(
    name="web_search",
    func=my_search,
    description="""
    Useful for when you need to search the internet for current information.
    Input should be a search query as a string.
    """
)

# Agent will use description to decide when to call this tool
```

### **3. Create Custom Tool**

```python
from langchain.tools import tool
from langchain_community.tools import Tool

# Method 1: Decorator (Clean)
@tool
def calculate_area(length: float, width: float) -> float:
    """Calculate rectangle area. Input: length and width in meters."""
    return length * width

# Now it's automatically a Tool!
# Agent can use it

# Method 2: Explicit Tool class
def multiply(a: float, b: float) -> float:
    return a * b

multiply_tool = Tool(
    name="multiply",
    func=multiply,
    description="Multiply two numbers. Input: two numbers."
)
```

### **4. Agent with Tools**

```python
from langchain_groq import ChatGroq
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.agents import create_react_agent, AgentExecutor
from langchain_core.prompts import PromptTemplate

# Initialize
llm = ChatGroq(model="llama-3.1-8b-instant")

# Tools
search = DuckDuckGoSearchRun()

tools = [
    Tool(
        name="search",
        func=search.run,
        description="Search the web for information"
    )
]

# Create agent (ReACT = Reasoning + Acting)
agent = create_react_agent(
    llm=llm,
    tools=tools,
    prompt=PromptTemplate.from_template("{input}")  # Custom prompt
)

# Execute
agent_executor = AgentExecutor.from_agent_and_tools(
    agent=agent,
    tools=tools,
    verbose=True  # See agent thinking
)

# Use
result = agent_executor.invoke({"input": "What is latest in AI?"})
print(result["output"])
```

### **5. Multiple Tools**

```python
from langchain_community.tools import (
    DuckDuckGoSearchRun,
    ArxivQueryRun,
    Tool
)
from langchain.agents import initialize_agent, Tool
from langchain_groq import ChatGroq

llm = ChatGroq(model="llama-3.1-8b-instant")

# Multiple tools
tools = [
    Tool(
        name="web_search",
        func=DuckDuckGoSearchRun().run,
        description="Search web for current info"
    ),
    Tool(
        name="arxiv_search",
        func=ArxivQueryRun().run,
        description="Search academic papers"
    ),
    Tool(
        name="calculator",
        func=lambda x: str(eval(x)),  # Simple calc
        description="Evaluate math expressions"
    )
]

# Agent chooses best tool
agent = initialize_agent(
    tools,
    llm,
    agent="zero-shot-react-description",
    verbose=True
)

# Complex task - agent will use multiple tools
result = agent.run("What's the square root of 144? Search for it online too.")
```

## 💡 Practical Patterns

### **Pattern 1: Web Search Agent**

```python
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_groq import ChatGroq
from langchain.agents import initialize_agent, AgentType

llm = ChatGroq(model="llama-3.1-8b-instant")
search = DuckDuckGoSearchRun()

tools = [
    Tool(
        name="search",
        func=search.run,
        description="Search for current information"
    )
]

agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# Use
response = agent.run("Who won the latest Nobel Prize?")
```

### **Pattern 2: Domain-Specific Tools**

```python
@tool
def query_database(query: str) -> str:
    """Query internal database. Input: SQL query or plain text search."""
    # Execute database query
    return "Result from database"

@tool
def check_inventory(product: str) -> str:
    """Check if product is in stock."""
    # Query inventory system
    return f"{product} - In Stock"

tools = [query_database, check_inventory]

agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION
)

# Agent uses right tool
result = agent.run("Is laptop in stock? Show me available inventory.")
```

### **Pattern 3: Complex Multi-Tool Task**

```python
@tool
def search_web(query: str) -> str:
    """Search web"""
    return DuckDuckGoSearchRun().run(query)

@tool
def summarize(text: str) -> str:
    """Summarize text using LLM"""
    return llm.invoke(f"Summarize: {text}").content

@tool
def save_to_file(text: str, filename: str) -> str:
    """Save text to file"""
    with open(filename, 'w') as f:
        f.write(text)
    return f"Saved to {filename}"

tools = [search_web, summarize, save_to_file]

agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION)

# Complex task
result = agent.run("""
Search for 'climate change latest developments'.
Summarize the results.
Save to 'climate_summary.txt'
""")
```

### **Pattern 4: Custom Tool Class**

```python
from langchain.tools import BaseTool
from pydantic import Field

class WeatherTool(BaseTool):
    name: str = "weather"
    description: str = "Get weather for a city"
    city: str = Field(description="City name")
    
    def _run(self, city: str) -> str:
        # Call weather API
        return f"Weather in {city}: Sunny, 25°C"

weather_tool = WeatherTool()

tools = [weather_tool]
agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION)

result = agent.run("What's the weather in London?")
```

## 📊 Tool Types Comparison

| Tool | Setup | Reliability | Use Case |
|------|-------|------------|----------|
| Web Search | Easy | Good | Current info |
| Calculator | Built-in | Perfect | Math |
| Database | Medium | Excellent | Structured data |
| API | Medium | Depends | External services |
| Custom | Medium | Full control | Domain-specific |

## 🎓 Advanced Concepts

### **Agent Types**

```
zero-shot-react-description:
├── Simplest
├── No memory of past actions
└── Good for: Single queries

react-docstore:
├── Intermediate complexity
├── Can revisit documents
└── Good for: Multi-step reasoning

conversational-react-description:
├── Most complex
├── Maintains conversation history
└── Good for: Multi-turn conversation
```

### **Tool Execution Flow**

```
1. Agent sees input
2. LLM generates thought
3. LLM chooses tool
4. Tool executes
5. Result returned to LLM
6. LLM decides: Done? Or use another tool?
7. Repeat until answer found
```

### **Error Handling in Tools**

```python
@tool
def safe_search(query: str) -> str:
    """Search safely with error handling"""
    try:
        return DuckDuckGoSearchRun().run(query)
    except Exception as e:
        return f"Search failed: {str(e)}"

# Agent can handle tool failures gracefully
```

## ⚠️ Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| Agent loops infinitely | Add max_iterations |
| Tool not used | Improve description |
| Wrong tool chosen | Clarify descriptions, examples |
| Slow execution | Cache tool results |

## 💡 Pro Tips

1. **Descriptions Matter**: Clear descriptions help agent choose right tool
2. **Few Examples**: Provide examples in system prompt
3. **Error Handling**: Always wrap tools in try-except
4. **Testing**: Test tools independently first
5. **Logging**: Enable verbose to see agent thinking

## 📚 Tool Best Practices

### **Clear Tool Specification**

```python
@tool
def calculate_discount(price: float, discount_percent: float) -> float:
    """
    Calculate final price after discount.
    
    Args:
        price: Original price in dollars
        discount_percent: Discount percentage (0-100)
    
    Returns:
        Final price after discount
    """
    return price * (1 - discount_percent / 100)
```

### **Input Validation**

```python
@tool
def divide(a: float, b: float) -> str:
    """Divide a by b"""
    if b == 0:
        return "Error: Cannot divide by zero"
    return str(a / b)
```

## 🚀 Next Steps

1. **Create custom tools**: Extend for your domain
2. **Multi-tool agents**: Combine 3-5 tools
3. **Persistent memory**: Add conversation history
4. **Evaluation**: Measure agent accuracy

## 📖 Related Topics

- **Folder 6**: Chains (simpler than agents)
- **Folder 7**: Runnables (underlying primitives)
- **Folder 12**: RAG (can be used as tool)

## 🔗 Tool Creation Checklist

```
☐ Define function
☐ Add clear docstring
☐ Specify input types
☐ Add error handling
☐ Create Tool wrapper
☐ Test independently
☐ Test with agent
☐ Iterate on description
```

---

**Agents & Tools Mastered! 🤖**