# SPDX-License-Identifier: GPL-3.0-or-later
"""Kamus Bahasa Gaul untuk Render Engines, Principled BSDF Material, 16 Tipe Object Data & Properti Inti."""

from __future__ import annotations

# Panduan Live berdasarkan Render Engine yang sedang aktif
RENDER_ENGINE_GUIDES: dict[str, dict[str, str]] = {
    "BLENDER_EEVEE": {
        "name": "EEVEE (Real-Time Cepat)",
        "en_keyword": "Blender EEVEE Render Settings Raytracing Shadows tutorial",
        "fungsi": "Mesin render super ngebut ala game engine modern! Hasilnya langsung kelihatan real-time tanpa nunggu lama — cocok banget buat animasi panjang, motion graphics, atau gaya anime/stylized.",
        "cara_pakai": "Nyalain 'Raytracing' biar pantulan lantai/kaca makin nyata, atur 'Samples' (misal 64–128 buat hasil bersih), dan cek bagian 'Shadows' kalau bayangan kelihatan kurang halus!",
    },
    "CYCLES": {
        "name": "Cycles (Path Tracer Super Realistis)",
        "en_keyword": "Blender Cycles Render Settings GPU Denoise Light Paths tutorial",
        "fungsi": "Mesin render kelas film Hollywood yang ngitung pantulan sinar cahaya fisik beneran! Pilihan nomor #1 kalau lu ngejar hasil fotorealistis (produk, arsitektur interior, kaca bening, perhiasan).",
        "cara_pakai": "1) Ganti 'Device' dari CPU ke **GPU Compute** biar berkali-kali lebih ngebut!\n2) Aktifkan **Denoise** (OpenImageDenoise) di bagian Render!\n3) Cukup set Noise Threshold = 0.05 & Max Samples = 256–512 biar hemat waktu tapi tetep bening!",
    },
    "BLENDER_WORKBENCH": {
        "name": "Workbench (Preview Cepat Studio)",
        "en_keyword": "Blender Workbench Render Clay Matcap Wireframe tutorial",
        "fungsi": "Mesin render tampilan kerja Solid Viewport! Dipakai buat bikin video preview animasi cepat (Playblast) atau pamer model polosan pakai MatCap / Clay.",
        "cara_pakai": "Pilih Lighting (Studio / MatCap / Flat), aktifkan Cavity (biar lekukan detail nonjol tegas) dan Shadow kalau mau pamer modeling!",
    },
}


