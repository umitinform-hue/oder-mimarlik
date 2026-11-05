from pathlib import Path
from PIL import Image
import re

root = Path(__file__).resolve().parents[1]

# 1) Generate responsive WebP/AVIF variants for the primary visual assets.
assets = {
    'assets/portfolio/seo/oder-mutfak-montaj-saha.jpg': 'oder-mutfak-montaj-saha',
    'assets/design-inspiration/mustafa/mustafa-02-clean.jpg': 'mustafa-02-clean',
}
out = root / 'assets' / 'optimized'
out.mkdir(parents=True, exist_ok=True)
for source, stem in assets.items():
    image = Image.open(root / source).convert('RGB')
    for width in (640, 1280, 1920):
        if image.width <= width:
            resized = image.copy()
        else:
            height = round(image.height * width / image.width)
            resized = image.resize((width, height), Image.Resampling.LANCZOS)
        resized.save(out / f'{stem}-{width}.webp', 'WEBP', quality=82, method=6)
        resized.save(out / f'{stem}-{width}.avif', 'AVIF', quality=58)

# Add preload=none to every video element in the deployable HTML.
for p in root.rglob('*.html'):
    if '.git' in p.parts:
        continue
    s = p.read_text()
    s = re.sub(r'<video\b(?![^>]*\bpreload=)', '<video preload="none"', s, flags=re.I)
    s = re.sub(r'preload="metadata"', 'preload="none"', s, flags=re.I)
    p.write_text(s)

# Add AVIF/WebP srcset to the two primary above-the-fold images while retaining JPG fallback.
def picture_markup(src, alt, prefix, stem, eager=''):
    loading = ' fetchpriority="high"' if eager else ' loading="lazy"'
    return (f'<picture class="responsive-picture">'
            f'<source type="image/avif" srcset="{prefix}assets/optimized/{stem}-640.avif 640w, {prefix}assets/optimized/{stem}-1280.avif 1280w, {prefix}assets/optimized/{stem}-1920.avif 1920w" sizes="(max-width: 760px) 100vw, 50vw">'
            f'<source type="image/webp" srcset="{prefix}assets/optimized/{stem}-640.webp 640w, {prefix}assets/optimized/{stem}-1280.webp 1280w, {prefix}assets/optimized/{stem}-1920.webp 1920w" sizes="(max-width: 760px) 100vw, 50vw">'
            f'<img src="{src}" srcset="{prefix}assets/optimized/{stem}-640.webp 640w, {prefix}assets/optimized/{stem}-1280.webp 1280w, {prefix}assets/optimized/{stem}-1920.webp 1920w" sizes="(max-width: 760px) 100vw, 50vw" alt="{alt}"{loading} width="1600" height="1067"></picture>')

p = root / 'index.html'
s = p.read_text()
old = re.search(r'<img alt="Ölçüye özel mutfak dolabı ve iç mimarlık uygulaması"[^>]+>', s)
if old and '<picture class="responsive-picture">' not in old.group(0):
    s = s[:old.start()] + picture_markup('assets/portfolio/seo/oder-mutfak-montaj-saha.jpg', 'Ölçüye özel mutfak dolabı ve iç mimarlık uygulaması', '', 'oder-mutfak-montaj-saha', True) + s[old.end():]
p.write_text(s)

p = root / 'bireysel-ev-dekorasyonu' / 'index.html'
s = p.read_text()
for original, alt, stem in [
    ('../assets/design-inspiration/mustafa/mustafa-02-clean.jpg', 'Özel ölçü mutfak ve yaşam alanı tasarımı', 'mustafa-02-clean'),
    ('../assets/portfolio/seo/oder-mutfak-montaj-saha.jpg', 'Ölçüye özel mutfak dolabı montajı', 'oder-mutfak-montaj-saha'),
]:
    pattern = rf'<img src="{re.escape(original)}" alt="{re.escape(alt)}"[^>]*>'
    match = re.search(pattern, s)
    if match:
        s = s[:match.start()] + picture_markup(original, alt, '../', stem, stem == 'mustafa-02-clean') + s[match.end():]
