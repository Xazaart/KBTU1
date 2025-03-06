import re

# Function to parse receipt

def parse_receipt(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()

    # Regex pattern to extract items
    item_pattern = re.compile(
        r'\d+\.\n(.+)\n(\d+,\d+) x (\d+[ ,\d]*)\n(\d+[ ,\d]*)', re.MULTILINE)

    items = item_pattern.findall(content)

    parsed_items = []

    for item in items:
        name = item[0].strip()
        quantity = float(item[1].replace(',', '.'))
        unit_price = float(item[2].replace(' ', '').replace(',', '.'))
        total_price = float(item[3].replace(' ', '').replace(',', '.'))

        parsed_items.append({
            'name': name,
            'quantity': quantity,
            'unit_price': unit_price,
            'total_price': total_price
        })

    # Extract total amount
    total_pattern = re.compile(r'ИТОГО:\n(\d+[ ,\d]*)')
    total_match = total_pattern.search(content)
    total_amount = float(total_match.group(1).replace(' ', '').replace(',', '.')) if total_match else None

    return parsed_items, total_amount

# Example usage
items, total_amount = parse_receipt('row.txt')

for item in items:
    print(item)

print('Total Amount:', total_amount)
