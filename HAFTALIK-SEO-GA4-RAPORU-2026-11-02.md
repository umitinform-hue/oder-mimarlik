# Öder Mimarlık Haftalık SEO + GA4 Performans Raporu

**Rapor tarihi:** 02 Kasım 2026
**Landing:** https://odermimarlik.com/bireysel-ev-dekorasyonu/
**İstenen URL:** https://odermimarlik.com/bireysel-ev-dekorasyonu/

## Özet

Canonical alan adı olan `https://odermimarlik.com/bireysel-ev-dekorasyonu/` canlı kontrolde HTTP 200 döndürüyor, landing içeriği, CTA’lar, form ve FAQ bölümü yükleniyor. Sitemap içinde landing URL’si mevcut.

Kritik bulgu: Kullanıcının verdiği Punycode URL (`odermimarlik.com`) standart HTTP istemcisinde landing path için HTTP 404 ve “Yönlendiriliyor…” noindex şablonu döndürüyor. JavaScript destekli tarayıcı sayfayı canonical domain’e taşıyabiliyor; ancak crawler ve bazı sosyal önizleme istemcileri JavaScript çalıştırmayabilir. Bu nedenle Punycode alan adından canonical alan adına sunucu seviyesinde 301 yönlendirme veya GitHub Pages custom-domain yapılandırması düzeltilmelidir.

Google hesap oturumu bu çalıştırmada yeniden giriş ekranına düştüğü için 02 Kasım’a ait yeni GA4 ve Search Console panel verileri doğrulanamadı. Aşağıdaki GA4/Search Console rakamları “son doğrulanabilir snapshot” olarak ayrıca etiketlenmiştir; yeni rapor dönemi verisi gibi sunulmamıştır.

## Canlı teknik test

| Kontrol | Sonuç |
|---|---|
| Canonical domain landing | HTTP 200 |
| Canonical domain sitemap | HTTP 200 |
| Canonical domain robots.txt | HTTP 200 |
| Canonical domain landing sitemap kaydı | Var |
| Punycode landing URL | HTTP 404 / JS yönlendirme şablonu |
| Punycode sitemap | HTTP 404 / JS yönlendirme şablonu |
| Landing içerik | Hero, hizmet kapsamı, süreç, form, FAQ ve WhatsApp CTA mevcut |
| Landing canonical etiketi | Punycode URL’ye işaret ediyor; erişilebilirlik sorunu nedeniyle yeniden düzenlenmeli |

## Search Console

### Yeni rapor dönemi

Yeni URL Inspection ve 7/28 günlük performans verisi bu çalıştırmada alınamadı; Google hesabı yeniden giriş ekranına yönlendirdi. Bu nedenle aşağıdaki alanlar **veri yok / doğrulanamadı** olarak kabul edilmelidir:

- Landing URL’nin kesin indeks durumu
- Son canlı URL Inspection sonucu
- Son 7 günlük landing tıklama ve gösterim
- Son 28 günlük landing tıklama ve gösterim
- Landing sorguları, CTR ve ortalama konum

### Son doğrulanabilir snapshot

Önceki Search Console canlı panel snapshot’ında:

- Toplam web arama tıklaması: 0
- Dizine eklenen sayfa: 1
- Dizine eklenmeyen sayfa: 0
- Dizine eklenmeyen video sayfası: 3
- Dizine eklenen video sayfası: 0
- Core Web Vitals: Veri yok
- HTTPS URL: 4
- HTTPS olmayan URL: 0

Bu değerler 02 Kasım’ın yeni ölçümü olarak değil, son doğrulanabilir panel snapshot’ı olarak değerlendirilmelidir.

## GA4

### Yeni rapor dönemi

GA4 hesabı bu çalıştırmada giriş ekranına yönlendiği için Öder Mimarlık hostname ve landing path filtreli yeni 7/28 günlük veriler alınamadı. Aşağıdaki metrikler bu nedenle **doğrulanamadı**:

- `odermimarlik.com` hostname’i için son 7 gün aktif kullanıcı
- Son 28 gün aktif kullanıcı
- `/bireysel-ev-dekorasyonu/` görüntüleme sayısı
- Landing kaynak/medium dağılımı
- Landing şehir dağılımı
- `oder_generate_lead`
- `oder_whatsapp_click`

