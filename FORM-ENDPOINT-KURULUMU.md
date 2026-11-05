# Form Endpoint Yapılandırması

`script.js` içinde şu sabit bulunur:

```js
const FORM_ENDPOINT = "";
```

Formspree hesabı oluşturulduktan sonra gerçek endpoint buraya yazılmalıdır:

```js
const FORM_ENDPOINT = "https://formspree.io/f/GERCEK_FORM_ID";
```

Endpoint boşken form kullanıcıya açıkça `mailto:` taslağı sunar ve `oder_generate_lead` göndermez. Endpoint 2xx başarı yanıtı verdiğinde form başarı mesajı gösterilir ve yalnızca o anda `oder_generate_lead` tetiklenir. Formspree ID bilinmeden sahte endpoint yazılmamıştır.
