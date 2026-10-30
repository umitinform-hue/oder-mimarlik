# Öder Mimarlık — İlk Gerçek Haftalık Rapor Simülasyonu

**Snapshot tarihi:** 30 Ekim 2026
**Amaç:** Aktif ScheduleTask’ın ilk çalıştıracağı raporun, mevcut canlı Google ekranlarından alınabilen verilerle simüle edilmesi.

> Bu rapor gerçek panel ekranındaki mevcut değerleri içerir; ancak ScheduleTask’ın otomatik ilk çalışması değildir. Landing URL’ye özel bazı metrikler mevcut GA4 ana sayfa kartından ayrılamadığı için açıkça “eksik” olarak işaretlenmiştir.

## 1. Executive summary

Öder Mimarlık ölçüm akışı çalışıyor: GA4 ana sayfa kartında son 7 gün için 23 etkin kullanıcı, 180 etkinlik ve 25 görüntüleme görünüyor. Gerçek zamanlı kartta Türkiye’den 1 etkin kullanıcı var. Trafikte Organic Search 16 oturumla en büyük kanal; Direct 12 oturum, AI Assistant 1 oturum ve Organic Social 2 oturumla geliyor. Search Console genel bakışında toplam web arama tıklaması 0; dizine eklenen 1 sayfa, dizine eklenmeyen 0 sayfa görünüyor. Bu hacim henüz müşteri potansiyeli için düşük, ancak Google ve AI Assistant kaynaklarının görünmeye başlaması olumlu sinyal.

## 2. Search Console canlı snapshot

| Metrik | Görülen değer |
|---|---:|
| Toplam web arama tıklaması | 0 |
| Dizi̇ne eklenen sayfa | 1 |
| Dizine eklenmeyen sayfa | 0 |
| Dizi̇ne eklenmeyen video sayfası | 3 |
| Dizine eklenen video sayfası | 0 |
| Core Web Vitals | Veri yok |
| HTTPS URL | 4 |
| HTTPS olmayan URL | 0 |

Search Console panelinde landing URL’si için ayrıntılı sorgu/CTR/konum tablosu bu snapshot sırasında ayrıca açılmadı. Bu nedenle sorgu, gösterim, CTR ve ortalama konum değerleri uydurulmamıştır. “İndeksleme isteği gönderildi” ile “dizine eklendi” ayrımı sonraki URL Inspection raporunda ayrıca tutulmalıdır.

## 3. GA4 canlı snapshot — mülk toplamı

GA4 ana sayfa kartında seçili aralık **Son 7 gün** olarak görünüyor:

| Metrik | Değer | Önceki döneme göre |
|---|---:|---:|
| Etkin kullanıcı | 23 | +%35,3 |
| Etkinlik sayısı | 180 | -%10,4 |
| Önemli faaliyetler | 0 | — |
| Görüntüleme sayısı | 25 | -%3,8 |
| Gerçek zamanlı etkin kullanıcı | 1 | Türkiye |

Bu kart, `www.odergroup.com.tr` mülkünün toplam görünümüdür; hostname filtresi uygulanmadığı için doğrudan yalnızca Öder Mimarlık landing page’i olarak yorumlanmamalıdır.

### Trafik kanalları

| Varsayılan kanal | Oturum |
|---|---:|
| Organic Search | 16 |
| Direct | 12 |
| AI Assistant | 1 |
| Organic Social | 2 |
| Referral | 0 |

### Kaynak / aracı

| Kaynak / aracı | Oturum veya etkin kullanıcı görünümü |
|---|---:|
| google / organic | 7 etkin kullanıcı; 16 oturum |
| (direct) / (none) | 12 etkin kullanıcı; 12 oturum |
| chatgpt.com / ai-assistant | 1 |
| linkedin / organic | 1 |
| ig / social | 1 |
| linkedin.com / referral | 1 |
| facebook.com / referral | 0 |

### Sayfa görünümü

