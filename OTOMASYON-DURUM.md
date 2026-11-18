# Öder Mimarlık — Otomasyon Durumu (SEO / AIO / CRO)

Son doğrulama tarihi: 18 Kasım 2026 (tur 2, zamanlanmış)
Kaynak depo: umitinform-hue/oder-mimarlik (yayın: GitHub Pages, `main`)

## Durum

| Alan | 16 Kas | 18 Kas | 18 Kas (tur 2) | Not |
|---|---|---|---|---|
| SEO teknik | İyi | İyi | İyi | Dil sayfalarının İngilizceye dönmesi düzeltildi; lang sr-ME; NAP tek biçim |
| SEO içerik-otorite | Zayıf | Zayıf | Orta− | Hizmet sayfaları 294–305 → 464–508 kelime; dış profil/yorum yok |
| AIO | Orta | Orta+ | Orta+ | 11 FAQPage; adreste posta kodu; GBP/yorum yok |
| CRO | Orta | Orta+ | Orta+ | Hizmet sayfalarında fayda satırı ve ikinci CTA; mobil sabit CTA yok |

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

## BEKLEYEN (öncelik sırasıyla)

1. **KRİTİK – Dil sayfalarında kalan Türkçe**: eyebrow'lar, kart açıklamaları, görsel alt metinleri, 10 H2, form ve fiyat hesaplayıcı etiketleri (menü/CTA/3 H2/kart başlıkları 18 Kas'ta yapıldı). `locale-content.js`'te bu metinlerin çevirisi yok; yeni çeviri gerekir. Bekleme: 2 tur → sonraki turda zorunlu (ERTELEME YASAĞI).
2. **UYARI – Büyük görseller**: 150 KB üstü JPG/PNG. WebP + width/height. Bekleme: 2 tur → sonraki turda zorunlu.
3. **UYARI – Ana sayfa formu** alan sayısı gözden geçirme. Bekleme: 2 tur → sonraki turda zorunlu (en azından ölçüm ve öneri).
4. **UYARI – Hizmet sayfalarında mobilde sabit telefon/WhatsApp CTA yok** (ana ve dil sayfalarında var). Bekleme: 0 tur.
5. **UYARI – Hizmet sayfalarında ortak "KAPSAM" bölümü ve ilk 3 SSS 11 sayfada birebir aynı** (yinelenen metin). Bekleme: 0 tur.
6. **BİLGİ – `locale-content.js` hiçbir sayfada yüklenmiyor** (ölü dosya). Silme yasak olduğundan dokunulmadı.

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

## Sonraki turun önceliği

Dil sayfalarında kalan Türkçe (BEKLEYEN 1) ve büyük görseller (BEKLEYEN 2) — ikisi de iki turdur bekliyor, sonraki turda PR'a girmeli. Ardından hizmet sayfalarına mobil sabit CTA.
