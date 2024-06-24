## It stores messages sent by users in payload.json format. ~~but it does not store messages sent by the assistant, so the assistant's messages may not appear in the chat section of the site. (will be fixed in the future)~~ If you want to use a different chatbot, you need to clean up the payload.json.

/////////////////////////

## Example Usage:

```python
from figgs.figgs import figgs

figs = figgs()
while True:
    your_message = input("You: ")
    response = figs.send_message(your_message)
    print(response)
```
