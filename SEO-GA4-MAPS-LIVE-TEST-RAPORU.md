# Öder Mimarlık — Schema, Google Maps ve UTM Canlı Test Raporu

**Rapor zamanı:** 30 Ekim 2026

## Canlı URL’ler

- Ana site: https://xn--odermimarlk-8zb.com/
- Landing: https://xn--odermimarlk-8zb.com/bireysel-ev-dekorasyonu/
- Sitemap: https://xn--odermimarlk-8zb.com/sitemap.xml
- Öder Group: https://www.odergroup.com.tr/

## Test özeti

| Kontrol | Sonuç | Açıklama |
|---|---:|---|
| Landing HTTP | PASS | Canlı landing page 200 döndü. |
| Ana sayfa HTTP | PASS | Ana site 200 döndü. |
| JSON-LD parse | PASS | Ana sayfa ve landing’deki JSON-LD blokları geçerli JSON. |
| `parentOrganization` | PASS | Öder Mimarlık entity’si Öder Group’a bağlandı. |
| Parent URL | PASS | `https://www.odergroup.com.tr/` olarak tanımlı. |
| `hasMap` | PASS | Google Maps arama URL’si schema içinde mevcut. |
| Ataşehir NAP | PASS | Telefon, e-posta ve adres sinyalleri landing schema’da mevcut. |
| Landing canonical | PASS | Canonical landing URL’sine işaret ediyor. |
| GBP UTM URL | PASS | Landing URL’si `utm_source=google`, `utm_medium=organic_local`, `utm_campaign=oder_mimarlik_gbp` taşıyor. |
| Sitemap landing | PASS | Landing URL’si canlı sitemap içinde mevcut. |

## Schema kontrolü

Beklenen ilişki:

```json
{
  "name": "Öder Mimarlık",
  "parentOrganization": {
    "@type": "Organization",
    "name": "Öder Group",
    "url": "https://www.odergroup.com.tr/"
  }
}
```

Bu ilişki hem ana site hem de bireysel ev dekorasyonu landing page’inde yer alır. Google’ın bu sinyali arama sonuçlarında göstermesi garanti değildir; schema, marka ilişkisini makine tarafından anlaşılır hale getirir.

## Google Maps bağlantısı

Schema’daki `hasMap` bağlantısı:

`https://www.google.com/maps/search/?api=1&query=Öder+Mimarlık+Ataşehir+İstanbul`

Google Maps URL’sine UTM parametresi eklemek yerine UTM, Maps profilinden siteye giden landing URL’sine eklenmiştir. Böylece Maps içindeki web tıklaması GA4’te ölçülebilir:

`https://xn--odermimarlk-8zb.com/bireysel-ev-dekorasyonu/?utm_source=google&utm_medium=organic_local&utm_campaign=oder_mimarlik_gbp`

## GA4 kontrolü

Kontrollü QA ziyaretiyle doğrulanan olaylar:

- `page_view`: 1
- `session_start`: 1
- `first_visit`: 1
- Sayfa başlığı: `Bireysel Ev Dekorasyonu İstanbul | Öder Mimarlık`
- Gerçek zamanlı aktif kullanıcı: 1 Türkiye kullanıcısı

Bu kayıt `manus_test` kaynağıyla oluşturulan test trafiğidir; gerçek müşteri trafiği olarak raporlanmamalıdır.

## Sınırlar

- `parentOrganization` schema’nın Google tarafından zengin sonuç olarak gösterileceği garanti edilemez.
- Google Business Profile hizmet/kategori değişiklikleri yetkili Öder Group hesabından yapılmalıdır.
- Search Console’da landing için indeksleme isteği gönderildi; “istek gönderildi” ile “dizine eklendi” aynı durum değildir.
- GA4 raporunda Öder Group toplamı ile Öder Mimarlık hostname/landing verisi ayrıştırılmalıdır.
