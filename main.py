from langchain.chains import RetrievalQA
from langchain.llms.ollama import Ollama
from langchain.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import GPT4AllEmbeddings
from langchain.vectorstores.chroma import Chroma
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnablePassthrough
from langchain.schema import StrOutputParser
import gradio as gr


ollama = Ollama(base_url="http://localhost:11434", model="llama2-uncensored")

loader = WebBaseLoader("https://hbr.org/1985/05/how-to-write-a-winning-business-plan")
data = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
all_splits = text_splitter.split_documents(data)
vector_store = Chroma.from_documents(persist_directory="./data", documents=all_splits, embedding=GPT4AllEmbeddings())
retriever = vector_store.as_retriever()


template = """
You are no longer an AI, you are a human. You are a business consultant and you are evaluating a business idea by analizing it using rationnal thinking, then giving it a grade from 0 to 10. The business idea is as follows:

{question}

Evaluate the business idea based only on the following context:
{context}

"""
prompt = ChatPromptTemplate.from_template(template)

chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | ollama
    | StrOutputParser()
)

print("""\



                                       ._ o o
                                       \_`-)|_
                                    ,""       \ 
                                  ,"  ## |   ಠ ಠ. 
                                ," ##   ,-\__    `.
                              ,"       /     `--._;)
                            ,"     ## /
                          ,"   ##    /


LLama 2 - Uncensored - Business Consultant (it's a girrafe because I didn't find a llama)
                    """)

def query(question):
    return chain.invoke(question)
  
  
 
title = "Llama Business Consulting, Inc."
description = '<center><img src="https://github.com/maksymalist/maksymalist/assets/79988159/ea967d6a-b829-499a-ab8e-400561c6385a" alt="Junk Judge" width="200px" height="200px">(its a girrafe because I could not find a llama)</center>'
theme = gr.themes.Default(primary_hue="slate").set(
    button_primary_background_fill="#000000",
    button_primary_text_color="#ffffff",
    button_primary_text_color_hover="#ffffff",
    button_primary_background_fill_hover="#e0e0e0",
    button_cancel_background_fill_dark="#ffffff",
    button_primary_text_color_dark="#ffffff",
)


gradio = gr.Interface(
    fn=query,
    inputs=gr.Textbox(lines=2, label="Business Idea"),
    outputs="text",
    flagging_options=["blurry", "incorrect", "other"],
    title=title,
    description= description,
    theme=theme,
    css="#component-1 {justify-content: center;align-items: center;flex-direction: column; width: 100%} #component-5 {justify-content: center;align-items: center;flex-direction: column; width: 100%} #component-6 {width: 100%; max-width: 900px} #component-11 {width: 100%; max-width: 900px} #component-12 {width: 100%}"
    
)
    
if __name__ == "__main__":
    gradio.launch(show_api=False)   