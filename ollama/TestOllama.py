from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="gemma3:1b")
response = llm.invoke("The first man on the moon was ...")
print(response)
