# %%
# %pip install requests

# %%
import json
import requests
import pickle

url = "https://ocr.asprise.com/api/v1/receipt"
# image = "template-walmart-1-1.png"
image = "template-walmart-3-screenshot-1.png"


# %%
res = requests.post(url,
    data= {
        'api_key': 'TEST',
        'recognizer': 'auto',
        'ref_no': 'oct_python_123'
    },
    files = {
        'file': open(image, 'rb')
    })
print(res)

# %%
with open("response2.json", "w") as f:
    json.dump(json.loads(res.text),f)

# %%
with open("response2.json", "r") as f:
    data = json.load(f)

print(data['receipts'][0].keys())
items = data['receipts'][0]['items']
print(f"Your purchase at {data['receipts'][0]['merchant_name']}")

for item in items:
    print(f"{item['description']} - ${item['amount']}")


# %%
print("-" * 30)

print(f"Subtotal: {data['receipts'][0]['subtotal']}")
print(f"Tax: {data['receipts'][0]['tax']}")
print("-" * 30)

print(f"Total: {data['receipts'][0]['tax']}")


# %%



