from langchain_community.document_loaders import UnstructuredEmailLoader
import spacy
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
#from langchain.document_loaders import TextLoader

# Replace with the path to your .eml file
file_path = "/Users/arijitbanerjee/Downloads/visa_email.eml"

# Create an instance of the loader with the file path
loader = UnstructuredEmailLoader(file_path, mode="elements", process_attachments=True,)

# Load the data from the .eml file
data = loader.load()
raw_text = data[0].page_content

# Print the loaded data
#for doc in data:
 #   print(doc)



# Load SpaCy's small English model
nlp = spacy.load("en_core_web_sm")

# Example confidential text
confidential_text = raw_text

# Process the text using SpaCy to identify entities
doc = nlp(confidential_text)


# Extended dictionary to map entity labels to generic placeholders
entity_placeholders = {
    "ORG": "Company A",             # Organization name
    "PERSON": "Person B",           # Person's name
    "GPE": "Location C",            # Geopolitical entity (country, city, state)
    "LOC": "Place D",               # Physical location (mountain, river, etc.)
    "DATE": "Date E",               # Dates
    "TIME": "Time F",               # Specific times
    "MONEY": "Amount G",            # Monetary values
    "PERCENT": "Percentage H",      # Percentages
    "CARDINAL": "Number I",         # General numerical values
    "QUANTITY": "Quantity J",       # Measurements (weight, size, etc.)
    "EVENT": "Event K",             # Named events (e.g., conferences, battles)
    "FAC": "Facility L",            # Buildings, airports, highways, bridges, etc.
    "NORP": "Group M",              # Nationalities, religious or political groups
    "LAW": "Law N",                 # Legal documents, statutes, treaties
    "PRODUCT": "Product O",         # Products, devices, vehicles, foods
    "WORK_OF_ART": "Work P",        # Books, songs, artworks
    "LANGUAGE": "Language Q",       # Languages
    "EMAIL": "email@example.com",   # Email addresses
    "PHONE": "Phone R",             # Phone numbers
    "ADDRESS": "Address S",         # Street addresses
    "URL": "http://example.com",    # URLs and website links
    "IP": "IP Address T",           # IP addresses
    "CREDIT_CARD": "Credit Card U", # Credit card numbers (use regex to identify)
    "SSN": "SSN V",                 # Social Security Numbers (use regex to identify)
    "BANK_ACCOUNT": "Account W",    # Bank account numbers (use regex to identify)
    "LICENSE_PLATE": "Plate X",     # Vehicle license plates
    "PASSPORT": "Passport Y",       # Passport numbers (use regex to identify)
    "ID_NUMBER": "ID Z",            # General ID numbers
    "DOB": "Birth Date AA",         # Date of birth
    "CREDIT_SCORE": "Credit Score BB" # Credit scores
}


# Replace entities with placeholders
redacted_text = confidential_text
for ent in doc.ents:
    if ent.label_ in entity_placeholders:
        redacted_text = redacted_text.replace(ent.text, entity_placeholders[ent.label_])

print("Redacted Text:", redacted_text)

# Further processing with LangChain for semantic understanding (optional)
""" mbeddings = OpenAIEmbeddings()
text_splitter = CharacterTextSplitter()
docs = text_splitter.split_text(redacted_text)
embedded_docs = embeddings.embed_documents(docs)

print("Embedded Docs:", embedded_docs)
 """