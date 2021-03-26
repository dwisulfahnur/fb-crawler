# FB Comments Crawler

## Project Specification

- Crawler Tools: Selenium, Beautifulsoup4
- Web Framework: Django
- Task Queue: Celery and Redis as Message Broker


## Run

```
docker-compose up -d --build
```

## API Docs

### Comment Crawler API

<img width="1292" alt="Screen Shot 2021-03-26 at 18 35 35" src="https://user-images.githubusercontent.com/12431528/112626137-62c5c700-8e62-11eb-8897-936e557cc854.png">

URL Format:
```http://127.0.0.1:8000/api/comments/<pid>_<post_id>/crawl```

Request sample with CURL:

```
curl -XPOST  http://127.0.0.1:8000/api/comments/583729738378157_3660159894068444/crawl
```

Response:
```json
{
  "pid": "583729738378157", 
  "post_id": "3748058435278589", 
  "status": "on_progress", 
  "comments": null
}
```


### Get Comment Result API

Request sample for the existing post comments data

```
curl -XGET  http://127.0.0.1:8000/api/comments/3660159894068444
```

Response Data field description:

| Field Name | Description                  |
|------------|------------------------------|
| pid        | PageID or UserId or Username |
| post_id    | Post ID                      |
| status     | Crawling status              |
| comments   | List of Comment              |

Comment fields description:

| Field Name        | Description                                                |
|-------------------|------------------------------------------------------------|
| id_post           | Post ID                                                    |
| parent_id_comment | Parent Comment ID (it mean the item is reply of a comment) |
| id_comment        | Comment/Comment-Reply ID                                   |
| user_comment      | Username of the comment/reply                              |
| text_comment      | Text Comment                                               |
| date_comment      | Date of the Comment                                        |
| count_replies     | Amount of the comment replies                              |

Response:

