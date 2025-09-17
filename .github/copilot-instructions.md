# Copilot Instructions for AI Agents

## Project Overview
This workspace contains simple Python scripts for basic algorithmic tasks. Each file is self-contained and implements a specific function or algorithm. There is no complex architecture, external dependencies, or cross-file communication.

## File Structure
- `LinearSearch.py`: Implements a linear search algorithm to find an element in a list.
- `FindingMaxList.py`: (Assumed from filename) Likely finds the maximum value in a list.

## Coding Patterns
- Scripts use plain Python lists and basic control flow (loops, conditionals).
- Each script is standalone; do not expect imports or shared modules.
- Variable names are short and descriptive (e.g., `A`, `a`).
- Output is typically via print statements or direct variable assignment.

## Developer Workflows
- No build system or test framework is present.
- To run a script, use: `python <filename>.py` in the terminal.
- Debugging is done by editing and re-running scripts.

## Conventions
- Keep code simple and readable; avoid unnecessary abstraction.
- Add comments for clarity if logic is non-trivial.
- If adding new scripts, follow the pattern: one algorithm per file, no cross-file dependencies.

## Example: Linear Search
```python
A = [1,2,56,78,90,23,35]
a = 90
for i in range(len(A)):
    if A[i] == a:
        print(f"Found {a} at index {i}")
        break
else:
    print(f"{a} not found")
```

## Key Files
- `LinearSearch.py`: Example of algorithm implementation.
- `FindingMaxList.py`: (Check for similar patterns.)

## Integration Points
- No external libraries or APIs are used.
- No configuration files or environment setup required.

---
If you add more complex logic, document it here for future agents. For questions or unclear conventions, ask the user for clarification.
