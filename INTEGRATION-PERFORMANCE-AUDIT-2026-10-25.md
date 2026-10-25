# Öder Mimarlık — Entegrasyon ve Mobil Performans Denetimi

**Denetim tarihi:** 25 Ekim 2026  
**Canlı adres:** https://xn--odermimarlk-8zb.com/  
**GitHub Pages deposu:** `umitinform-hue/oder-mimarlik`

## 1. Google Search Console

**Güncel sonuç — 25 Ekim 2026:** Öder Mimarlık, mevcut Öder Group Google hesabı (`umitoder@odergroup.com.tr`) altında Search Console mülkü olarak oluşturuldu ve HTML dosyası yöntemiyle başarıyla doğrulandı. Ana sayfa URL Inspection sonucunda **“URL Google’da mevcut”** durumunda.

Google doğrulama meta etiketi canlı ana sayfada ve dil sayfalarında yayınlandı:

```html
<meta name="google-site-verification" content="ukpuxGaiKbvccd1zeR9RMFis0AcvLymvjkRfpJo_1HY">
```

Canlı HTML yanıtında token görüldü. Buna rağmen 25 Ekim kontrolünde `umitoder@odergroup.com.tr` hesabıyla Search Console mülkü açıldığında Google hâlâ **“Maalesef bu mülke erişiminiz yok”** ve **“Mülkiyetinizi doğrulayın”** mesajını gösteriyor. Görünen mülk URL’si `https://odermimarlık.com/`; bu hesap için doğrulanmış Search Console erişimi oluşmamış.

**URL Inspection:** Ana sayfa başarıyla incelendi ve **Google’da mevcut** olarak görüldü. Bu nedenle ana sayfa için ayrıca “Dizine eklenmesini iste” gönderilmesine gerek kalmadı; Search Console mevcut dizin durumunu doğruladı. Dil ve hizmet sayfaları için ayrı URL Inspection istekleri gerektiğinde aynı doğrulanmış mülk üzerinden yapılabilir.

**Sitemap gönderimi:** İki sitemap de Search Console’a başarıyla gönderildi ve durumları “Başarılı” olarak görüldü. Ana sitemap 23 sayfa, video sitemap 1 sayfa ve 7 video keşfetti. Google’ın kendi yönergelerine göre sitemap gönderimi Search Console’da izlenebilir, ancak sayfalar sitemap olmadan da keşfedilebilir [1].

Sitede dosyalar canlı ve geçerli:

- `https://xn--odermimarlk-8zb.com/sitemap.xml` → HTTP 200, 23 URL
- `https://xn--odermimarlk-8zb.com/video-sitemap.xml` → HTTP 200
- `https://xn--odermimarlk-8zb.com/robots.txt` → HTTP 200; iki sitemap’i bildiriyor

**Tamamlanan adım:** Mülk Öder Group hesabı altında tam canonical URL ön ekiyle doğrulandı; `/sitemap.xml` ve `/video-sitemap.xml` gönderildi. Search Console tablosunda her ikisi de “Başarılı” olarak görünüyor. Google URL Inspection ana sayfa için “Google’da mevcut” sonucunu verdi [1].

## 2. Bing Webmaster Tools

25 Ekim kontrolünde Bing Webmaster Tools oturumu açık değildi; sayfa giriş/başlangıç ekranında kaldı. Bu nedenle:

- Bing mülk doğrulaması doğrulanamadı.
- Bing sitemap gönderimi yapılamadı.
- Bing URL Submission veya IndexNow anahtarı kurulmuş görünmüyor.
- Bing performans ve SEO/GEO raporları alınamadı.

Bing hesabı için canlı sitede gerekli sitemap ve robots altyapısı hazır. Harici hesap oturumu açıldıktan sonra site eklenmeli, doğrulama yapılmalı ve şu iki sitemap gönderilmelidir:

- `https://xn--odermimarlk-8zb.com/sitemap.xml`
- `https://xn--odermimarlk-8zb.com/video-sitemap.xml`

## 3. Diğer harici entegrasyonlar

### Google Analytics / GTM

Canlı kaynakta ölçüm ve olay izleme kodu için yer tutucu/olay isimleri mevcut; ancak siteye ait doğrulanmış bir `G-...` GA4 ölçüm kimliği tespit edilmedi. Açık Google Analytics hesabında görülen mülk `www.odergroup.com.tr` kapsamındaydı; bunun Öder Mimarlık alan adı için veri akışı olduğu doğrulanamadı.

Sonuç: Öder Mimarlık için gerçek trafik, dönüşüm ve reklam ilişkilendirmesi şu anda güvenilir biçimde ölçülüyor kabul edilmemeli. Ayrı bir GA4 web veri akışı oluşturulmalı veya doğru mevcut akışın ölçüm kimliği siteye eklenmelidir.

### Form / CRM

