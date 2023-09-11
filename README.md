# python_ai_pdf_summarizer
A Python script that utilizes PyPDF2 to turn pdf's into text files then OpenAI's API to summarize them.
This script accepts a pdf file via the reader variable and then transcribed that to a text file utilize a Python free open source library.
Then the data in the text file is seperated into smaller chunks which are then summarized by Chat-GPT text-davinci-003 model.
Feel free to download this code and add to it as you please. The reader and API key variables will need updated before usage.

Possible improvments:
* Integrating it into a web app with an UI
* summarizing each chunk, then putting the summaries together and summarize the whole article one more time for accuracy
* Any other ideas? I'd love to hear them! 


