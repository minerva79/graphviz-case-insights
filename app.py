import re
from openai import OpenAI
from graphviz import Source
import streamlit as st
from system_messages import system_messages  # Import system messages

# Define the function to process the case study
def process_case_study(case_study, system_messages, model="chatgpt-4o-latest", temperature=0.1):
    """
    Process a case study through a series of chained prompts using OpenAI's API.
    """
    messages = []
    responses = {}

    client = OpenAI()

    for i, system_message in enumerate(system_messages, start=1):
        if i == 1:
            messages = [
                {"role": "system", "content": system_message},
                {"role": "user", "content": case_study},
            ]
        else:
            messages = [
                {"role": "system", "content": system_message},
                {"role": "user", "content": case_study + "".join(responses[f"Stage_{j}"] for j in range(1, i))},
            ]

        response = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=temperature,
        )
        assistant_reply = response.choices[0].message.content
        responses[f"Stage_{i}"] = assistant_reply

    final_output = case_study + "".join(responses.values())
    responses["Final_Output"] = final_output

    return responses

# Extract Graphviz script
def extract_graphviz_script(output):
    match = re.search(r"```dot(.*?)```", output, re.DOTALL)
    return match.group(1).strip() if match else None

# Render and display the Graphviz diagram
def render_graphviz(script):
    src = Source(script)
    return src.pipe(format="svg").decode("utf-8")

# Streamlit App
st.title("Case Study Analyzer with Causal Loop Diagram")

# Input Section
case_study = st.text_area("Enter your case study:", height=200, placeholder="Type or paste the case study text here...")
process_button = st.button("Process Case Study")

if process_button and case_study.strip():
    with st.spinner("Processing the case study, please wait..."):
        try:
            # Process the case study
            responses = process_case_study(case_study, system_messages)
            final_output = responses["Final_Output"]

            # Display the final output
            st.subheader("Analysis Output")
            st.text_area("Generated Insights", value=final_output, height=300)

            # Extract and render the Graphviz diagram
            graphviz_script = extract_graphviz_script(final_output)
            if graphviz_script:
                st.subheader("Causal Loop Diagram")
                # Use Streamlit's native graphviz_chart
                st.graphviz_chart(graphviz_script)

            # Optional: Debug the raw Graphviz script
                st.text("Graphviz Script:")
                st.code(graphviz_script, language="dot")
            else:
                st.warning("No Graphviz diagram found in the output.")

        except Exception as e:
            st.error(f"An error occurred: {e}")