Form akışı gerçek bir CRM veya webhook endpointine bağlı görünmüyor; `mailto:` tabanlı yedek akış kullanılıyor. Bu nedenle form dönüşümleri, lead kaynağı ve otomatik takip ölçümü sınırlı. Gerçek endpoint, KVKK açık rıza metni ve veri saklama politikası kesinleşmeden üçüncü taraf CRM’e veri gönderilmemeli.

### GitHub Pages / HTTPS

Site `umitinform-hue/oder-mimarlik` reposundan yayınlanıyor. Özel alan adı HTTPS zorlaması daha önce etkinleştirildi. Canlı site HTTPS üzerinden HTTP 200 yanıt veriyor.

## 4. Mobil uyumluluk ve performans denetimi

Canlı ana sayfa ham HTML ve varlık istekleriyle incelendi:

- Ana sayfa HTTP 200, yaklaşık 35.3 KB HTML.
- `meta name="viewport"` mevcut.
- Canonical mevcut ve gerçek canlı alan adını kullanıyor.
- 13 dil/alternatif bağlantı mevcut.
- 15 görsel, 1 video bulunuyor.
- 10 görselde `loading="lazy"` kullanılmış.
- Hero video yaklaşık 459 KB MP4; mobil için kabul edilebilir düzeyde ancak poster ve video indirme davranışı ayrıca izlenmeli.
- En büyük tek görsel yaklaşık 429 KB; görsellerin çoğu yaklaşık 178–429 KB aralığında.
- `/does-not-exist/` HTTP 404 dönüyor; soft-404 riski görülmedi.
- Dil rotaları `/en/`, `/bg/`, `/ro/`, `/sr/`, `/sq/`, `/el/`, `/bs/`, `/hr/`, `/mk/`, `/sl/`, `/me/` HTTP 200 dönüyor.

### Güçlü taraflar

Site mobil temel gereksinimlerini karşılıyor: viewport etiketi var, CSS içinde responsive medya sorguları var, görsellerin çoğu lazy-load ediliyor, gerçek içerik ham HTML içinde bulunuyor, canonical/hreflang/sitemap/robots altyapısı mevcut ve 404 rotası doğru durum kodu veriyor.

### Öncelikli iyileştirmeler

1. Hero video için `poster`, `preload="metadata"` ve mobilde düşük veri tercihini destekleyen kontrollü bir görsel fallback kullanılmalı. Video otomatik oynatma deneyimi korunacaksa `muted`, `playsinline` ve `aria-label` davranışı test edilmeli.
2. En büyük görseller WebP/AVIF alternatifleriyle yaklaşık 150–250 KB hedef aralığına indirilmeli; özellikle `serkan-018.jpg` ve logo PNG’si adaydır.
3. Tüm görsellere gerçek boyut (`width`/`height`) veya `aspect-ratio` verilmeli. Bu, CLS riskini azaltır.
4. Mobil ilk ekranda kritik olmayan üçüncü taraf/analytics kodları ertelenmeli. Gerçek GA4 kimliği eklendiğinde `defer` ve olay yükünü tekrar ölçmek gerekir.
5. Google PageSpeed API bu denetimde kota sınırına (`HTTP 429`) takıldı; bu yüzden sayısal Lighthouse skoru raporlanmadı. Gerçek saha değerlendirmesi Search Console Core Web Vitals verisi oluştuğunda yapılmalı. Google, CWV değerlendirmesini gerçek kullanıcı verisiyle ve 75. yüzdelik dilimde LCP, INP ve CLS üzerinden izlemeyi önerir [2].

### Hedefler

- LCP: 2.5 saniye veya daha iyi
- INP: 200 ms veya daha iyi
- CLS: 0.1 veya daha düşük

Bu eşikler Google’ın güncel Web Vitals rehberindeki iyi kullanıcı deneyimi hedefleridir [2].

## Son durum

**Güncel entegrasyon özeti:** Öder Mimarlık mülkü Öder Group Search Console altyapısına bağlandı; ana sitemap (23 sayfa) ve video sitemap (7 video) başarıyla gönderildi; ana URL Google’da mevcut. Bing Webmaster Tools ve Öder Mimarlık’e özel GA4 veri akışı hâlâ bekleyen harici hesap işlemleridir.

Site teknik olarak taranabilir ve mobil uyumluluk temeli iyi durumda. Ancak **Search Console doğrulaması tamamlanmış değil**, dolayısıyla URL Inspection ve sitemap gönderim durumu Google panelinden teyit edilemiyor. **Bing Webmaster Tools doğrulaması ve sitemap gönderimi de tamamlanmış değil.** En kritik ticari ölçüm eksiği, Öder Mimarlık’e ait doğrulanmış GA4 veri akışı ve gerçek CRM/form endpointidir.

## References

[1]: https://developers.google.com/search/docs/monitor-debug/search-console-start "Google Search Console başlangıç ve doğrulama yönergeleri"
[2]: https://web.dev/articles/vitals "Web Vitals ve Core Web Vitals eşikleri"
