from langchain.chat_models import init_chat_model
import os
import pandas as pd
import duckdb

llm = init_chat_model(
    model = "llama-3.1-8b-instant",
    model_provider = "openai",
    base_url = "https://api.groq.com/openai/v1",
    api_key = os.getenv("GROQ_API_KEY")
)

conversation = [
    {"role":"system","content":"You are SQLite expert developer with 10 years of ex[perince"}
]

csv_file = input("Entr path od a file:")
df = pd.read_csv(csv_file)
print("csv schema")
print(df.dtypes)

con = duckdb.connect()
con.register("data",df)

while True:
    user_input = input("Ask anything about this csv...")
    if user_input == "exit":
        break

    llm_input = f"""
    Table Name : data
    Table Schema : {df.dtypes}
    Question : {user_input}
    Instruction :  
            You are an expert SQLite developer.

    Table Name: data
    Table Schema:
    {df.dtypes}

    Question:
    {user_input}

    Instruction:
    - Write ONLY a valid SQL query
    - No explanation
    - If impossible, return Error
        """

    sql_response = llm.invoke(llm_input).content.strip()
    print("\nGenerated SQL:")
    print(sql_response)

    try:
        result_df = con.execute(sql_response).df()
        print("\nQuery Result")
        print(result_df)

    except Exception as e:
        print("SQL Execution Error :",e)

    explain_prompt = f"""
    Explain the following SQL query result in simple English.

    User Question:
    {user_input}

    SQL Query:
    {sql_response}

    Result:
    {result_df.head(10).to_string(index=False)}
    """

    explanation = llm.invoke(explain_prompt).content
    print("\nExplanation:")
    print(explanation)