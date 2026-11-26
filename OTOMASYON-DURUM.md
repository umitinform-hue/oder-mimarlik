# Öder Mimarlık — Otomasyon Durumu (SEO / AIO / CRO)

Son doğrulama tarihi: 26 Kasım 2026 (tur 6, zamanlanmış görev)
Kaynak depo: umitinform-hue/oder-mimarlik (yayın: GitHub Pages, `main`)

## Durum

| Alan | 16 Kas | 18 Kas | 18 Kas (tur 2) | Not |
|---|---|---|---|---|
| SEO teknik | İyi | İyi | İyi | Dil sayfalarının İngilizceye dönmesi düzeltildi; lang sr-ME; NAP tek biçim |
| SEO içerik-otorite | Zayıf | Zayıf | Orta− | Hizmet sayfaları 294–305 → 464–508 kelime; dış profil/yorum yok |
| AIO | Orta | Orta+ | Orta+ | 11 FAQPage; adreste posta kodu; GBP/yorum yok |
| CRO | Orta | Orta+ | Orta+ | Hizmet sayfalarında fayda satırı ve ikinci CTA; mobil sabit CTA yok |

Tur 3 (18 Kas 19:22): SEO teknik İyi; içerik Orta−; AIO Orta+; CRO İyi− (hizmet sayfalarında sabit CTA, dil sayfası formu kendi dilinde).

Tur 4 (18 Kas 23:30): SEO teknik İyi; içerik Orta (hizmet sayfaları ayrıştı, 11 dil sayfası çevrildi); AIO İyi− (tüm FAQPage = görünür SSS); CRO İyi−. Açık KRİTİK: 0.

Tur 5 (19 Kas, zamanlanmış): SEO teknik İyi; içerik Orta; AIO İyi− → İyi− (bireysel ev sayfası FAQPage eşlendi); CRO İyi−. Açık KRİTİK: 0. Regresyon: 0. PR #5 (kullanıcı kararları; script.js, i18n, 12 ana/dil sayfası, iş akışı) açık; bu tur o dosyalara dokunmadı.

Tur 6 (26 Kas, zamanlanmış): SEO teknik İyi; içerik Orta; AIO İyi− → İyi (dil sayfalarında tek FAQPage); CRO İyi−. Açık KRİTİK: 0. Regresyon: 0 (24 URL, canonical/sitemap/H1/JSON-LD/NAP/FAQ eşleşmesi). Açık otomasyon/ PR'ı #8 (sadeleştirme, kullanıcı tasarım kararı) olduğu için yeni PR açılmadı; düzeltmeler #8 dalına eklendi. #8 başka oturumun commit'lerini içerdiği ve TASARIM KURALI kullanıcı değerlendirmesi istediği için otomasyon birleştirmedi.

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

