# Öder Mimarlık — Otomatik SEO ve GA4 Raporlama Kurgusu

## Hedef

Her pazartesi 09:00’da Öder Mimarlık landing page’i için Türkçe performans özeti üretmek. Rapor Öder Group toplam verisini Öder Mimarlık verisinden ayırmalı ve test/QA trafiğini gerçek müşteri trafiği olarak saymamalıdır.

## Rapor kapsamı

Search Console bölümünde landing URL’sinin canlı test sonucu, indeksleme durumu, sitemap durumu ve mevcutsa son 7/28 günlük tıklama, gösterim, CTR, ortalama konum ve sorgular raporlanır. “İndeksleme isteği gönderildi” ile “dizine eklendi” ayrı durumlar olarak yazılır.

GA4 bölümünde `xn--odermimarlk-8zb.com` hostname’i için son 7/28 günlük aktif kullanıcı, oturum, landing page görüntüleme, şehir, kaynak/medium ve kampanya değerleri raporlanır. `oder_generate_lead`, `oder_whatsapp_click`, `oder_hero_lead` ve `oder_form_validation_error` olayları ayrı gösterilir. `manus_test`, `qa` ve benzeri test kampanyaları gerçek müşteri dönüşümü olarak sayılmaz.

Yerel SEO bölümünde Öder Group Business Profile içindeki Öder Mimarlık hizmet kolunun kategori/hizmet güncellemeleri, Maps’ten landing page’e gelen `oder_mimarlik_gbp` kampanyası ve NAP tutarlılığı takip edilir.

## Hazır zamanlama

- Başlık: Öder Mimarlık haftalık SEO ve GA4 raporu
- Cron: `0 0 9 * * 1`
- Rapor dili: Türkçe
- Çalışma: mevcut Manus görevi bağlamında
- Hedef: kullanıcıya rapor mesajı

## Mevcut blokaj

Manus ScheduleTask oluşturma denemesi, bu statik GitHub Pages projesinin Manus webdev panelinde deploy edilmemiş olması nedeniyle `project not deployed yet` hatası verdi. GitHub Pages yayını canlı olsa da bu, Manus ScheduleTask için yeterli deployment kaydı oluşturmuyor. Bu nedenle henüz aktif bir zamanlama varmış gibi raporlanmamalıdır.

Zamanlama iki yoldan biriyle açılabilir:

1. Site Manus webdev panelinde ayrıca deploy edilir ve yukarıdaki ScheduleTask oluşturulur. Bu, GitHub Pages’in yanına ikinci bir yayın yüzeyi getirir; tercih edilirse ayrıca onaylanmalıdır.
2. Search Console ve GA4 API erişimleriyle GitHub Actions üzerinde cron workflow kurulur. Bunun için OAuth/service-account secret’ları gerekir; mevcut hesap erişimleriyle bu secret’lar otomatik varsayılmamalıdır.

## Beklenen rapor biçimi

1. Kısa özet
2. Search Console indeksleme ve organik arama
3. GA4 trafik ve landing akışı
4. Lead/WhatsApp olayları
5. Google Maps ve yerel SEO
6. Değişim, risk ve sonraki aksiyonlar
