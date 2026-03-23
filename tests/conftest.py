import os


def pytest_configure(config):
    """
    This hook runs BEFORE any tests or modules are imported.
    """
    os.environ["EMBEDDING_MODEL"] = "sk-or-v1-fake-key-for-testing"
    os.environ["EMBEDDING_API_KEY"] = "sk-or-v1-fake-key-for-testing"
    os.environ["LLM_OPENROUTER_MODEL"] = "sk-or-v1-fake-key-for-testing"
    os.environ["LLM_OPENROUTER_API_KEY"] = "sk-or-v1-fake-key-for-testing"
    os.environ["LLM_GEMINI_MODEL"] = "sk-or-v1-fake-key-for-testing"
    os.environ["LLM_GEMINI_API_KEY"] = "sk-or-v1-fake-key-for-testing"
    os.environ["LLM_GROQ_MODEL"] = "sk-or-v1-fake-key-for-testing"
    os.environ["LLM_GROQ_API_KEY"] = "sk-or-v1-fake-key-for-testing"
