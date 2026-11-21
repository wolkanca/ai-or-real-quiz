# Gerçek mi, Yapay Zekâ mı? — Wolkanca Oyun Laboratuvarı (v1)

Mobil öncelikli, WordPress'te iframe ile gömülebilen bir **görsel tahmin quiz'i**. `wolkanca/redlist-quiz` projesindeki tek sayfa HTML/CSS/JavaScript yaklaşımını örnek alır, fakat mevcut projeyi değiştirmez.

## Özellikler

- Her tur **10 soru**: **5 gerçek fotoğraf + 5 yapay zekâ görseli**.
- V1 soru havuzunda **23 kaynaklı görsel** (11 AI, 12 gerçek).
- Görsellerin cevapları **Wikimedia Commons dosya kayıtlarından** alınmıştır; tahmini otomatik AI algılama sistemi yoktur.
- Her cevaptan sonra açıklama, kaynak bağlantısı, yayınlayan/kredi ve belirtilen lisans gösterilir.
- **Süreli mod** isteğe bağlıdır (görsel yüklendikten sonra 20 saniye).
- Puan/seri, sonuç ekranı, tekrar oynama, `localStorage`'da rekor, Web Share/kopyalama.
- Klavye kısayolları: `1` = Gerçek, `2` = Yapay Zekâ.
- Harici JS/CSS kütüphanesi, API anahtarı veya backend yok. Görseller Wikimedia Commons'tan yüklenir.
- Görsel yüklenemezse puan kaybettirmeden başka görsele geçme imkânı vardır.

## 30 saniyede başlat

**En kolay yol:** `index.html` dosyasını tarayıcıda aç. Oyun ve sorular tek HTML dosyasının içine gömülüdür. Görsellerin yüklenmesi için internet gerekir.

**Yerel sunucu ile:**

```bash
python3 -m http.server 8080
```

Tarayıcıda `http://localhost:8080/` adresine git.

## GitHub Pages ile yayımla (önerilir)

1. GitHub'da örneğin `ai-or-real-quiz` adlı **yeni** bir public repo oluştur.
2. `index.html` dosyasını repo kök dizinine koyup `main` dalına gönder. İstersen README ve `questions.json` da ekle.
3. **Settings → Pages → Build and deployment → Deploy from a branch → main / (root)** seç.
4. Varsayılan olarak URL `https://KULLANICI.github.io/ai-or-real-quiz/` biçiminde olur. Kullandığın repo adı ve kullanıcı adına göre URL değişir.
5. WordPress'e `wordpress-embed.html` içeriğini **Özel HTML** bloğunda ekle; iframe `src` adresini yayımlanan gerçek URL ile değiştir. WordPress güvenlik filtresi `<script>` etiketini kaldırırsa otomatik yükseklik kısmını kaldır; `height="940"` ile iframe yine çalışır.

**Alternatif:** Dosyayı kendi alan adındaki ayrı bir statik HTML dizininde yayımla; örneğin `/oyunlar/ai-or-real/`. WordPress medya kütüphanesi HTML dosyalarını yüklemeyi engelleyebilir; bunun için FTP/SFTP, hosting dosya yöneticisi veya statik site dağıtımı kullan.

## Soru ekleme/değiştirme

- `questions.json`: tüm soruların tek bakım kaynağı.
- `index.template.html`: çalıştırılabilir HTML için şablon.
- `build.py`: `questions.json` içeriğini tek HTML içine gömer ve doğru Wikimedia dosya URL'lerini oluşturur.
- `index.html`: doğrudan dağıtılacak oluşturulmuş dosya.

Değişiklik sonrası:

```bash
python3 build.py
```

Örnek kayıt:

```json
{
  "id": "real-yeni-fotograf",
  "type": "real",
  "file": "Commons_Dosya_Adi.jpg",
  "title": "Yeni manzara",
  "explanation": "Fotoğrafın kanıtlanmış kaynağı.",
  "credit": "Fotoğrafçı adı",
  "license": "CC0 1.0",
  "source": "https://commons.wikimedia.org/wiki/File:Commons_Dosya_Adi.jpg"
}
```

`type` sadece `real` veya `ai` olabilir. Kullanılan görsel, Commons dosya adına göre yüklenir. Diğer sitelerden görsel kullanmak istersen dosyanın lisansını ve gerçekliğini doğrula, sonra barındırma kodunu uyarlayabilirsin.

## Lisans ve kaynak notu

Kendi HTML/CSS/JS oyun kodun ile görsel lisansları **ayrı konulardır**. Bu pakette görsellerin kendisi kopyalanmamıştır; kaynak sitelerdeki görsellere internet üzerinden bağlantı kurulur. Her kayıt için dosyanın Wikimedia Commons kaynak sayfası verilmiştir. Kullanım koşulları zamanla değişebilir. Üretken AI görsellerinin telif değerlendirmesi ülkeye göre değişebilir; yayın öncesinde dosya sayfalarını ve kullanım izinlerini tekrar kontrol et.

Oyun bir eğlence ve medya okuryazarlığı çalışmasıdır. **Görsele bakarak tek başına güvenilir AI tespiti yaptığını iddia etmez.** Gerçeklik/AI etiketleri kaynakta belirtilen üretim türüne bağlıdır.

## Bir sonraki sürüm için öneri

Gerçek yayımlamada Commons görsellerini tek tek inceleyip **izinleri uygunsa optimize edilmiş WebP kopyalarını kendi CDN'inde barındır**; böylece üçüncü taraf erişimine bağımlılık azalır. Yeni sorularda kaynak ve üretim kaydı şart olsun. Daha sonra WordPress kısa kodu, günlük meydan okuma ve sonuç paylaşımı için dinamik Open Graph görseli eklenebilir.