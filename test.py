"""GitHub'dan indirilen script için ek kütüphane örneği."""

import pandas as pd
import requests


def main():
    # requests ile bir HTTP isteği hazırla; bu örnek ağ bağlantısı yapmaz.
    istek = requests.Request(
        "GET",
        "https://raw.githubusercontent.com/methimi/Test/main/test.py",
        params={"ornek": "kutuphane"},
    ).prepare()
    print(f"requests sürümü: {requests.__version__}")
    print(f"Hazırlanan istek: {istek.method} {istek.url}")

    # pandas ile örnek satışların toplam tutarını hesapla.
    satislar = pd.DataFrame(
        {
            "urun": ["Kalem", "Defter", "Kalem", "Defter"],
            "adet": [3, 2, 5, 1],
            "birim_fiyat": [10, 40, 10, 40],
        }
    )
    satislar["tutar"] = satislar["adet"] * satislar["birim_fiyat"]
    ozet = satislar.groupby("urun", as_index=False)[["adet", "tutar"]].sum()

    print(f"\npandas sürümü: {pd.__version__}")
    print(ozet.to_string(index=False))
    print(f"\nToplam satış: {satislar['tutar'].sum()} TL")


if __name__ == "__main__":
    main()
