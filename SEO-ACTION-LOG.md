# Öder Mimarlık — SEO / AEO / GEO / CRO Uygulama Notu

## Bu sürümde uygulananlar

- İngilizce, Bulgarca, Romence, Sırpça, Arnavutça, Yunanca, Boşnakça, Hırvatça, Makedonca, Slovence ve Karadağca rotalarına JavaScript beklemeden görünen yerel SEO giriş metni ve üç özgün soru-cevap eklendi.
- Her yerel rota için `WebPage` ve yerel `FAQPage` JSON-LD üretildi; `WebSite.inLanguage` ve Open Graph locale değerleri düzeltildi.
- Karşılıklı hreflang seti ülke bölge kodlarıyla güncellendi: `tr-TR`, `bg-BG`, `ro-RO`, `sr-RS`, `sr-ME`, `sq-AL`, `el-GR`, `bs-BA`, `hr-HR`, `mk-MK`, `sl-SI` ve `x-default`.
- Ticari niyetli landing sayfaları eklendi: ölçüye özel mobilya, showroom/mağaza, oturma odası/salon, çocuk odası ve ekstrem özel projeler.
- Yeni landing sayfalarının Service ve BreadcrumbList schema kayıtları, canonical ve OG bilgileri route’a özel hale getirildi.
- Dönüşüm olayları `dataLayer` ve mevcutsa `gtag` ile uyumlu olacak şekilde hazırlandı: `hero_cta_click`, `whatsapp_click`, `phone_click`, `email_click`, `form_start`, `generate_lead` (başarılı Formspree gönderimi), `form_error`, `cta_click`, `calculator_complete`, `calculator_add_to_project`, `language_select`, `country_select`, `project_gallery_open`.
- `prefers-reduced-motion` ve `Save-Data` durumunda autoplay hero video durduruluyor; poster görseli korunuyor.
- Görsel ve içerik blokları için mobil responsive stil eklendi.

## Harici hesap gerektiren kalan işlemler

- Google Search Console domain doğrulaması ve URL Inspection isteği.
- Bing Webmaster Tools doğrulaması ve sitemap gönderimi.
- Google Business Profile, Apple Business Connect, Armut.com ve Sahibinden.com hesaplarında NAP bilgisi/ilan yayınlama.
- ~~Formun `mailto` taslağı yerine gerçek endpointe geçirilmesi~~ — 12 Kasım 2026'da Formspree'ye bağlandı.
- Gerçek Analytics ölçümü için GA4/GTM ölçüm kimliği eklenmesi.

Bu maddeler, hesap girişi, doğrulama veya işletme adına veri işleme onayı gerektirdiği için statik GitHub Pages paketi içinde otomatik olarak uydurulmamıştır.

## 18 Kasım 2026 — Otomasyon turu 1

- Dil sayfalarındaki yanlış "e-posta taslağı" notu ve iç not kaldırıldı; BiH/HR/ME başlıkları ayrıştırıldı.
- `llms.txt`, sitemap `lastmod`, özel `404.html` eklendi.
- 11 hizmet sayfasına telefon CTA'sı, ilgili hizmetler bloğu, çalışma saatli alt bilgi ve olay takibi (`phone_click`, `whatsapp_click`, `email_click`, `cta_click`; `page_type=service`) eklendi.
- İşletme şemasına Instagram `sameAs` ve yazım varyantları eklendi.
- Dil sayfalarında KVKK onayı forma iletilmiyordu; düzeltildi. Ayrıntı: `OTOMASYON-DURUM.md`.

## 18 Kasım 2026 — Otomasyon turu 2 (zamanlanmış)

- 11 hizmet sayfasına sayfaya özgü "Hizmet ayrıntısı", "Teklif için" bölümleri, fayda satırı, +2 SSS ve FAQPage şeması eklendi (294–305 → 464–508 kelime).
- Dil sayfalarında Türkçe dışı tarayıcıda içerik İngilizceye dönüyordu; `script.js` otomatik dil geçişi yalnız `lang="tr"` sayfada çalışacak şekilde sınırlandı.
- Dil sayfalarında menü, hero CTA, 3 H2 ve 6 kart başlığı çevrildi; /me/ `lang` → `sr-ME`; adres tek biçime getirildi (posta kodu 34746). Ayrıntı: `OTOMASYON-DURUM.md`.

## 18 Kasım 2026 — Otomasyon turu 3 (elle başlatılan sınama)

- 68 büyük görsel için WebP kopyası; sayfa, galeri ve poster referansları WebP (orijinaller duruyor).
- Dil sayfalarında yanlış gizlilik notu düzeltildi; form, iletişim metni, 10 H2 ve sabit çubuk çevrildi.
- Hizmet sayfalarına sabit "Ara / WhatsApp" çubuğu eklendi. Ayrıntı: `OTOMASYON-DURUM.md`.

## 18 Kasım 2026 — Tur 4 (proje sohbetinden elle)

- Hizmet sayfalarında ortak KAPSAM ve ilk 3 SSS sayfaya özgü yazıldı; mobilya-dekorasyon sayfasının odağı ayrıştırıldı.
- 11 dil sayfasında kalan Türkçe (statik + betikle üretilen) çevrildi; `i18n/<dil>.js` eklendi; ana ve dil sayfalarında FAQPage görünür SSS ile eşlendi.
- Türkçe ana sayfanın Türkçe olmayan tarayıcıda İngilizceye dönmesi kaldırıldı. Ayrıntı: `OTOMASYON-DURUM.md`.

## 2026-11-19 — Kullanıcı kararları

- Müşteri adı tüm yayın içeriğinden kaldırıldı; video başlığı "Tekstil fuarı standı — ev tekstili ve perde teşhiri" oldu (videos.js, hizmet sayfası, VideoObject, video-sitemap.xml, i18n ×11).
- B2B bölümündeki Bauhaus/IKEA cümlesi 12 sayfadan kaldırıldı.
- İletişim formu: telefon zorunlu, e-posta isteğe bağlı (12 sayfa); e-posta boşsa mailto yedeğinde "Belirtilmedi" yazılıyor.
- GA4 rapor iş akışının pazartesi zamanlaması kapatıldı; workflow_dispatch korunuyor.
