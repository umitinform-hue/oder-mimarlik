# Öder Mimarlık — Kısa Kurulum Rehberi

## 1. Formspree ve KVKK

1. Formspree.io’da işletme hesabı açın ve yeni form oluşturun.
2. Form endpoint’ini kopyalayın; örnek biçim: `https://formspree.io/f/xxxxx`.
3. Repository’de `script.js` içindeki `FORM_ENDPOINT = ""` değerine bu endpoint’i yazın.
4. GitHub’a commit/push edin; form başarıyla 2xx dönerse `oder_generate_lead` olayı tetiklenir.
5. Formspree panelinde bildirim e-postasını, spam korumasını ve veri saklama ayarlarını işletme adına kontrol edin.
6. KVKK checkbox kısa iletişim onayı içindir. Aydınlatma metni, saklama süresi, veri sorumlusu ve açık rıza gerekip gerekmediği işletmenin hukuk danışmanı tarafından kesinleştirilmelidir.

Form endpoint’i yapılandırılmadan site şeffaf `mailto:` yedeğini kullanır ve başarı olmadan `oder_generate_lead` göndermez.

## 2. Punycode domain için 301

GitHub Pages tek bir custom domain’i doğrudan sunar; ikinci alan adı için server-level 301 kuralı GitHub Pages panelinde tek başına oluşturulamaz.

1. Alan adı kayıt kuruluşunda veya Cloudflare DNS’te Punycode domain’i yönetin.
2. `xn--odermimarlk-8zb.com/*` için Redirect Rule oluşturun.
3. Hedefi path korunacak şekilde `https://odermimarlik.com/$1` yapın.
4. Durum kodunu **301 Permanent Redirect** seçin.
5. Şu iki URL’yi test edin:
   - `https://xn--odermimarlk-8zb.com/`
   - `https://xn--odermimarlk-8zb.com/bireysel-ev-dekorasyonu/`
6. Her ikisi de path’i koruyarak `odermimarlik.com` adresine gitmeli; 404 veya `noindex` HTML dönmemeli.

## 3. Search Console sitemap ve URL Inspection

1. Search Console’da `https://odermimarlik.com/` property’sini seçin.
2. Sol menüden **Site haritaları** seçin.
3. `sitemap.xml` yazıp **Gönder** seçin.
4. **URL denetimi** alanına `https://odermimarlik.com/bireysel-ev-dekorasyonu/` yapıştırın.
5. Canlı URL testini çalıştırın.
6. Gerekirse **Dizine eklenmesini iste** seçin.
7. “İstek gönderildi” ile “Google tarafından dizine eklendi” durumlarını ayrı raporlayın.

## 4. GA4 Key Event / dönüşüm işaretleme

1. GA4 → **Yönetici** → **Etkinlikler** bölümünü açın.
2. `oder_generate_lead` olayını bulun; **Önemli etkinlik olarak işaretle** seçeneğini açın.
3. Aynı işlemi `oder_whatsapp_click` için yapın.
4. GA4 **Gerçek zamanlı** raporda test formu ve WhatsApp tıklamasını kontrol edin.
5. Raporlarda `hostname = odermimarlik.com` ve `page_path = /bireysel-ev-dekorasyonu/` filtrelerini kullanın.
6. `manus_test`, `qa` ve benzeri test kampanyalarını gerçek lead olarak raporlamayın.
