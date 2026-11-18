# Öder Mimarlık — Otomasyon Durumu (SEO / AIO / CRO)

Son doğrulama tarihi: 18 Kasım 2026 (tur 3, elle başlatılan sınama turu)
Kaynak depo: umitinform-hue/oder-mimarlik (yayın: GitHub Pages, `main`)

## Durum

| Alan | 16 Kas | 18 Kas | 18 Kas (tur 2) | Not |
|---|---|---|---|---|
| SEO teknik | İyi | İyi | İyi | Dil sayfalarının İngilizceye dönmesi düzeltildi; lang sr-ME; NAP tek biçim |
| SEO içerik-otorite | Zayıf | Zayıf | Orta− | Hizmet sayfaları 294–305 → 464–508 kelime; dış profil/yorum yok |
| AIO | Orta | Orta+ | Orta+ | 11 FAQPage; adreste posta kodu; GBP/yorum yok |
| CRO | Orta | Orta+ | Orta+ | Hizmet sayfalarında fayda satırı ve ikinci CTA; mobil sabit CTA yok |

Tur 3 (18 Kas 19:22): SEO teknik İyi; içerik Orta−; AIO Orta+; CRO İyi− (hizmet sayfalarında sabit CTA, dil sayfası formu kendi dilinde).

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

| 9 | İnce hizmet sayfaları | 18 Kas tur 2, `otomasyon/seo-aio-cro-2026-11-18b` | 294–305 → 464–508 kelime; SSS 3 → 5; FAQPage 0 → 11; fayda satırı 0 → 11 |
| — | "teşhir/depoma" yazım hatası | aynı | 11 → 0 |
| — | Dil sayfalarında Türkçe dışı tarayıcıda (Googlebot dahil) hero İngilizceye dönüyor, `lang="en"` oluyordu (script.js otomatik dil geçişi) | aynı | 11 sayfa → 0 (Playwright, en-US) |
| 2 (kısmi) | Dil sayfalarında Türkçe menü, hero CTA, 3 H2, 6 kart başlığı | aynı | 11 × 16 = 176 öğe çevrildi (locale-content.js değerleri) |
| 5 | /me/ `lang="me"` | aynı | 13 → 0 (`sr-ME`) |
| — | Adres iki farklı biçimde, posta kodu yok | aynı | görünür 12 + şema 25 + .md 2 tek biçime; postalCode 0 → 25 |

| 3 | 150 KB üstü görseller | 18 Kas tur 3, `otomasyon/seo-aio-cro-2026-11-18c` | 68 WebP kopyası; 14735 → 6351 KB; img src 168 + galeri 65 + poster 23 referans WebP; ana sayfa görsel aktarımı (390 px, kaydırmalı) 3075 → 1882 KB; hizmet sayfası 251 → 133 KB |
| — | photos.js alt alanında iç not "Serkan klasöründen…" | aynı | 65 → 0 |
| — | Dil sayfalarında yanlış gizlilik notu ("e-posta taslağı… yayına almadan önce doğrulanmalıdır") — 18 Kas tur 1'de kaçmıştı | aynı | 11 → 0 |
| 2 (kısmi) | Dil sayfalarında form, iletişim metni, 10 H2, sabit çubuk | aynı | 11 × 26 = 286 öğe; Türkçe görünür parça (bg) 228 → 201 |
| 4 | Hizmet sayfalarında mobil sabit CTA yok | aynı | 0 → 11 |

## BEKLEYEN (öncelik sırasıyla)

