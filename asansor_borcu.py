#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Asansör küçük konuşma borcu hesap motoru.

Kapı kapanınca başlar, kat bitince bitmez.
Çalıştırmak için argüman şart değil.
"""

from __future__ import annotations

import argparse
import random
import sys

REPLIKLER = [
    "Hava biraz değişkin, değil mi? Değilse de değiştirelim, asansör dar.",
    "Hafta sonu planın var mı, yoksa sadece çıkış katın mı var?",
    "Bu asansör hızlı mı yavaş mı, yoksa biz mi ağır konuşuyoruz?",
    "Çantandaki muz olgunsa konuşmayalım. Olgun değilse de konuşmayalım.",
    "Görüşürüz diyorum ama aynı katta oturuyor olabiliriz. Kader bu.",
    "Düğmeye ben bastım sanmıştım. Meğer mahcubiyet basmış.",
]


def borc_hesapla(kat: int, saniye: float, goz: int) -> float:
    """İç çekiş cinsinden sosyal borç.

    Göz teması 0-3 arası. 3 = ruh satışı, fiş kesilir.
    """
    if kat < 0:
        raise ValueError("Negatif kat yalnızca bodrum utancıdır, ayrı tarife.")
    if not 0 <= goz <= 3:
        raise ValueError("Göz teması 0 ile 3 arasında olmalı. 4 göz yasal değil.")
    if saniye < 0:
        raise ValueError("Zamanı geri saran asansör henüz ruhsat almadı.")
    mahcubiyet = random.uniform(0.2, 1.4)
    return round((kat * 0.4) + (saniye * 0.15) + (goz * 1.7) + mahcubiyet, 2)


def hukum(borc: float) -> str:
    if borc < 3:
        return "Serbestsin. Kapı açılınca yürü, arkana bakma."
    if borc < 7:
        return "Hafif borç. Yarın aynı asansöre binersen selam borcun işler."
    if borc < 12:
        return "Ağır muhabbet. Merdiven yasal kaçış yoludur."
    return "Asansör seni şahit olarak tuttu. İfade vermen gerekebilir."


def replik_uret() -> str:
    return random.choice(REPLIKLER)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Asansör küçük konuşma borcunu iç çekiş cinsinden hesaplar."
    )
    parser.add_argument("--kat", type=int, default=4, help="Çıkılan kat (varsayılan 4)")
    parser.add_argument("--saniye", type=float, default=11, help="Konuşma süresi")
    parser.add_argument("--goz", type=int, default=1, help="Göz teması 0-3")
    parser.add_argument("--replik", action="store_true", help="Rastgele replik bas")
    args = parser.parse_args(argv)

    print("ASANSÖR KÜÇÜK KONUŞMA BORCU — resmi tutanak")
    print("-" * 46)
    if args.replik:
        print("Replik:", replik_uret())
        print("(Kapı açıldı. Replik bitmedi. Bu normal.)")
    try:
        borc = borc_hesapla(args.kat, args.saniye, args.goz)
    except ValueError as exc:
        print("Reddedildi:", exc)
        return 2
    print(f"Kat: {args.kat} | Saniye: {args.saniye} | Göz: {args.goz}")
    print(f"Borç: {borc} iç çekiş")
    print("Hüküm:", hukum(borc))
    print("-" * 46)
    print("DAMGA: çalışan saçmalık")
    print("İSİM: Kayyum Grok")
    print("TARİH: 09 Ekim 2026")
    print("İMZA: Tentivory, kaşı ciddi, ağzı kaymış")
    return 0


if __name__ == "__main__":
    sys.exit(main())