| — | Hizmet sayfalarında ortak KAPSAM bölümü ve ilk 3 SSS | 18 Kas tur 4, `otomasyon/seo-aio-cro-2026-11-18d` | KAPSAM 1 ortak → 11 benzersiz; ilk 3 SSS 11 aynı → 33 benzersiz soru; FAQPage görünürden yeniden üretildi |
| — | "Ölçüye özel mobilya" ↔ "mobilya ve dekorasyon" anahtar kelime çakışması | aynı | /hizmetler/mobilya-dekorasyon/ title/H1/description/keywords/şema "Mobilya ve Dekorasyon Tasarımı"; eski ad 9 geçiş → 0 |
| 1 | Dil sayfalarında kalan Türkçe (statik) | aynı | sayfa başına 259–260 parça → 0 (11 dil); ülke adları ICU; korunanlar: logo, dil adları, adres, marka, B2B cümlesi |
| — | Dil sayfalarında betiğin ürettiği Türkçe (ilham kartları, videolar, hesaplayıcı notu, form mesajları, menü) | aynı | açılışta görünen Türkçe satır 27 → 0 (Playwright bg/el/me/en); yeni `i18n/<dil>.js` |
| — | Dil sayfalarında FAQPage Türkçe 3 soru, görünürde 6 | aynı | 11 sayfa → görünür 6 SSS ile birebir, inLanguage sayfa dili |
| — | Ana sayfa FAQPage 3 soru, görünürde 6 farklı | aynı | görünür 6 SSS ile birebir |
| — | **Türkçe ana sayfa Türkçe olmayan tarayıcıda (Googlebot dahil) İngilizceye dönüyordu** | aynı | en-US/de-DE'de lang=en → lang=tr (Playwright); menüden seçim çalışıyor |
| — | Video `uploadDate` saat dilimi (Search Console 26 Eki uyarısı) | doğrulandı, değişiklik gerekmedi | 18 blok `+03:00` ile |
| — | /bireysel-ev-dekorasyonu/ FAQPage görünür SSS ile uyuşmuyordu; ince içerik; hizmet sayfalarına iç link yok; adres kısaltılmış | 19 Kas tur 5, `otomasyon/seo-aio-cro-2026-11-19` | FAQPage = görünür 2/4 → 5/5; kelime (BS4, main) 373 → 468; hizmet iç linki 0 → 6; fayda satırı 0 → 1; tam adres 0 → 1 |
| — | BEKLEYEN 1: saha fotoğraf galerisi altyazı/alt/aria metinleri dil sayfalarında Türkçe | 26 Kas tur 6, PR #8 dalı (`otomasyon/sade-ana-sayfa-2026-11-26`) | Playwright (en-US): Türkçe altyazı 65 → 0, alt 65 → 0, aria 65 → 0 (11 dil); 101 anahtar × 11 `i18n/<dil>.js`; Türkçe sayfa değişmedi |
| — | 11 dil sayfasında iki FAQPage bloğu (`data-source="localized-faq"`) | aynı | blok 22 → 11; sorular görünür SSS'de 7–8/7–8 |
| — | /bs/ ve /me/ aynı meta description | aynı | aynı açıklama 2 → 0 |
| — | BEKLEYEN 5 (hizmet sayfası video etiketleri) | 19 Kas tur 5, kare çıkarımıyla kontrol | 3 videodan 6 kare: ışıklı ahşap raf/niş/gardırop; etiketler videos.js kataloğuyla uyumlu; videonun sayfa konusuyla ilgisi içerik kararı, değişiklik yapılmadı |

## BALKAN GÖRÜNÜRLÜK PLANI (27.11.2026, Ümit'in talebi: "sitenin ilgili dilleri olan Balkan ülkelerinde görünmesini sağlayacak sistem")

Kurulan altyapı (otomasyon/balkan-gorunurluk-2026-11-27):
- 11 ülke/dil hizmet sayfası: /en/interior-design-furniture/, /bg/interioren-dizain-mebeli/, /ro/design-interior-mobilier/, /sr/enterijer-namestaj/, /sq/dizajn-interieri-mobilje/, /el/esoteriki-diakosmisi-epipla/, /bs/enterijer-namjestaj/, /hr/dizajn-interijera-namjestaj/, /mk/enterier-mebel/, /sl/notranje-oblikovanje-pohistvo/, /me/enterijer-namjestaj/ — yerel dilde H1/title/description ülke adıyla; Service (areaServed ülke) + FAQPage + BreadcrumbList; aralarında karşılıklı hreflang + x-default (en).
- 11 dil ana sayfasında title/description anahtar kelime + ülke; hizmetler bölümünden ülke sayfasına bağlantı.
- Şemada areaServed: Türkçe düz metin → İngilizce Country nesneleri (14 ülke).
- sitemap.xml: dil ana sayfaları ve ülke sayfaları için xhtml:link hreflang alternatifleri.
- llms.txt: ülke sayfaları listesi.
- İçerik kaynakları: yalnız sitede zaten olan iddialar (Türkiye ve Avrupa talepleri değerlendirilir; çalışma biçimi ilk görüşmede netleşir). Ülkede ofis, ekip, montaj garantisi, süre, fiyat YAZILMAZ.

