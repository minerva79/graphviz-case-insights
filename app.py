import re
from openai import OpenAI
from graphviz import Source
import streamlit as st
from system_messages import system_messages  # Import system messages

# Define the function to process the case study
def process_case_study(case_study, api_key, system_messages, model="chatgpt-4o-latest", temperature=0.1):
    """
    Process a case study through a series of chained prompts using OpenAI's API.
    """
    messages = []
    responses = {}

    client = OpenAI(api_key=api_key)

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

# Export the Graphviz diagram as a PDF
def save_graphviz_as_pdf(script):
    src = Source(script)
    pdf_data = src.pipe(format="pdf")
    return pdf_data

# Initialize session state variables
if "final_output" not in st.session_state:
    st.session_state.final_output = None
if "graphviz_script" not in st.session_state:
    st.session_state.graphviz_script = None

# Streamlit App
st.title("Case Study Analyzer with Causal Loop Diagram")

# API Key Input
if "api_key" not in st.session_state:
    st.session_state.api_key = None

api_key = st.text_input("Enter your OpenAI API key:", type="password")
if api_key:
    st.session_state.api_key = api_key

# Check if API key is provided
if st.session_state.api_key:
    # Input Section
    case_study = st.text_area(
        "Enter your case study:",
        height=200,
        placeholder="Type or paste the case study text here..."
    )
    process_button = st.button("Process Case Study")

    if process_button and case_study.strip():
        with st.spinner("Processing the case study, please wait..."):
            try:
                # Process the case study
                responses = process_case_study(case_study, st.session_state.api_key, system_messages)
                st.session_state.final_output = responses["Final_Output"]

                # Extract and store the Graphviz script in session state
                graphviz_script = extract_graphviz_script(st.session_state.final_output)
                st.session_state.graphviz_script = graphviz_script

                # Display the final output
                st.subheader("Analysis Output")
                st.text_area("Generated Insights", value=st.session_state.final_output, height=300)

                # Display the Graphviz diagram
                if st.session_state.graphviz_script:
                    st.subheader("Causal Loop Diagram")
                    st.graphviz_chart(st.session_state.graphviz_script)
                else:
                    st.warning("No Graphviz diagram found in the output.")
            except Exception as e:
                st.error(f"An error occurred: {e}")

    # Add download buttons if outputs are available
    if st.session_state.final_output:
        st.download_button(
            label="Download Markdown Output",
            data=st.session_state.final_output,
            file_name="analysis_output.md",
            mime="text/markdown"
        )
    if st.session_state.graphviz_script:
        pdf_data = save_graphviz_as_pdf(st.session_state.graphviz_script)
        st.download_button(
            label="Download Graphviz PDF",
            data=pdf_data,
            file_name="causal_loop_diagram.pdf",
            mime="application/pdf"
        )
else:
    st.warning("Please enter your OpenAI API key to proceed.")
