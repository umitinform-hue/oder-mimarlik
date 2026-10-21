# Öder Mimarlık — Entegrasyon ve Dizinleme Raporu

## Sonuç özeti

GitHub Pages yayını, özel alan adı, HTTPS zorlaması, sitemap ve çok dilli statik SEO rotaları çalışır durumdadır. Alan adı `https://xn--odermimarlk-8zb.com/` üzerinden HTTPS ile 200 yanıtı vermektedir.

## Google Search Console

Google hesabında Search Console açıldı ve mülk ekleme ekranına ulaşıldı. Ancak alan adı formu tarayıcı devrinde doldurulmadan kaldı; Google mülk ekleme işlemini tamamlamadı. Alan adı mülkü DNS TXT doğrulaması istediği için, mülk oluşturulmadan sitemap gönderimi yapılamaz.

Gönderilecek sitemap adresleri hazırdır:

- `https://xn--odermimarlk-8zb.com/sitemap.xml`
- `https://xn--odermimarlk-8zb.com/video-sitemap.xml`

## Bing Webmaster Tools

Bing Webmaster açıldı. Microsoft hesabı oturumu bulunmadığı için Google ile giriş denendi; Google OAuth akışı `oauth_failure` ile Bing’e geri döndü. Bing panelinde mülk ekleme ve sitemap gönderimi bu nedenle tamamlanamadı.

## GA4 / GTM

Google Analytics hesabında `www.odergroup.com.tr` ile ilişkili mevcut bir GA4 mülkü bulundu ve veri topladığı görüldü. Bu mülkün ölçüm kimliği Öder Mimarlık alan adına ait olarak doğrulanamadığı için başka bir markanın ölçüm kimliği siteye eklenmedi.

Öder Mimarlık sitesindeki dönüşüm altyapısı hazırdır. `dataLayer` olayları ve varsa `gtag` çağrıları şu olayları üretir: `oder_form_start`, `oder_form_submit`, `oder_hero_cta_click`, `oder_whatsapp_click`, `oder_phone_click`, `oder_email_click`, `oder_calculator_complete`, `oder_calculator_add_to_project`, `oder_language_select`, `oder_country_select` ve `oder_project_gallery_open`.

Gerçek GA4/GTM ölçümünün aktif olması için Öder Mimarlık’e ait GA4 Measurement ID (`G-...`) veya GTM Container ID (`GTM-...`) gerekir. Bu kimlik olmadan script eklemek ölçüm üretmez ve yanlış markanın verisini kirletir.

## Form endpointi

Form şu anda güvenli bir `mailto:` taslağı oluşturur ve bilgileri harici bir sunucuya sessizce göndermez. Gerçek webhook/CRM endpointi mevcut değildir. Bir form sağlayıcısı veya CRM seçilmeden endpoint uydurulması; müşteri verilerinin nereye aktarıldığının belirsizleşmesine ve KVKK açısından risk oluşmasına neden olur.

Bu nedenle form gönderimi çalışır biçimde test edildi: zorunlu alan doğrulaması, iletişim olayı ve e-posta taslağı akışı aktiftir. Kalıcı CRM/webhook bağlantısı için seçilecek sağlayıcının endpointi ve KVKK saklama/aydınlatma metni gerekir.

## Uygulanan teknik doğrulamalar

23 HTML rotası, JSON-LD blokları, sitemap XML dosyaları, hizmet landing sayfaları ve HTTPS yayını doğrulandı. GitHub Pages API sonucu `status: built` ve `https_enforced: true` durumundadır.

## Kalan iki gerçek hesap adımı

Google Search Console’da `xn--odermimarlk-8zb.com` mülkünün eklenip DNS doğrulamasının tamamlanması ve Bing Webmaster’da Microsoft/Google hesabıyla giriş yapılması gerekir. Bu iki işlem tamamlanır tamamlanmaz sitemap gönderimi yapılabilir; mevcut statik site kodunda ek değişiklik gerekmemektedir.
