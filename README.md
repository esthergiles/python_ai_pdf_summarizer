# PDF Text Summarizer

This Python script utilizes the PyPDF2 library to extract text from a PDF file and then employs OpenAI's GPT-3.5-turbo model to generate a summary of the extracted text. The summarized text is intended to provide a concise overview of the content within the PDF document. This README file explains how to set up and use the code effectively.

## Prerequisites

Before you begin, ensure you have the following components installed:

- **Python**: This code is written in Python and requires a Python interpreter to run.
- **PyPDF2**: You can install it using `pip` with the following command:
`pip install PyPDF2`
- **OpenAI API Key**: You need to obtain an OpenAI API key, which will be used to access the GPT-3.5-turbo model. You should store this key securely and consider using environment variables for security.

## Usage

1. **Installation**: First, make sure you have Python and PyPDF2 installed.

2. **Set Up OpenAI API Key**: Store your OpenAI API key securely. You can do this by creating an environment variable named `OPENAI_API_KEY` and storing your API key as its value. This is crucial for security and keeping your API key private.

3. **Run the Script**:

 - Replace `"pdfname.pdf"` in the `PdfReader` initialization with the path to the PDF file you want to summarize.
 - Execute the script using the Python interpreter:
   ```
   python your_script_name.py
   ```

4. **Output**: The script will extract text from the PDF, split it into chunks, and then generate a summary for each chunk using the GPT-3.5-turbo model. The summarized text will be printed to the console.

## Functions

### `split_text(text)`

This function splits the input text into chunks based on a maximum chunk size of 2048 characters. It ensures that each chunk is no larger than the specified limit to optimize the summarization process.

### `generate_summary(text)`

This function takes a text input, splits it into manageable chunks using `split_text`, and then generates a summary for each chunk using the GPT-3.5-turbo model. It concatenates the summarized chunks into a single string and returns it as the summarized text.

## Note

- The script is configured to use the GPT-3.5-turbo engine, which is suitable for most text summarization tasks.
- You can customize the `max_tokens` parameter in the `generate_summary` function to control the length of the generated summaries.

Remember to handle your OpenAI API key securely and follow OpenAI's usage guidelines to ensure responsible and ethical use of AI models.

Enjoy summarizing PDF content with ease using this script!