1. **KRİTİK – Dil sayfalarında kalan Türkçe** (sayfa başına ~200 parça / ~1130 kelime: tasarım laboratuvarı, hizmet kartı açıklamaları, fiyat hesaplayıcı, süreç, SSS, alt metinler, aria-label'lar, script.js form mesajları). Tur 1–3'te menü, CTA, 13 H2, form ve kartlar yapıldı. Engel: 11 dil × ~1100 kelime bir turda güvenli çevrilemiyor; her tur bir blok (sırada: SSS + süreç, sonra hesaplayıcı). Bekleme: 3 tur (kısmi ilerleme her turda).
2. **UYARI – Ana sayfa formu**: e-posta zorunlu, telefon isteğe bağlı; kalite kapısı "ad, telefon, şehir, mekân türü, ihtiyaç, not" diyor. Zorunlu alan değişikliği dönüşümü etkileyeceği için KULLANICI KARARI'na taşındı. Bekleme: 3 tur.
3. **UYARI – Hizmet sayfalarında ortak "KAPSAM" bölümü ve ilk 3 SSS 11 sayfada birebir aynı**. Bekleme: 1 tur.
4. **UYARI – Büyük kaynak logolar** (assets/logo/*-source.png, 1,7–1,9 MB) hiçbir sayfada kullanılmıyor; silme yasak, dokunulmadı. og:image ve şema görselleri bilinçli olarak JPG bırakıldı.
5. **BİLGİ – `locale-content.js` hiçbir sayfada yüklenmiyor** (ölü dosya). Silme yasak olduğundan dokunulmadı.

## KULLANICI KARARI BEKLEYEN

- **Görünür metinde üçüncü taraf marka adları**: ana ve dil sayfalarındaki B2B bölümünde "Bauhaus, IKEA ve benzeri markaların satın alma… ekipleri" cümlesi (12 sayfa). Kural gereği otomasyon silmedi ve çevirmedi; kaldırılması/yeniden yazılması için onay bekleniyor.
- Ana sayfa formunda e-posta yerine telefonun zorunlu olması (kalite kapısı önerisi) — karar bekleniyor.

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

| Sorgu | 16 Kas | 18 Kas | 18 Kas (tur 2) |
|---|---|---|---|
| Öder Mimarlık | çıkmadı | DOĞRULANAMADI | çıkmadı |
| Oder Mimarlık Ataşehir | — | — | çıkmadı |
| odermimarlik.com | çıkmadı | DOĞRULANAMADI | — |
| ölçüye özel mobilya Ataşehir | çıkmadı | DOĞRULANAMADI | çıkmadı (armut.com ağırlıklı) |
| mutfak dolabı tasarımı İstanbul | — | — | çıkmadı (pazar yerleri, armut.com) |
| fuar standı tasarımı İstanbul | — | — | çıkmadı (expoassist.net, stand firmaları) |
| iç mimarlık firması Ataşehir | — | — | çıkmadı (armut.com ağırlıklı) |

## Alınan dersler

- 16 Kas: zamanlanmış tur depoya yazamadı → kök neden: Claude GitHub uygulaması depo sahibinin hesabında kurulu değildi (ortak çalışan daveti tek başına yetmiyor) → kural: erişim hatasında gerçek hata mesajını yaz, tahmin etme.
- 18 Kas: `lang` kodunu değiştirmek `locale-content.js` çevirisini bozacaktı → kural: `lang` değişikliğini çeviri anahtarıyla birlikte yap.
- 18 Kas: ana sayfa KVKK kutusu doğruydu, dil sayfaları değil → kural: ana sayfayı kopya sayfalarla aynı varsayma, her dosyayı say.

- 18 Kas (tur 2): `locale-content.js` hiçbir sayfada yüklenmiyordu; durum dosyası aksini varsayıyordu → kural: bir dosyanın etkisini varsaymadan önce hangi sayfaların yüklediğini say.
- 18 Kas (tur 2): Dil sayfaları main'de Türkçe dışı tarayıcıda İngilizceye dönüyordu; yalnız kaynak okuyarak görülmedi, Playwright `locale: en-US` ile görüldü → kural: dil sayfalarını Türkçe dışı yerel ayarla da render et.

- 18 Kas (tur 3): Tur 1 "e-posta taslağı" notunu 11 → 0 saymıştı ama alt bilgideki farklı cümle ("taslak oluşturmak") kaçmıştı → kural: kaldırılan iddiayı tek ifade ile değil anahtar kelime ailesiyle say (taslak, mailto, e-posta uygulaması).
- 18 Kas (tur 3): WebP'ye geçişte video poster'ı JPG kalınca aynı görsel iki kez indi → kural: görsel değişiminde img, srcset, poster ve CSS background referanslarını birlikte say, Playwright aktarım baytıyla doğrula.

## Sonraki turun önceliği

Dil sayfalarında SSS ve süreç bölümlerinin çevirisi (BEKLEYEN 1), ardından hizmet sayfalarında yinelenen KAPSAM/SSS metinlerinin ayrıştırılması.
