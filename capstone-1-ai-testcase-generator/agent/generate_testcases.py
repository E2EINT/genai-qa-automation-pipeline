from pathlib import Path

def generate_test_cases(context: str) -> str:
    """
    Simulated LLM output.
    Replace this function later with OpenAI / Azure / local LLM.
    """
    return f"""
Test Case 1: Valid Login
- Given user is on login page
- When user enters valid username and password
- Then user should be logged in successfully

Test Case 2: Invalid Password
- Given user is on login page
- When user enters valid username and invalid password
- Then error message should be displayed

Context Used:
{context[:500]}...
"""

if __name__ == "__main__":
    retrieved_context_file = Path("../output/retrieved_context.txt")

    if not retrieved_context_file.exists():
        print("No retrieved context found. Run retrieval step first.")
        exit(1)

    context = retrieved_context_file.read_text(encoding="utf-8")

    test_cases = generate_test_cases(context)

    output_file = Path("../output/generated_test_cases.txt")
    output_file.write_text(test_cases, encoding="utf-8")

    print("Test cases generated successfully.")
