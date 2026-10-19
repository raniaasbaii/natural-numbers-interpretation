# Natural Numbers Interpretation

Omilia Programming Assignment — Phone number interpretation from spoken natural numbers with ambiguity detection.

## Language & Version

- **Language:** Python 3.10+
- **No external dependencies** — uses only the Python standard library.

## How to Run

```bash
python3 phone_interpreter.py
```

The application runs interactively from the command line. Enter a sequence of natural numbers separated by spaces, and it will:

1. Generate all possible digit-string interpretations (handling merge/split ambiguities).
2. Validate each interpretation as a Greek phone number (10 digits starting with `2` or `69`, or 14 digits starting with `00302` or `003069`).

Type `quit` to exit.

### Example

```
Input: 2 10 69 30 6 6 4

#     Output                    Phone number
--------------------------------------------------
1     21060930664               INVALID
2     2106093664                VALID
3     2106930664                VALID
4     210693664                 INVALID
```

## Ambiguity Rules

- **Merge:** Adjacent round tens (20–90) + single digit (1–9) may form one number (e.g., `20 5` → `25`). Similarly, round hundreds (100–900) + remainder (1–99), and three-way hundreds + tens + ones.
- **Split:** A compound number (21–99) may represent separate spoken numbers (e.g., `75` → `70, 5` producing digits `"705"`). Same logic extends to three-digit numbers.
