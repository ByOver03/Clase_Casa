text = "Python,Odoo,Docker,Ubuntu"
text = text.split(",")
for i in range(len(text)):
    print(text[i])
text = " ". join(text)
print(text)