# Öder Mimarlık — statik web sitesi

Tek sayfalı, mobil uyumlu site taslağı. HTML, CSS ve sade JavaScript ile çalışır; paket kurulumuna gerek yoktur. GitHub Pages, Netlify veya benzeri statik hosting için uygundur.

## Yayına hazırlık

1. `index.html` içindeki örnek `odermimarlik.com` adreslerini doğrulanmış domain ile güncelleyin: canonical, Open Graph görseli, JSON-LD `url`, robots ve sitemap.
2. `script.js` başındaki `CONTACT_EMAIL` değerine gerçekten kullanılan ve doğrulanmış iletişim e-postasını yazın. Form, kullanıcının e-posta uygulamasında gönderime hazır taslak açar; kendi başına veri toplamaz.
3. `pricing-config.js`, kullanıcı tarafından sağlanan altı kategori €/m² taban fiyatını, üç kalite çarpanını ve 40 ülke/bölge katsayısını içerir. `script.js` içindeki `window.calculateProjectEstimate(areaM2, category, quality, countryCode)` fonksiyonu temel tutarı ve ±%15 fiyat aralığını hesaplar. `extreme` kategorisinde alan 100 m² üstündeyse %10 danışmanlık payı uygulanır. Bu değerler ön tahmindir; kesin teklif değildir.
4. `assets/portfolio/` içindeki Serkan saha arşivinden 65 benzersiz fotoğraf içerir. Küçük görsele tıklanınca yüksek çözünürlüklü orijinal açılır. `assets/videos/` içinde 7 benzersiz MP4 video doğrudan oynatılır. Mustafa klasöründen 6 logosuz kırpılmış görsel ayrı bir 3D tasarım konsepti alanında sunulur. Fotoğraf ve videoları yayına almadan önce yayın hakkını ve proje atıflarını doğrulayın.
5. Fotoğraf tasarım laboratuvarı, seçilen resmi tarayıcıda tutar ve seçilen stil/renk paletiyle indirilebilir bir konsept panosu hazırlar. Bu özellik üretken yapay zekâ ile fotoğrafı yeniden çizmez ve yüklemeyi sunucuya göndermez. Gerçek fotoğraf üstü AI tasarımı için güvenli bir sunucu tarafı görsel API entegrasyonu gerekir.
6. Dil menüsünde 40'tan fazla dil seçeneği bulunur. Seçim Google Translate Websites ekranını açıp URL'yi panoya kopyalar; ziyaretçi çeviriyi ayrıca başlatır. Otomatik ülke algılama ve tüm içeriklerin her dilde otomatik çevrilmesi uygulanmış değildir. Bunun için IP/ülke servisi ve çeviri katmanı veya insan kontrolünden geçmiş dil sayfaları gerekir. Menüdeki dış çeviri SEO için indekslenebilir yerel sayfalar oluşturmaz. Google Translate web sitesi widget'ı 1 Ekim 2026 itibarıyla desteklenmediği için kullanılmadı ([Google duyurusu](https://developers.google.com/search/blog/2020/05/google-translates-website-translator?hl=en)). Kalıcı çok dilli SEO için dil başına URL, insan kontrolünden geçmiş çeviri, hreflang/canonical/sitemap eşleri ve her dilde yapılandırılmış veri ekleyin.
7. SSS AEO için kısa, doğrudan yanıtlar ve FAQ structured data içerir; arama motorlarında zengin sonuç garantisi değildir. Yerel adres, koordinat, yorum ve tamamlanmış proje iddiaları doğrulanmadan eklenmemiştir. Site Türkiye ve Avrupa genelinde hizmeti hedefleyen taslak içeriğe sahiptir; gerçek hizmet kapsamı ve operasyon ülkelerini yayından önce kesinleştirin. Bauhaus ve IKEA metin içinde olası kurumsal teklif hedefleri olarak anılır; iş ortaklığı veya tedarikçi ilişkisi anlamına gelmez.

## GitHub Pages — farklı GitHub kullanıcısı

1. GitHub'da yayınlayacak kullanıcı ile boş bir repository oluşturun; repository adını, erişim izinlerini ve varsa özel domaini kullanıcı kendi hesabında doğrulasın.
2. Bu klasörün içeriğini yeni repository'ye aktarın. Erişimi doğrulamak için hesabın kendi GitHub CLI oturumu veya SSH anahtarı kullanılabilir; token/parola site dosyalarına konmamalıdır.
3. Repository ayarlarında Pages kaynağını `main` branch ve repository kök klasörü (`/`) seçin. Özel domain kullanılacaksa DNS'i sağlayıcı yönergelerine göre kurup HTTPS'i açın.
4. Pages'in verdiği URL'yi açıp telefonda menü, dil seçimi, maliyet formu, SSS ve iletişim akışını kontrol edin. Gerçek e-posta/domain eklendikten sonra canonical, sitemap ve robots değerlerini son kez kontrol edin.

Bu çalışma alanında repository oluşturma/yükleme ve GitHub Pages bağlantısı henüz tamamlanmamıştır. Mevcut düzenleme yerel proje dosyalarında hazırdır. Pages repository URL'si belli olunca canonical, sitemap ve robots alanlarını gerçek adresle güncelleyin.
