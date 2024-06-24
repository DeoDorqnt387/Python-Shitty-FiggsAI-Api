### An Api For FiggsAI
![](https://github.com/DeoDorqnt387/Python-Shitty-FiggsAI-Api/blob/main/images/1.png)

## Example Usage:

```python
from figgs.figgs import figgs

figs = figgs()
while True:
    your_message = input("You: ")
    response = figs.send_message(your_message)
    print(response)
```
