# Öder Mimarlık Haftalık SEO + GA4 Raporu — Örnek Çıktı

> Bu dosya format örneğidir. Aşağıdaki sayısal değerler örnek/temsili değerlerdir; gerçek ScheduleTask çalışması yerine geçmez.

**Rapor tarihi:** 03 Kasım 2026
**Dönem:** 27 Ekim–02 Kasım 2026
**Landing:** https://xn--odermimarlk-8zb.com/bireysel-ev-dekorasyonu/

## Özet

Landing page canlı, HTTP 200 ve sitemap içinde. Search Console tarafında URL Inspection sonucu “indeksleme isteği gönderildi” olarak raporlanıyor; bu, URL’nin kesin olarak dizine eklendiği anlamına gelmiyor. GA4 hostname filtresinde 7 günlük trafik düşük fakat ölçüm akışı çalışıyor. Test/QA ziyaretleri gerçek müşteri trafiğinden ayrıldı.

## Search Console

| Metrik | Son 7 gün | Son 28 gün |
|---|---:|---:|
| Tıklama | 2 | 6 |
| Gösterim | 41 | 118 |
| CTR | %4,9 | %5,1 |
| Ortalama konum | 37,4 | 42,8 |

Öne çıkan sorgu kümeleri: “Ataşehir iç mimarlık”, “bireysel ev dekorasyonu İstanbul”, “özel ölçü mutfak dolabı”. URL Inspection sonucu ayrıca “istek gönderildi” ve “dizine eklendi” durumlarından hangisi gerçekse açıkça yazılmalıdır.

## GA4 trafik ve landing akışı

| Metrik | Son 7 gün |
|---|---:|
| Aktif kullanıcı | 4 |
| Oturum | 5 |
| Landing page görüntüleme | 6 |
| Google organic/local | 2 oturum |
| Direkt | 2 oturum |
| Referral | 1 oturum |

Hostname filtresi: `xn--odermimarlk-8zb.com`. Öder Group toplam property verisi bu tabloya dahil edilmemiştir.

## Lead ve WhatsApp olayları

| Olay | Sayı | Değerlendirme |
|---|---:|---|
| `oder_whatsapp_click` | 1 | CTA etkileşimi ölçülmüş |
| `oder_generate_lead` | 0 | Henüz doğrulanmış form lead’i yok |
| `oder_hero_lead` | 1 | Hero CTA tıklaması |
| `oder_form_validation_error` | 0 | Form sürtünmesi görünmüyor |

`manus_test`, `qa` ve benzeri kampanyalar gerçek dönüşüm sayımına alınmaz.

## Google Maps ve yerel SEO

Öder Mimarlık, Öder Group Business Profile içinde grup içi hizmet kolu olarak konumlandırılmalı. Mükerrer bağımsız profil açılmamalı. Landing bağlantısında `utm_source=google`, `utm_medium=organic_local`, `utm_campaign=oder_mimarlik_gbp` kullanılmalı.

## Değişim, risk ve sonraki aksiyonlar

1. Bireysel ev dekorasyonu landing page’i için yeni sorgu kümelerini izlemeye devam et.
2. Google Business Profile içinde Öder Mimarlık hizmet listesini ve gerçek proje fotoğraflarını tamamla.
3. WhatsApp tıklamasından gerçek müşteri görüşmesine geçişi işletme tarafında haftalık olarak eşleştir.
4. Organik hacim düşük olduğu için 7 günlük değişimleri tek başına büyüme kanıtı sayma; 28 günlük trendi esas al.
