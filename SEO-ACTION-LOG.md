# Öder Mimarlık — SEO / AEO / GEO / CRO Uygulama Notu

## Bu sürümde uygulananlar

- İngilizce, Bulgarca, Romence, Sırpça, Arnavutça, Yunanca, Boşnakça, Hırvatça, Makedonca, Slovence ve Karadağca rotalarına JavaScript beklemeden görünen yerel SEO giriş metni ve üç özgün soru-cevap eklendi.
- Her yerel rota için `WebPage` ve yerel `FAQPage` JSON-LD üretildi; `WebSite.inLanguage` ve Open Graph locale değerleri düzeltildi.
- Karşılıklı hreflang seti ülke bölge kodlarıyla güncellendi: `tr-TR`, `bg-BG`, `ro-RO`, `sr-RS`, `sr-ME`, `sq-AL`, `el-GR`, `bs-BA`, `hr-HR`, `mk-MK`, `sl-SI` ve `x-default`.
- Ticari niyetli landing sayfaları eklendi: ölçüye özel mobilya, showroom/mağaza, oturma odası/salon, çocuk odası ve ekstrem özel projeler.
- Yeni landing sayfalarının Service ve BreadcrumbList schema kayıtları, canonical ve OG bilgileri route’a özel hale getirildi.
- Dönüşüm olayları `dataLayer` ve mevcutsa `gtag` ile uyumlu olacak şekilde hazırlandı: `hero_cta_click`, `whatsapp_click`, `phone_click`, `email_click`, `form_start`, `form_submit`, `calculator_complete`, `calculator_add_to_project`, `language_select`, `country_select`, `project_gallery_open`.
- `prefers-reduced-motion` ve `Save-Data` durumunda autoplay hero video durduruluyor; poster görseli korunuyor.
- Görsel ve içerik blokları için mobil responsive stil eklendi.

## Harici hesap gerektiren kalan işlemler

- Google Search Console domain doğrulaması ve URL Inspection isteği.
- Bing Webmaster Tools doğrulaması ve sitemap gönderimi.
- Google Business Profile, Apple Business Connect, Armut.com ve Sahibinden.com hesaplarında NAP bilgisi/ilan yayınlama.
- Formun `mailto` taslağı yerine gerçek CRM/webhook endpointine geçirilmesi; bunun için bir form/CRM sağlayıcı hesabı ve KVKK saklama/onay metninin işletme tarafından kesinleştirilmesi gerekir.
- Gerçek Analytics ölçümü için GA4/GTM ölçüm kimliği eklenmesi.

Bu maddeler, hesap girişi, doğrulama veya işletme adına veri işleme onayı gerektirdiği için statik GitHub Pages paketi içinde otomatik olarak uydurulmamıştır.
