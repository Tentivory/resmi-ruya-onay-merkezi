#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Resmi Rüya Onay Merkezi — çalışan, resmi görünümlü, tamamen saçma karar motoru."""

from __future__ import annotations

import hashlib
import random
import textwrap
from datetime import datetime

KARARLAR = [
    ("ONAYLANDI", "Rüya kamu yararına uygun bulunmuştur."),
    ("REDDEDİLDİ", "Fazla uçuş sahnesi. Yerçekimi yönetmeliğine aykırı."),
    ("EK PROTOKOL-7", "Teknik inceleme şart. Çay molasından sonra bakılacak."),
    ("MÜHÜR BEKLİYOR", "Mühür müdür odasında. Müdür rüyada."),
    ("ŞARTLI KABUL", "Rüya onaylanır; içindeki kedi konuşamaz."),
    ("ARŞİVE", "Karar yok. Dosya kalınlaşsın diye arşive alındı."),
]


def damga(metin: str) -> str:
    h = hashlib.sha256(metin.encode("utf-8")).hexdigest()[:12].upper()
    return f"RROM-{h}"


def karar_ver(ruya: str) -> tuple[str, str]:
    tohum = int(hashlib.md5(ruya.encode("utf-8")).hexdigest(), 16)
    rng = random.Random(tohum)
    return rng.choice(KARARLAR)


def belge(ruya: str) -> str:
    baslik, gerekce = karar_ver(ruya)
    no = damga(ruya + str(datetime.now().date()))
    tarih = datetime.now().strftime("%d.%m.%Y %H:%M")
    govde = textwrap.fill(ruya.strip() or "(boş rüya — yine de işleme alındı)", 56)
    return f"""
============================================================
          T.C.  RESMİ RÜYA ONAY MERKEZİ
                 KARAR BELGESİ
============================================================
Belge No : {no}
Tarih    : {tarih}
Karar    : {baslik}
------------------------------------------------------------
RÜYA ÖZETİ:
{govde}
------------------------------------------------------------
GEREKÇE:
{gerekce}
------------------------------------------------------------
DAMGA : {no}
İMZA  : Kayyum Grok
TARİH : 9 Eylül 2026
NOT   : Ciddi görünür. Ciddi değildir.
============================================================
"""


def main() -> None:
    print("Resmi Rüya Onay Merkezi'ne hoş geldiniz.")
    print("Rüyanızı tek satırda anlatın. Çıkmak için boş bırakın.\n")
    while True:
        try:
            ruya = input("Rüya > ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGise kapandı.")
            break
        if not ruya:
            print("Gise kapandı.")
            break
        print(belge(ruya))


if __name__ == "__main__":
    main()