```json

  "pid": "583729738378157",
  "post_id": "3660159894068444",
  "status": "completed",
  "comments": [
    {
      "id_post": "583729738378157",
      "parent_id_comment": null,
      "id_comment": "3662227383861695",
      "user_comment": "yudha.a.putra.397",
      "text_comment": "Saya punya 2 kartu dengan 2 nomor kpj berbeda, tapi sudah download aplikasi bpjstku hanya ada  1 kartu yg terdaftar saldonya, dan setelah saya mau login dengan kartu yg satunya lgi tidak bisa dengan keterangan harus pake email yg lain dan nomor hp yg berbeda, bagaimana ini BPJS",
      "date_comment": "1613202800",
      "count_replies": 4
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3662227383861695",
      "id_comment": "3670542889696811",
      "user_comment": "dewiiiku",
      "text_comment": "satu2 lebih enak ngajuinnya",
      "date_comment": "1613493523",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3662227383861695",
      "id_comment": "3670266683057765",
      "user_comment": "wiwi.sawiah.7121",
      "text_comment": "BPJS Ketenagakerjaan maaf mau tanya juga. Kalau cara pengajuan dengan melampirkan 3kartu bagaimana ya . Mohon bantuannya",
      "date_comment": "1613484376",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3662227383861695",
      "id_comment": "3664942126923554",
      "user_comment": "#",
      "text_comment": "Ijin gabung..Saya menambahkan no kpj tapi tulisan nya tidak valid email..Padahal email bisa buat buka apliksi..…Lihat Lainnya",
      "date_comment": "1613294783",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3662227383861695",
      "id_comment": "3664537736963993",
      "user_comment": "BPJSTKinfo",
      "text_comment": "Siang, Sahabat. Mohon informasikan kembali, apakah sudah melakukan tambah KPJ? -Radu",
      "date_comment": "1613279654",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": null,
      "id_comment": "3662276587190108",
      "user_comment": "endah.s.hermawan",
      "text_comment": "Halo, saya mau tanya. Bagaimana kalau lupa alamat email yg sudah terdaftar di akun BPJStku kita ya? Tdk bisa masuk akun. Daftar akun baru tdk bs, infonya sudah terdaftar nomornya. Saya ingat passwordnya tp lupa alamat email.",
      "date_comment": "1613204716",
      "count_replies": 16
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3662276587190108",
      "id_comment": "3674735089277591",
      "user_comment": "iaaeankclalu.pdaamoee",
      "text_comment": "Cek inbok pak",
      "date_comment": "1613637534",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3662276587190108",
      "id_comment": "3671190239632076",
      "user_comment": "BPJSTKinfo",
      "text_comment": "BP Jamsostek tidak meminta atau menerima imbalan berupa apapun dari peserta. Mohon berinteraksi dengan kami melalui akun resmi FB BPJS Ketenagakerjaan, twitter @bpjstkinfo, email care@bpjsketenagakerjaan.go .id, atau Contact Center 1 7 5 untuk menghindari penyalahgunaan data.",
      "date_comment": "1613514727",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3662276587190108",
      "id_comment": "3672211589529941",
      "user_comment": "endah.s.hermawan",
      "text_comment": "Agoeng Bangkit sudah selesai",
      "date_comment": "1613554807",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3662276587190108",
      "id_comment": "3669455356472231",
      "user_comment": "BPJSTKinfo",
      "text_comment": "Siang, Sahabat. Perihal pencairan, sahabat dijadwalkan antrean untuk tanggal berapa dan diinformasikan berapa hari kerja? -Ruhi",
      "date_comment": "1613454642",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3662276587190108",
      "id_comment": "3667330590018041",
      "user_comment": "bazlia.bazlia.5",
      "text_comment": "Kalo saya ga bisa buka lewat aplikasi ,karena no nik saya pernah terdaftar di email lain .itu gmn solusinya ya ?",
      "date_comment": "1613379865",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3662276587190108",
      "id_comment": "3667220653362368",
      "user_comment": "chugas.ajjah",
      "text_comment": "Siang ka kalo kaya gini gmn , trus ada 2 no kpj yg diklaim yg 1 ptnya udah tutup apakah harus menunggu verifikasi dari perusahaan yg sudah tutup ..",
      "date_comment": "1613375174",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3662276587190108",
      "id_comment": "3666743503410083",
      "user_comment": "doewy.dech",
      "text_comment": "Admin cek dm yaa",
      "date_comment": "1613355827",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3662276587190108",
      "id_comment": "3664588753625558",
      "user_comment": "endah.s.hermawan",
      "text_comment": "BPJS Ketenagakerjaan sudah bisa login kembali sudah tlp ke 175",
      "date_comment": "1613281675",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3662276587190108",
      "id_comment": "3664588013625632",
      "user_comment": "endah.s.hermawan",
      "text_comment": "Ii'iezzt Wahyuu stlh install bpjstku, tinggal pilih pendaftaran baru, masukan nama, no. KTP, no kartu bpjsnya, email, bikin password. Klo udah berhasil, bisa login,  bisa cek saldo jht",
      "date_comment": "1613281643",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3662276587190108",
      "id_comment": "3664585536959213",
      "user_comment": "endah.s.hermawan",
      "text_comment": "Ojzet'geutihsunda Lang'lang Buana bisa. Call center 24jam.",
      "date_comment": "1613281554",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3662276587190108",
      "id_comment": "3664538493630584",
      "user_comment": "BPJSTKinfo",
      "text_comment": "Siang, Sahabat. Jika demikian, silakan informasikan data berikut melalui inbox Facebook BPJS Ketenagakerjaan agar terjaga kerahasiaan datanya: 1. Nomor referensi/nomor peserta;…Lihat Lainnya",
      "date_comment": "1613279681",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3662276587190108",
      "id_comment": "3662962597121507",
      "user_comment": "wahyu.ingintdslwcetya",
      "text_comment": "Untuk dftr akun baru gmn y kakk..  kok g bisaa y kakk...",
      "date_comment": "1613226681",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3662276587190108",
      "id_comment": "3662397817177985",
      "user_comment": "bagaz.jouw",
      "text_comment": "Endah Suharti emang th hari libur bisa",
      "date_comment": "1613209212",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3662276587190108",
      "id_comment": "3662395010511599",
      "user_comment": "endah.s.hermawan",
      "text_comment": "Ojzet'geutihsunda Lang'lang Buana tlp call center pak. Saya barusan sekali tlp beres. Tlp ke 175",
      "date_comment": "1613209102",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3662276587190108",
      "id_comment": "3662391547178612",
      "user_comment": "bagaz.jouw",
      "text_comment": "Direset itu gimana caranya saya juga lupa password nya th gimana cara daftar lagi dihape baru",
      "date_comment": "1613208955",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3662276587190108",
      "id_comment": "3662323580518742",
      "user_comment": "cuiitiey.amourtafully",
      "text_comment": "Endah Suharti direset brati kak solusinya",
      "date_comment": "1613206474",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": null,
      "id_comment": "3660325394051894",
      "user_comment": [
        "100053971230919"
      ],
      "text_comment": "",
      "date_comment": "1613134360",
      "count_replies": 4
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3660325394051894",
      "id_comment": "3670609149690185",
      "user_comment": "alay.cobra.7",
      "text_comment": "Walau pun brda nomer kpj? Eamang ngak bisa",
      "date_comment": "1613495795",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3660325394051894",
      "id_comment": "3663163773768056",
      "user_comment": "BPJSTKinfo",
      "text_comment": "Malam, Sahabat. Perihal pencairan JHT dilakukan sekaligus, saat ini apakah masih aktif bekerja? -Mazid",
      "date_comment": "1613232537",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3660325394051894",
      "id_comment": "3662367203847713",
      "user_comment": "ridwan.chebhontot",
      "text_comment": "Alay Samber Nyawa harus di cairkan semua nya",
      "date_comment": "1613207981",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3660325394051894",
      "id_comment": "3660777400673360",
      "user_comment": "alay.cobra.7",
      "text_comment": "Mau tanya saya punya 2 kartu kpj beda nomer,, apakah bisa dicairkan salah 1 yang ada pklaringnya",
      "date_comment": "1613148142",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": null,
      "id_comment": "3660174884066945",
      "user_comment": "azkha.rafa.545",
      "text_comment": "Min mau tanya, cara mengetahui nomer kartu JHT gmn jika kartu sudah hilang & belum di masukan ke aplikasi JHTku, cara lacak nomer kartunya gmn????",
      "date_comment": "1613129156",
      "count_replies": 7
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3660174884066945",
      "id_comment": "3662314287186338",
      "user_comment": "BPJSTKinfo",
      "text_comment": "Sore, Sahabat. Perihal informasi nomor kepesertaan, silakan konfirmasi dengan HRD perusahaan atau ke kantor cabang terdaftar dengan membawa EKTP, KK, dan paklaring. -Ziah",
      "date_comment": "1613206122",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3660174884066945",
      "id_comment": "3660306080720492",
      "user_comment": [
        "100009278805854"
      ],
      "text_comment": "Azkha Rafa pen dapet yg gratis haha",
      "date_comment": "1613133734",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3660174884066945",
      "id_comment": "3660213594063074",
      "user_comment": "azkha.rafa.545",
      "text_comment": "",
      "date_comment": "1613130566",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3660174884066945",
      "id_comment": "3660201717397595",
      "user_comment": "azkha.rafa.545",
      "text_comment": "Ridone Ahmad caranya gua dh tau sebenernya",
      "date_comment": "1613130152",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3660174884066945",
      "id_comment": "3660200777397689",
      "user_comment": "azkha.rafa.545",
      "text_comment": "Ridone Ahmad iseng. Wkwkk",
      "date_comment": "1613130111",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3660174884066945",
      "id_comment": "3660185870732513",
      "user_comment": "ridone.ahmad.52",
      "text_comment": "Bukanya u calo. Koq malah nanya si bro wkwkwk",
      "date_comment": "1613129536",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3660174884066945",
      "id_comment": "3660180007399766",
      "user_comment": "ridone.ahmad.52",
      "text_comment": "Azkha Rafa tanya hrd perushaan tmpat bekerja",
      "date_comment": "1613129319",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": null,
      "id_comment": "3660194850731615",
      "user_comment": "taryat.nurhidayat",
      "text_comment": "Cuman minta solusi inbok saya juga ga di tanggapi",
      "date_comment": "1613129872",
      "count_replies": 2
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3660194850731615",
      "id_comment": "3662430630508037",
      "user_comment": "BPJSTKinfo",
      "text_comment": "Selamat sore, sahabat. Silakan interaksi selanjutnya melalui inbox. Terima kasih. -Ina",
      "date_comment": "1613210489",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3660194850731615",
      "id_comment": "3661391950611905",
      "user_comment": "taryat.nurhidayat",
      "text_comment": "Azkha Rafa Siang min..Gimana solusinya mau ngurusin JKMsedangkan orang yang bersangkutan tidak memiliki buku nikah,,hanya nikah siri…Lihat Lainnya",
      "date_comment": "1613170134",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": null,
      "id_comment": "3669305099820590",
      "user_comment": "sulik.idy",
      "text_comment": "Selamat siang bpk / ibu. Saya dulu pernah mendaftar akun di aplikasi bpjstku menggunakan email lama, dan saya lupa kata sandi email tersebut. Saya buat akun baru tapi tidak bisa dikarenakan sebelumnya sudah pernah daftar di email lama🙏",
      "date_comment": "1613448247",
      "count_replies": 1
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3669305099820590",
      "id_comment": "3671656706252096",
      "user_comment": "BPJSTKinfo",
      "text_comment": "Selamat pagi, Sahabat. Perihal lupa akun, silakan informasikan data berikut terlebih dulu agar dibantu cek : 1. Nomor referensi/nomor kepesertaan; 2. Nama lengkap;…Lihat Lainnya",
      "date_comment": "1613531958",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": null,
      "id_comment": "3661972083887225",
      "user_comment": "rihardia.nugrahani",
      "text_comment": "Susah ya buat ambilnya..... data di bilang gak valid karena kartu lama....pdhl yg cetak BPJS itu sendiri...... aneh banget, padahal uang sendiri tp di tahan....ngenes",
      "date_comment": "1613191933",
      "count_replies": 1
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3661972083887225",
      "id_comment": "3662051750545925",
      "user_comment": "muktardoang.muktar",
      "text_comment": "Rihardia Nugrahani inbox siapa tau sya bisa bntu",
      "date_comment": "1613195224",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": null,
      "id_comment": "3660359030715197",
      "user_comment": "nony.ibay",
      "text_comment": "Urus kartu bpjs yg hilang gimana ya",
      "date_comment": "1613135440",
      "count_replies": 9
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3660359030715197",
      "id_comment": "3662595470491553",
      "user_comment": "BPJSTKinfo",
      "text_comment": "Selamat sore, sahabat. Perihal kartu hilang silakan konfirmasi ke HRD perusahaan untuk informasi nomor kepesertaan. Jika telah terinformasi nomor kepesertaannya, silakan lakukan registrasi akun kemudian cetak kartu digital melalui aplikasi BPJSTKu atau website http ://sso.bpjsketenagakerjaan.go .id/. -Ina",
      "date_comment": "1613216431",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3660359030715197",
      "id_comment": "3662325990518501",
      "user_comment": "cuiitiey.amourtafully",
      "text_comment": "Noni Nuraini ada paklaringnya kak?",
      "date_comment": "1613206575",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3660359030715197",
      "id_comment": "3662270597190707",
      "user_comment": "nony.ibay",
      "text_comment": "Iya trims di bantuin jawab aq udah minta no kpj😄",
      "date_comment": "1613204467",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3660359030715197",
      "id_comment": "3661982540552846",
      "user_comment": "aya.subekti",
      "text_comment": "Kresna Fajar kalo lewat apk gimana caranya ya cetak kartunya",
      "date_comment": "1613192377",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3660359030715197",
      "id_comment": "3661831590567941",
      "user_comment": "love18062011love",
      "text_comment": "Noni Nuraini  klo apal nik bpjs daftar ajj lewat apk,, nnti baru cetak kartunya lewat apk.. Klo engga apal dateng ke perusahaan tanyain nomer nik bpjsnya",
      "date_comment": "1613186280",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3660359030715197",
      "id_comment": "3661827090568391",
      "user_comment": "arinipuspita.s",
      "text_comment": "Noni Nuraini mba hafal nomer kpjnya ga? Klo hafal download aplikasi bpjstku aja",
      "date_comment": "1613186124",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3660359030715197",
      "id_comment": "3661747983909635",
      "user_comment": [
        "100061169406771"
      ],
      "text_comment": "Tiger siapa bilang mas😀",
      "date_comment": "1613183409",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3660359030715197",
      "id_comment": "3661746307243136",
      "user_comment": [
        "100061169406771"
      ],
      "text_comment": "Kalau masih krja lapor ke hrdnya mb ,,punyaq juga ilang ,,nanti bisa pakai mobile bpjstku aq jg pakai itu sekarang bisa lewat online",
      "date_comment": "1613183342",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3660359030715197",
      "id_comment": "3660396547378112",
      "user_comment": "bagus.ade.5015",
      "text_comment": "Noni Nuraini datang Ke kantor Bpjsnya Mba Minta Surat Pengantar Dari Perusahaan Bawah KTP Asli",
      "date_comment": "1613136663",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": null,
      "id_comment": "3664633716954395",
      "user_comment": "leiyanawatei.sisulung",
      "text_comment": "Punya jHT tpi gk ada paklaring apa bisa dicairkan",
      "date_comment": "1613283350",
      "count_replies": 1
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3664633716954395",
      "id_comment": "3666691403415293",
      "user_comment": "BPJSTKinfo",
      "text_comment": "Selamat pagi, Sahabat. Perihal pencairan, apakah perusahaan masih beroperasional? -Vey",
      "date_comment": "1613353708",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": null,
      "id_comment": "3661356203948813",
      "user_comment": "mukhroni04",
      "text_comment": "Padahal itu uang kita sendiri tapi kok susah buat nyairin,, kasus saya... saya tidak ada nomer kjp dan paklaring tp perusahaan saya sudah tutup dan gak ada solusi dr bpjstk buat nyairin, bilang.e harus lengkap syarat.e....",
      "date_comment": "1613168702",
      "count_replies": 5
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3661356203948813",
      "id_comment": "3670538099697290",
      "user_comment": "dewiiiku",
      "text_comment": "n'DRa sama kasusnya kya sy kmrn. terdftr d perusahaan yg ga pernah sama sekali sy bekerja dstu. Cm disuruh bikin surat pernyataan kak",
      "date_comment": "1613493363",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3661356203948813",
      "id_comment": "3664944616923305",
      "user_comment": "https:web.facebook.comBPJSTKinfoposts3660159894068444",
      "text_comment": "Kalo tidak pernah bekerja tapi tercantum d bpjs kerja d situ gmn?",
      "date_comment": "1613294877",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3661356203948813",
      "id_comment": "3663454167072350",
      "user_comment": "BPJSTKinfo",
      "text_comment": "Pagi, Sahabat. Perihal paklaring tidak ada dan perusahaan tutup, silakan membuat surat pernyataan yang berisi bahwa peserta sudah benar-benar berhenti bekerja, perusahaan tutup, dan belum pernah mencairkan JHT disaksikan oleh petugas cabang. Jika dimun…Lihat Lainnya",
      "date_comment": "1613241397",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3661356203948813",
      "id_comment": "3662420233842410",
      "user_comment": "Sitiqoriah.Amd",
      "text_comment": "Taufik Mukhroni sama kasusnya bang",
      "date_comment": "1613210098",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3661356203948813",
      "id_comment": "3662054740545626",
      "user_comment": "muktardoang.muktar",
      "text_comment": "Taufik Mukhroni bisa saya bantu ajukan inbox aja",
      "date_comment": "1613195353",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": null,
      "id_comment": "3666158940135206",
      "user_comment": [
        "100007480698716"
      ],
      "text_comment": "Daftar di bpjstku susah di bagian verifikasi no handphone,sudah di masukan no hp yg aktif kode nya gk muncul2...Gimana ini gan?",
      "date_comment": "1613332610",
      "count_replies": 1
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3666158940135206",
      "id_comment": "3667288793355554",
      "user_comment": "BPJSTKinfo",
      "text_comment": "Sore, Sahabat. Mohon maaf atas ketidaknyamanannya. Perihal kendala kode verifikasi aplikasi BPJSTKu, sebelumnya menggunakan provider kartu apa? -Radu",
      "date_comment": "1613378069",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": null,
      "id_comment": "3662498537167913",
      "user_comment": "deni.mulyana.927980",
      "text_comment": "suruh kirim data doang,,,dah sebulan lebih g Di follow up...",
      "date_comment": "1613213054",
      "count_replies": 3
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3662498537167913",
      "id_comment": "3664764053608028",
      "user_comment": "BPJSTKinfo",
      "text_comment": "Selamat siang, sahabat. Perihal kendala tambah KPJ kami cek data sesuai, apakah bersedia dibantu reset akun dan registrasi kembali? -Ina",
      "date_comment": "1613288329",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3662498537167913",
      "id_comment": "3664551320295968",
      "user_comment": "zaetun",
      "text_comment": "Deni Mulyana Wa.me/6285773331187 1 jam beres",
      "date_comment": "1613280187",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3662498537167913",
      "id_comment": "3662499247167842",
      "user_comment": "deni.mulyana.927980",
      "text_comment": "inbox dibaca doang...",
      "date_comment": "1613213085",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": null,
      "id_comment": "3661514333933000",
      "user_comment": "rinawatichank.diaslamanya",
      "text_comment": "gimanna iya caranya cara cek saldo ..saya lupa email yg terdftar di bpjsku . tapi sandi saya ingat...saya mau nyoba bikin email baru tapi ngk bisa.mohon solusinya ?",
      "date_comment": "1613174880",
      "count_replies": 6
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3661514333933000",
      "id_comment": "3663598953724538",
      "user_comment": "BPJSTKinfo",
      "text_comment": "Pagi, Sahabat. Apaka sudah pilih menu lupa kata sandi? -Mazid",
      "date_comment": "1613246420",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3661514333933000",
      "id_comment": "3662685610482539",
      "user_comment": "love18062011love",
      "text_comment": "Telpon terus kak smpe nyambung ke cs,, saya wktu itu selalu sibuk berkali kali smpe pulsa mau abis,, alhamdulillah nyambung trs konfirmasi nik ini lupa imel dan pasword minta di hapus",
      "date_comment": "1613219468",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3661514333933000",
      "id_comment": "3662565397161227",
      "user_comment": "rinawatichank.diaslamanya",
      "text_comment": "Kresna Fajar ngk ada responnya kk",
      "date_comment": "1613215402",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3661514333933000",
      "id_comment": "3661825890568511",
      "user_comment": "love18062011love",
      "text_comment": "Rina Wati Borreg  telpon cs. Suruh imel klo udh apus imel. baru daftar lagi via apk bpjstku",
      "date_comment": "1613186075",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3661514333933000",
      "id_comment": "3661679613916472",
      "user_comment": "hendry.betawi.5",
      "text_comment": "Rina Wati Borreg reset akun secara total",
      "date_comment": "1613180935",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3661514333933000",
      "id_comment": "3661571943927239",
      "user_comment": "yudhi.joe.908",
      "text_comment": "Rina Wati Borreg  di aplikasi coba daftar baru lagi pake alamat email baru entar entar ada blsan bahwa anda terdaftar dengan akun ini la itu baru akun mbak pakai keluar",
      "date_comment": "1613177052",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": null,
      "id_comment": "3661780547239712",
      "user_comment": "jacoob.barlan",
      "text_comment": "rekening nya pake ewalet dana atau yg lain nya bisa gk",
      "date_comment": "1613184576",
      "count_replies": 3
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3661780547239712",
      "id_comment": "3662107933873640",
      "user_comment": "muktardoang.muktar",
      "text_comment": "Jaccob Jaccob gk bisa....bca bri juga bisa",
      "date_comment": "1613197564",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3661780547239712",
      "id_comment": "3662106180540482",
      "user_comment": "jacoob.barlan",
      "text_comment": "Atang Muktar yang bisa bikin online skrg apa ya . klo via ewalet emang gak bisa ya",
      "date_comment": "1613197486",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3661780547239712",
      "id_comment": "3662053623879071",
      "user_comment": "muktardoang.muktar",
      "text_comment": "Jaccob Jaccob bikin rekening aja",
      "date_comment": "1613195305",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": null,
      "id_comment": "3660508480700252",
      "user_comment": "afiati.azizah",
      "text_comment": "Itu uang JHT ayah saya yg ga di respon sampai sekarang gegara ini ya min ? 😭",
      "date_comment": "1613140006",
      "count_replies": 9
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3660508480700252",
      "id_comment": "3664524790298621",
      "user_comment": [
        "100050054325056"
      ],
      "text_comment": "Yang mau dibantu pencairan nya dgn kendala berkas yuk wa🙏",
      "date_comment": "1613279141",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3660508480700252",
      "id_comment": "3664310906986676",
      "user_comment": [
        "100014412011388"
      ],
      "text_comment": "Alhamdulillah bulan kmren ayah sya lgsung cair..Semoga yg belum cair sgera cair, tdk ada hmbatan apapun. Aminn",
      "date_comment": "1613271319",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3660508480700252",
      "id_comment": "3662881803796253",
      "user_comment": "https:web.facebook.comBPJSTKinfoposts3660159894068444",
      "text_comment": "Pantesan ,gue udh mengira sihh ,g bner",
      "date_comment": "1613224772",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3660508480700252",
      "id_comment": "3662001537217613",
      "user_comment": "bolokotok.tok.1",
      "text_comment": "Pantesan kartu KIS  saya di cabut ma pemerintahan",
      "date_comment": "1613193155",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3660508480700252",
      "id_comment": "3661567993927634",
      "user_comment": "yudhi.joe.908",
      "text_comment": "Klo masalah duit paling cepet ngembatnya.....hukum di negara ini sudah lemah buat koruptor",
      "date_comment": "1613176890",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3660508480700252",
      "id_comment": "3661312487286518",
      "user_comment": "taufan.badai1",
      "text_comment": "Ngeri gan",
      "date_comment": "1613166913",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3660508480700252",
      "id_comment": "3660970450654055",
      "user_comment": "https:web.facebook.comBPJSTKinfoposts3660159894068444",
      "text_comment": "Waduh....apakah skrg jd susah untuk mencairkan uang milik sendiri? Tega banget yg korupsi uang pekerja.",
      "date_comment": "1613154387",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3660508480700252",
      "id_comment": "3660653857352381",
      "user_comment": "ahmad.sarnubi.1694059",
      "text_comment": "Astagfirulloh 😭😭",
      "date_comment": "1613144310",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3660508480700252",
      "id_comment": "3660579424026491",
      "user_comment": "bramantheoo",
      "text_comment": "Afiati Azizah Mari dikawal bersama. UP terus berita ini",
      "date_comment": "1613142156",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": null,
      "id_comment": "3662384577179309",
      "user_comment": "sugix.sugix.7545",
      "text_comment": "",
      "date_comment": "1613208672",
      "count_replies": 0
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": null,
      "id_comment": "3661860393898394",
      "user_comment": "https:web.facebook.comBPJSTKinfoposts3660159894068444",
      "text_comment": "Min saya mau reset data atasnama Iskandar saya punya KPJ baru kpj lama sudah d nonaktipkn",
      "date_comment": "1613187339",
      "count_replies": 2
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3661860393898394",
      "id_comment": "3664308940320206",
      "user_comment": "BPJSTKinfo",
      "text_comment": "Pagi, Sahabat. Perihal reset akun, silakan yang bersangkutan berinteraksi menggunakan akun facebook pribadi. -Ruhi",
      "date_comment": "1613271248",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3661860393898394",
      "id_comment": "3662372113847222",
      "user_comment": "ridwan.chebhontot",
      "text_comment": "Boiz Pelangi Senja kartu nya ada kga",
      "date_comment": "1613208172",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": null,
      "id_comment": "3660412747376492",
      "user_comment": "away.aaza",
      "text_comment": "Mnus paklaring 2 kartu nya satu dan nama ktp am kpj nya beda apa bisa di cairkan .minta inpo nya min.",
      "date_comment": "1613137132",
      "count_replies": 6
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3660412747376492",
      "id_comment": "3666858060065294",
      "user_comment": "BPJSTKinfo",
      "text_comment": "Sama-sama. Terima kasih telah berinteraksi dengan kami. -Gea",
      "date_comment": "1613360167",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3660412747376492",
      "id_comment": "3664810243603409",
      "user_comment": "away.aaza",
      "text_comment": "Oohhh. Yaudh mkaih info nya",
      "date_comment": "1613290050",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3660412747376492",
      "id_comment": "3664806690270431",
      "user_comment": "BPJSTKinfo",
      "text_comment": "Selamat sore, Sahabat. Mohon maaf atas ketidaknyamanannya. Perihal informasi nomor kepesertaan, silakan konfirmasi ke kantor cabang terdaftar dengan membawa EKTP, KK, dan paklaring. -Ina",
      "date_comment": "1613289943",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3660412747376492",
      "id_comment": "3662687110482389",
      "user_comment": "away.aaza",
      "text_comment": "Kartu kpj nya satu. Yg pertama blm sempet dpet pabrik nya udh tutup.  Jd di tempat perusahaan yg k 2 jd melanjut kan dari yg awal..",
      "date_comment": "1613219519",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3660412747376492",
      "id_comment": "3662345943849839",
      "user_comment": "away.aaza",
      "text_comment": "Siti Mukhtoromah cara nya .??",
      "date_comment": "1613207296",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3660412747376492",
      "id_comment": "3662331813851252",
      "user_comment": "cuiitiey.amourtafully",
      "text_comment": "Away Aaza bisa tp hrus di sesuaikan dlu kak",
      "date_comment": "1613206811",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": null,
      "id_comment": "3660480197369747",
      "user_comment": "dinda.chacha",
      "text_comment": "Malam admin.. tolong respon pesan saya di messenger ya.. Trimakasih",
      "date_comment": "1613139076",
      "count_replies": 2
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3660480197369747",
      "id_comment": "3662817990469301",
      "user_comment": "BPJSTKinfo",
      "text_comment": "Malam, Sahabat. Informasi yang dibutuhkan sudah kami tanggapi melalui inbox. Silakan pengecekan kembali untuk interaksi selanjutnya. -Beni",
      "date_comment": "1613222943",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3660480197369747",
      "id_comment": "3660705344013899",
      "user_comment": [
        "100053476250368"
      ],
      "text_comment": "Dinda Pabela Hutagaol knpa teh",
      "date_comment": "1613145852",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": null,
      "id_comment": "3662577653826668",
      "user_comment": "https:web.facebook.comBPJSTKinfoposts3660159894068444",
      "text_comment": "Halo admin bagaimana mencairkan BPJS tanpa ada surat rekomendasi ? Soalnya sudah 1 bulan saya minta dari kantor tapi alasan belum keluar suratnya ada yang bisa ngasih solusi 🙏",
      "date_comment": "1613215819",
      "count_replies": 3
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3662577653826668",
      "id_comment": "3667277083356725",
      "user_comment": "BPJSTKinfo",
      "text_comment": "Selamat sore, sahabat. Berikut syarat pencairan bagi peserta yang berhenti bekerja karena habis kontrak: 1. Kartu peserta BPJS Ketenagakerjaan; 2. EKTP;…Lihat Lainnya",
      "date_comment": "1613377574",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3662577653826668",
      "id_comment": "3665819076835859",
      "user_comment": "BPJSTKinfo",
      "text_comment": "BPJS Ketenagakerjaan habis kontrak",
      "date_comment": "1613321521",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3662577653826668",
      "id_comment": "3665443333540100",
      "user_comment": "BPJSTKinfo",
      "text_comment": "Malam, Sahabat. Perihal kendala pada surat paklaring, sahabat berhenti bekerja karena mengundurkan diri, habis kontrak atau PHK? -Radu",
      "date_comment": "1613310709",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": null,
      "id_comment": "3662384063846027",
      "user_comment": "sugix.sugix.7545",
      "text_comment": "Aku dapet sms ini bener apa hoak",
      "date_comment": "1613208647",
      "count_replies": 1
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3662384063846027",
      "id_comment": "3664864020264698",
      "user_comment": "BPJSTKinfo",
      "text_comment": "Selamat sore, Sahabat. Silakan informasi kembali capture yang diberikan melalui inbox agar dibantu pengecekan. Terima kasih. -Ina",
      "date_comment": "1613292119",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": null,
      "id_comment": "3660307884053645",
      "user_comment": "https:web.facebook.comBPJSTKinfoposts3660159894068444",
      "text_comment": "Inbox ku tolong di respon min,",
      "date_comment": "1613133802",
      "count_replies": 3
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3660307884053645",
      "id_comment": "3667220626695704",
      "user_comment": "BPJSTKinfo",
      "text_comment": "Siang, Sahabat. Silakan informasikan nomor kepesertaan sahabat melalui inbox agar dibantu pengecekan data. Terima kasih. -Aji",
      "date_comment": "1613375173",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3660307884053645",
      "id_comment": "3665612883523145",
      "user_comment": "BPJSTKinfo",
      "text_comment": "BPJS Ketenagakerjaan saya mengetahui nomor kerpesertaan yg di daftarkan",
      "date_comment": "1613315404",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3660307884053645",
      "id_comment": "3662522770498823",
      "user_comment": "BPJSTKinfo",
      "text_comment": "Sore, Sahabat. Mohon maaf atas ketidaknyamanannya. Perihal kendala pencairan, apakah sahabat mengetahui nomor kepesertaan yang didaftarkan tersebut? -Beni",
      "date_comment": "1613213905",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": null,
      "id_comment": "3661932170557883",
      "user_comment": "nazwa.arul.5",
      "text_comment": "Mw naya dong saya mw riset cara nya gmna ya?",
      "date_comment": "1613190282",
      "count_replies": 5
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3661932170557883",
      "id_comment": "3670300016387765",
      "user_comment": "BPJSTKinfo",
      "text_comment": "Malam, Sahabat. Terima kasih atas informasi data yang diberikan. Perihal reset akun BPJSTKu, kami belum bisa melakukan pengecekan jika bukan peserta langsung konfirmasi melalui kami menggunakan akun pribadi atas nama peserta yang bersangkutan, silakan melalui email di care@bpjsketenagakerjaan.go .id atau melalui call center kami di nomor 1 7 5. -Aji",
      "date_comment": "1613485480",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3661932170557883",
      "id_comment": "3668860059865094",
      "user_comment": "nazwa.arul.5",
      "text_comment": "Iya ka",
      "date_comment": "1613433076",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3661932170557883",
      "id_comment": "3667873909963709",
      "user_comment": "nazwa.arul.5",
      "text_comment": "1.nomer perserta:200492895472.IRFAN3.BOGOR.04-JUNI-1988…Lihat Lainnya",
      "date_comment": "1613399565",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3661932170557883",
      "id_comment": "3667166086701158",
      "user_comment": "nazwa.arul.5",
      "text_comment": "Mohon maaf ka.sblm nya.kk bner dari kntor BPJS Ketenagakerjaan.takut nya ka jaman skrng?kk pham kan maksud saya.🙏🙏",
      "date_comment": "1613372835",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3661932170557883",
      "id_comment": "3667086540042446",
      "user_comment": "BPJSTKinfo",
      "text_comment": "Gustita Aqilah",
      "date_comment": "1613369271",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": null,
      "id_comment": "3661542243930209",
      "user_comment": "liezhhaa.nathhalieaa",
      "text_comment": "Mw tnya min...q punya bpjs 1 kluarga 3 orang. Seumpama bayar 2 orang aja boleh kah...",
      "date_comment": "1613175902",
      "count_replies": 1
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3661542243930209",
      "id_comment": "3661779587239808",
      "user_comment": "jacoob.barlan",
      "text_comment": "LiezHhaa NathhaLieaa beda wkwkwk",
      "date_comment": "1613184543",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": null,
      "id_comment": "3660177847399982",
      "user_comment": "gen.ahmad.370",
      "text_comment": "Inbox respon woooy, upload mulu keluhan orang ga di gubris, ga berkah gaji anda semua bikin sengsara orang yang lagi susah, bukan membantu malah mempersulit",
      "date_comment": "1613129241",
      "count_replies": 3
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3660177847399982",
      "id_comment": "3661656100585490",
      "user_comment": "gen.ahmad.370",
      "text_comment": "Asep Sinoeraya ntah ini jelas2 di setiap sudut kacab itu ada spanduk anti calo berantas calo, tapi di komen banyak bersliweran calo ga ada tindakan apa pun dri Bpjs",
      "date_comment": "1613180113",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3660177847399982",
      "id_comment": "3661653333919100",
      "user_comment": "gen.ahmad.370",
      "text_comment": "Riaa blm cair jg mba?",
      "date_comment": "1613180012",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3660177847399982",
      "id_comment": "3661486710602429",
      "user_comment": "riaa.riaa.3152130",
      "text_comment": "Iya mempersulit banget kita, bukannya membantu malah mempersulit😡",
      "date_comment": "1613173750",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": null,
      "id_comment": "3666634790087621",
      "user_comment": "https:web.facebook.comBPJSTKinfoposts3660159894068444",
      "text_comment": "Sy kan terdaftar di dua perusahaan dgn no yg berbeda. Lalu sy ajukan pencarian, ternyat dapat email balasan utk lampirkan ,kedua nya , pertanyaan saya apa kah saya harus ganti formulir nya ? Krn pas pengajuan formulir nya hanya satu sy buat?",
      "date_comment": "1613351472",
      "count_replies": 1
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3666634790087621",
      "id_comment": "3667416293342804",
      "user_comment": "BPJSTKinfo",
      "text_comment": "Sore, Sahabat. Mohon informasikan kembali, tanggal berapa terjadwal pencairannya? -Radu",
      "date_comment": "1613383468",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": null,
      "id_comment": "3662573983827035",
      "user_comment": "sheyla.la.908",
      "text_comment": "BPJS Ketenagakerjaan",
      "date_comment": "1613215685",
      "count_replies": 1
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3662573983827035",
      "id_comment": "3665437383540695",
      "user_comment": "BPJSTKinfo",
      "text_comment": "Selamat malam, Sahabat. Perihal apa yang bisa kami bantu seputar BPJS Ketenagakerjaan? -Radu",
      "date_comment": "1613310536",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": null,
      "id_comment": "3661956030555497",
      "user_comment": "suro.karto.568",
      "text_comment": "Tanya min. Klo punya 2 kartu. Beda pt Besuk pas pencairan dana packlaringnya apa juga harus 2 pt.   Soalnya pt yang baru katanya mau meneruskan dari pt lama tapi malah dibuatkan kpj baru. Atau bagaimana caranya menggabungkan kpj lama dengan yg baru.  Makasih.",
      "date_comment": "1613191219",
      "count_replies": 6
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3661956030555497",
      "id_comment": "3667101790040921",
      "user_comment": "suro.karto.568",
      "text_comment": "Terima kasih atas penjelasannya",
      "date_comment": "1613369969",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3661956030555497",
      "id_comment": "3667012096716557",
      "user_comment": "BPJSTKinfo",
      "text_comment": "Selamat siang, Sahabat. Perihal pencairan, silakan melampirkan paklaring dari masing-masing perusahaan yang terdafatr jika saldo belum digabungkan. -Vey",
      "date_comment": "1613366146",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3661956030555497",
      "id_comment": "3665052293579204",
      "user_comment": "suro.karto.568",
      "text_comment": "Belum.  Karena dari pt  baru katanya mau digabung. Tapi ternyata malah dibuatkan kpj baru",
      "date_comment": "1613298625",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3661956030555497",
      "id_comment": "3664509353633498",
      "user_comment": "BPJSTKinfo",
      "text_comment": "Selamat siang, sahabat. Apakah sebelumnya saldo sudah digabungkan? -Ina",
      "date_comment": "1613278536",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3661956030555497",
      "id_comment": "3662656357152131",
      "user_comment": "suro.karto.568",
      "text_comment": "Siti Mukhtoromah packlaringnya pakai pt baru atau  pakai  22 nya mbak",
      "date_comment": "1613218535",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3661956030555497",
      "id_comment": "3662333903851043",
      "user_comment": "cuiitiey.amourtafully",
      "text_comment": "Suro Karto Vastenburg nnti ktika pncairan otomats digabungkan",
      "date_comment": "1613206879",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": null,
      "id_comment": "3666863076731459",
      "user_comment": "ichigo.hae",
      "text_comment": "Niat pada kerja gak sih. Saya telpon ke call center manapun tidak di angkat angkat telpon ke cabang cirebon nya juga sama tidak di angkat. Udah 2 minggu telat verifikasi. Ngabisin pulsa,kuota dan waktu aja.",
      "date_comment": "1613360366",
      "count_replies": 0
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": null,
      "id_comment": "3662154923868941",
      "user_comment": "https:web.facebook.comBPJSTKinfoposts3660159894068444",
      "text_comment": "Min.. bener ngak BPJS lagi2 ada temuan. . .maaf 🙏🙏",
      "date_comment": "1613199681",
      "count_replies": 0
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": null,
      "id_comment": "3660266977391069",
      "user_comment": "gevarieldhean.saerang",
      "text_comment": "Giliran mau Klaim, nyusahin banget gak ada toleransi..",
      "date_comment": "1613132454",
      "count_replies": 1
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3660266977391069",
      "id_comment": "3669649876452779",
      "user_comment": "gevarieldhean.saerang",
      "text_comment": "Tiger bukan hal saya gimana itu saldo saya",
      "date_comment": "1613463027",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": null,
      "id_comment": "3662063347211432",
      "user_comment": "umi.n.khoiri.1",
      "text_comment": "Sama dengan nasib BPJS milik suami saya..",
      "date_comment": "1613195715",
      "count_replies": 0
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": null,
      "id_comment": "3662661693818264",
      "user_comment": [
        "100063565633455"
      ],
      "text_comment": "Admin tolong bantu klarifikasi inbox saya selanjutnya 🙏 KPJ 1200685xxxx",
      "date_comment": "1613218691",
      "count_replies": 1
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3662661693818264",
      "id_comment": "3669011693183264",
      "user_comment": "hendry.betawi.5",
      "text_comment": "Imas Masitoh kendala apa teh?",
      "date_comment": "1613438320",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": null,
      "id_comment": "3660841374000296",
      "user_comment": [
        "100024824831068"
      ],
      "text_comment": "Apakah 6 kartu KPJ beda perusahan bisa sekaligus dicairin",
      "date_comment": "1613150159",
      "count_replies": 1
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3660841374000296",
      "id_comment": "3662557403828693",
      "user_comment": [
        "100024824831068"
      ],
      "text_comment": "Tiger bacotmu",
      "date_comment": "1613215119",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": null,
      "id_comment": "3662393920511708",
      "user_comment": "AyuWandirraNaTyan",
      "text_comment": "Min BSU gelombang 3 ada atau ditiadakan?",
      "date_comment": "1613209054",
      "count_replies": 1
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3662393920511708",
      "id_comment": "3667231480027952",
      "user_comment": "dewi.purwatiningsih.71",
      "text_comment": "Ismy Ayu Wandirra udah di hapus.dari bulan Januari.",
      "date_comment": "1613375675",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": null,
      "id_comment": "3661782797239487",
      "user_comment": "hatake.kakase",
      "text_comment": "Untung punya sy Uda di ambil..",
      "date_comment": "1613184661",
      "count_replies": 0
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": null,
      "id_comment": "3674942915923475",
      "user_comment": "astria.achi",
      "text_comment": "Mohon pencerahannya....katanya sekarang kl mau nyairin harus semua/data yg dlu pernah di jamsostek juga harus dicairin?Yg ke 2....no dan kartu jamsosteknya sy udh ga ada...dan ga pernah di daftarin ke BPJSTKU....krn wkt dlu kan ga ada aplikasi ini....mohon solusi dan infonya",
      "date_comment": "1613644091",
      "count_replies": 2
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3674942915923475",
      "id_comment": "3677182645699502",
      "user_comment": "astria.achi",
      "text_comment": "Perusahaannya masih,tapi outletnya tutup",
      "date_comment": "1613718037",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3674942915923475",
      "id_comment": "3677147125703054",
      "user_comment": "BPJSTKinfo",
      "text_comment": "Siang, Sahabat. Perihal terdaftar beberapa kartu, maka pencairan dilakukan seluruhnya. Apakah perusahaan lama masih beroperasional? -Ruhi",
      "date_comment": "1613716477",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": null,
      "id_comment": "3666883423396091",
      "user_comment": [
        "100012605446130"
      ],
      "text_comment": "Kapan pencairan BPJS untuk tenaga Kebersihan",
      "date_comment": "1613361156",
      "count_replies": 1
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3666883423396091",
      "id_comment": "3667714886646278",
      "user_comment": "BPJSTKinfo",
      "text_comment": "Malam, Sahabat. Mohon maaf atas ketidaknyamanannya. Silakan informasikan detail pertanyaan agar bisa kami bantu informasi lebih lanjut. -Radu",
      "date_comment": "1613394401",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": null,
      "id_comment": "3671575009593599",
      "user_comment": "https:web.facebook.comBPJSTKinfoposts3660159894068444",
      "text_comment": "Hai.. saya mau tnya biasanya berapa lama klu mau cairin via online? Apa gak bisa klu qta ngajuin langsung gtu ke kantor dlam masa pandemi gini... Cz ngajuin online mesti tulisannya blm dproses... Klu blm proses gtu gmn dong?",
      "date_comment": "1613528947",
      "count_replies": 0
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": null,
      "id_comment": "3661906623893771",
      "user_comment": "ciintaehhokanong",
      "text_comment": "saya lupa e_mail sma kta sandi sayagimana cara nya reset e_mail secara online",
      "date_comment": "1613189188",
      "count_replies": 2
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3661906623893771",
      "id_comment": "3663658720385228",
      "user_comment": "wahyu.ingintdslwcetya",
      "text_comment": "Kak klo bikin akun baru lgii kok susah ya hbs nulis nama lengkp trs tnggl lhir kok balik lgi k nama lngkp kak..🙏🙏",
      "date_comment": "1613248590",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3661906623893771",
      "id_comment": "3662052880545812",
      "user_comment": "muktardoang.muktar",
      "text_comment": "Heri Yana Ramdan bisa saya bantu risetkan akunya inbox aja",
      "date_comment": "1613195268",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": null,
      "id_comment": "3669042026513564",
      "user_comment": "wandidemilano",
      "text_comment": "Admin bisa ga pencairan bpjs tanpa paklarin?",
      "date_comment": "1613439398",
      "count_replies": 1
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3669042026513564",
      "id_comment": "3670413389709761",
      "user_comment": "BPJSTKinfo",
      "text_comment": "Malam, Sahabat. Perihal kendala pada surat paklaring, sahabat berhenti bekerja karena mengundurkan diri, habis kontrak atau PHK? -Radu",
      "date_comment": "1613489104",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": null,
      "id_comment": "3664095017008265",
      "user_comment": [
        "100063565633455"
      ],
      "text_comment": "Admin tolong bantu klarifikasi inbox saya mengenai reset akun selanjutnya 🙏 KPJ 1200685xxxx",
      "date_comment": "1613264088",
      "count_replies": 0
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": null,
      "id_comment": "3669055879845512",
      "user_comment": "https:web.facebook.comBPJSTKinfoposts3660159894068444",
      "text_comment": "Selamat pagi .. min bagaimana cara untuk mencairkan BPJS ketenagakerjaan BPU?",
      "date_comment": "1613439857",
      "count_replies": 3
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3669055879845512",
      "id_comment": "3673537056064061",
      "user_comment": "BPJSTKinfo",
      "text_comment": "Pagi, Sahabat. Kartu peserta digital dapat digunakan untuk pencairan dana JHT dan memiliki fungsi, nilai, serta manfaat yang sama sesuai dengan program yang diikuti. -Aji",
      "date_comment": "1613597413",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3669055879845512",
      "id_comment": "3671413819609718",
      "user_comment": "BPJSTKinfo",
      "text_comment": "BPJS Ketenagakerjaan baik.. saya hanya punya kartu BPJS digital karena waktu itu daftar secara online apakah bisa ?",
      "date_comment": "1613522560",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3669055879845512",
      "id_comment": "3671407806276986",
      "user_comment": "BPJSTKinfo",
      "text_comment": "Pagi, Sahabat. Perihal pencairan kepesertaan BPU bisa dilakukan apabila sudah tidak memiliki penghasilan, silakan kunjungi kantor cabang terdekat dengan membawa berkas asli dan fotokopi. -Gea",
      "date_comment": "1613522325",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": null,
      "id_comment": "3661929673891466",
      "user_comment": "yanzueach",
      "text_comment": "Sampai sekarang blm masuk rek,,sblm nya nama rek sama ktp beda tp udh di benerin ke bank nya,,, tp sampai sekarang blm cair mohon info nya?",
      "date_comment": "1613190173",
      "count_replies": 6
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3661929673891466",
      "id_comment": "3666652520085848",
      "user_comment": "BPJSTKinfo",
      "text_comment": "Pagi, Sahabat. Proses video call dilakukan pada tanggal berapa dan informasi yang diberikan prosesnya berapa hari? -Gea",
      "date_comment": "1613352186",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3661929673891466",
      "id_comment": "3664614020289698",
      "user_comment": "yanzueach",
      "text_comment": "BPJS Ketenagakerjaan sudah",
      "date_comment": "1613282561",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3661929673891466",
      "id_comment": "3664453856972381",
      "user_comment": "BPJSTKinfo",
      "text_comment": "Selamat siang, sahabat. Apakah sudah dikonfirmasi melalui video call oleh petugas? -Ina",
      "date_comment": "1613276417",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3661929673891466",
      "id_comment": "3663150790436021",
      "user_comment": "ridone.ahmad.52",
      "text_comment": "Waduh pasti ga bakal cair tuh pantesan lama",
      "date_comment": "1613232148",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3661929673891466",
      "id_comment": "3662873717130395",
      "user_comment": "yanzueach",
      "text_comment": "Reza Ardian di buku rek nama nya yan yan sedangkan di KTP yayan,,,JD harus sama nama nya",
      "date_comment": "1613224535",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3661929673891466",
      "id_comment": "3662573713827062",
      "user_comment": [
        "100061413420984"
      ],
      "text_comment": "Yan'z Alamsyah kok bisa beda mba ??? Aduh aku jadi deg deg an keluar berapa hari ya ??",
      "date_comment": "1613215678",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": null,
      "id_comment": "3667036236714143",
      "user_comment": "rrezpe",
      "text_comment": "saya coba adukan ingin riset id sampai sekarang tidak ada tanggapan dari BPJS Ketenagakerjaan  lebih 1 tahun apa memang begini pelayananya.?",
      "date_comment": "1613367112",
      "count_replies": 1
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3667036236714143",
      "id_comment": "3669032569847843",
      "user_comment": "BPJSTKinfo",
      "text_comment": "Pagi, Sahabat. Interaksi kami lanjutkan via inbox. -Gea",
      "date_comment": "1613439071",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": null,
      "id_comment": "3660235714060862",
      "user_comment": "fitri.kanslalubertahan",
      "text_comment": "Tolong di coment dong ini kira\" cairnya hari apa?",
      "date_comment": "1613131369",
      "count_replies": 5
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3660235714060862",
      "id_comment": "3667690846648682",
      "user_comment": "fitri.kanslalubertahan",
      "text_comment": "Sore min, sudah, tapi blm da reapon min...",
      "date_comment": "1613393608",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3660235714060862",
      "id_comment": "3664760850275015",
      "user_comment": "BPJSTKinfo",
      "text_comment": "Selamat sore, Sahabat. Apakah sudah konfirmasi ke kantor cabang pengajuan? -Ina",
      "date_comment": "1613288193",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3660235714060862",
      "id_comment": "3661593100591790",
      "user_comment": "fitri.kanslalubertahan",
      "text_comment": "Zaechun Za tapi belum masuk k rekening sampe hari ini pun..",
      "date_comment": "1613177859",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3660235714060862",
      "id_comment": "3661379960613104",
      "user_comment": "yhbba.q",
      "text_comment": "Fitriani lihat di video ini kak penjelasannya..https://youtu.be/4JcuRAgPEwc",
      "date_comment": "1613169644",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3660235714060862",
      "id_comment": "3660258594058574",
      "user_comment": "zaetun",
      "text_comment": "Fitriani udah cair harusnya",
      "date_comment": "1613132169",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": null,
      "id_comment": "3666769326740834",
      "user_comment": "agung.ae.1004",
      "text_comment": "Kami siap membantu pendaftaran BPJS ketenagakerjaanSilahkan menghubungi…Lihat Lainnya",
      "date_comment": "1613356816",
      "count_replies": 2
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3666769326740834",
      "id_comment": "3685370528214047",
      "user_comment": "https:web.facebook.comBPJSTKinfoposts3660159894068444",
      "text_comment": "Makanya nya kerja lancar ,, biar tdak ada orang menipu disini,, kebanyakan tidur bpjs senin sampai jumaat tidur !!!! Lamaa",
      "date_comment": "1614011153",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3666769326740834",
      "id_comment": "3667444450006655",
      "user_comment": "BPJSTKinfo",
      "text_comment": "BP Jamsostek tidak meminta atau menerima imbalan berupa apapun dari peserta. Mohon berinteraksi dengan kami melalui akun resmi FB BPJS Ketenagakerjaan, twitter @bpjstkinfo, email care@bpjsketenagakerjaan.go .id, atau Contact Center 1 7 5 untuk menghindari penyalahgunaan data.",
      "date_comment": "1613384605",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": null,
      "id_comment": "3661958143888619",
      "user_comment": "BPJSTKinfo",
      "text_comment": "BPJS Ketenagakerjaan Cairin di bank bisa kagaaa?????? tolong jawab kawan",
      "date_comment": "1613191315",
      "count_replies": 2
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3661958143888619",
      "id_comment": "3670453463039087",
      "user_comment": "BPJSTKinfo",
      "text_comment": "Malam, Sahabat. Perihal pengajuan pencairan melalui bank SPO, saat ini ingin pengajuan melalui bank apa? Silakan informasikan domisili sahabat agar dibantu pengecekan bank kerja sama. -Aji",
      "date_comment": "1613490440",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3661958143888619",
      "id_comment": "3668074743276959",
      "user_comment": "BPJSTKinfo",
      "text_comment": "BPJS Ketenagakerjaan lokasi di jakarta dmna saja?",
      "date_comment": "1613406025",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": null,
      "id_comment": "3661827933901640",
      "user_comment": "love18062011love",
      "text_comment": "Ini saya udh daftar online dan udah lewat tanggal claim telpon....!! Mau smpe kapan nungguinnya",
      "date_comment": "1613186152",
      "count_replies": 4
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3661827933901640",
      "id_comment": "3661883573896076",
      "user_comment": "love18062011love",
      "text_comment": "Ridone Ahmad udh prnah ke kantor cabang tapi kata satpamnya suruh tungguin ajj.. Saya mnta mau ktmu sama csnya ajj langsung tapi kaga bolehhhh.. Emosiii ajj jadinya sama satpam",
      "date_comment": "1613188264",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3661827933901640",
      "id_comment": "3661864567231310",
      "user_comment": "ridone.ahmad.52",
      "text_comment": "Kresna Fajar coba telpon/cari kantor cabang yg berskangkutan biasanya ada di google",
      "date_comment": "1613187505",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3661827933901640",
      "id_comment": "3661860397231727",
      "user_comment": "love18062011love",
      "text_comment": "Ridone Ahmad  sama bang modelnya kaya bgtu juga",
      "date_comment": "1613187339",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3661827933901640",
      "id_comment": "3661859377231829",
      "user_comment": "ridone.ahmad.52",
      "text_comment": "Kresna Fajar cek email coba",
      "date_comment": "1613187295",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": null,
      "id_comment": "3662296070521493",
      "user_comment": "yhbba.q",
      "text_comment": "Buat temen-temen yang punya kendala masalah bpjs ketenagakerjaan, sekarang sudah banyak solusinya di youtube..salah satunya ada di channel ini membahas seputar solusi-solusi permasalahan bpjs ketenagakerjaan..…Lihat Lainnya",
      "date_comment": "1613205453",
      "count_replies": 0
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": null,
      "id_comment": "3662270140524086",
      "user_comment": "https:web.facebook.comBPJSTKinfoposts3660159894068444",
      "text_comment": "Banyak calok....anjimng",
      "date_comment": "1613204457",
      "count_replies": 0
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": null,
      "id_comment": "3662152423869191",
      "user_comment": "kiki.noviastuti.1",
      "text_comment": "Admin mohon tolong cek inbox 🙏 saya mau riset aplikasi bpjstku punya saya di karenakan lupa password nya",
      "date_comment": "1613199574",
      "count_replies": 3
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3662152423869191",
      "id_comment": "3666588840092216",
      "user_comment": "BPJSTKinfo",
      "text_comment": "Pagi, Sahabat. Interaksi kami lanjutkan via inbox. -Gea",
      "date_comment": "1613349516",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3662152423869191",
      "id_comment": "3664559580295142",
      "user_comment": "kiki.noviastuti.1",
      "text_comment": "BPJS Ketenagakerjaan admin mohon cek inbox, sudah saya perbsiki bln lahir nya 🙏",
      "date_comment": "1613280514",
      "count_replies": null
    },
    {
      "id_post": "583729738378157",
      "parent_id_comment": "3662152423869191",
      "id_comment": "3664528846964882",
      "user_comment": "BPJSTKinfo",
      "text_comment": "Siang, Sahabat. Silakan infokan bulan lahir sesuai EKTP melalui inbox. -Ziah",
      "date_comment": "1613279314",
      "count_replies": null
    }
  ]
}
```
