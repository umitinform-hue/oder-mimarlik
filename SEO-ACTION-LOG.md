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

## 2026-11-26 — Görsel ve kurumsal görünüm düzeltmeleri (kullanıcı geri bildirimi)

- Logo yazısı: amblem + ince altın ayraç + geniş aralıklı "ÖDER" + tek satır "MİMARLIK VE MOBİLYA TASARIM" (ana sayfa ve 11 dil).
- Bireysel ev dekorasyonu ve 11 hizmet sayfasında yalnız yazı olan logo yerine aynı amblemli logo.
- Hizmetler bölümü: 6 kart → 11 hizmetin tamamı + görüşme kartı; her kart kendi hizmet sayfasına gidiyor. Yeni 4:5 kart görselleri (assets/portfolio/cards/), TV ekranlı görsel ve telefon filigranları çıkarıldı.
- Dil sayfalarında mevcut 6 hizmet kartının görselleri yenilendi (dil sayfalarına ait hizmet sayfası olmadığı için kartlar #iletisim'e gitmeye devam ediyor).
- Menü: "Mobilya Tasarım" artık Hizmetler ile aynı yere değil, mobilya detayları bölümüne gidiyor.
- Menüden bölüme geçişte başlığın üstündeki ~108 px boşluk ~40 px'e indirildi.
- "Tüm saha fotoğraflarını gör" küçük satırdan büyük, görselli, turuncu düğmeli çağrı alanına çevrildi.

## 2026-11-26 (2) — Sadeleştirme ve logo

- "Anında fiyat tahmini" (#maliyet) ve "Fotoğrafınızı yükleyin" (#foto-tasarim) bölümleri ana sayfa ve 11 dil sayfasından kaldırıldı (kullanıcı kararı). Laboratuvar çalışıyordu ama yalnız yüklenen fotoğrafı hazır bir metin ve 3 renkle gösteriyordu; gerçek tasarım üretmediği için kaldırıldı.
- İlgili SSS sorusu görünür SSS'den ve FAQPage şemasından birlikte çıkarıldı (5 soru, eşleşme korunuyor). llms.txt güncellendi.
- Menüde "Tasarım laboratuvarı" yerine "İletişim" (11 dilde çevrili).
- Logo yazısı: önceki stil daha baskın eski bir kurala takıldığı için canlıda değişmemişti; Cormorant Garamond serif, geniş harf aralığı, altın çizgili alt yazı ile yeniden yapıldı.
- script.js: fiyat hesaplayıcı kodu eleman yoksa çalışmayacak şekilde korumaya alındı.

## 2026-11-26 (3) — Haftalık otomasyon turu 6 (PR #8 dalına eklendi)

- Saha fotoğraf galerisi altyazı, alt ve aria metinleri 11 dilde çevrildi (`tx()` + `i18n/<dil>.js`, 101 anahtar); dil sayfalarında Türkçe altyazı 65 → 0.
- 11 dil sayfasında iki FAQPage bloğu tek blokta birleştirildi (22 → 11).
- /bs/ ve /me/ meta description ayrıştırıldı.
- script.js ve i18n sürüm parametreleri yenilendi (önbellek).

## 2026-11-26 (4) — Kurumsal logo, B2B bölümü, rehber/blog, hız (kullanıcı talebi)

- Logo: ÖDER GROUP kılavuzundaki İnşaat & Mimarlık alt marka logosu, yatay WebP (18 KB); 24 sayfada 36 yer. Şemaya `logo` eklendi (24 blok).
- B2B (#kurumsal, 12 sayfa): metin 12 → 18 px, maddeler görselden metne taşındı, 4 tıklanabilir görsel (b2b/kurumsal-1..4.webp, 39–54 KB), dönen "Kurumsal teklif" rozeti (forma gider, `data-b2b-cta`).
- /rehber/ (3) ve /blog/ (3) + iki ana sayfa: Article/BlogPosting, FAQPage, BreadcrumbList, "Kısa cevap" kutusu, içindekiler; sitemap 24 → 32; llms.txt; 11 hizmet sayfasından ve ana sayfa menüsünden iç link.
- Hız: Google Fonts CSS'i render'ı bloklamıyor (13 sayfa), hizmet sayfalarında kullanılmayan font kaldırıldı (11), kullanılmayan video preload kaldırıldı (12), Manrope ailesi kaldırıldı.
- Bing: IndexNow anahtar dosyası köke eklendi.
