Token Usage:
GitHub Tokens: 8233
LLM Input Tokens: 8242
LLM Output Tokens: 1532
Total Tokens: 18007

FileTree:
app.py
driver.py
example.cpp
openaigpt4.py
parse_clang.py
pdfreader.py
read_email.py
requirements.txt
sample_neo4j_query.py
sort.py
train_cypher.py
train_utils.py

Analysis:
```markdown
# Neo4j POC with OpenAI Integration

This repository contains a proof-of-concept (POC) application that integrates Neo4j graph database with OpenAI's language models. The application allows users to query a Neo4j database using natural language, which is then translated into Cypher queries using OpenAI's GPT-4 model.

## Overview

The application consists of several Python scripts that work together to provide a seamless user experience:

-   **`app.py`**: The main Streamlit application that provides the user interface for interacting with the Neo4j database.
-   **`driver.py`**: Handles the connection to the Neo4j database and executes Cypher queries.
-   **`openaigpt4.py`**:  Interfaces with the OpenAI GPT-4 model to generate Cypher queries from natural language input.
-   **`train_cypher.py`**: Defines example queries, node properties, and relationship properties for training the OpenAI model.
-   **`train_utils.py`**: Contains utility functions for constructing the system message and schema text used by the OpenAI model.
-   **`example.cpp`**: A C++ file used by `parse_clang.py` to demonstrate AST parsing.
-   **`parse_clang.py`**: Parses a C++ source file (`example.cpp`) using `libclang` to extract information about the code structure (classes, functions, loops, etc.).
-   **`pdfreader.py`**: A Streamlit application that allows users to chat with multiple PDF documents using Langchain.
-   **`read_email.py`**: Reads and redacts sensitive information from an email file using SpaCy and Langchain.
-   **`sample_neo4j_query.py`**:  A script to populate the Neo4j database with sample data (nodes, relationships, and attributes).
-   **`sort.py`**:  A utility script for sorting filenames in a specific format (e.g., "Chapter\_X.json").

## Requirements

Before running the application, ensure you have the following installed:

-   Python 3.7+
-   Neo4j graph database
-   OpenAI API key

Install the required Python packages using pip:

```bash
pip install -r requirements.txt
```

## Setup and Configuration

1.  **Neo4j Database:**
    -   Install and configure a Neo4j database instance.
    -   Update the connection details in `driver.py` and `sample_neo4j_query.py` with your Neo4j host, username, and password.  The default is:
        ```python
        host = 'bolt://localhost:7687'
        user = 'neo4j'
        password = 'pass'
        ```

2.  **OpenAI API Key:**
    -   Obtain an API key from OpenAI.
    -   Set the `openai.api_key` variable in `app.py` and `openaigpt4.py` with your API key.
        ```python
        openai.api_key = 'YOUR_OPENAI_API_KEY'
        ```

3.  **Populate Neo4j Database (Optional):**
    -   Run `sample_neo4j_query.py` to create sample nodes, relationships, and attributes in your Neo4j database.

4.  **libclang (Optional):**
    -   If you intend to use `parse_clang.py`, ensure you have `libclang` installed and configured correctly. The path to `libclang.dylib` might need to be adjusted depending on your system.

## Running the Application

1.  **Streamlit App:**

    To start the main application, run:

    ```bash
    streamlit run app.py
    ```

    This will open the application in your web browser. You can then enter natural language queries to search the Neo4j database.

2.  **Other Scripts:**

    You can run the other scripts directly using Python:

    ```bash
    python pdfreader.py  # Run the PDF chat application
    python read_email.py # Run the email redaction script
    python parse_clang.py # Run the C++ AST parser
    ```

## Usage

1.  **Neo4j POC App (`app.py`):**
    -   Enter your question in the chat input box.
    -   The application will generate a Cypher query based on your input and execute it against the Neo4j database.
    -   The results will be displayed in the chat interface.

2.  **PDF Chat App (`pdfreader.py`):**
    -   Upload one or more PDF documents using the file uploader in the sidebar.
    -   Click the "Process" button to process the documents and create a vector store.
    -   Ask questions about the documents in the chat input box.

3.  **Email Redaction (`read_email.py`):**
    -   Update the `file_path` variable in `read_email.py` with the path to your `.eml` file.
    -   Run the script to redact sensitive information from the email content.

## File Descriptions

*   **`app.py`**:  Streamlit application for natural language querying of Neo4j.
*   **`driver.py`**:  Neo4j database connection and query execution.
*   **`openaigpt4.py`**: OpenAI GPT-4 integration for Cypher query generation.
*   **`train_cypher.py`**: Training data for the OpenAI model (examples, schema).
*   **`train_utils.py`**: Utility functions for OpenAI model training.
*   **`example.cpp`**: Sample C++ file for AST parsing.
*   **`parse_clang.py`**:  Parses C++ code using `libclang`.
*   **`pdfreader.py`**:  Streamlit app for chatting with PDF documents.
*   **`read_email.py`**:  Email redaction script using SpaCy and Langchain.
*   **`sample_neo4j_query.py`**: Populates Neo4j with sample data.
*   **`sort.py`**: Filename sorting utility.
*   **`requirements.txt`**: List of Python dependencies.

## Notes

-   This is a POC and may require further development for production use.
-   The accuracy of the generated Cypher queries depends on the quality of the training data and the complexity of the queries.
-   Ensure that your OpenAI API key is kept secure.
-   The C++ parsing functionality is basic and can be extended to extract more detailed information from the code.
-   The PDF Chat App and Email Redaction scripts are separate functionalities demonstrating the use of Langchain for different tasks.

## License

This project is licensed under the [MIT License](LICENSE).
```

