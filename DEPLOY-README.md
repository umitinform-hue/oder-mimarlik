# Öder Mimarlık — GitHub Pages launch package

Bu paket `umitinform-hue/oder-mimarlik` canlı kaynağı üzerinden hazırlanmıştır. `CNAME` dosyası korunmuştur: `xn--odermimarlk-8zb.com`.

## İçerik

- Premium hero ve gerçek saha görselleriyle görsel sistem
- Harici Unsplash görsellerinin gerçek proje görselleriyle değiştirilmesi
- Telefon ve WhatsApp hızlı iletişim CTA’ları
- Premium sabit dönüşüm barı
- Twitter/X kart metadata’sı ve favicon
- `ProfessionalService`, `Organization`, `WebSite`, `FAQPage` ve yerel hizmet bilgileri için JSON-LD
- İngilizce, Bulgarca, Romence, Sırpça ve Arnavutça indekslenebilir landing page’leri: `/en/`, `/bg/`, `/ro/`, `/sr/`, `/sq/`
- Dil sayfaları arasında `hreflang` ve `x-default` bağlantıları
- Bölgesel hedefleme: Türkiye, Bulgaristan, Yunanistan, Sırbistan, Kuzey Makedonya, Arnavutluk, Kosova, Bosna-Hersek, Karadağ ve Romanya
- Form gönderimi mevcut e-posta taslağı akışını korur; WhatsApp hızlı kanal olarak eklenmiştir.

## Yayın

GitHub Pages kaynağı `main` branch ve root `/` olarak kalmalıdır. CNAME dosyası silinmemelidir. Özel domain HTTPS ayarı GitHub Pages panelinde zorunlu tutulmalıdır.

## Notlar

Windows workspace bağlantısı bu oturumda henüz erişilebilir olmadığından, masaüstündeki ek görseller pakete alınamamıştır. Paket mevcut canlı depodaki gerçek ÖDER saha görselleriyle çalışır; masaüstü görselleri bağlandığında aynı klasör yapısına eklenebilir.

Lead kaybını tamamen önlemek için sonraki adımda statik `mailto:` formu yerine serverless form endpoint’i veya CRM webhook’u bağlanmalıdır. Mevcut paket, kullanıcıyı WhatsApp ve telefonla doğrudan temasa yönlendirir.
