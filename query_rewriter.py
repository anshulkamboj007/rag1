from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from llm_chain import get_llm

def rewrite_query(query: str) -> str:
    """
    Rewrite user queries to be more effective for retrieval using LangChain Expression Language.
    """
    # Prompt that encourages semantic improvement
    prompt = PromptTemplate.from_template(
        "Rewrite the following user query to improve retrieval effectiveness:\n\n{query}"
    )

    # Use the shared LLM instance (supports .invoke())
    llm = get_llm

    # LCEL chain: Prompt → LLM → String output
    rewrite_chain = prompt | llm | StrOutputParser()

    return rewrite_chain.invoke({"query": query})
