import requests
prompt="a traffic camera image to count vehicles by type and estimate congestion level at an intersection."
url="https://image.pollinations.ai/prompt/"+requests.utils.quote(prompt)
img=requests.get(url).content
with open("o.png","wb") as f:
    f.write(img)