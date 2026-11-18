# Öder Mimarlık — Otomasyon Durumu (SEO / AIO / CRO)

Son doğrulama tarihi: 18 Kasım 2026
Kaynak depo: umitinform-hue/oder-mimarlik (yayın: GitHub Pages, `main`)

## Durum

| Alan | 16 Kas | 18 Kas | Not |
|---|---|---|---|
| SEO teknik | İyi | İyi | lastmod, 404 ve ayrışık başlıklar eklendi |
| SEO içerik-otorite | Zayıf | Zayıf | Hizmet sayfaları hâlâ ince; dış profil/yorum yok |
| AIO | Orta | Orta+ | llms.txt ve sameAs eklendi; yorum ve GBP yok |
| CRO | Orta | Orta+ | Hizmet sayfalarında telefon, iç link ve olay takibi |

## TAMAMLANDI

| # | Bulgu | Tur / dal | Önce → sonra |
|---|---|---|---|
| 1 | Dil sayfalarında "Form gönderimi e-posta taslağı açar" yanlış notu | 18 Kas, `otomasyon/seo-aio-cro-2026-11-18` | 11 → 0 geçiş |
| 1b | /en/ ve diğer dil sayfalarında "Mustafa klasöründeki…" iç notu | aynı | 11 → 0 geçiş |
| 2 | /llms.txt yok | aynı | 404 → dosya var |
| 3 | sitemap.xml lastmod yok | aynı | 0/24 → 24/24 |
| 4a | Hizmet sayfalarında tel: bağlantısı yok | aynı | 11 sayfada 0 → 3 |
| 4b | Hizmet sayfaları arası iç link yok | aynı | 0 → 5 (+ev sayfalarında bireysel ev) |
| 4c | Hizmet sayfalarında dönüşüm olayı yok | aynı | 0 → phone/whatsapp/email/cta_click |
| 5a | sameAs yok | aynı | 0 → 25 şema bloğu (Instagram) |
| 5b | Görünür çalışma saati yok | aynı | 0 → 24 sayfa (13 ana/dil/ev + 11 hizmet) |
| 7 | /bs/, /hr/, /me/ aynı title | aynı | 3 aynı → 3 farklı |
| 8 | SEO-ACTION-LOG.md `form_submit` diyordu, kod `generate_lead` | aynı | belge koda uyduruldu |
| 10a | Özel 404 sayfası yok | aynı | eklendi (noindex) |
| — | Dil sayfalarında KVKK onay kutusunun name alanı yoktu; Formspree'ye `kvkk_consent=not_accepted` gidiyordu | aynı | 1/12 → 12/12 sayfa |
| — | Formspree hatasında olmayan "e-posta taslağı"na yönlendiren mesaj | aynı | düzeltildi + `form_error` olayı |

## BEKLEYEN (öncelik sırasıyla)

1. **KRİTİK – İnce hizmet sayfaları** (11 sayfa, ~220–240 kelime, aynı üç H2): sayfaya özgü kapsam, süreç, teklif için gerekenler ve SSS (görünür SSS = FAQPage). Bekleme: 1 tur.
2. **KRİTİK – Dil sayfalarında Türkçe kalan arayüz** (menü, konsept panosu, fiyat hesaplayıcı, form, 13 H2). Çeviri `locale-content.js` anahtarlarıyla yapılmalı. Bekleme: 1 tur.
3. **UYARI – Büyük görseller**: 150 KB üstü 60 JPG/PNG (serkan-*.jpg 250–456 KB; logo kaynakları 1,7–1,9 MB). WebP + width/height. Bekleme: 1 tur.
4. **UYARI – Ana sayfa formu**: alan sayısı/zorunlu alan gözden geçirilmeli. Bekleme: 1 tur.
5. **UYARI – /me/ `lang="me"`** geçerli bir dil kodu değil; `locale-content.js` bu anahtarı kullandığı için ikisi birlikte `sr-ME`'ye taşınmalı. Bekleme: 1 tur.

## KULLANICI KARARI BEKLEYEN

- Öder Mimarlık'a ait Google İşletme Profili bağlantısı (varsa) — bilgi bekleniyor.
- Diğer sosyal profiller (Instagram dışında) — bilgi bekleniyor.
- Gerçek müşteri yorumları / adı verilebilir referanslar (onaylı metin olarak) — bilgi bekleniyor.
- Çalışma günleri (şemaya `openingHoursSpecification` için) — bilgi bekleniyor.
- Ofis koordinatı (şemaya `geo` için) — bilgi bekleniyor.
- Google Search Console indeks kontrolü ve sitemap gönderimi — kullanıcı işi.
- odermimarlik.com.tr için sunucu tarafı 301 — kullanıcı işi (alan adı sağlayıcısı/Cloudflare).

## Kullanıcının verdiği bilgiler

- 16 Kas 2026: Instagram kullanıcı adı `odermimarlik` → https://www.instagram.com/odermimarlik/ (profil içeriği otomasyon tarafından DOĞRULANAMADI: instagram.com robots kuralı okumayı engelliyor).

## Onaylı metinler

- "Mobilya iyi, mekân bambaşka." (slogan)

## Bilinçli yapılmayanlar

- Öder Group GitHub'ı (odergroup2023-design hesabındaki depolar) bu iş için kullanılmaz — 17 Kas 2026.
- `openingHoursSpecification` gün bilgisi olmadan eklenmez.
- Hizmet sayfalarına ana sayfaya özgü `script.js` yüklenmez (hesaplayıcı/form öğelerini arar, hata verir); sayfa içi küçük takip betiği kullanılır.

## Görünürlük gözlemi (ABD tabanlı arama aracı; sıralama değil)

| Sorgu | 16 Kas | 18 Kas |
|---|---|---|
| Öder Mimarlık | çıkmadı | DOĞRULANAMADI |
| odermimarlik.com | çıkmadı | DOĞRULANAMADI |
| ölçüye özel mobilya Ataşehir | çıkmadı | DOĞRULANAMADI |

## Alınan dersler

- 16 Kas: zamanlanmış tur depoya yazamadı → kök neden: Claude GitHub uygulaması depo sahibinin hesabında kurulu değildi (ortak çalışan daveti tek başına yetmiyor) → kural: erişim hatasında gerçek hata mesajını yaz, tahmin etme.
- 18 Kas: `lang` kodunu değiştirmek `locale-content.js` çevirisini bozacaktı → kural: `lang` değişikliğini çeviri anahtarıyla birlikte yap.
- 18 Kas: ana sayfa KVKK kutusu doğruydu, dil sayfaları değil → kural: ana sayfayı kopya sayfalarla aynı varsayma, her dosyayı say.

## Sonraki turun önceliği

İnce hizmet sayfalarının içeriği (BEKLEYEN 1), ardından dil sayfası çevirileri (BEKLEYEN 2).
