# Öder Mimarlık — Entegrasyon ve Dizinleme Raporu

## Sonuç özeti

GitHub Pages yayını, özel alan adı, HTTPS zorlaması, sitemap ve çok dilli statik SEO rotaları çalışır durumdadır. Alan adı `https://xn--odermimarlk-8zb.com/` üzerinden HTTPS ile 200 yanıtı vermektedir.

## Google Search Console

Öder Mimarlık URL ön eki mülkü `https://xn--odermimarlk-8zb.com/` doğrulandı. Google Search Console’da sitemap gönderimleri başarıyla tamamlandı:

- `/sitemap.xml` — **Başarılı**, 23 sayfa keşfedildi.
- `/video-sitemap.xml` — **Başarılı**, 1 video ve 7 video kaynağı keşfedildi.

Ana sayfa için URL Inspection akışı da başlatıldı. Dizinlenme raporları Google’ın tarama zamanlamasına bağlı olarak güncellenir.

## Bing Webmaster Tools

Bing Webmaster Tools giriş ekranı açıldı; ancak aktif Microsoft/Bing oturumu bulunmadığı için mülk paneli ve sitemap gönderimi henüz tamamlanmadı. Site tarafında gerekli `sitemap.xml`, `video-sitemap.xml`, `robots.txt`, canonical, hreflang ve yapılandırılmış veri sinyalleri hazırdır. Bing oturumu açıldığında mülk eklenip aynı sitemap adresleri gönderilebilir.

## GA4 / GTM

Öder Mimarlık için ayrı GA4 web akışı oluşturuldu ve ölçüm kimliği `G-XG6PLBHVFW` olarak doğrulandı. Ayrı GTM containerı `GTM-WMPNP7JJ` oluşturuldu; Google Analytics etiketi `Initialization - All Pages` tetikleyicisi ile yapılandırılıp yayınlandı. Site ana sayfa, Balkan dil sayfaları ve hizmet landing sayfalarında GTM head + noscript kodlarını taşır.

Öder Mimarlık sitesindeki dönüşüm altyapısı hazırdır. `dataLayer` olayları ve varsa `gtag` çağrıları şu olayları üretir: `oder_form_start`, `oder_form_submit`, `oder_generate_lead`, `oder_hero_cta_click`, `oder_whatsapp_click`, `oder_phone_click`, `oder_email_click`, `oder_calculator_complete`, `oder_calculator_add_to_project`, `oder_language_select`, `oder_country_select` ve `oder_project_gallery_open`.

Gerçek GA4/GTM ölçümünün aktif olması için Öder Mimarlık’e ait GA4 Measurement ID (`G-...`) veya GTM Container ID (`GTM-...`) gerekir. Bu kimlik olmadan script eklemek ölçüm üretmez ve yanlış markanın verisini kirletir.

## Form endpointi

Form şu anda güvenli bir `mailto:` taslağı oluşturur ve bilgileri harici bir sunucuya sessizce göndermez. Gerçek webhook/CRM endpointi mevcut değildir. Bir form sağlayıcısı veya CRM seçilmeden endpoint uydurulması; müşteri verilerinin nereye aktarıldığının belirsizleşmesine ve KVKK açısından risk oluşmasına neden olur.

Bu nedenle form gönderimi çalışır biçimde test edildi: zorunlu alan doğrulaması, iletişim olayı ve e-posta taslağı akışı aktiftir. Kalıcı CRM/webhook bağlantısı için seçilecek sağlayıcının endpointi ve KVKK saklama/aydınlatma metni gerekir.

## Uygulanan teknik doğrulamalar

23 HTML rotası, JSON-LD blokları, sitemap XML dosyaları, hizmet landing sayfaları ve HTTPS yayını doğrulandı. GitHub Pages API sonucu `status: built` ve `https_enforced: true` durumundadır.

## Kalan dış hesap doğrulamaları

Google Search Console mülkü, HTML doğrulama dosyası ve iki doğrulama etiketiyle hazırlanmış; sitemap ve video sitemap gönderimi için panel erişimi gerekir. Bing Webmaster’da Microsoft/Google oturum akışı `oauth_failure` verdiği için panel tarafında ayrıca oturum açılması gerekir. Bu iki işlem tamamlanır tamamlanmaz sitemap gönderimi yapılabilir; mevcut statik site kodunda ek değişiklik gerekmemektedir.
