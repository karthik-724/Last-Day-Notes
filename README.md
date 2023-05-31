# Last-Day-Notes-
A simple application to generate notes using ChatGPT API 

All you need is the chapter name and syllabus 
What you get is a downloadable pdf file of complete notes covering all the topics point wise

* Note that Chat gpt api key free validity is limited .
* In the web interface Chat GPT Api key must be provided.

Steps to get an API key in chat GPT
    * Go to https://platform.openai.com/account/api-keys
    * Create a new secret key 
    * Copy the api key and store it safely.
    
Application ( planned as of 31-05-2023 )
    * provide the api key ( so it uses your account to search for topics )
    * provide the chapter name or subject name 
    * provide the syllabus separated using commas ','
    * Click on submit 
    * click on download to get the pdf 
    
Backend
    * The syllabus list is split into topic list 
    * Each topic is then searched using chatgpt API.
    * The topics and explainations are made into a document .
    * The document is saved as pdf and made available .