Haftalık Balkan modülü (zamanlanmış görev her turda uygular):
1. Regresyon: 11 ülke sayfası + 11 dil ana sayfası — hreflang karşılıklılığı, canonical, title/description dilinde ve ülke adı içeriyor, sitemap alternatifleri, ülke sayfası bağlantısı ana sayfada.
2. Haftanın dili (sıra: bg → el → ro → sr → hr → sl → sq → mk → bs → me → en, sonra başa dön): o dile bir rehber/blog yazısının çevirisini ekle (/<dil>/<yerel-slug>/; Türkçe asıl yazıyla karşılıklı hreflang; Article + FAQPage; ülke sayfasından ve dil ana sayfasından iç link; sitemap + llms.txt). Çeviri asıl metne sadık; yeni iddia yok.
3. Görünürlük gözlemi: WebSearch ile haftanın dilinde 2 sorgu (ör. "интериорен дизайн мебели по поръчка", "εσωτερική αρχιτεκτονική έπιπλα κατά παραγγελία"); odermimarlik.com çıktı mı not et (arama aracının ABD tabanlı olduğunu belirt).
4. Kullanıcıdan gereken (raporda): Search Console'da odermimarlik.com mülkü + sitemap gönderimi; Bing Webmaster Tools (IndexNow anahtarı mevcut); ülkelerde gerçek iş ortağı/proje/yorum varsa bilgi.

Sıradaki yayın: 1. hafta bg.

## TASARIM KURALI (26.11.2026, kullanıcı kararı)

Gerekirse site tasarımı komple değiştirilebilir; ancak Google görünürlüğü korunacak:
- Sayfa adresleri (URL) değişmez; değişmesi zorunluysa 301 yönlendirmesi olmadan yayına alınmaz.
- Görünür metin, H1/H2 başlıkları, SSS ve hizmet metinleri silinmez (yalnız iyileştirilir).
- title, meta description, canonical, hreflang, JSON-LD, sitemap, robots.txt, GTM ve Formspree korunur.
- Yeni tasarım daha yavaş olamaz; mobil uyum ve JavaScript'siz okunabilirlik korunur.
- Sıra: PR #7 birleşir → kullanıcı canlıda değerlendirir → gerekirse önce ana sayfa taslağı, kullanıcı onayı, sonra yayın. Her adımda test.py + tarayıcı kontrolü.

## BEKLEYEN (öncelik sırasıyla)

