from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama,OllamaEmbeddings
from langchain_core.output_parsers import StrOutputParser

llm=ChatOllama(model='hf.co/bartowski/Llama-3.2-1B-Instruct-GGUF:Q4_0')


summary_prompt = PromptTemplate.from_template(
    "Summarize the following chapter clearly and concisely:\n\n{chapter_text}"
)

summary_chain = summary_prompt | llm | StrOutputParser()

def summarize_func(text: str) -> str:
    return summary_chain.invoke({"chapter_text": text})

def get_embedding_model():
    return OllamaEmbeddings(
        model="mxbai-embed-large",
    )