# Seluruh Input Principled BSDF di Blender 5.2 (urutan persis di Tab Material!)
PRINCIPLED_BSDF_GAUL: list[tuple[str, str, str, str]] = [
    ("Base Color", "Blender Principled BSDF Base Color", "Warna cat dasar permukaan objek (atau tempat nyolok gambar tekstur warna Albedo/Diffuse).", "Klik kotak warnanya buat ganti warna, atau klik titik kuning di kirinya -> pilih 'Image Texture' buat masukin gambar foto!"),
    ("Metallic", "Blender Principled BSDF Metallic", "Nentuin apakah bahan ini Non-Logam (0.0 = plastik/kayu/batu/kulit) atau Logam Murni (1.0 = besi/emas/perak/tembaga).", "Isi 0.0 atau 1.0 aja (jarang banget benda nyata di tengah-tengah 0.5 kecuali logam berdebu/karat)!"),
    ("Roughness", "Blender Principled BSDF Roughness", "Tingkat kekasaran permukaan — penentu utama objek kelihatan BASAH MENGKILAP atau KERING BURAM!", "0.0 = licin mulus kayak cermin/air; 0.2 = plastik glossy; 0.5 = kayu/semi-doff; 1.0 = kasar buram kayak kapur/tanah kering!"),
    ("IOR", "Blender Principled BSDF IOR Index of Refraction", "Indeks pembiasan cahaya (seberapa kuat kaca/air membelokkan bayangan di belakangnya & seberapa kuat pantulan sudutnya).", "Default 1.50 pas buat kaca/plastik umum; isi 1.333 buat Air jernih; isi 2.42 buat Berlian berkilau!"),
    ("Alpha", "Blender Principled BSDF Alpha Transparency", "Tingkat ketembusan pandang / transparansi tipis (kayak stiker PNG bolong, daun, jaring kawat, atau hantu).", "1.0 = padat gak tembus; 0.0 = hilang transparan penuh! Di EEVEE pastikan Render Method di Settings diset sesuai kebutuhan."),
    ("Thin Wall", "Blender Principled BSDF Thin Wall glass bubble", "Mode dinding tipis (gelembung sabun / kaca jendela selembar Plane tipis) supaya cahaya kaca gak bengkok berlebihan kayak balok kaca tebal!", "Centang ini kalau lu bikin kaca jendela cuma dari 1 lembar Plane tipis tanpa ketebalan Solidify."),
    ("Normal", "Blender Normal Map Bump Map node tutorial", "Input buat ngasih efek tekstur timbul-kasar palsu (serat kain, pori batu, goresan besi) TANPA nambah berat jumlah poligon!", "Di Shader Editor: colok Image Texture (Non-Color) -> node Normal Map (atau Tekstur Hitam Putih -> node Bump) -> masuk ke lubang Normal ini!"),
    ("Subsurface Weight", "Blender Subsurface Scattering skin wax leaf tutorial", "Efek cahaya menembus masuk lalu berpendar lembut di bawah kulit (wajib buat kulit manusia/telinga kena senter, lilin, giok, susu, daun, atau anggur)!", "Naikkan Subsurface Weight (misal 0.5–1.0) lalu atur Subsurface Scale (misal 0.01m) biar cahayanya merah hangat alami di kulit!"),
    ("Specular IOR Level", "Blender Specular IOR Level Principled BSDF", "Mengatur kekuatan kilap pantulan putih pada benda non-logam.", "Biarkan di angka standar 0.5 untuk 99% benda realistis; turunkan ke 0 kalau mau benda hitam pekat mati tanpa kilap sama sekali."),
    ("Transmission Weight", "Blender Glass Water Material Transmission Principled BSDF", "TOMBOL PEMBUAT KACA & AIR BENING! Mengizinkan sinar cahaya menembus masuk membiaskan isi belakang objek.", "Naikkan Transmission Weight ke **1.0** + turunkan **Roughness ke 0.0** (jadi kaca bening!) atau Roughness 0.25 (jadi kaca es buram)!"),
    ("Coat Weight", "Blender Clear Coat Car Paint Principled BSDF", "Lapisan pernis bening mengkilap di atas permukaan dasar (kayak pernis cat mobil mewah, kayu pelitur basah, atau lantai keramik basah)!", "Naikkan Coat Weight ke 1.0 dengan Coat Roughness kecil (0.03) biar bagian dasarnya bertekstur tapi luarnya tetap kinclong licin!"),
    ("Sheen Weight", "Blender Sheen Velvet Cloth Material Principled BSDF", "Efek kilau halus serabut kain di tepi lipatan (wajib buat kain beludru/velvet, kaos katun, sofa kain, atau debu halus)!", "Naikkan Sheen Weight ke 0.5–1.0 pada material baju/kain supaya lipatan pinggirnya kelihatan lembut kayak kain beneran."),
    ("Emission Color", "Blender Emission Glowing Neon Material tutorial", "Warna cahaya yang dipancarkan sendiri oleh permukaan ini (lampu neon, layar HP, lava pijar, mata robot).", "Pilih warna terangnya di Emission Color, lalu WAJIB naikkan angka **Emission Strength** di bawahnya (kalau 0 belum bakal nyala!)."),
    ("Emission Strength", "Blender Emission Strength Bloom Glare tutorial", "Seberapa terang watt pancaran cahaya dari objek ini.", "Isi 1.0 buat layar TV/HP, atau 5.0–20.0+ buat lampu neon terang yang menyinari benda-benda di sekitarnya!"),
    ("Thin Film Thickness", "Blender Thin Film Iridescence soap bubble oil slick", "Efek warna-warni pelangi tipis ala gelembung sabun, tumpahan oli di aspal, kaca kacamata pantai, atau sayap kumbang!", "Naikkan Thin Film Thickness (misal 300–600 nm) buat memunculkan kilau pelangi fisik otomatis!"),
]


