from PyPDF2 import PdfReader
import openai

reader = PdfReader("BrianDrolet.pdf")
number_of_pages = len(reader.pages)
page = reader.pages[0]

# Needs to be stored in an evniromental variable for security
openai.api_key = 'your key'

#-------------- Functions----------------------
# Preprocess Data
def split_text(text):
    max_chunk_size = 2048
    chunks = []
    current_chunk = ""
    for sentence in text.split("."):
        if len(current_chunk) + len(sentence) < max_chunk_size:
            current_chunk += sentence + "."
        else:
            chunks.append(current_chunk.strip())
            current_chunk = sentence + "."
    if current_chunk:
        chunks.append(current_chunk.strip())
    return chunks

# Summarize Data using GPT-3.5-turbo
def generate_summary(text):
    input_chunks = split_text(text)
    output_chunks = []
    for chunk in input_chunks:
        prompt = f"Please summarize the following text:\n{chunk}\n\nSummary:"
        response = openai.Completion.create(
            engine="text-davinci-003",  # GPT-3.5-turbo engine
            prompt=prompt,
            max_tokens=150,
            n=1,
            stop=None
        )
        summary = response.choices[0].text.strip()
        output_chunks.append(summary)
    return " ".join(output_chunks)

#-------------- Main Calls ----------------------
# Extracted text from PDF
text = page.extract_text()

# Call the generate_summary function and get the summarized text
summarized_text = generate_summary(text)

# Print the summarized text
print("Summarized Text:", summarized_text)