p.write_text(s)

# 2) KVKK consent checkbox on the main contact form.
p = root / 'index.html'
s = p.read_text()
needle = '<label class="consent"><input required="" type="checkbox"/><span>İletişim talebimin yanıtlanması amacıyla bilgilerimin kullanılmasını kabul ediyorum. <a href="#gizlilik">Gizlilik notu</a></span></label>'
replacement = '<label class="consent"><input required="" name="kvkk_consent" value="accepted" type="checkbox"/><span>İletişim talebimin yanıtlanması için bilgilerimin kullanılmasını kabul ediyorum. <a href="#gizlilik">KVKK/gizlilik notunu</a> okudum.</span></label>'
if needle in s:
    s = s.replace(needle, replacement)
p.write_text(s)

# 3) Replace mailto-first submit with optional Formspree endpoint + safe fallback.
p = root / 'script.js'
s = p.read_text()
s = s.replace('const CONTACT_EMAIL = "info@odergroup.com.tr";', 'const CONTACT_EMAIL = "info@odergroup.com.tr";\n// Set this to the real Formspree endpoint after creating the business form.\nconst FORM_ENDPOINT = "";')
old = re.search(r'const contactForm=document\.querySelector\(\'#contact-form\'\);.*?\n', s)
new = '''const contactForm=document.querySelector('#contact-form');
let formStarted=false;
contactForm.addEventListener('focusin',()=>{if(!formStarted){formStarted=true;track('form_start')}});
contactForm.addEventListener('submit',async event=>{
  event.preventDefault();
  const form=event.currentTarget;
  if(!form.reportValidity()) return;
  const data=new FormData(form);
  const feedback=document.querySelector('.form-feedback');
  const payload={name:data.get('name'),email:data.get('email'),phone:data.get('phone')||'',location:data.get('location'),message:data.get('message'),kvkk_consent:data.get('kvkk_consent')==='accepted'?'accepted':'not_accepted',page_url:location.href};
  const subject=encodeURIComponent(`Web sitesi proje talebi — ${payload.name}`);
  const body=encodeURIComponent(`Ad: ${payload.name}\\nE-posta: ${payload.email}\\nTelefon: ${payload.phone||'Belirtilmedi'}\\nKonum: ${payload.location}\\n\\nProje: ${payload.message}`);
  if(FORM_ENDPOINT){
    const submitButton=form.querySelector('button[type="submit"]');
    submitButton.disabled=true; feedback.textContent='Talebiniz gönderiliyor…';
    try{
      const response=await fetch(FORM_ENDPOINT,{method:'POST',headers:{'Accept':'application/json','Content-Type':'application/json'},body:JSON.stringify(payload)});
      if(!response.ok) throw new Error('form_endpoint_failed');
      track('generate_lead',{lead_method:'formspree',service:'genel_proje_talebi',city:payload.location});
      feedback.textContent='Talebiniz ulaştı. En kısa sürede sizinle iletişime geçeceğiz.'; form.reset();
    }catch(error){
      feedback.textContent='Gönderim şu anda tamamlanamadı. WhatsApp’tan yazabilir veya e-posta taslağını kullanabilirsiniz.';
    }finally{submitButton.disabled=false}
    return;
  }
  // Until a real provider endpoint is configured, preserve a transparent fallback without counting a lead.
  if(!CONTACT_EMAIL){feedback.textContent='Form sağlayıcısı henüz yapılandırılmadı. WhatsApp’tan yazabilirsiniz.';return}
  window.location.href=`mailto:${CONTACT_EMAIL}?subject=${subject}&body=${body}`;
  feedback.textContent='E-posta taslağı oluşturuldu. İletmek için e-posta uygulamanızdan gönderin.';
});
'''
if old:
    s = s[:old.start()] + new + s[old.end():]
p.write_text(s)

print('optimization-application-complete')
