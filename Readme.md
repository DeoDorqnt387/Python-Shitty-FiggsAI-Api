## It stores messages sent by users in payload.json format. ~~but it does not store messages sent by the assistant, so the assistant's messages may not appear in the chat section of the site. (will be fixed in the future)~~ If you want to use a different chatbot, you need to clean up the payload.json.

/////////////////////////

## Example Usage:

```python
from figgs import figgs

auth = "your-auth-key"

figs = figgs(
    auth=auth,
)

room_id = "room-id"
bot_id = "bot-id"

while True:
    your_message = input("You: ")
    response = figs.send_message(your_message, room_id, bot_id)
    print(response)
```

## Usage

```python
from figgs import figgs
```

To use the code below you need auth, go to this site `https://www.figgs.ai/` and after registering, right click, inspect, find cookies in the applications section and copy the `figgs-auth-prod` part and paste it into the "your-auth-key" section:

```python
figs = figgs(
    auth = "your-auth-key",
)
```

Now you can use some methods:

## Change username

To change your username, all you need to do is this:

```python
figs.change_user_name("your_username")
```

## Change Description

To change the description, all you need to do is this:

```python
figs.change_bio("your-desc")
```

## To make settings like nsfw True, False

You just need to use this make settings like nsfw True, False:

```python
figs.change_suggistives(True, False)
```

## Send a message to any bot


To send a message to any bot in Figgs.ai you need room_id and bot_id. You can see them in the link section when you enter any bot. The right one is for room_id and the left one is for bot_id.

```python
response = figs.send_message(
    "your-message",
    "your-room-id",
    "your-bot-id"
)
print(response)
```

## That's all for now.
