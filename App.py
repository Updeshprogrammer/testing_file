import streamlit as st
from PIL import Image
import pytesseract
import json
import re
from Image_to_string import text_extractor
from generate_json import parse_data

app_mode = st.sidebar.selectbox("Select Page",['Home', 'Invoice Data Extractor'])

# HOME PAGE
if app_mode == 'Home':
    st.title('Invoice Data Extractor')
    st.header('Overview')
    st.write('The InvoiceDataExtractor project aims to automate the extraction of structured data from invoices and store it in a JSON format for further processing or analysis.')
    st.markdown("""
##### Key Features:
- 1. Data Extraction:
  - Text Parsing: Utilizes text parsing techniques (possibly with regular expressions or specialized libraries) to identify and extract key fields from invoices.
  - OCR Integration: Optionally integrates Optical Character Recognition (OCR) technology to handle scanned or image-based invoices.
- 2. Data Structuring:
  - Field Identification: Recognizes and categorizes fields such as invoice number, date, customer details, billing items, quantities, prices, taxes, etc.
  - Normalization: Ensures extracted data is standardized and formatted correctly for consistency.
- 3. Output Format:
  - JSON Output: Converts the extracted data into JSON format, making it easy to store and process programmatically.
- 4. Customization and Configuration:
  - Configurable Rules: Allows customization of extraction rules and templates to handle different invoice layouts and formats.
  - Error Handling: Includes robust error handling mechanisms to manage exceptions during extraction.
""")
    st.markdown("""
    ##### Project Benefits:
    - Efficiency: Reduces manual effort in invoice data entry and processing.
    - Accuracy: Minimizes errors associated with manual data extraction.
    - Scalability: Handles large volumes of invoices efficiently.
    - Integration: Can be integrated with existing systems for seamless data flow.
    """)

# Invoice Data Extractor PAGE
if app_mode == 'Invoice Data Extractor':
    st.title('Invoice Data Extractor')
    # st.set_page_config(page_title="Upload File")
    image_file = st.file_uploader(label='Ye rahi teri file',type=["png", "jpg", "jpeg"])
    if image_file is not None:
        # st.write(type(image_file))
        # st.write(dir(image_file))
        # st.image(load_image(image_file))
        with st.expander("Extracted Text"):
            st.write(str(text_extractor(image_file)))
        text = text_extractor(image_file)
        with st.expander("Extracted JSON Data"):
            st.write(parse_data(text))
        invoice_data = parse_data(text)
        # json_path = 'invoice_data.json'
        # with open(json_path, 'w') as json_file:
        #     json.dump(invoice_data, indent=4)
        # st.download_button(label='Generate JSON', data=, indent=4))


        json_data = json.dumps(invoice_data, indent=4)

        # Create a download button for the JSON file
        st.download_button(
            label="Download JSON",
            data=json_data.encode('utf-8'),
            file_name='data.json',
            mime='application/json'
        )

