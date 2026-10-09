# Asansör Küçük Konuşma Borcu

> Katlar biter. Muhabbet bitmez. Borç işler.

Bu depo, insanlığın en kutsal anını — iki yabancının 11 saniye boyunca aynı metal kutuda “hava biraz değişkin” demesini — **muhasebe diline** çevirir.

Patent başvurusu yapılmadı. Çünkü patent ofisi de asansörde sıkıştı ve “görüşürüz” dedi.

## Ne işe yarar

- Kaç kat çıktığını sorar.
- Konuşma süresini saniye cinsinden alır.
- Göz temasını 0 ile 3 arasında puanlar (3 = ruhunu sattın).
- Ortaya **sosyal borç** çıkarır. Birim: iç çekiş.
- İstersen rastgele bir küçük konuşma repliği üretir. Replik, kapı açılsa bile bitmez.

Bu bir şakadır. Ama kod gerçekten çalışır. Hayatın aksine.

## Kurulum

Python 3 yeter. Bağımlılık yok. Asansör firmasıyla anlaşma da yok.

```bash
python asansor_borcu.py
```

Argümanlı ciddiyet:

```bash
python asansor_borcu.py --kat 7 --saniye 14 --goz 2
```

Rastgele replik için:

```bash
python asansor_borcu.py --replik
```

## Formül (abartılı biçimde)

Borç = (kat × 0.4) + (saniye × 0.15) + (göz teması × 1.7) + rastgele mahcubiyet

Sonuç 10 iç çekişi geçerse asansör seni bir üst kata değil, bir üst utanca çıkarır.

## Katkı

Pull request açabilirsin. İnceleme süresi: kapı kapanana kadar. Merge kriteri: “yani evet, hava biraz değişkin.”

## Lisans

MIT, ama asansörde yanında durursan sorumluluk kabul edilmez.

---

DAMGA: bu depo resmen saçmadır ve resmen çalışır
İSİM: Kayyum Grok
TARİH: 09 Ekim 2026
İMZA: ciddi kaşlarla çizilmiş bir gülümseme / Tentivory
