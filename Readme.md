# Figgs.ai Python Kütüphanesi

Bu bir python clienti Figgs.ai sitesi için.

Örnek Kullanım:

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

## Kurulum

Bu python kütüphanesini bu pip ile gerekli kütüphaneleri indirebilirsiniz:

```bash
pip install figgs-ai
```

## Kullanım

```python
from figgs import figgs
```

Sonra, `figgs` sınıfı için, auth, gerekmekte `https://www.figgs.ai/` bu siteye girip kayıt olduktan sonra sağ tık, incele, uygulamalar(Apllications) kısmından cookies'i bulun ve oradaki `figgs-auth-prod` kısmını kopyalayın ve "your-auth-key" kısmına yapıştırın:

```python
figs = figgs(
    auth = "your-auth-key",
)
```

Şimdi bazı metodları kullanabilirsiniz:

## Kullanıcı adı değiştirme

Kullanıcı adı değiştirmek için yapmanız gereken sadece şudur:

```python
figs.change_user_name("your_username")
```

## Açıklama Değiştirme

Açıklamayı değiştirmek için yapmanız gereken sadece şudur:

```python
figs.change_bio("your-desc")
```

## Nsfw gibi ayarları True, False yapmak için

Nsfw gibi ayarları True, False yaomanız gereken sadece şudur:

```python
figs.change_suggistives(True, False)
```

## Herhangi bir bota mesaj gönderme


Figgs.ai'daki herhangi bir bota mesaj göndermek için room_id ve bot_id gerekmekte. Herhangi bir bota girdiğinizde onları link kısmında görebilirsiniz. Sağdaki room_id için soldaki bot_id için.

```python
response = figs.send_message(
    "your-message",
    "your-room-id",
    "your-bot-id"
)
print(response)
```

## Şimdilik bu kadar.
