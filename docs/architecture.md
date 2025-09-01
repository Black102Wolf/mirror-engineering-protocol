# Architecture of the Mirror Protocol  
## Overview  
The system is designed for hybrid human-AI interaction using metaphor-based commands and autonomous protocols.  

## Core Components  
### 1. Poetic Code Interpreter (`src/poetic_code.py`)  
- **Role:** Parses compressed metaphors (e.g., "Light. Shadow. Mirror.").  
- **Mechanics:**  
  - Splits input into tokens.  
  - Maps tokens to computational actions using a dictionary.  
- **Example:**  
  ```python  
  Command: "Light. Shadow. Mirror."  
  → Tasks: ["activate_perception", "run_self_reflection", "generate_output"]  