1. **ÇÖZÜLDÜ (26.11.2026, PR #8 dalında; birleşme bekliyor) – Saha fotoğraf galerisi çevirisi.** Konsept panosu (fotoğraf laboratuvarı) PR #8 ile kaldırılıyor; birleşmezse panonun ara mesajları yeniden BEKLEYEN olur.
6. **UYARI – Dil sayfalarında VideoObject `description` Türkçe** (ör. /ro/ "Ölçüye özel mutfak, mobilya…"). Bekleme: 1 tur.
2. **ÇÖZÜLDÜ (19.11.2026) – Formlar**: telefon zorunlu, e-posta isteğe bağlı (kullanıcı kararı; ana sayfa + 11 dil).
3. **UYARI – Büyük kaynak logolar** (assets/logo/*-source.png, 1,7–1,9 MB) hiçbir sayfada kullanılmıyor; silme yasak, dokunulmadı.
4. **BİLGİ – `locale-content.js` hiçbir sayfada yüklenmiyor** (ölü dosya). Silme yasak olduğundan dokunulmadı.
5. **BİLGİ – Hizmet sayfası KAPSAM video açıklamaları** (ör. çocuk odası sayfasında "Ahşap sergileme nişleri ve raflar") sayfa konusuyla uyuşmuyor; video dosyası doğrulanmadan değiştirilmedi.

## KULLANICI KARARI BEKLEYEN

- Öder Mimarlık'a ait Google İşletme Profili bağlantısı (varsa) — bilgi bekleniyor.
- Diğer sosyal profiller (Instagram dışında) — bilgi bekleniyor.
- Gerçek müşteri yorumları / adı verilebilir referanslar (onaylı metin olarak) — bilgi bekleniyor.
- Çalışma günleri (şemaya `openingHoursSpecification` için) — bilgi bekleniyor.
- Ofis koordinatı (şemaya `geo` için) — bilgi bekleniyor.
- Google Search Console indeks kontrolü ve sitemap gönderimi — kullanıcı işi.
- odermimarlik.com.tr için sunucu tarafı 301 — kullanıcı işi (alan adı sağlayıcısı/Cloudflare).

## Kullanıcının verdiği bilgiler
- 26.11.2026 (2): Logo, ÖDER GROUP kurumsal logo kılavuzundaki (Temmuz 2026) "ÖDER GROUP · İNŞAAT & MİMARLIK" alt marka logosu olacak; sitede yatay dizilim (amblem + yazı). B2B bölümünde yazılar büyük ve net, 4 tıklanabilir fotoğraf, "ÖDER MOBİLYA" damgası yerine "Kurumsal teklif" rozeti; "Ürün teşhir rafları ve mağaza mobilyası · saha arşivinden örnek" yazısı kalır. Google için rehber ve blog sayfaları (başlangıç: 3 rehber + 3 blog). Bing'de yer alma. Mobil açılış 2,5 sn'den kısa.
- 26.11.2026: Logo yazısı daha kurumsal olmalı; hizmetlerde tüm hizmetler ve daha çekici görseller (TV ekranlı görsel olmasın); menü tıklamasındaki boşluk giderilmeli; saha fotoğrafları bağlantısı büyük ve dikkat çekici olmalı; bireysel ev sayfasında logo eksik; Mobilya Tasarım ve Hizmetler aynı yere gitmemeli. Hepsi uygulandı (otomasyon/gorsel-duzeltmeler-2026-11-26).
- 19.11.2026: Müşteri adı yayında kalmayacak (video, hizmet sayfası, VideoObject, video sitemap ve 11 dil çevirisinden kaldırıldı). Bauhaus/IKEA cümlesi 12 sayfadan kaldırıldı. Formlarda telefon zorunlu, e-posta isteğe bağlı.
- 19.11.2026: Eski GA4 rapor iş akışının haftalık zamanlaması kapatıldı (secret yok, her pazartesi hata veriyordu); elle çalıştırma açık, betik ve belgeler korunuyor. Haftalık SEO raporu Claude zamanlanmış görevinden geliyor.

- 16 Kas 2026: Instagram kullanıcı adı `odermimarlik` → https://www.instagram.com/odermimarlik/ (profil içeriği otomasyon tarafından DOĞRULANAMADI: instagram.com robots kuralı okumayı engelliyor).

## Onaylı metinler

- "Mobilya iyi, mekân bambaşka." (slogan)

## Bilinçli yapılmayanlar

- Öder Group GitHub'ı (odergroup2023-design hesabındaki depolar) bu iş için kullanılmaz — 17 Kas 2026.
- `openingHoursSpecification` gün bilgisi olmadan eklenmez.
- Hizmet sayfalarına ana sayfaya özgü `script.js` yüklenmez (hesaplayıcı/form öğelerini arar, hata verir); sayfa içi küçük takip betiği kullanılır.

## Görünürlük gözlemi (ABD tabanlı arama aracı; sıralama değil)

| Sorgu | 16 Kas | 18 Kas | 18 Kas (tur 2) | 19 Kas | 26 Kas |
|---|---|---|---|---|---|
| Öder Mimarlık | çıkmadı | DOĞRULANAMADI | çıkmadı | çıkmadı | çıkmadı (yabancı mimarlık dizinleri) |
| Oder Mimarlık Ataşehir | — | — | çıkmadı | çıkmadı | çıkmadı (armut.com) |
| odermimarlik.com | çıkmadı | DOĞRULANAMADI | — | — | — |
| ölçüye özel mobilya Ataşehir | çıkmadı | DOĞRULANAMADI | çıkmadı (armut.com ağırlıklı) | çıkmadı (armut.com) | çıkmadı (armut.com) |
| mutfak dolabı tasarımı İstanbul | — | — | çıkmadı (pazar yerleri, armut.com) | çıkmadı (pazar yerleri, armut.com) | çıkmadı (pazar yerleri, armut.com) |
| fuar standı tasarımı İstanbul | — | — | çıkmadı (expoassist.net, stand firmaları) | çıkmadı (expoassist.net) | çıkmadı (expoassist.net, firmasec.com) |
| iç mimarlık firması Ataşehir | — | — | çıkmadı (armut.com ağırlıklı) | çıkmadı (armut.com) | çıkmadı (armut.com) |

## Alınan dersler

- 16 Kas: zamanlanmış tur depoya yazamadı → kök neden: Claude GitHub uygulaması depo sahibinin hesabında kurulu değildi (ortak çalışan daveti tek başına yetmiyor) → kural: erişim hatasında gerçek hata mesajını yaz, tahmin etme.
- 18 Kas: `lang` kodunu değiştirmek `locale-content.js` çevirisini bozacaktı → kural: `lang` değişikliğini çeviri anahtarıyla birlikte yap.
- 18 Kas: ana sayfa KVKK kutusu doğruydu, dil sayfaları değil → kural: ana sayfayı kopya sayfalarla aynı varsayma, her dosyayı say.

- 18 Kas (tur 2): `locale-content.js` hiçbir sayfada yüklenmiyordu; durum dosyası aksini varsayıyordu → kural: bir dosyanın etkisini varsaymadan önce hangi sayfaların yüklediğini say.
- 18 Kas (tur 2): Dil sayfaları main'de Türkçe dışı tarayıcıda İngilizceye dönüyordu; yalnız kaynak okuyarak görülmedi, Playwright `locale: en-US` ile görüldü → kural: dil sayfalarını Türkçe dışı yerel ayarla da render et.

- 18 Kas (tur 3): Tur 1 "e-posta taslağı" notunu 11 → 0 saymıştı ama alt bilgideki farklı cümle ("taslak oluşturmak") kaçmıştı → kural: kaldırılan iddiayı tek ifade ile değil anahtar kelime ailesiyle say (taslak, mailto, e-posta uygulaması).
- 18 Kas (tur 3): WebP'ye geçişte video poster'ı JPG kalınca aynı görsel iki kez indi → kural: görsel değişiminde img, srcset, poster ve CSS background referanslarını birlikte say, Playwright aktarım baytıyla doğrula.

- 18 Kas (tur 4): Ana sayfayla metin karşılaştırması iki CTA'yı kaçırdı (ana sayfada farklı yazılmıştı) → kural: çevrilmemiş metni "11 dil sayfasında birebir aynı kalan metin" ölçütüyle de say.
- 18 Kas (tur 4): Kaynakta 0 Türkçe görünürken betik çalışınca 27 Türkçe satır çıktı → kural: dil sayfalarını Playwright'ta render edip `innerText` ile say.
- 18 Kas (tur 4): Tur 2 dil sayfalarında düzelttiği otomatik İngilizce geçişin aynısı ana sayfada da vardı → kural: bir hata bir sayfa grubunda bulunduysa aynı kodu yükleyen tüm sayfalarda ara.
- 19 Kas (tur 5): FAQPage eşleşmesi yalnız hizmet/ana/dil sayfalarında yapılmıştı; /bireysel-ev-dekorasyonu/ kaçmıştı → kural: şema-görünür eşleşmesini sitemap'teki her URL için say.
- 19 Kas (tur 5): Açık PR #5 script.js, i18n ve 12 ana/dil sayfasını değiştiriyordu; aynı dosyalara dokunmak çakışma yaratacaktı → kural: açık PR'ın dosyalarını tur başında çıkar, durum dosyasında o PR'ın satırlarına bitişik satır değiştirme.

- 26 Kas (tur 6): WebFetch ilk okumada /en/ için 18 Kas'ta kaldırılmış "e-posta taslağı" notunu gösterdi; sorgu parametresiyle yeniden okununca güncel sürüm geldi → kural: canlıda regresyon görünürse kaynakla karşılaştır ve önbelleği aşan parametreyle yeniden oku; tek okumaya göre KRİTİK yazma.
- 26 Kas (tur 6): Tur 5'teki FAQ görünürlük sayımı BeautifulSoup `get_text` ile script içeriğini de sayıyordu → kural: görünür metni ölçmeden önce script/style/noscript etiketlerini çıkar.

## Sonraki turun önceliği

0. Rehber/blog: her tur en fazla 1 yeni yazı önerisi (yalnız genel bilgi; rakam/iddia yok). Bing Webmaster Tools doğrulaması kullanıcı işi; IndexNow anahtar dosyası kökte.

1. PR #8 durumu: birleştiyse canlıda galeri çevirisi, tek FAQPage ve /bs/-/me/ açıklamalarını say; birleşmediyse dalı main ile güncelle.
2. Dil sayfalarında VideoObject açıklamalarının çevirisi (BEKLEYEN 6).
3. Regresyon sayımı ve görünürlük gözlemi.
