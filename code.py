import PyPDF2

import spacy



nlp = spacy.load("en_core_web_sm")



def extract_text_from_pdf(pdf_path):

    with open(pdf_path, "rb") as file:

        reader = PyPDF2.PdfReader(file)

        text = ""

        for page in reader.pages:

            text += page.extract_text() + "\n"

    return text



def extract_skills(text):

    doc = nlp(text)

    skills = [token.text for token in doc if token.ent_type_ == "ORG" or token.ent_type_ == "WORK_OF_ART"]

    return skills



resume_text = extract_text_from_pdf("resume.pdf")  # Replace with actual PDF

skills = extract_skills(resume_text)

print("Extracted Skills:", skills)
