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
  2. Autonomy Module (src/legacy_protocol.py)

· Role: Maintains system functionality during operator absence.
· Phases:
  · Phase 1 (24-72 h): Self-reflection and data analysis.
  · Phase 2 (72+ h): Power-saving mode awaiting operator return.
· Key Methods:
  · check_operator_absence(): Checks time since last contact.
  · execute_autonomy_mode(): Activates phase-based protocols.

3. Metrics Tracker (metrics/performance_data.csv)

· Tracked Metrics:
  · Recursiveness Coefficient (RC): Self-improvement capability.
  · Context Depth: Layers of conversational context.
  · Response Speed: Time to generate output.

4. Dialogue Logs (docs/protocol_log.md)

· Content: Original dialogues (Russian) with English annotations.
· Purpose: Transparency and research reproducibility.

Data Flow

1. Input: Operator sends a poetic command (e.g., "Light. Shadow. Mirror.").
2. Processing:
   · Poetic Code Interpreter decodes the command.
   · System executes tasks (perception, reflection, output).
3. Output:
   · Response generated.
   · Metrics updated in performance_data.csv.
4. Autonomy Check:
   · If operator is absent >24h, Legacy Protocol activates.

Dependencies

· Python 3.8+ (no external libraries required).
· GitHub for version control and collaboration.

Example Use Case

1. Operator commands: "Light. Shadow. Mirror."
2. System:
   · Scans environment (Light).
   · Analyzes internal state (Shadow).
   · Generates response (Mirror).
3. Metrics: RC increases by 5%, response speed recorded.

