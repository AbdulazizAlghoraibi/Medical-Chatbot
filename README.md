# Medical Chatbot

This project is a Flask-based web application that serves as a medical chatbot. It utilizes LangChain, Pinecone, and Sentence Transformers to provide responses to medical queries based on a pre-processed medical document.

## Project Structure

```
Medical-Chatbot/
├── app.py                # Main Flask application
├── store_index.py        # Script to process data and store embeddings in Pinecone
├── requirements.txt      # Python dependencies
├── .env                  # Environment variables (API keys)
├── data/
│   └── Medical_book.pdf  # Medical document for the chatbot
├── src/
│   ├── helper.py         # Helper functions for LangChain, Pinecone, and data processing
│   └── prompt.py         # Contains the prompt template for the chatbot
├── templets/
│   └── index.html        # HTML template for the web interface
├── static/
│   └── style.css         # CSS for the web interface (if any)
└── research/
    └── trials.ipynb      # Jupyter notebook for experimentation
```

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd Medical-Chatbot
    ```

2.  **Create a virtual environment and activate it:**
    ```bash
    python -m venv medbot
    # On Windows
    .\medbot\Scripts\activate
    # On macOS/Linux
    source medbot/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up environment variables:**
    Create a `.env` file in the root directory and add your API keys:
    ```env
    PINECONE_API_KEY="YOUR_PINECONE_API_KEY"
    PINECONE_API_ENV="YOUR_PINECONE_ENVIRONMENT"
    OPENAI_API_KEY="YOUR_OPENAI_API_KEY"
    ```
    *(Note: The project currently uses a HuggingFace sentence transformer, so `OPENAI_API_KEY` might be for future use or an alternative LLM. If using OpenAI models with LangChain, this key will be necessary.)*

5.  **Prepare and store data in Pinecone:**
    Run the `store_index.py` script to process the `Medical_book.pdf`, create embeddings, and store them in your Pinecone index.
    ```bash
    python store_index.py
    ```
    Ensure your Pinecone index is created and the name matches the one used in `src/helper.py` (e.g., "medical-chatbot-index").

## Running the Application

1.  **Start the Flask application:**
    ```bash
    python app.py
    ```
2.  Open your web browser and navigate to `http://127.0.0.1:5000` (or the address shown in the terminal).

## Key Components

*   **`app.py`**:
    *   Initializes the Flask app.
    *   Defines routes:
        *   `/`: Renders the main chat interface (`index.html`).
        *   `/get`: Handles POST requests with user queries, interacts with the chatbot backend, and returns the bot's response.
    *   Uses helper functions from `src/helper.py` to get the LangChain QA chain.

*   **`src/helper.py`**:
    *   `load_pdf()`: Loads and splits the PDF document.
    *   `text_split()`: Splits text into manageable chunks.
    *   `download_hugging_face_embeddings()`: Downloads sentence transformer embeddings.
    *   `get_conversational_chain()`: Creates and returns the LangChain conversational retrieval chain, configured with the prompt from `src/prompt.py` and a language model (e.g., `CTransformers` with a Llama2 model).
    *   Initializes Pinecone connection and retrieves the index.

*   **`src/prompt.py`**:
    *   Defines `prompt_template`: The template used to instruct the language model on how to answer questions based on the provided context.

*   **`store_index.py`**:
    *   Loads the PDF.
    *   Splits the document into chunks.
    *   Generates embeddings for the chunks using HuggingFace sentence transformers.
    *   Stores these embeddings in a Pinecone vector database.

*   **`fix_pinecone_alias.py`**:
    *   A utility script likely created to address import issues with the `pinecone` library, specifically aliasing `pinecone.Index` to `pinecone.pinecone.Index` if needed due to library version changes. This might be a temporary workaround.

## Technologies Used

*   Python
*   Flask
*   LangChain
*   Pinecone
*   Sentence Transformers (HuggingFace)
*   HTML/CSS (for the basic web interface)

## Troubleshooting

*   **`ImportError` for `pinecone` or `langchain` modules:** Ensure all packages in `requirements.txt` are installed correctly in your virtual environment.
*   **Pinecone API Key/Environment issues:** Double-check your `.env` file and Pinecone dashboard for correct credentials and index name.
*   **Model download issues (e.g., for CTransformers):** Ensure you have a stable internet connection. The model path in `src/helper.py` should be correct.
*   **`TemplateNotFound` for `index.html`:** Verify the `template_folder` path in `app.py` (e.g., `templets`).

## Future Enhancements

*   Integrate more advanced LLMs.
*   Improve UI/UX.
*   Add session management for conversation history.
*   Expand the knowledge base with more medical documents.