# Panduan Spesifik untuk SEMUA 16 Tipe Object Data (Tab Hijau 'DATA')
OBJECT_DATA_GUIDES: dict[str, dict] = {
    "MESH": {
        "title": "Mesh Data (Jeroan Model Poligon 3D)",
        "en_keyword": "Blender Mesh Object Data Vertex Groups Shape Keys UV Maps",
        "gaul": "Tempat nyimpen data titik-titik model 3D lu: grup seleksi/tulang, ekspresi morphing wajah, peta lipatan gambar tekstur, dan warna titik.",
        "items": [
            ("Vertex Groups", "Blender Vertex Groups Weight Paint tutorial", "Folder penyimpan seleksi titik + bobot tulang! Dipakai buat milih area mana aja yang kena Modifier (kayak rambut, kain Pin Group, Mask, Bevel) atau ketarik tulang."),
            ("Shape Keys", "Blender Shape Keys facial animation tutorial", "Mesin perekam perubahan bentuk (Morphing)! Klik '+' pertama buat 'Basis' (wajah normal), klik '+' kedua ('Key 1') lalu edit senyum/kedip di Edit Mode — tinggal geser Value 0 ke 1!"),
            ("UV Maps", "Blender UV Mapping Unwrap beginner tutorial", "Peta pola jahitan 2D supaya gambar tekstur foto bisa menempel rapi membungkus permukaan 3D tanpa melar gepeng."),
            ("Color Attributes (Vertex Colors)", "Blender Color Attributes Vertex Paint tutorial", "Data cat warna yang langsung disimpan nempel di tiap titik poligon tanpa butuh file gambar luar (hasil lukis di Vertex/Sculpt Paint)."),
            ("Attributes", "Blender Geometry Nodes Mesh Attributes", "Daftar variabel data di tiap titik/garis/poligon (termasuk 'sharp_edge' buat garis tajam atau atribut buatan Geometry Nodes)."),
            ("Texture Space & Remesh", "Blender QuadriFlow Voxel Remesh Object Data", "Tombol Remesh instan (Voxel atau QuadriFlow) buat merapikan ulang jaring poligon hasil Sculpting langsung jadi permanen."),
        ],
    },
    "CAMERA": {
        "title": "Camera Data (Lensa, Zoom, Sensor & Blur Bokeh)",
        "en_keyword": "Blender Camera Settings Focal Length Depth of Field tutorial",
        "gaul": "Semua settingan lensa kamera syuting lu! Pengen gambar kelihatan lebar dramatis atau sinematik ngeblur di belakang subjek? Aturnya di sini!",
        "items": [
            ("Type (Perspective / Orthographic / Panoramic)", "Blender Orthographic vs Perspective Camera Isometric", "Perspective = pandangan mata normal; **Orthographic** = datar tanpa perspektif jauh-dekat (wajib buat bikin kamar **Isometric** imut atau denah 2D!)."),
            ("Focal Length (mm)", "Blender Camera Focal Length 24mm 50mm 85mm", "Ukuran lensa! 18–24mm = lebar dramatis ruangan sempit; 50mm = mata manusia standar; **85–135mm** = potret produk/karakter sinematik ganteng gak distorsi!"),
            ("Clip Start & End", "Blender Camera Clipping Fix disappearing objects", "Batas jarak pandang kamera! Kalau gunung/gedung yang jauh tiba-tiba kepotong hilang di kamera, gedein angka **Clip End** (misal dari 100m jadi 1000m)!"),
            ("Depth of Field (Bokeh Blur)", "Blender Camera Depth of Field Focus Object Aperture F-Stop", "Centang ini buat efek background blur ala kamera mahal! Pilih objek utama di **Focus on Object**, lalu KECILIN angka **F-Stop** (misal 0.5–1.4) biar makin ngeblur bokeh!"),
            ("Viewport Display -> Passepartout & Composition Guides", "Blender Camera Passepartout Rule of Thirds Guides", "Naikin 'Passepartout' ke 0.95 biar luar kotak kamera jadi gelap fokus, & centang 'Thirds' buat garis bantu komposisi fotografi!"),
            ("Background Images", "Blender Camera Background Image Reference", "Nempelin foto sketsa referensi transparan pas di bingkai layar kamera buat nyontek proporsi atau nyamain sudut kamera."),
        ],
    },
    "LIGHT": {
        "title": "Light Data (Jenis Lampu, Watt, Warna & Kelembutan Bayangan)",
        "en_keyword": "Blender Lighting Point Sun Spot Area Light tutorial",
        "gaul": "Pengaturan bola lampu pencahayaan! Beda jenis lampu & ukuran radiusnya bakal ngubah drastis mood adegan 3D lu dari amatir jadi sekelas studio foto!",
        "items": [
            ("Light Type (Point / Sun / Spot / Area)", "Blender 4 Light Types Point Sun Spot Area", "Point = bohlam segala arah; Sun = matahari sejajar seisi dunia; Spot = lampu senter kerucut panggung; **Area** = softbox kotak studio foto (paling cakep buat produk/karakter!)."),
            ("Color & Power / Strength", "Blender Light Power Exposure Temperature", "Atur warna lampu (hangat oranye sore atau biru dingin malam) dan kekuatan terangnya dalam Watt (khusus Sun biasanya cukup angka kecil 1–10 aja!)."),
            ("Radius / Size (Kunci Bayangan Halus!)", "Blender Soft Shadows vs Hard Shadows Light Size", "RAHASIA LIGHTING PRO: Lampu ukuran kecil (0.01m) bikin bayangan tajam keras; gedein **Radius / Size** (misal 1m–3m) biar bayangannya langsung lembut memudar mewah!"),
            ("Spot Shape (Size & Blend) / Area Spread", "Blender Spot Light Cone Blend Area Light Spread", "Pada lampu Spot/Area, 'Blend' melembutkan pinggiran sorotan senter, sedangkan 'Spread' di Area Light memfokuskan cahaya kayak sarang tawon (honeycomb grid) studio!"),
        ],
    },
    "CURVE": {
        "title": "Curve Data (Garis Lengkung, Pipa 3D & Jalur Animasi)",
        "en_keyword": "Blender Bezier Curve Bevel Extrude Pipe Cable tutorial",
        "gaul": "Ngatur garis Bezier/NURBS! Selain buat jalur lintasan, lu bisa langsung ngubah garis tipis ini jadi kabel, pipa, sedotan, atau cetakan list plafon rumah tanpa modifier!",
        "items": [
            ("Shape (2D / 3D, Resolution Preview/Render, Fill Mode)", "Blender 2D vs 3D Curve Fill Mode", "Mode '2D' otomatis menutup bidang datar tertutup (cocok buat logo SVG!); naikin 'Resolution Preview U' biar belokan garisnya mulus gak patah!"),
            ("Geometry -> Extrude & Bevel (Depth / Object / Profile)", "Blender Curve Bevel Depth Cable Pipe Profile", "CARA KILAT BIKIN KABEL/PIPA: Buka bagian **Geometry -> Bevel -> Round**, terus naikin angka **'Depth'**! Centang 'Fill Caps' biar lubang ujung pipanya ketutup!"),
            ("Taper & Bevel Object", "Blender Curve Taper Object stylized hair horn", "Isi 'Taper Object' pakai kurva lain buat bikin pipa yang tebal di pangkal tapi meruncing tajam di ujung (kayak tanduk, akar, atau rambut anime!)."),
            ("Path Animation", "Blender Curve Path Animation Frames", "Pengaturan durasi frame saat kurva ini dipakai sebagai rel lintasan gerak (Follow Path)."),
        ],
    },
    "CURVES": {
        "title": "Hair Curves Data (Sistem Rambut & Bulu Generasi Baru)",
        "en_keyword": "Blender Hair Curves Sculpting Surface UV Map tutorial",
        "gaul": "Objek helai rambut modern Blender! Mengatur ke objek kulit mana akar rambut ini menempel supaya pas karakternya geleng-geleng kepala, rambutnya ikut nempel rapi.",
        "items": [
            ("Surface & Surface UV Map", "Blender Hair Curves Surface Object UV Map warning fix", "WAJIB TERISI: Pilih model kepala/badan di 'Surface' dan pastikan model itu punya 'Surface UV Map' yang rapi supaya modifier rambut bisa jalan tanpa tanda seru error!"),
        ],
    },
    "FONT": {
        "title": "Text / Font Data (Tulisan 3D, Ganti Huruf & Paragraf)",
        "en_keyword": "Blender 3D Text Font Extrude Bevel tutorial",
        "gaul": "Ngubah tulisan ketikan biasa (pencet Tab buat ngetik kata-katanya!) jadi huruf logo 3D tebal mengkilap lengkap sama font custom dari komputer lu!",
        "items": [
            ("Geometry (Extrude & Bevel Depth)", "Blender 3D Text Extrude Bevel Round Corners", "Naikin **'Extrude'** buat ngasih ketebalan 3D ke belakang huruf, terus naikin dikit **'Bevel -> Depth'** biar pinggiran depan hurufnya menonjol manis menangkap cahaya!"),
            ("Font (Regular / Bold / Italic)", "Blender Change Font Custom TTF OTF tutorial", "Klik ikon folder di 'Regular' terus arahin ke `C:\\Windows\\Fonts` (atau file `.ttf` / `.otf` download-an lu) buat ganti gaya huruf!"),
            ("Paragraph & Spacing (Alignment, Character/Word/Line Spacing)", "Blender 3D Text Center Alignment Spacing", "Ganti Horizontal Alignment ke **Center** biar titik tengah huruf pas di tengah-tengah, dan atur jarak renggang antar huruf di Character Spacing."),
        ],
    },
    "ARMATURE": {
        "title": "Armature Data (Pusat Kendali Kerangka Tulang / Rig)",
        "en_keyword": "Blender Armature Pose Rest Position In Front Bone Collections",
        "gaul": "Pengaturan master satu kerangka tulang utuh! Mau tulang kelihatan tembus badan biar gampang diklik, atau mau ngeriset pose karakter jadi patung T-Pose lagi? Di sini tempatnya!",
        "items": [
            ("Pose Position vs Rest Position", "Blender Pose Position vs Rest Position Rigging", "'Pose Position' = pose gerak aktif; klik **'Rest Position'** kalau mau balik sementara ke bentuk patung awal (T-Pose/A-Pose) buat benerin model baju!"),
            ("Bone Collections", "Blender Bone Collections Rigging Layers", "Folder pengelompok tulang modern di Blender 4/5! Pisahin tulang IK, FK, Wajah, dan tulang Deform ke grup masing-masing biar gampang disembunyiin/dimunculin pakai ikon mata!"),
            ("Viewport Display (Display As & In Front!)", "Blender Armature In Front Stick B-Bone Display", "TRIK WAJIB RIGGING: Centang **'In Front'** supaya tulang selalu kelihatan tembus di depan daging badan karakter! Ganti 'Display As' ke B-Bone kalau pakai Bendy Bones."),
        ],
    },
    "GREASEPENCIL": {
        "title": "Grease Pencil Data (Layer Gambar 2D, Onion Skinning & Strokes)",
        "en_keyword": "Blender Grease Pencil v3 Layers Masks Onion Skinning tutorial",
        "gaul": "Studio animasi 2D di dalam ruang 3D! Mirip panel Layer di Photoshop/Procreate lengkap dengan fitur bayangan frame sebelum-sesudah (Onion Skinning) buat animator!",
        "items": [
            ("Layers (Opacity, Blend Mode, Use Lights, Masks)", "Blender Grease Pencil Layers Clipping Mask Use Lights", "Pisahin layer 'Garis Sketsa', 'Tinta Bersih', dan 'Warna Isi'! Matikan 'Use Lights' kalau mau warna gambar 2D cerah murni tanpa terpengaruh gelap-terang lampu 3D."),
            ("Onion Skinning", "Blender Grease Pencil Onion Skinning 2D Animation", "Nampilin bayangan transparan gambar di frame sebelumnya (hijau) & sesudahnya (biru) biar gampang ngegambar gerakan animasi 2D yang mulus!"),
        ],
    },
    "LATTICE": {
        "title": "Lattice Data (Jumlah Titik Kotak Kandang Pembengkok)",
        "en_keyword": "Blender Lattice Resolution U V W Interpolation",
        "gaul": "Ngatur seberapa banyak potongan garis kotak pada kandang karet Lattice lu.",
        "items": [
            ("Resolution U, V, W & Interpolation", "Blender Lattice U V W Points Linear BSpline", "Naikin angka U (kiri-kanan), V (depan-belakang), dan W (atas-bawah) dari 2 ke 3 atau 4 kalau butuh titik tekukan tengah! Pilih BSpline biar lengkungannya mulus."),
        ],
    },
    "META": {
        "title": "Metaball Data (Bola Cairan Lengket Menyatu / Blobs)",
        "en_keyword": "Blender Metaballs Resolution Liquid Blob Modeling",
        "gaul": "Objek unik kayak tetesan air raksa/lendir — begitu dua Metaball dideketin, kulitnya otomatis meleleh nyambung jadi satu bentuk organik!",
        "items": [
            ("Resolution Viewport & Render", "Blender Metaball Resolution Convert to Mesh", "KECILIN angka Resolution Viewport (misal dari 0.2m ke 0.05m) supaya bentuk lelehannya mulus tajam gak kotak-kotak kasar! Klik kanan -> Convert to Mesh kalau udah pas."),
        ],
    },
    "VOLUME": {
        "title": "Volume Data (File OpenVDB Awan, Api & Asap)",
        "en_keyword": "Blender OpenVDB Volume Sequence Import Render",
        "gaul": "Mengatur file volume 3D (.vdb) seperti awan, ledakan api, atau kabut untuk kebutuhan VFX.",
        "items": [
            ("File Path, Sequence & Grids (Density, Flame, Temperature)", "Blender OpenVDB Sequence Grids Density Temperature", "Centang 'Sequence' kalau file VDB lu berupa urutan animasi per-frame, dan atur kepadatan tampilan di Viewport Display."),
        ],
    },
    "LIGHT_PROBE": {
        "title": "Light Probe Data (Penangkap Pantulan & Cahaya Bantu EEVEE)",
        "en_keyword": "Blender EEVEE Light Probes Sphere Plane Volume Bake",
        "gaul": "Alat bantu khusus di mesin EEVEE untuk merekam pantulan cermin akurat (Plane/Sphere Probe) dan sebaran cahaya tidak langsung ruangan (Volume Probe).",
        "items": [
            ("Probe Distance, Resolution & Bake Lighting", "Blender Light Probe Volume Bake Indirect Lighting", "Posisikan kotak Volume Probe melingkupi isi kamar interior lu, lalu klik Bake untuk hasil cahaya pantulan tembok yang lembut dan akurat di EEVEE."),
        ],
    },
    "EMPTY": {
        "title": "Empty Data (Titik Pegangan / Alat Bantu Tak Terlihat Saat Render)",
        "en_keyword": "Blender Empty Object Display As Image Reference",
        "gaul": "Objek hantu serbaguna! Kelihatan di layar kerja buat jadi pegangan induk (Parent), titik fokus kamera, atau foto referensi, TAPI 100% gak bakal kelihatan waktu dirender!",
        "items": [
            ("Display As (Plain Axes, Cube, Sphere, Arrows, Image) & Size", "Blender Reference Image Empty Opacity Orthographic", "Ganti Display As ke 'Image' untuk memasukkan gambar blueprint/sketsa referensi modeling dengan pengaturan Opacity transparan!"),
        ],
    },
    "SPEAKER": {
        "title": "Speaker Data (Sumber Suara 3D Ruang)",
        "en_keyword": "Blender 3D Speaker Sound Attenuation Doppler",
        "gaul": "Pengeras suara 3D di dalam adegan! Kalau kamera menjauh suaranya otomatis mengecil, kalau di sebelah kiri suaranya terdengar di kuping kiri headset!",
        "items": [
            ("Sound Open, Volume, Pitch & Distance Attenuation", "Blender Speaker Object 3D Audio Animation", "Klik 'Open' buat masukin file MP3/WAV, lalu atur Volume dan jarak redamannya (Attenuation) terhadap posisi kamera."),
        ],
    },
    "SURFACE": {
        "title": "Surface NURBS Data (Permukaan Lengkung Matematika Halus)",
        "en_keyword": "Blender NURBS Surface Modeling Resolution",
        "gaul": "Permukaan lengkung berbasis rumus matematika NURBS untuk membuat bodi kapal atau bentuk lengkung mulus.",
        "items": [
            ("Resolution U/V & Endpoint", "Blender NURBS Surface Endpoint U V", "Naikkan Resolution U dan V untuk menghaluskan kelengkungan permukaan, dan centang Endpoint U/V agar tepi menempel ke titik kontrol terluar."),
        ],
    },
    "POINTCLOUD": {
        "title": "Point Cloud Data (Kumpulan Jutaan Titik 3D / LiDAR Scan)",
        "en_keyword": "Blender Point Cloud Render Geometry Nodes",
        "gaul": "Data jutaan titik koordinat di ruang 3D (biasanya dari pemindaian laser 3D LiDAR atau partikel Geometry Nodes) yang langsung bisa dirender super cepat sebagai bola-bola kecil.",
        "items": [
            ("Attributes (radius, color, position)", "Blender Point Cloud Radius Color Attribute", "Gunakan atribut 'radius' dan 'color' di Geometry Nodes / Shader Editor untuk mengatur ukuran dan warna tiap butir titik."),
        ],
    },
}
