"""Telegram botu ile mesaj gönderir."""

from getpass import getpass
import sys
import requests


def mesaj_gonder(token, chat_id, mesaj):
    try:
        yanit = requests.post(
            f"https://api.telegram.org/bot{token}/sendMessage",
            json={"chat_id": chat_id, "text": mesaj},
            timeout=30,
        )
    except requests.RequestException:
        # Hata URL'si token içerebilir; ekrana yazdırma.
        raise RuntimeError("Telegram bağlantısı kurulamadı veya zaman aşımına uğradı.") from None

    try:
        sonuc = yanit.json()
    except ValueError:
        raise RuntimeError(f"Geçersiz Telegram yanıtı (HTTP {yanit.status_code}).") from None

    if not yanit.ok or not sonuc.get("ok"):
        raise RuntimeError(sonuc.get("description", "Mesaj gönderilemedi."))
    return sonuc["result"]["message_id"]


def main():
    print("Telegram mesaj gönderimi", flush=True)
    if sys.stdin.isatty():
        token = getpass("Bot tokenı (gizli): ").strip()
    else:
        print("Bu konsolda bot tokenı yazarken görünür olacaktır.", flush=True)
        token = input("Bot tokenı: ").strip()
    chat_id = input("Alıcı sohbet ID'si: ").strip()
    mesaj = input("Gönderilecek mesaj: ").strip()

    if not token or not chat_id or not mesaj:
        print("Bot tokenı, sohbet ID'si ve mesaj boş bırakılamaz.")
        return

    try:
        mesaj_id = mesaj_gonder(token, chat_id, mesaj)
        print(f"Mesaj gönderildi. Mesaj ID: {mesaj_id}")
    except RuntimeError as hata:
        print(f"Hata: {hata}")


if __name__ == "__main__":
    main()
