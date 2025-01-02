# Graphviz Case Insights

**Graphviz Case Insights** is a user-friendly web application that combines natural language processing and data visualization to analyze case studies. It uses OpenAI's GPT API to generate insights and produces causal loop diagrams rendered with Graphviz.

## Features

- Analyze case studies and generate textual insights.
- Create causal loop diagrams for visual representation of relationships.
- Interactive interface built with Streamlit.
- Easy deployment and use.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/graphviz-case-insights.git
   cd graphviz-case-insights
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Install Graphviz system package:
   - On **Windows**: [Download and install Graphviz](https://graphviz.org/download/)
   - On **macOS**:
     ```bash
     brew install graphviz
     ```
   - On **Linux**:
     ```bash
     sudo apt-get install graphviz
     ```

5. Set up your OpenAI API key:
   - Add the `OPENAI_API_KEY` as an environment variable:
     ```bash
     export OPENAI_API_KEY=your_openai_api_key  # On Windows: set OPENAI_API_KEY=your_openai_api_key
     ```

## Usage

1. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

2. Open your browser and navigate to `http://localhost:8501`.

3. Enter a case study in the text input box, click "Process Case Study," and view the generated insights and causal loop diagram.

## Deployment

You can deploy this app on [Streamlit Cloud](https://streamlit.io/cloud) or other hosting platforms. Ensure you set the `OPENAI_API_KEY` as a secret during deployment.

## Repository Structure

- `app.py`: Main Streamlit application file.
- `system_messages.py`: Contains the system messages used for OpenAI prompts.
- `requirements.txt`: List of Python dependencies.
- `README.md`: Repository documentation.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Feel free to fork this repository, make changes, and submit a pull request.

## Acknowledgments

- [Streamlit](https://streamlit.io/)
- [OpenAI GPT](https://platform.openai.com/)
- [Graphviz](https://graphviz.org/)

---

### **LICENSE (MIT License)**

```plaintext
MIT License

Copyright (c) 2025 Your Name

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
