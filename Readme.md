# Figgs.ai Python Kütüphanesi

Bu bir python clienti Figgs.ai sitesi için.

## Kurulum

Bu python kütüphanesini bu pip ile gerekli kütüphaneleri indirebilirsiniz:

```bash
pip install figgs-ai
```

## Kullanım

İlk olarak `figgs` clientini çağırın ve import deriken `figgs` Yazın:

```python
from figgs import figgs
```

Sonra, `figgs` sınıfı için, auth, gerekmekte `https://www.figgs.ai/` bu siteye girip kayıt olduktan sonra sağ tık, incele, uygulamalar(Apllications) kısmından cookies'i bulun ve oradaki `figgs-auth-prod` kısmını kopyalayın:

```python
figs = figgs(
    auth = "your-auth-key",
)
```

Şimdi bazı metodları kullanabilirsiniz:

## Kullanıcı adı değiştirme

Kullanıcı adı değiştirmek için yapmanız gereken sadece şudur:

```python
client.change_user_name("your_username")
```

## Açıklama Değiştirme

Kullanıcı adı değiştirmek için yapmanız gereken sadece şudur:

```python
client.change_bio("your-desc")
```

## Nsfw gibi ayarları True, False yapmak için

Nsfw gibi ayarları True, False yaomanız gereken sadece şudur:

```python
client.change_suggistives(True, False)
```

## Herhangi bir bota mesaj gönderme


Figgs.ai'daki herhangi bir bota mesaj göndermek için room_id ve bot_id gerekmekte. Herhangi bir bota girdiğinizde onları link kısmında görebilirsiniz. Birisi sağdaki room_id için soldaki bot_id için.

```python
client.send_message("your-message", "your-room-id", "your-bot-id")
```

## Şimdilik bu kadar.
