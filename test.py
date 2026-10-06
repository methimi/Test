"""Telegram botu ile mesaj gönderir."""

import requests
import time


BOT_TOKEN = "8978352240:AAEE0QVJDCsS933q9fsiwrQnbl-iZL8QfIs"
CHAT_ID = "536477799"
TEST_MESAJI = "Merhaba! Bu, Python uygulamasından gönderilen bir test mesajıdır."


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
    if (
        not BOT_TOKEN.strip()
        or not CHAT_ID.strip()
        or BOT_TOKEN == "BURAYA_BOT_TOKENINI_YAZ"
        or CHAT_ID == "BURAYA_CHAT_ID_YAZ"
    ):
        print("Dosyanın başındaki BOT_TOKEN ve CHAT_ID alanlarını doldur.")
        return

    print("Her 10 saniyede bir mesaj gönderilecek. Durdurmak için Ctrl+C.", flush=True)
    try:
        while True:
            try:
                mesaj_id = mesaj_gonder(BOT_TOKEN, CHAT_ID, TEST_MESAJI)
                print(f"Mesaj gönderildi. Mesaj ID: {mesaj_id}", flush=True)
            except RuntimeError as hata:
                print(f"Hata: {hata}", flush=True)
            time.sleep(10)
    except KeyboardInterrupt:
        print("\nMesaj gönderimi durduruldu.", flush=True)


if __name__ == "__main__":
    main()
