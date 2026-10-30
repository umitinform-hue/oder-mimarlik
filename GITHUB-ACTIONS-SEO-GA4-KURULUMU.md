# GitHub Actions SEO + GA4 Raporlama Kurulumu

Workflow dosyası `.github/workflows/weekly-seo-ga4-report.yml` olarak eklenmiştir. Her pazartesi 09:00 Türkiye saati hedeflenmiştir; GitHub Actions UTC kullandığı için yaz saati dönemlerinde saat karşılığı değişebilir. Manuel `workflow_dispatch` da açıktır.

## Gerekli repository secrets
GitHub repository Settings → Secrets and variables → Actions bölümüne şu iki secret eklenmelidir:
- `GA4_PROPERTY_ID`: Öder Mimarlık GA4 mülk ID’si.
- `GOOGLE_SERVICE_ACCOUNT_JSON`: Google Analytics Data API ve Search Console read-only erişimi olan service-account JSON içeriği.
Service account e-posta adresi GA4 mülkünde Viewer, Search Console property’sinde Full user/Owner seviyesinde yetkilendirilmelidir. JSON anahtarı sohbet içinde paylaşılmamalı, yalnızca GitHub secret alanına eklenmelidir.
## 403 teşhisi
`umitinform-hue` hesabı repository üzerinde admin yetkisine sahip ve Actions etkin durumdadır. Ancak bu oturumdaki GitHub entegrasyon token’ında OAuth scope bulunmuyor; Secrets API isteği `Resource not accessible by integration` ve `X-Accepted-Github-Permissions: secrets=read` yanıtı veriyor. Bu nedenle token ile repository secret yazılamaz. Bu, repository’nin admin yetkisiz olduğu anlamına gelmez; entegrasyonun secret yazma kapsamı yoktur.
Mevcut aktif çözüm Manus ScheduleTask + Google tarayıcı bağlantısıdır. GitHub Actions kanalını gerçekten çalıştırmak için repository sahibinin GitHub web arayüzünden bu iki secret’ı eklemesi veya secret yönetimi yetkili bir GitHub OAuth/PAT bağlantısının etkinleştirilmesi gerekir. Gerçek Google service-account JSON’u olmadan sahte credential üretilemez.

## Rapor çıktısı

Her çalışmada `reports/weekly-seo-ga4-report.md` üretilir ve GitHub Actions artifact’i olarak saklanır. Landing page, son 7 günlük GA4 sayfa/kaynak/olay verileri ve son 28 günlük Search Console sorguları ayrı bölümlerde yer alır.

## Güvenlik ve sınır

Secret değerleri bu commit’e yazılmamıştır. Secret’lar eklenmeden workflow güvenli şekilde bekler; sahte veri veya sahte credential üretilmez. Ayrıca GitHub Actions raporu mevcut siteyi değiştirmez.
