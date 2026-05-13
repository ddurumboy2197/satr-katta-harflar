def katta_harflar(text):
    return ' '.join(word.capitalize() for word in text.split())

text = "satrdagi har bir so'zning birinchi harfini katta qiling"
print(katta_harflar(text))
```

```python
def katta_harflar(text):
    return text.title()

text = "satrdagi har bir so'zning birinchi harfini katta qiling"
print(katta_harflar(text))
