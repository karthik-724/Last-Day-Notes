import openai
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


openai.api_key = "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"

chapter = input("Enter chapter name : ")
syllabus = input("Enter syllabus (list of topics separated using commas ',')")

def extract_topics(syllabus):
    topics = []
    syllabus_list = syllabus.split(',')
    for topic in syllabus_list:
            topics.append(topic.strip())

    return topics

def create_pdf(topics, explanations, filename):
    doc = SimpleDocTemplate(filename, pagesize=letter)
    styles = getSampleStyleSheet()
    elements = []

    for topic, explanation in zip(topics, explanations):
        topic_paragraph = Paragraph(topic, styles['Heading1'])
        elements.append(topic_paragraph)
        paragraphs = explanation.split('\n')
        for paragraph in paragraphs:
            explanation_paragraph = Paragraph(paragraph, styles['BodyText'])
            elements.append(explanation_paragraph)

        elements.append(Spacer(1, 12))

    doc.build(elements)
    print(f"PDF created: {filename}")


topics = extract_topics(syllabus)
topic_explainations = []

for  topic in topics:
    print("querying topic : " + topic)
    query = "Explain in detail about "  + topic + "in " + chapter
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": query }] )
    topic_explainations.append(response["choices"][0]["message"]["content"])


create_pdf(topics, topic_explainations, 'nlp.pdf')


                                                                             
                                             