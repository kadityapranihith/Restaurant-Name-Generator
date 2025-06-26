import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.chains import SequentialChain

def generate_name_and_items(cuisine):
    os.environ["GOOGLE_API_KEY"] = "AIzaSyBJIuu49S76KqdDslnTnO5GPtGMnJpEcLU"
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",  # or gemini-1.5-pro
        temperature=1
    )


    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",  # or gemini-1.5-pro
        temperature=1
    )
    prompt_template_name = PromptTemplate(
        input_variables=['cuisine'],
        template="I want to to open a restaurant for {cuisine} food, suggest a royal name for this, just one single name"
    )
    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key='restaurant')

    prompt_template_food_items = PromptTemplate(
        input_variables=['restaurant'],
        template="suggest some menu items for {restaurant}, return them as comma separated list"

    )
    food_items_chain = LLMChain(llm=llm, prompt=prompt_template_food_items, output_key="menu_items")



    chain = SequentialChain(
        chains=[name_chain, food_items_chain],
        input_variables=['cuisine'],
        output_variables=['restaurant', 'menu_items']
    )
    return chain({'cuisine': cuisine})

res=generate_name_and_items('Indian')
print(res)