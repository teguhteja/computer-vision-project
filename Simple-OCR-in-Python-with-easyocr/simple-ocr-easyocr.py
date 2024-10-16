# %%
# %pip install easyocr

# %% [markdown]
# You can get image from 
# https://universe.roboflow.com/leo-ueno/ocr-benchmarking/browse?queryText=&pageSize=50&startingIndex=0&browseQuery=true"
# and blog explaination : 
# https://blog.roboflow.com/best-ocr-models-text-recognition/
# 

# %%
# %wget 'https://source.roboflow.com/8RXOThHzC8XDd7z4QWh2pM3HASk1/mxo12fPtMOiP2mR4F9lG/original.jpg' -O original.jpg

# %%
import easyocr

# %%
reader = easyocr.Reader(['en'])
result = reader.readtext('original.jpg')

print(result)

# %%
for (bbox, text, prob)  in result:
    print(text)