GA4 ana sayfa kartında `Öder Mimarlık ve Mobilya Tasarım | Türkiye & Avrupa` başlıklı sayfa için 6 görüntüleme görünüyor. Bu, mevcut snapshot’ta görülen Öder Mimarlık sayfa başlığıdır; landing URL’sinin kesin 6 görüntüleme aldığı iddiası değildir. Landing path filtresi ScheduleTask’ın gerçek raporunda ayrıca uygulanmalıdır.

### Ülke ve şehir sinyalleri

Ülke kartında Türkiye 12 etkin kullanıcı, United States 4, China 2, Poland 2, Spain 1 ve Singapore 1 görünmektedir. Şehir kartında Istanbul 7, Ankara 1, Chengdu 2, Corlu 1, Council Bluffs 2, Izmir 1 ve Antalya 1 etkin kullanıcı görünmektedir. Council Bluffs/Chengdu gibi şehirler bot, veri merkezi veya VPN olasılığı nedeniyle lead olarak yorumlanmamalıdır.

## 4. Lead ve CRO durumu

GA4 ana sayfa kartında önemli faaliyet sayısı 0 görünmektedir. Bu snapshot’ta `oder_generate_lead` ve `oder_whatsapp_click` olaylarının sayısı ayrı olay raporundan alınmadı; ScheduleTask’ın gerçek çalışmasında bu olaylar hostname ve landing path filtresiyle raporlanmalıdır.

Landing CTA kodu denetlendi ve düzeltildi. Hero WhatsApp ve floating WhatsApp bağlantıları artık standart `oder_whatsapp_click` olayına; `service`, `city`, `lead_method` ve `source` parametrelerine bağlanıyor. Düzeltme commit’i: `6462f72`.

## 5. AIO / SEO / CRO kalite kapısı durumu

| Kapı | Durum | Kanıt |
|---|---|---|
| AIO ilk ekran mesajı | Uygulandı | `bireysel-ev-dekorasyonu/index.html` hero metni ve CTA |
| FAQ semantiği | Uygulandı | FAQPage JSON-LD ve görünür FAQ bölümü |
| Öder Group ilişkisi | Uygulandı | `parentOrganization` JSON-LD |
| Canonical / OG | Uygulandı | landing head metadata |
| Sitemap | Uygulandı | `sitemap.xml` landing URL’si |
| Mobil WhatsApp CTA | Uygulandı | hero, form ve floating CTA |
| Lead olayları | Uygulandı | landing inline script + GTM/GA4 dataLayer |
| Landing-specific GA4 raporu | Eksik | Saved exploration/hostname+page_path raporu yok |
| Önemli faaliyet dönüşümü | Eksik | GA4 kartında 0 görünüyor; event’ler conversion olarak işaretlenmemiş olabilir |
| Google Business Profile yayını | Hesap işlemi bekliyor | Öder Group yetkili hesabında hizmet/gönderi güncellemesi gerekli |
| GitHub Actions API raporu | Blokajlı | Entegrasyon token’ında Actions Secrets write yetkisi yok |

## 6. Kalan eksikler ve öncelik

1. GA4’te `oder_generate_lead` ve `oder_whatsapp_click` olaylarını Önemli Faaliyet olarak işaretle ve landing path/hostname filtresiyle özel rapor oluştur.
2. Search Console URL Inspection’ta bireysel ev dekorasyonu URL’sinin son durumunu ayrıca al; genel “1 sayfa dizinde” göstergesini landing URL’siyle eşitleme.
3. Öder Group Business Profile içinde Öder Mimarlık hizmetlerini, gerçek proje fotoğraflarını ve landing bağlantısını yayınla.
4. Google Search Console’da landing URL için sorgu, gösterim, CTR ve konum tablosunu ilk rapor döneminden sonra karşılaştır.
5. GitHub Actions yedek raporunu çalıştırmak için GitHub connector’a Actions Secrets write yetkisi veya manuel secret girişi gerekir. Ana haftalık rapor yolu olan Manus ScheduleTask aktiftir.