### Son doğrulanabilir GA4 snapshot’ı

Önceki GA4 panelinde son 7 gün mülk toplamı şu şekilde görünüyordu. Bu değerler Öder Group toplam mülk görünümüdür; Öder Mimarlık’a özel kabul edilmemelidir:

| Metrik | Son doğrulanabilir değer |
|---|---:|
| Etkin kullanıcı | 23 |
| Etkinlik sayısı | 180 |
| Görüntüleme sayısı | 25 |
| Önemli faaliyet | 0 |
| Gerçek zamanlı kullanıcı | 1 |

Kanal görünümü:

| Kanal | Oturum |
|---|---:|
| Organic Search | 16 |
| Direct | 12 |
| AI Assistant | 1 |
| Organic Social | 2 |
| Referral | 0 |

Kaynak sinyalleri:

- `google / organic`: 16 oturum
- `(direct) / (none)`: 12 oturum
- `chatgpt.com / ai-assistant`: 1
- `linkedin / organic`: 1
- `ig / social`: 1
- `linkedin.com / referral`: 1

Bu snapshot içinde test/QA kampanyaları gerçek müşteri trafiği olarak raporlanmamıştır.

## Dönüşüm sinyalleri

Landing kodu şu olayları üretmektedir:

- `oder_generate_lead`
- `oder_whatsapp_click`
- `oder_hero_lead`
- `oder_form_validation_error`

CTA standardizasyonu `6462f72` commit’inde yapıldı. Ancak GA4 paneli erişilemediği için bu rapor döneminde olayların gerçek adetleri doğrulanamadı. Önceki snapshot’ta önemli faaliyet sayısı 0’dı; bu olayların GA4’te önemli faaliyet olarak işaretlenmesi halen kontrol edilmelidir.

## Kaynaklar

- Canlı landing: `https://odermimarlik.com/bireysel-ev-dekorasyonu/`
- Sitemap: `https://odermimarlik.com/sitemap.xml`
- Robots: `https://odermimarlik.com/robots.txt`
- Repository: `umitinform-hue/oder-mimarlik`
- Son landing CTA düzeltme commit’i: `6462f72`
- Son rapor dokümantasyonu commit’i: `43393b1`

## Değişim ve önerilen aksiyonlar

### Öncelik 1 — Punycode/canonical erişim sorunu

Punycode custom domain için server-level 301 yönlendirmesi kurulmalı veya GitHub Pages custom domain/CNAME yapılandırması, hem Punycode hem Unicode alan adında aynı dosya ağacını sunacak şekilde düzeltilmelidir. Hedef:

```text
https://odermimarlik.com/bireysel-ev-dekorasyonu/
→ 301 → https://odermimarlik.com/bireysel-ev-dekorasyonu/
```

Punycode URL’de 404/noindex HTML bırakılmamalıdır.

### Öncelik 2 — Canonical uyumu

Canonical etiketleri erişilebilir ve tekil canonical domain olan `https://odermimarlik.com/` ile uyumlu hale getirilmeli. Search Console property’si de kullanılan canonical domain ile aynı tercih üzerinde raporlanmalıdır.

### Öncelik 3 — GA4 özel raporu

GA4’te şu koşullarla landing özel rapor kaydedilmeli:

```text
hostname = odermimarlik.com veya odermimarlik.com
page_path = /bireysel-ev-dekorasyonu/
```

Ayrıca `oder_generate_lead` ve `oder_whatsapp_click` önemli faaliyet olarak işaretlenmeli.

### Öncelik 4 — Search Console URL Inspection

Canonical domain landing URL’si ve Punycode URL’si ayrı ayrı incelenmeli. “İndeksleme isteği gönderildi” durumu “dizine eklendi” olarak raporlanmamalı.

### Öncelik 5 — GBP ve gerçek lead eşleştirme

Öder Group Business Profile içinde Öder Mimarlık hizmet linki ve fotoğrafları güncellenmeli. WhatsApp tıklaması gerçek görüşmeye dönüşüyor mu işletme tarafındaki müşteri konuşmalarıyla haftalık eşleştirilmelidir.
