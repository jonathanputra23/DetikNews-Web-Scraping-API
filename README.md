# DetikNews Web Scraping API
 API for scraping news detail from DetikNews and its other Detik website.

o The API description
DetikNews Web Scraping API is a python programs to scrape news detail from keywords payload. It scrapes Detik website and its subdomain sites.
It currently have two function:
1. getUrl: To get the full URL queries from the payload
2. scrape: To get news detail from the payload queries

o How it works?

DetikNews Web Scraping API uses Python Django Rest Framework to build the APIs and BeautiulSoup4 to extract data from URL also Swagger for documentation and testing.

o Endpoint description (e.g., payload and response details)

Endpoint | HTTP Method | Result
-- | -- |-- 
`getUrl/` | POST | Return full string of URL query
`scrape/` | POST | Return JSON object of news detail result

o Payload Details

REQUEST:
```json
    {
        "site": "detikcom",
        "fromDate": "2017-1-12",
        "keywords": "james",
        "toDate": "2018-8-7",
        "page": 1
    }
```
RESPONSE:

```json
{
    "1": {
        "title": "Dave Bautista Ancam Tinggalkan 'Guardians of the Galaxy'",
        "link": "https://hot.detik.com/detiktv/d-4154476/dave-bautista-ancam-tinggalkan-guardians-of-the-galaxy",
        "date": "detikHotSelasa, 07 Agu 2018 16:17 WIB",
        "summary": "Dave Bautista mengancam akan meninggal kan Guardians of the Galaxy Vol. 3 bila Marvel tak menggunakan naskah James Gunn."
    },
    "2": {
        "title": "Ancaman Dave Bautista pada Disney soal Dipecatnya James Gunn",
        "link": "https://hot.detik.com/movie/d-4153809/ancaman-dave-bautista-pada-disney-soal-dipecatnya-james-gunn",
        "date": "detikHotSelasa, 07 Agu 2018 11:40 WIB",
        "summary": "Pemecatan James Gunn oleh Disney memastikan dirinya tak lagi ambil kendali dalam lanjutan 'Guardians of The Galaxy 3'."
    },
    "3": {
        "title": "Meski Ada Keita dan Fabinho, Henderson Tetap Penting untuk The Reds",
        "link": "https://sport.detik.com/sepakbola/liga-inggris/d-4153260/meski-ada-keita-dan-fabinho-henderson-tetap-penting-untuk-the-reds",
        "date": "SepakbolaSelasa, 07 Agu 2018 03:58 WIB",
        "summary": "Liverpool memang punya dua gelandang baru berkualitas, Fabinho dan Naby Keita. Tapi, bukan berarti Jordan Henderson tak lagi penting untuk The Reds."
    },
    "4": {
        "title": "Musisi Senior Ini Mengeluh, Harga Pakaian Zaman Now Mahal-mahal",
        "link": "https://wolipop.detik.com/entertainment-news/d-4152895/musisi-senior-ini-mengeluh-harga-pakaian-zaman-now-mahal-mahal",
        "date": "WolipopSenin, 06 Agu 2018 19:01 WIB",
        "summary": "Banyak selebriti, influencer hingga orang awam mengeluarkan uang ratusan juta rupiah demi penampilan. Hal itu rupanya membuat penyanyi senior ini jengah."
    },
    "5": {
        "title": "Chairman Jababeka Group Rilis Buku Kelima Tentang Peran Pengusaha",
        "link": "https://news.detik.com/adv-nhl-detikcom/d-4152674/chairman-jababeka-group-rilis-buku-kelima-tentang-peran-pengusaha",
        "date": "detikNewsSenin, 06 Agu 2018 17:40 WIB",
        "summary": "Buku tersebut berisi pandangan S. D. Darmono mengenai peran pengusaha untuk memberdayakan masyarakat dalam proses pembangunan bangsa."
    },
    "6": {
        "title": "James Gunn Dipecat, Dave Bautista Hanya Jalankan Kewajiban di 'GOTG'",
        "link": "https://hot.detik.com/movie/d-4151854/james-gunn-dipecat-dave-bautista-hanya-jalankan-kewajiban-di-gotg",
        "date": "detikHotSenin, 06 Agu 2018 11:23 WIB",
        "summary": "Dave Bautista pemeran Drax menjadi salah satu bintang yang tak terima sutradara James Gunn dipecat."
    },
    "7": {
        "title": "Bukan Hal yang Mudah Bagi Disney Tarik James Gunn Kembali",
        "link": "https://hot.detik.com/movie/d-4151666/bukan-hal-yang-mudah-bagi-disney-tarik-james-gunn-kembali",
        "date": "detikHotSenin, 06 Agu 2018 09:51 WIB",
        "summary": "Setelah James Gunn dipecat oleh Disney dan tak lagi menjadi sutradara 'Guardians of The Galaxy', selebriti hingga fans menyampaikan berbagai dukungan."
    },
    "8": {
        "title": "Klopp: Nilai Seberapa Kuat Skuat Liverpool di Akhir Musim",
        "link": "https://sport.detik.com/sepakbola/liga-inggris/d-4150756/klopp-nilai-seberapa-kuat-skuat-liverpool-di-akhir-musim",
        "date": "SepakbolaMinggu, 05 Agu 2018 14:55 WIB",
        "summary": "Liverpool melakukan pembelian besar di musim ini. Juergen Klopp menegaskan bahwa kekuatan skuat The Reds baru bisa dinilai di akhir musim."
    },
    "9": {
        "title": "Menang 5-0 atas Napoli, Liverpool Masih Butuh Perbaikan",
        "link": "https://sport.detik.com/sepakbola/liga-inggris/d-4150388/menang-5-0-atas-napoli-liverpool-masih-butuh-perbaikan",
        "date": "SepakbolaMinggu, 05 Agu 2018 08:23 WIB",
        "summary": "Liverpool meraih kemenangan meyakinkan atas Napoli dalam pertandingan uji coba pramusim. Meski demikian, Juergen Klopp menilai masih ada yang perlu dibenahi."
    }
}
```

DATA DESCRIPTION:
Key | Type | Description
--- | --- | ---
id | integer | Unique identifier for a payload.
title | string | The title of article.
link | string | The link of article.
date | string | The date and time the article published.
summary | string | The summary of the article.
keywords | string | The search keywords.
site | string | The domain name ex:detikcom, detikfinance, detiksport.
page | integer | Page identifier.
fromDate | date | Search filter from date(format YYYY-MM-DD).
toDate | date | Search filter to date(format YYYY-MM-DD).


## Usage
o Requirements:
- Python
- Django Rest Framework
- BeautifulSoup
- Requests
- Swagger

o How to setup the API

1. Download this API and unpack on selected folder. 
2. Enter virtual environment.
3. run server.
4. API is ready to use.

o How to test the API

This API already includes swagger-ui, you can use swagger by using {localhost:8000}/swagger-ui/.
