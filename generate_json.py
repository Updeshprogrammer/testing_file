# from Image_to_string import text
import re


def parse_data(text):
    data = {}
    data['invoice_number'] = re.search(r'INV-\d+', text).group(0)
    data['invoice_date'] = re.search(r'([0-9]{2})\s([A-Za-z]{3})\s([0-9]{4})', text).group(0)
    data['place_to_supply'] = re.search(r'\d+-[A-Za-z]+', text).group(0)

    lines = text.split("\n")

    for i, line in enumerate(lines):
        if "Billing address:" in line:
            data['Billing_address'] = lines[i + 1].strip()[1:-16] + lines[i + 1 + 1].strip()[1:-15]
        elif 'Item ' in line:
            data['item_1'] = lines[i + 1].strip()[2:12]
            data['item_2'] = lines[i + 3].strip()[2:26]

    data['HSN'] = re.search(r'\b\d{8}\b', text).group(0)
    data['TAX_amount_item1'] = re.search(r'(\d{1,3},\d{3}\.\d{2})\n\(28%\)', text).group(0)
    data['TAX_amount_item2'] = re.search(r'\d+\.\d+ \(28%\)', text).group(0)
    data['Amount_item_1'] = re.search(r'\d{1,3},\d{3}.0{2}', text).group(0)
    data['Amount_item_2'] = re.search(r'\b\d{1},\d{3}.0{2}', text).group(0)
    data['Total_Taxable_amount'] = re.search(r'Taxable Amount = ([\d,]+\.\d{2})', text).group(1)
    data['Total_IGST'] = re.search(r'IGST 28.0% %(\d{1},\d{2},\d{3}\.\d{2})', text).group(1)
    data['Total_Amount_Payable'] = re.search(r'Amount Payable: . (\d{1},\d{2},\d{3}\.\d{2})', text).group(1)
    return data


# invoice_data = parse_data(text)
# print(invoice_data)
