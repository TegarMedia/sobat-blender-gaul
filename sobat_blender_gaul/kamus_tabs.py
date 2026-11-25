# SPDX-License-Identifier: GPL-3.0-or-later
"""Panduan Bahasa Indonesia Gaul & Mudah Dipahami Pemula untuk SELURUH 20 Tab Properties Blender."""

from __future__ import annotations

# Tooltip saat kursor hover di ikon Tab sebelah kiri Properties Editor (sebelum diklik!)
TAB_ICON_TOOLTIPS: dict[str, str] = {
    "Active Tool and Workspace settings": (
        "Fungsi: Tempat ngatur settingan 'Alat Aktif' (kuas sculpt, extrude, move, dll) yang lagi lu pegang sekarang.\n"
        "Cara Pakai: Pilih alat di toolbar kiri layar (pencet T), terus atur kekuatan/ukuran/opsinya di tab ini!"
    ),
    "Render Properties": (
        "Fungsi: Ruang mesin utama buat nentuin kualitas gambar/video hasil akhir (pakai EEVEE yang ngebut atau Cycles yang super realistis).\n"
        "Cara Pakai: Pilih Render Engine dulu di paling atas, atur Samples (ketajaman), nyalain Denoise biar gak bintik-bintik!"
    ),
    "Output Properties": (
        "Fungsi: Tempat ngatur ukuran resolusi layar (misal Full HD / 4K), FPS animasi, format file (PNG/MP4), dan folder tempat nyimpen hasil render.\n"
        "Cara Pakai: Atur Resolution X/Y -> pilih Frame Rate -> scroll ke bagian Output buat nentuin lokasi save file sebelum pencet Render!"
    ),
    "View Layer Properties": (
        "Fungsi: Ngatur 'lapisan render' (Render Passes) kayak bayangan terpisah, kabut (Mist), cahaya terpisah, atau garis kartun Freestyle buat diedit lagi di Compositor.\n"
        "Cara Pakai: Centang pass yang lu butuhin (misal Ambient Occlusion, Mist, atau Cryptomatte) kalau mau ngedit hasil render lebih lanjut."
    ),
    "Scene Properties": (
        "Fungsi: Pengaturan dasar satu dunia/adegan lu: kamera mana yang aktif dipakai syuting, satuan ukuran (meter/cm), dan arah gravitasi.\n"
        "Cara Pakai: Buka tab ini kalau mau ganti kamera utama, ngubah ukuran ke Centimeters, atau matiin gravitasi biar objek melayang!"
    ),
    "World Properties": (
        "Fungsi: Ngatur langit, warna background dunia, dan cahaya lingkungan global (HDRI) yang nyinarin seluruh objek dari segala arah.\n"
        "Cara Pakai: Klik titik kuning di samping 'Color' -> pilih 'Environment Texture' buat masukin gambar langit HDRI biar lighting langsung cakep!"
    ),
    "Collection Properties": (
        "Fungsi: Pengaturan khusus buat 'Folder Objek' (Collection) yang lagi aktif dipilih, kayak mau di-render atau cuma jadi bayangan (Holdout).\n"
        "Cara Pakai: Pilih collection di Outliner kanan atas, terus atur visibilitas atau Line Art-nya di sini."
    ),
    "Object Properties": (
        "Fungsi: KTP & posisi objek yang lagi lu klik: koordinat Lokasi (X,Y,Z), Rotasi, Ukuran (Scale), Parent (induk objek), dan tampilan di layar.\n"
        "Cara Pakai: Geser angka Location/Rotation/Scale, atau buka Visibility/Viewport Display kalau mau bikin objek tampil tembus pandang (Wire)!"
    ),
    "Modifier Properties": (
        "Fungsi: SENJATA PALING SAKTI DI BLENDER! Efek otomatis non-permanen buat ngebentuk objek (tumpulin sudut, cermin, tebelin, bolongin, halusin) tanpa ngerusak bentuk asli.\n"
        "Cara Pakai: Klik 'Add Modifier' -> arahin kursor ke nama modifier buat baca fungsinya -> klik pasang -> atur angkanya!"
    ),
    "Particle Properties": (
        "Fungsi: Mesin pembuat ribuan partikel bertebaran (hujan, percikan api, debu, serpihan) atau sistem rambut/rumput klasik.\n"
        "Cara Pakai: Klik tombol '+' buat bikin slot partikel baru -> pilih 'Emitter' (partikel nembak keluar) atau 'Hair' (rambut/rumput nempel)."
    ),
    "Physics Properties": (
        "Fungsi: Laboratorium fisika otomatis! Bikin objek jatuh kena gravitasi (Rigid Body), jadi kain lemes (Cloth), air/asap (Fluid), empuk kayak jelly (Soft Body), atau angin.\n"
        "Cara Pakai: Klik salah satu tombol fisika sesuai efek yang dimau (misal Cloth buat baju + Collision di badan karakternya), terus pencet Spacebar buat play!"
    ),
    "Object Constraint Properties": (
        "Fungsi: 'Aturan main / tali pengikat' otomatis antar objek! Misalnya bikin kamera selalu nengok ke karakter, atau objek nempel ikut jalan di jalur garis.\n"
        "Cara Pakai: Klik 'Add Object Constraint' -> pilih aturan (misal Track To / Copy Location / Follow Path) -> pilih objek Target-nya!"
    ),
    "Object Data Properties": (
        "Fungsi: Isi jeroan terdalam sesuai jenis objek yang lagi lu pilih! Kalau Mesh isinya Vertex Group & UV Map; kalau Kamera isinya Lensa & Blur; kalau Lampu isinya Terang Watt.\n"
        "Cara Pakai: Klik objeknya dulu di 3D Viewport, ikon tab hijau ini bakal otomatis berubah bentuk ngikutin jenis objek lu!"
    ),
    "Bone Properties": (
        "Fungsi: Pengaturan satu batang tulang (Bone) yang lagi lu pilih di Armature: posisi tulang, hubungan induk-anak tulang, lenturnya Bendy Bones, dan kunci pergerakan.\n"
        "Cara Pakai: Pilih satu tulang di Edit Mode atau Pose Mode, terus atur Deform, Relations, atau Bendy Bones di sini."
    ),
    "Bone Constraint Properties": (
        "Fungsi: Aturan gerak otomatis khusus buat TULANG di Pose Mode! Di sinilah tempat pasang IK (Inverse Kinematics) biar kaki/tangan karakter gampang digerakin!\n"
        "Cara Pakai: Masuk ke Pose Mode -> klik satu tulang (misal tulang betis) -> klik 'Add Bone Constraint' -> pilih Inverse Kinematics (IK) atau Copy Rotation."
    ),
    "Material Properties": (
        "Fungsi: Tempat ngasih cat, warna, kilap besi (Metallic), kasar-halus (Roughness), kaca transparan, atau efek nyala lampu (Emission) ke permukaan objek.\n"
        "Cara Pakai: Klik tombol '+ New' -> ganti Base Color buat warna -> geser Metallic & Roughness! Aktifin mode Material Preview (Z) di layar biar kelihatan."
    ),
    "Texture Properties": (
        "Fungsi: Tempat bikin gambar corak/pola (kayak awan Noise, kotak-kotak Checker, atau foto dari komputer) buat dipakai di kuas Sculpt, Displace Modifier, atau Partikel.\n"
        "Cara Pakai: Klik '+ New' -> pilih Type (misal Clouds, Voronoi, atau Image or Movie) -> atur Size/Contrast pola teksturnya."
    ),
    "Visual Effects Properties": (
        "Fungsi: Efek visual instan khusus objek gambar 2D Grease Pencil — kayak efek bersinar (Glow), bayangan jatuh (Shadow), blur, pixelate, atau gelombang!\n"
        "Cara Pakai: Pilih objek Grease Pencil -> klik 'Add Effect' -> pilih efek (misal Glow atau Shadow) -> aktifin mode Render Preview biar langsung kelihatan!"
    ),
    "Strip Properties": (
        "Fungsi: Pengaturan klip video/audio/gambar yang lagi dipilih di Video Editing (Sequencer): posisi, transparansi, kecepatan video, dan volume suara.\n"
        "Cara Pakai: Klik potongan klip (Strip) di timeline Video Sequencer, terus atur Transform, Compositing, atau Sound di sini."
    ),
    "Strip Modifier Properties": (
        "Fungsi: Filter warna & suara non-permanen buat klip video/audio di Video Sequencer (kayak Color Balance, Brightness/Contrast, Curves, atau Equalizer).\n"
        "Cara Pakai: Pilih klip di Video Sequencer -> klik 'Add Strip Modifier' -> pilih efek koreksi warna atau audio yang lu butuhin."
    ),
}


# Panduan lengkap per-tab untuk Panel Interaktif di semua 20 Tab Properties
TAB_GUIDES: dict[str, dict] = {
    "TOOL": {
        "title": "Tab Active Tool & Workspace (Alat Aktif & Ruang Kerja)",
        "en_keyword": "Blender Active Tool and Workspace Properties",
        "gaul_summary": (
            "Tab paling atas ini isinya semua pengaturan buat 'alat' yang lagi lu pegang di tangan kanan sekarang "
            "(misalnya kuas Sculpt, alat Move/Extrude, kuas Texture Paint) plus opsi tampilan ruang kerja."
        ),
        "cara_pakai": (
            "1. Pencet 'T' di 3D Viewport buat munculin deretan ikon alat di kiri.\n"
            "2. Klik salah satu alat (misal Bevel Tool, Loop Cut, atau kuas Clay Strips pas Sculpting).\n"
            "3. Buka tab ini buat ngatur ukuran kuas (Radius), kekuatan (Strength), Symmetry (cermin otomatis), sampai Auto Merge!"
        ),
        "sections": [
            ("Active Tool / Brush Settings", "Blender Active Tool Brush Settings", "Ngatur ukuran (Radius/F), kekuatan (Strength/Shift+F), arah tarik/dorong (+/-), dan tekstur kuas yang lagi aktif."),
            ("Stroke & Falloff", "Blender Brush Stroke Stabilize Falloff", "Ngatur cara tarikan kuas: 'Stabilize Stroke' bikin tarikan tangan gemeteran jadi mulus rapi; 'Falloff' ngatur pinggiran kuas tajam atau lembut."),
            ("Symmetry / Mirror", "Blender Sculpt Mesh Symmetry X Y Z", "Nyalain cermin X/Y/Z biar pas lu ngukir atau ngedit sisi kanan wajah, sisi kirinya otomatis ngikut kembar!"),
            ("Options (Auto Merge / Correct Face Attributes)", "Blender Edit Mode Options Auto Merge Correct Face Attributes", "Auto Merge otomatis ngelem titik yang nempel di posisi sama; Correct Face Attributes ngejaga tekstur UV gak melar pas lu geser titik!"),
            ("Workspace & Add-on Filter", "Blender Workspace Filter Addons", "Bisa nyembunyiin add-on tertentu khusus di workspace ini biar panel kanan (N-Panel) lu gak penuh sesak."),
        ],
    },
    "RENDER": {
        "title": "Tab Render Properties (Mesin Pengolah Gambar Akhir)",
        "en_keyword": "Blender Render Properties EEVEE Cycles settings",
        "gaul_summary": (
            "Ibarat dapur kamera & kartu grafis! Di sini lu nentuin apakah hasil 3D lu mau kelihatan kayak game real-time yang cepet (EEVEE) "
            "atau kayak film bioskop super nyata dengan pantulan cahaya fisik (Cycles)."
        ),
        "cara_pakai": (
            "1. Pilih 'Render Engine': EEVEE (super ngebut, cocok buat animasi/stylized) atau Cycles (super realistis buat kaca/cahaya).\n"
            "2. Kalau pakai Cycles, ganti 'Device' ke 'GPU Compute' biar ngerender pakai VGA (jauh lebih kenceng!).\n"
            "3. Aktifin 'Denoise' di bagian Sampling biar hasil render mulus bebas bintik-bintik semut!"
        ),
        "sections": [
            ("Render Engine (EEVEE / Cycles / Workbench)", "Blender EEVEE vs Cycles Render Engine", "Pilih otak perendernya! EEVEE = cepet instan; Cycles = cahaya & pantulan realistis fisik; Workbench = preview simpel super ringan."),
            ("Sampling (Viewport & Render + Denoise)", "Blender Render Sampling Noise Threshold Denoise", "Max Samples = seberapa teliti cahaya dihitung (makin gede makin bersih tapi lama). Denoise = AI penghilang bintik semut otomatis!"),
            ("Light Paths / Clamping (Cycles) & Raytracing (EEVEE)", "Blender Light Paths Max Bounces Raytracing", "Ngatur berapa kali cahaya mantul di kaca/tembok. Naikin Transmission Bounces kalau kaca lu kelihatan item gelap!"),
            ("Volumes, Curves (Hair), & Simplify", "Blender Render Volumes Curves Simplify", "Ngatur kehalusan asap/kabut, bentuk helai rambut 3D, dan fitur 'Simplify' buat nurunin beban poligon pas ngedit adegan berat."),
            ("Motion Blur & Film (Transparent)", "Blender Motion Blur Film Transparent Background", "Motion Blur bikin objek ngebut ada efek bayangan gerak sinematik. Centang 'Film -> Transparent' kalau mau background bolong transparan (PNG)!"),
            ("Performance & Freestyle", "Blender Render Performance Persistent Data Freestyle", "Centang 'Persistent Data' di Cycles biar render animasi jauh lebih ngebut! Centang 'Freestyle' kalau mau ngasih garis tepi ala komik/anime."),
            ("Color Management (AgX / Filmic / Exposure / Look)", "Blender Color Management AgX Exposure Contrast", "Filter warna terakhir sebelum jadi foto! Pakai View Transform 'AgX' + Look 'Medium High Contrast' biar warna terang gak gosong putih!"),
        ],
    },
    "OUTPUT": {
        "title": "Tab Output Properties (Ukuran Layar, FPS & Simpan File)",
        "en_keyword": "Blender Output Properties Resolution Frame Rate FFmpeg",
        "gaul_summary": (
            "Tempat nentuin spesifikasi file hasil render lu: ukuran piksel (vertikal TikTok/Reels atau horizontal YouTube), "
            "durasi animasi dari frame berapa sampai berapa, kecepatan FPS, dan mau disimpan jadi foto PNG atau video MP4."
        ),
        "cara_pakai": (
            "1. Format: isi Resolution X=1920, Y=1080 (buat YouTube) atau X=1080, Y=1920 (buat TikTok/Shorts), dan Frame Rate (misal 24 atau 30 fps).\n"
            "2. Frame Range: tentuin animasi mulai (Frame Start) dan berhenti (End).\n"
            "3. Output: klik ikon map folder buat milih tempat save, lalu pilih File Format (PNG buat gambar aman, atau FFmpeg Video -> MPEG-4 buat MP4)!"
        ),
        "sections": [
            ("Format (Resolution X/Y, %, Aspect, Frame Rate)", "Blender Output Resolution Frame Rate", "Ukuran kanvas kamera & jumlah gambar per detik (FPS). Slider '%' enak dipakai buat tes render ukuran separuh (50%) biar cepet!"),
            ("Frame Range & Time Stretching", "Blender Frame Range Step Time Stretching", "Batas awal-akhir timeline animasi lu. Step=1 artinya semua frame dirender; Time Stretching bisa bikin efek slow-motion seluruh adegan."),
            ("Stereoscopy (3D VR / Kacamata 3D)", "Blender Stereoscopy 3D Render", "Khusus kalau lu mau bikin video 3D kiri-kanan buat headset VR atau kacamata 3D bioskop."),
            ("Output (File Path, File Format, Color Depth, Video Codec)", "Blender Output File Format PNG OpenEXR FFmpeg MP4", "Tips Emas Pemula: Kalau render animasi panjang, mending pilih 'PNG' dulu baru digabung jadi video, jadi kalau mati lampu gak ngulang dari nol!"),
            ("Metadata & Post Processing", "Blender Output Burn Into Image Compositing Sequencer", "'Burn Into Image' buat nyetak info frame/kamera ke pojok gambar; pastikan 'Compositing' & 'Sequencer' tetap tercentang sesuai kebutuhan."),
        ],
    },
    "VIEW_LAYER": {
        "title": "Tab View Layer Properties (Lapisan Render & Render Passes)",
        "en_keyword": "Blender View Layer Properties Render Passes Cryptomatte",
        "gaul_summary": (
            "Kalau lu mau ngedit hasil render kayak pro di Compositor/After Effects/Photoshop, tab ini gunanya buat misah-misahin informasi gambar "
            "jadi lapisan terpisah: warna doang, bayangan doang, pantulan doang, kedalaman kabut (Z/Mist), sampai seleksi otomatis (Cryptomatte)!"
        ),
        "cara_pakai": (
            "1. Kalau cuma mau render biasa langsung jadi, tab ini gak perlu diutak-atik pun aman!\n"
            "2. Kalau mau nambahin kabut di Compositor, centang 'Passes -> Data -> Mist'.\n"
            "3. Kalau mau gampang ganti warna 1 objek pas post-pro tanpa seleksi manual, centang 'Cryptomatte -> Object / Material'!"
        ),
        "sections": [
            ("View Layer (Use for Rendering & Override)", "Blender View Layer Material Override", "Bisa matiin/nyalain layer ini pas render, atau pasang 'Material Override' buat ngecat seluruh isi scene pakai 1 material (misal clay render putih)!"),
            ("Passes — Data (Combined, Z, Mist, Normal, Vector)", "Blender Render Passes Z Depth Mist Normal", "Ngeluarin data posisi/kedalaman/arah permukaan buat efek Depth of Field, kabut jarak jauh, atau Motion Blur di Compositor."),
            ("Passes — Light (Diffuse, Glossy, Transmission, Emission, AO, Shadow)", "Blender Light Passes Diffuse Glossy Shadow Catcher", "Misahin cahaya langsung, cahaya pantulan, bayangan, dan kilap supaya terangnya bisa diatur ulang tanpa render ulang!"),
            ("Cryptomatte (Object / Material / Asset)", "Blender Cryptomatte Tutorial", "Fitur ajaib buat bikin masker seleksi otomatis yang super rapi sampe ke helai rambut & objek blur di Compositor!"),
            ("Light Groups & AOVs", "Blender Light Groups Shader AOV", "Light Groups bikin lu bisa ngubah warna & terang lampu SETELAH kelar render tanpa nunggu render ulang!"),
            ("Freestyle Line Set & Line Style", "Blender Freestyle Line Set Anime Outline", "Ngatur garis pinggir kartun/sketsa: garis mana yang digambar (Silhouette, Crease, Border), ketebalan, warna, dan gaya goresan kuasnya."),
        ],
    },
    "SCENE": {
        "title": "Tab Scene Properties (Pengaturan Adegan, Satuan Ukuran & Gravitasi)",
        "en_keyword": "Blender Scene Properties Units Gravity Audio",
        "gaul_summary": (
            "Pusat aturan dasar dunia 3D di file lu sekarang: siapa kamera utamanya, pakai ukuran Meter atau Centimeter, "
            "seberapa kenceng tarikan gravitasi bumi, dan pengaturan master suara."
        ),
        "cara_pakai": (
            "1. Punya banyak kamera di scene? Pilih kamera yang mau dipakai render di kolom 'Scene -> Camera'.\n"
            "2. Mau bikin desain produk/arsitektur presisi ukuran cm atau mm? Buka 'Units' -> ganti 'Length' ke Centimeters atau Millimeters!\n"
            "3. Mau simulasi luar angkasa? Matiin centang 'Gravity'!"
        ),
        "sections": [
            ("Scene (Camera, Background Scene, Active Clip)", "Blender Scene Active Camera Background Scene", "Nentuin kamera mana yang aktif pas pencet Numpad 0 / F12, dan bisa numpuk adegan latar (Background Scene) dari scene lain."),
            ("Units (Metric / Imperial, Unit Scale, Length)", "Blender Units Metric Centimeters Millimeters Scale", "Ngatur satuan ukur dunia 3D lu (Meters, Centimeters, Millimeters, atau Inches/Feet) supaya ukuran objek akurat kayak dunia nyata."),
            ("Gravity", "Blender Scene Gravity Physics", "Arah & kekuatan gravitasi global (default Z = -9.8 m/s² ke bawah kayak di Bumi) buat semua simulasi fisika."),
            ("Keying Sets & Audio", "Blender Keying Sets Scene Audio", "Keying Sets nentuin properti apa yang otomatis dikunci pas pencet 'I' buat animasi; Audio ngatur volume global & efek suara 3D Doppler."),
            ("Rigid Body World", "Blender Rigid Body World Cache Speed Substeps", "Pusat kendali simulasi benda keras jatuh/tabrakan buat satu scene penuh: kecepatan waktu simulasi, akurasi Substeps, dan Bake Cache."),
        ],
    },
    "WORLD": {
        "title": "Tab World Properties (Langit, Background & Cahaya HDRI)",
        "en_keyword": "Blender World Properties HDRI Sky Texture Mist",
        "gaul_summary": (
            "Ngatur suasana langit dan lingkungan di sekeliling objek lu! Kalau hasil render lu gelap gulita atau warnanya kusam abu-abu doang, "
            "di sinilah tempat pasang langit cerah (Sky Texture) atau foto lingkungan 360° (HDRI) biar objek langsung kelihatan hidup!"
        ),
        "cara_pakai": (
            "1. Buka panel 'Surface' -> klik bulatan kuning kecil di samping 'Color'.\n"
            "2. Pilih 'Environment Texture' terus klik 'Open' buat masukin file HDRI (.hdr / .exr), ATAU pilih 'Sky Texture' buat langit matahari otomatis!\n"
            "3. Geser angka 'Strength' buat ngatur terangnya cahaya langit tersebut."
        ),
        "sections": [
            ("Surface (Background Color / HDRI / Strength)", "Blender World Environment Texture HDRI Setup", "Cahaya latar dari segala penjuru langit. Pakai HDRI gratis (misal dari Poly Haven) adalah cara tercepat bikin render kelihatan pro!"),
            ("Volume (Volume Scatter / Absorption Kabut Dunia)", "Blender World Volume Scatter Fog God Rays", "Ngasih efek kabut tipis atau debu udara di seluruh dunia 3D biar sorotan lampu kelihatan punya berkas cahaya (God Rays) dramatis!"),
            ("Ray Visibility & Settings (Cycles)", "Blender World Ray Visibility Camera", "Trik rahasia: matiin centang 'Ray Visibility -> Camera' kalau lu mau objek tetep kena pantulan cahaya HDRI tapi background-nya gak ikut kelihatan!"),
            ("Mist Pass & Viewport Display", "Blender World Mist Pass Start Depth", "Ngatur jarak mulai (Start) dan tebal jauhnya (Depth) lapisan kabut Mist Pass untuk Compositor."),
        ],
    },
    "COLLECTION": {
        "title": "Tab Collection Properties (Pengaturan Folder Grup Objek)",
        "en_keyword": "Blender Collection Properties Holdout Shadow Only",
        "gaul_summary": (
            "Collection itu kayak 'Map Folder' di Outliner buat ngelompokkin objek (misal folder Karakter, folder Lampu, folder Properti). "
            "Di tab ini lu bisa ngatur perilaku satu grup penuh sekaligus waktu dirender atau di-link ke file lain!"
        ),
        "cara_pakai": (
            "1. Klik nama Collection di Outliner (pojok kanan atas).\n"
            "2. Atur apakah isi folder ini muncul di Viewports/Renders, atau pakai 'Instance Offset' kalau grup ini mau digandain sebagai aset."
        ),
        "sections": [
            ("Restriction Toggles & Instancing Offset", "Blender Collection Instance Offset", "Ngatur titik pusat (pivot) saat satu Collection dipakai sebagai Collection Instance, serta visibilitas grup di render."),
            ("Line Art Usage", "Blender Collection Line Art Intersection Mask", "Ngatur gimana modifier Line Art ngegambar garis tepi buat semua objek di dalam folder ini (Include, Occlusion Only, atau Exclude)."),
            ("Exporters", "Blender Collection Exporters glTF FBX USD", "Fitur praktis Blender modern buat nyimpen preset export (FBX/glTF/OBJ/USD) langsung nempel ke satu Collection!"),
        ],
    },
    "OBJECT": {
        "title": "Tab Object Properties (Posisi, Ukuran, Induk & Visibilitas Objek)",
        "en_keyword": "Blender Object Properties Transform Relations Visibility",
        "gaul_summary": (
            "Ini kartu identitas (KTP) luar dari objek yang lagi lu klik! Mau geser koordinat angka secara presisi, ngunci sumbu biar gak kegeser, "
            "nyambungin objek anak ke induk (Parent), bikin objek cuma nangkep bayangan (Shadow Catcher), atau bikin tampilannya tembus pandang — semuanya di sini!"
        ),
        "cara_pakai": (
            "1. Panel Transform: ketik angka presisi Location (posisi), Rotation (putar), atau Scale (ukuran).\n"
            "2. Tips Wajib Pemula: Kalau habis gedein/gepengin objek pakai Scale di Object Mode, biasain pencet Ctrl+A -> 'Apply Scale' biar angka Scale balik rapi 1.0!\n"
            "3. Mau bikin objek pemotong Boolean gak ngalangin pandangan? Buka 'Viewport Display' -> ganti 'Display As' jadi 'Wire'!"
        ),
        "sections": [
            ("Transform & Delta Transform", "Blender Object Transform Location Rotation Scale Delta", "Koordinat posisi, rotasi, dan skala objek. Klik ikon gembok di kanannya kalau mau ngunci objek biar gak sengaja kegeser!"),
            ("Relations (Parent, Pass Index)", "Blender Object Parent Relations", "Ngatur siapa 'Induk' (Parent) objek ini — kalau induknya jalan/muter, anaknya otomatis ikut kebawa!"),
            ("Instancing (Vertices / Faces)", "Blender Object Instancing on Vertices Faces", "Ngegandain objek anak ke setiap titik atau permukaan objek ini secara ringan hemat memori."),
            ("Motion Paths (Jejak Lintasan Animasi)", "Blender Object Motion Paths Animation", "Nampilin garis titik-titik lintasan gerak objek di 3D Viewport biar gampang ngecek lengkungan animasi lu udah mulus atau belum."),
            ("Visibility (Viewport, Renders, Shadow Catcher, Holdout, Ray Visibility)", "Blender Shadow Catcher Holdout Ray Visibility", "'Shadow Catcher' bikin lantai transparan tapi tetep nangkep bayangan (buat gabungin 3D ke foto asli!). 'Ray Visibility' bisa bikin lampu/objek tak terlihat di kamera tapi cahayanya ada!"),
            ("Viewport Display (Show Name, Wireframe, Display As, Color)", "Blender Object Viewport Display Wire Bounds", "Ngubah gaya tampilan objek di viewport (Textured, Solid, Wire/rangka kawat, atau Bounds/kotak doang) biar kerja enak & ringan."),
            ("Shading (Light Linking & Shadow Linking)", "Blender Light Linking Shadow Linking", "Fitur pro buat nentuin lampu tertentu CUMA nyinarin objek tertentu aja tanpa kena objek sebelahnya!"),
        ],
    },
    "MODIFIER": {
        "title": "Tab Modifier Properties (Efek Pembentuk Otomatis Paling Penting!)",
        "en_keyword": "Blender Modifiers Complete Beginner Guide",
        "gaul_summary": (
            "INI DIA TAB FAVORIT SEMUA 3D ARTIST! Modifier itu ibarat 'filter/mesin ajaib tumpuk' yang ngubah bentuk objek lu secara otomatis "
            "(bikin cermin simetris, numpulin sudut tajam, mulusin permukaan, nebelin tembok, ngelubangin objek) TANPA ngerusak bentuk aslinya! "
            "Kapan aja bisa dimatiin, diubah angkanya, atau diganti urutannya!"
        ),
        "cara_pakai": (
            "1. Klik objek lu dulu -> klik 'Add Modifier' -> arahin kursor ke kategori (Generate, Deform, Edit, Normals, Physics) buat baca penjelasan gaul tiap modifier!\n"
            "2. Urutan dari ATAS ke BAWAH itu SANGAT NGARUH! Blender ngerjain modifier paling atas dulu, baru hasilnya dilempar ke modifier bawahnya (misal: Mirror dulu di atas, baru Subdivision di bawahnya!).\n"
            "3. Ikon layar kecil = nyala/mati di Viewport; ikon kamera = nyala/mati pas Render; pencet Ctrl+A di atas kotak modifier kalau mau dijadiin permanen (Apply)!"
        ),
        "sections": [
            ("Generate Modifiers (Pembuat & Pengganda Bentuk)", "Blender Generate Modifiers Array Bevel Boolean Mirror Subsurf Solidify", "Bikin geometri baru: Array (baris berderet), Bevel (tumpulin sudut), Boolean (potong/gabung), Mirror (cermin), Solidify (kasih ketebalan), Subdivision Surface (halusin poligon)!"),
            ("Deform Modifiers (Pembengkok & Pengubah Bentuk)", "Blender Deform Modifiers Armature Curve Displace Lattice Shrinkwrap Simple Deform", "Melengkungin atau nempel objek tanpa nambah titik: Simple Deform (plintir/tekuk), Curve (ikut jalur melengkung), Shrinkwrap (nempel ke permukaan lain), Armature (ikut tulang), Displace (timbul pakai tekstur)!"),
            ("Normals Modifiers (Perapi Pantulan Cahaya)", "Blender Smooth by Angle Weighted Normal Modifier", "'Smooth by Angle' & 'Weighted Normal' bikin pantulan cahaya di objek mekanik/hard-surface kelihatan super rapi dan kinclong tanpa belang!"),
            ("Edit Modifiers (Pengolah Data Titik & UV)", "Blender Data Transfer UV Project Vertex Weight Modifiers", "Mindahin normal/UV antar objek (Data Transfer), nembak proyeksi tekstur (UV Project), atau ngatur bobot Vertex Group secara dinamis."),
            ("Physics & Hair Asset Modifiers", "Blender Hair Curves Modifiers Physics Stack", "Modifier simulasi fisika (Cloth, Fluid, Ocean, Collision) dan koleksi modifier rambut modern (Generate/Interpolate/Clump/Curl/Frizz Hair Curves)."),
        ],
    },
    "PARTICLES": {
        "title": "Tab Particle Properties (Mesin Partikel Hujan, Api, Debu & Sebaran)",
        "en_keyword": "Blender Particle System Emitter Hair Tutorial",
        "gaul_summary": (
            "Mesin buat nyemburin ribuan benda kecil dari permukaan objek! Mau bikin hujan turun, percikan las listrik, daun berguguran, "
            "kerumunan burung/ikan (Boids), atau taburan meses di atas donat klasik — semuanya bisa diatur di sini."
        ),
        "cara_pakai": (
            "1. Klik objek pemancar -> klik tombol '+' di pojok kanan atas daftar partikel.\n"
            "2. Pilih 'Emitter' buat partikel yang menyembur/jatuh seiring waktu (pencet Spacebar buat lihat semburannya!), atau 'Hair' buat partikel diam nempel.\n"
            "3. Mau partikelnya berubah jadi bentuk objek 3D (misal batu/daun)? Buka 'Render' -> ganti 'Render As' jadi 'Object' -> pilih objeknya!"
        ),
        "sections": [
            ("Emission (Number, Frame Start/End, Lifetime, Source)", "Blender Particle Emission Lifetime Source", "Ngatur jumlah total partikel (Number), kapan mulai & berhenti keluar (Start/End), dan berapa lama partikel hidup sebelum hilang (Lifetime)."),
            ("Velocity & Rotation", "Blender Particle Velocity Normal Randomize Rotation", "'Normal' di Velocity ngatur seberapa kenceng partikel nyembur keluar dari permukaan; nyalain Rotation + Dynamic kalau mau partikel ikut muter pas mental!"),
            ("Physics (Newtonian, Boids, Fluid, Drag, Brownian)", "Blender Particle Physics Newtonian Boids Brownian", "Newtonian = fisika jatuh biasa; Brownian = gerak acak melayang kayak debu/kunang-kunang; Boids = kecerdasan kawanan burung/ikan yang bisa ngejar musuh!"),
            ("Render (Render As Halo / Object / Collection & Scale)", "Blender Particle Render As Object Collection Scale Randomness", "Ganti bulatan putih standar jadi objek 3D atau satu folder Collection penuh dengan ukuran acak (Scale Randomness)."),
            ("Children (Simple / Interpolated)", "Blender Particle Children Interpolated Clumping", "Trik hemat spek PC: bikin sedikit partikel utama aja, terus nyalain 'Children' buat ngegandain anaknya puluhan kali lipat secara ringan!"),
            ("Field Weights & Vertex Groups", "Blender Particle Field Weights Gravity Density Vertex Group", "Bisa matiin efek Gravity khusus partikel ini biar melayang, atau pakai Vertex Group di 'Density' biar partikel cuma tumbuh di area yang lu lukis!"),
        ],
    },
    "PHYSICS": {
        "title": "Tab Physics Properties (Simulasi Fisika: Kain, Air, Asap, Benda Jatuh & Angin)",
        "en_keyword": "Blender Physics Simulation Rigid Body Cloth Fluid Tutorial",
        "gaul_summary": (
            "Malas ngerjain animasi baju berkibar, gelas pecah jatuh, atau air tumpah secara manual satu-satu? Serahin ke komputer lewat tab Physics! "
            "Tinggal kasih sifat fisika ke objek, pencet Play (Spacebar), dan biarin hukum alam simulasi yang kerja!"
        ),
        "cara_pakai": (
            "1. Benda Keras Jatuh: Klik objek jatuh -> pilih 'Rigid Body' (Type: Active). Klik objek lantai -> pilih 'Rigid Body' (Type: Passive) biar gak ikut terjun ke jurang!\n"
            "2. Kain/Baju: Klik objek kain (pastikan sudah banyak poligon/Subdivide!) -> klik 'Cloth'. Klik objek badan/meja -> klik 'Collision' biar kainnya nyangkut gak tembus!\n"
            "3. Angin: Pencet Shift+A -> Force Field -> Wind, arahin panahnya ke kain/partikel!"
        ),
        "sections": [
            ("Rigid Body & Rigid Body Constraint", "Blender Rigid Body Active Passive Constraint Hinge", "Simulasi benda padat keras (kotak jatuh, rantai besi, engsel pintu, mobil tabrakan). Active = ikut jatuh gerak; Passive = diam jadi penahan/lantai."),
            ("Cloth (Simulasi Kain, Bendera, Baju & Bantal)", "Blender Cloth Simulation Pin Group Self Collisions", "Ubah mesh jadi kain! Pakai ikon 'Presets' di kanan atas Cloth buat milih bahan (Cotton, Silk, Leather, Denim), nyalain 'Self Collisions' biar kain gak tembus dirinya sendiri, & pakai 'Pressure' buat bikin bantal gembung!"),
            ("Soft Body (Benda Kenyal / Jelly / Per)", "Blender Soft Body Simulation Goal Edges", "Bikin objek membal kenyal kayak agar-agar, perut goyang, atau antena goyang. Matiin 'Goal' kalau mau objeknya ikut jatuh bebas."),
            ("Fluid (Asap, Api & Cairan Air Mantaflow)", "Blender Fluid Simulation Domain Flow Liquid Smoke Fire", "Butuh minimal 2 objek: 1 kotak gede pembungkus dikasih Fluid Type 'Domain' (Gas/Liquid), dan 1 objek pemancar di dalamnya dikasih Fluid Type 'Flow' (Smoke/Fire/Liquid Inflow)!"),
            ("Collision (Penahan Tumbukan)", "Blender Collision Physics Thickness Outer", "Wajib dipasang ke objek meja/lantai/badan supaya kain (Cloth), Soft Body, dan Partikel bisa mental atau nyangkut di permukaannya."),
            ("Dynamic Paint (Cat Basah, Jejak Kaki di Salju & Riak Air)", "Blender Dynamic Paint Canvas Brush Waves Displace", "Satu objek jadi 'Canvas' (lantai salju/tembok), objek lain jadi 'Brush' (sepatu/bola) — pas bersentuhan otomatis ninggalin cat atau jejak penyok!"),
            ("Force Field (Angin, Pusaran Vortex, Turbulence)", "Blender Force Fields Wind Turbulence Vortex", "Sumber gaya tak kasat mata buat niup kain, asap, dan partikel biar berkibar atau berputar keren!"),
        ],
    },
    "CONSTRAINT": {
        "title": "Tab Object Constraint Properties (Tali Aturan Otomatis Antar Objek)",
        "en_keyword": "Blender Object Constraints Track To Follow Path Child Of",
        "gaul_summary": (
            "Constraint itu kayak 'peraturan otomatis' buat ngendaliin gerak/rotasi/ukuran objek berdasarkan objek lain! "
            "Contoh paling sering dipakai: bikin kamera selalu nengok ke wajah karakter kemanapun dia lari, atau bikin mobil jalan ngikutin garis jalan raya."
        ),
        "cara_pakai": (
            "1. Klik objek yang mau diatur (misalnya Kamera) -> klik 'Add Object Constraint'.\n"
            "2. Pilih jenis aturannya (misal 'Damped Track' atau 'Track To' buat nengok ke target, atau 'Child Of' buat digenggam tangan).\n"
            "3. Isi kolom 'Target' pakai pipet ke objek sasaran! Slider 'Influence' (0–1) bisa dianimasiin buat nyalain/lepasin ikatannya kapan aja!"
        ),
        "sections": [
            ("Transform Constraints (Copy Location / Rotation / Scale / Limit)", "Blender Copy Location Rotation Limit Constraints", "Niru posisi/putaran objek lain atau masang pagar batas (Limit) supaya pintu/laci gak bisa dibuka kelewat batas!"),
            ("Tracking Constraints (Damped Track, Track To, Stretch To)", "Blender Damped Track vs Track To Camera Target", "Bikin kamera, mata, atau lampu sorot selalu ngelirik tepat ke arah objek Target secara otomatis."),
            ("Relationship Constraints (Child Of, Follow Path, Floor, Shrinkwrap)", "Blender Child Of Follow Path Constraint Tutorial", "'Child Of' = cara paling bener bikin karakter mungut terus ngelempar barang (Influence 1 pas dipegang, 0 pas dilepas!). 'Follow Path' = jalan di sepanjang garis Curve."),
            ("Motion Tracking Constraints (Camera Solver / Object Solver)", "Blender Camera Solver Constraint VFX", "Dipakai buat VFX gabungin objek 3D ke rekaman video HP/kamera asli hasil tracking."),
        ],
    },
    "DATA": {
        "title": "Tab Object Data Properties (Jeroan Spesifik Sesuai Jenis Objek!)",
        "en_keyword": "Blender Object Data Properties Vertex Groups Shape Keys UV Maps Camera Light",
        "gaul_summary": (
            "Ikon tab warna HIJAU ini bunglon — bentuk dan isinya otomatis berubah sesuai objek apa yang lagi lu klik! "
            "Klik Mesh muncul Vertex Groups/Shape Keys/UV Maps; klik Kamera muncul Lensa & Blur (DOF); klik Lampu muncul Watt & Warna; klik Teks muncul Font & Ketebalan 3D!"
        ),
        "cara_pakai": (
            "1. Klik objeknya dulu di layar 3D.\n"
            "2. Kalau Mesh: pakai 'Vertex Groups' buat nyimpen seleksi titik, 'Shape Keys' buat ekspresi wajah kedip/senyum, dan 'UV Maps' buat peta tekstur.\n"
            "3. Kalau Kamera: atur 'Focal Length' (makin gede mm-nya makin zoom sinematik!) dan nyalain 'Depth of Field' buat background bokeh/blur!"
        ),
        "sections": [
            ("Mesh Data (Vertex Groups, Shape Keys, UV Maps, Color Attributes, Normals)", "Blender Vertex Groups Shape Keys UV Maps Explained", "Pusat data titik model 3D: Vertex Groups (grup bobot tulang/modifier), Shape Keys (animasi perubahan bentuk/wajah), & UV Maps (kulit tekstur 2D)."),
            ("Camera Data (Focal Length, Sensor, Clip Start/End, Depth of Field)", "Blender Camera Focal Length Depth of Field Clip End", "Atur zoom lensa (50mm standar, 85mm+ potret sinematik), naikin 'Clip End' kalau pemandangan jauh kepotong hilang, & aktifin 'Depth of Field' buat efek blur kamera DSLR!"),
            ("Light & Light Probe Data (Point, Sun, Spot, Area — Power, Color, Radius)", "Blender Lighting Power Radius Soft Shadows Tutorial", "Power = terangnya lampu; Radius/Size = makin lebar ukuran lampunya, bayangannya makin halus lembut (soft shadow)!"),
            ("Curve, Hair Curves & Text/Font Data (Resolution, Extrude, Bevel, Font)", "Blender Curve Bevel Extrude 3D Text Font", "Di Curve/Text, cukup naikin 'Geometry -> Extrude' & 'Bevel Depth' buat nyulap garis tipis atau tulisan 2D langsung jadi pipa/huruf 3D bervolume!"),
            ("Armature & Grease Pencil Data (Pose/Rest Position, Bone Collections, Layers)", "Blender Armature Pose Rest Position Grease Pencil Layers", "Di Armature bisa ganti tampilan tulang (Octahedral/Stick/B-Bone) & nyalain 'In Front' biar tulang kelihatan tembus badan; di Grease Pencil tempat ngatur Layer gambar 2D."),
        ],
    },
    "BONE": {
        "title": "Tab Bone Properties (Pengaturan Satu Tulang Rigging)",
        "en_keyword": "Blender Bone Properties Deform Bendy Bones Relations",
        "gaul_summary": (
            "Muncul khusus waktu lu lagi milih objek tulang (Armature)! Kalau tab hijau Armature ngatur satu kerangka utuh, "
            "tab gambar satu tulang ini ngatur spesifik SATU batang tulang yang lagi lu klik sekarang."
        ),
        "cara_pakai": (
            "1. Masuk Edit Mode atau Pose Mode di Armature, lalu klik satu tulang.\n"
            "2. Kalau tulang itu cuma buat tombol pegangan (Controller/IK Target) dan BUKAN buat narik daging kulit, matiin centang 'Deform'!\n"
            "3. Mau tulang melengkung lentur kayak kartun? Naikin 'Bendy Bones -> Segments' (dan ganti tampilan Armature ke B-Bone)!"
        ),
        "sections": [
            ("Transform & Lock (Pose Mode)", "Blender Pose Bone Transform Lock", "Posisi/rotasi tulang saat Pose Mode, lengkap sama gembok sumbu biar animator gak salah putar arah engsel tulang."),
            ("Bendy Bones (Segments, Curve In/Out)", "Blender Bendy Bones Rigging Tutorial", "Memecah 1 batang tulang jadi banyak ruas lentur mulus — enak banget buat tulang punggung, ekor, tentakel, atau alis kartun!"),
            ("Relations (Parent, Connected, Inherit Rotation/Scale)", "Blender Bone Parent Connected Inherit Scale", "Ngatur induk tulang ini, apakah ujungnya nempel nyambung (Connected), dan apakah ikut membesar kalau induknya di-scale."),
            ("Deform & Inverse Kinematics Limits", "Blender Bone Deform Envelope IK Stretch Lock", "Matikan centang 'Deform' buat tulang kontrol bantu! Di bagian IK lu juga bisa ngunci arah tekukan lutut/siku biar gak patah ke belakang."),
            ("Viewport Display (Custom Object Shape / Warna Tulang)", "Blender Bone Custom Shape Color Rigging", "Ubah tampilan tulang runcing standar jadi bentuk lingkaran/panah keren pakai 'Custom Object' & kasih warna biar rig gampang dibaca!"),
        ],
    },
    "BONE_CONSTRAINT": {
        "title": "Tab Bone Constraint Properties (IK & Otomatisasi Gerak Tulang!)",
        "en_keyword": "Blender Bone Constraints Inverse Kinematics IK Tutorial",
        "gaul_summary": (
            "Rahasia utama kenapa karakter 3D bisa digerakin gampang kayak boneka! Tab ini cuma aktif kalau lu lagi di **Pose Mode** pada tulang (Armature). "
            "Di sinilah tempat masang **Inverse Kinematics (IK)** biar pas telapak kaki/tangan ditarik, paha dan betisnya otomatis nekuk sendiri!"
        ),
        "cara_pakai": (
            "1. Klik Armature -> pindah dari Object Mode ke **Pose Mode** (Ctrl+Tab).\n"
            "2. Klik tulang yang mau dikasih aturan (misal tulang betis bawah) -> klik 'Add Bone Constraint' -> pilih 'Inverse Kinematics'.\n"
            "3. Pilih Armature di Target, pilih tulang kontrol kaki di Bone, dan isi 'Chain Length = 2' (biar cuma betis + paha yang ikut nekuk, gak sampe kepala!)."
        ),
        "sections": [
            ("Inverse Kinematics (IK) & Pole Target", "Blender Inverse Kinematics Chain Length Pole Angle", "Wajib isi 'Chain Length' (jumlah tulang yang ikut nekuk)! Isi 'Pole Target' buat ngarahin dengkul/siku menghadap ke mana (atur Pole Angle kalau melintir)."),
            ("Copy Rotation / Location / Transforms (Target Space: Local Space!)", "Blender Bone Constraint Local Space vs World Space", "Tips Penting Rigging: Saat niru putaran antar tulang (misal jari tangan mengepal bareng), ganti Target & Owner Space dari 'World Space' ke 'Local Space'!"),
            ("Damped Track, Stretch To, & Spline IK", "Blender Bone Damped Track Stretch To Spline IK", "Damped Track buat tulang mata ngelirik target; Stretch To buat efek squash-and-stretch kartun; Spline IK buat ekor/tali ngikut kurva."),
        ],
    },
    "MATERIAL": {
        "title": "Tab Material Properties (Cat Warna, Besi, Kaca, Kulit & Cahaya Objek)",
        "en_keyword": "Blender Material Properties Principled BSDF Beginner Tutorial",
        "gaul_summary": (
            "Tempat dandanin permukaan objek 3D lu! Mau dibikin kayak plastik doff, besi krom mengkilap, emas, air bening, kaca buram, "
            "kulit manusia tembus cahaya, atau neon menyala — semuanya tinggal geser slider di Principled BSDF di sini!"
        ),
        "cara_pakai": (
            "1. Pencet tombol 'Z' di 3D Viewport -> pilih 'Material Preview' atau 'Rendered' dulu biar warnanya kelihatan!\n"
            "2. Klik '+ New' -> ganti 'Base Color' buat warna dasar.\n"
            "3. Rumus Cepat: Besi/Emas = naikin 'Metallic' ke 1.0 + kecilin 'Roughness'! Plastik Mengkilap = Metallic 0 + Roughness kecil (0.1)! Kaca Bening = naikin 'Transmission Weight' ke 1.0 + Roughness 0!"
        ),
        "sections": [
            ("Material Slots (+ / - / Assign di Edit Mode)", "Blender Assign Multiple Materials One Object", "Satu objek bisa punya BANYAK warna! Tambah slot pakai ikon '+', masuk Edit Mode, pilih face yang mau dibedain warnanya, klik slotnya lalu klik 'Assign'!"),
            ("Surface — Principled BSDF (Base Color, Metallic, Roughness, IOR, Alpha)", "Blender Principled BSDF Metallic Roughness IOR Alpha", "Base Color = warna cat; Metallic = 0 non-logam / 1 logam; Roughness = 0 licin kayak cermin / 1 kasar buram kayak kapur; Alpha = transparansi tipis."),
            ("Subsurface, Transmission, Coat, Sheen & Emission", "Blender Subsurface Transmission Coat Sheen Emission", "Subsurface = efek cahaya tembus daging/lilin/daun; Transmission = kaca/air tembus pandang; Coat = lapisan pernis cat mobil; Sheen = kain beludru; Emission = nyala bersinar!"),
            ("Volume & Displacement", "Blender Material Displacement Bump Only vs Displacement and Bump", "Ngatur isi volume objek (asap/air keruh) dan apakah tekstur tinggi-rendah beneran menonjolkan poligon (Displacement and Bump di Cycles)."),
            ("Settings & Viewport Display (Backface Culling, Render Method)", "Blender Material Blended vs Dithered Backface Culling", "Ngatur metode transparansi (Dithered vs Blended di EEVEE modern), bayangan, dan warna preview material saat di mode Solid."),
        ],
    },
    "TEXTURE": {
        "title": "Tab Texture Properties (Katalog Pola Tekstur Kuas, Displace & Partikel)",
        "en_keyword": "Blender Texture Properties Brush Displace Noise Voronoi",
        "gaul_summary": (
            "Catatan Penting Pemula: Buat ngasih gambar tekstur ke warna/material objek, sekarang pakainya **Shader Editor** (atau klik titik kuning di tab Material), BUKAN di sini! "
            "Tab papan catur merah-putih ini khusus buat bikin tekstur yang dipakai sama **Displace Modifier**, **Kuas Sculpt/Paint**, atau **Partikel**!"
        ),
        "cara_pakai": (
            "1. Misalnya lu habis pasang 'Displace Modifier' buat bikin tanah berbukit -> buka tab Texture ini -> klik '+ New'.\n"
            "2. Ganti 'Type' dari 'Image or Movie' ke 'Clouds' atau 'Voronoi' buat pola gunung alami, atau klik 'Open' buat masukin foto hitam-putih (Heightmap)!\n"
            "3. Atur 'Size' di bagian Mapping/Noise buat ngecilin atau nggedein lebar gelombang teksturnya."
        ),
        "sections": [
            ("Texture Slot Selector (Brush / Modifier / Particle)", "Blender Texture Context Selector Displace Brush", "Pilih dulu di paling atas tekstur ini mau dipakai buat siapa: apakah buat Kuas (Brush), Displace Modifier, atau Partikel."),
            ("Procedural Textures (Clouds, Noise, Voronoi, Musgrave/Stucci, Wood, Marble)", "Blender Procedural Textures Clouds Voronoi Marble", "Tekstur matematika otomatis buatan Blender yang tajam tanpa pecah buat bikin permukaan batu, keriput, air, atau kayu."),
            ("Image or Movie & Colors (Ramp / Brightness / Contrast)", "Blender Texture Color Ramp Contrast Displace", "Masukin gambar hitam-putih dari komputer (putih = menonjol naik, hitam = cekung turun) dan atur tajam kontrasnya pakai Color Ramp!"),
        ],
    },
    "SHADERFX": {
        "title": "Tab Visual Effects Properties (Efek Keren Khusus Grease Pencil 2D/3D)",
        "en_keyword": "Blender Grease Pencil Visual Effects Glow Shadow Blur",
        "gaul_summary": (
            "Tab tongkat sihir ini muncul khusus waktu lu ngeklik objek gambar **Grease Pencil**! "
            "Isinya efek kamera instan kayak sinar neon (Glow), bayangan jatuh (Shadow), lampu tepi (Rim Light), sensor kotak-kotak (Pixelate), sampai gelombang air!"
        ),
        "cara_pakai": (
            "1. Pilih objek Grease Pencil -> pindah tampilan layar ke 'Rendered' (pencet Z -> Rendered) supaya efeknya aktif kelihatan!\n"
            "2. Klik 'Add Effect' -> pilih misal 'Glow' buat efek pedang cahaya/sihir, atau 'Rim' buat highlight pinggir karakter anime!\n"
            "3. Geser warna, ukuran blur, dan Blend Mode (misal 'Add' buat Glow biar makin terang menyala)."
        ),
        "sections": [
            ("Glow & Rim Effect", "Blender Grease Pencil Glow Rim Effect Tutorial", "Glow bikin goresan bersinar neon (bisa difilter cuma warna tertentu aja yang nyala!); Rim nambahin cahaya pinggir dramatis ala anime."),
            ("Shadow & Blur Effect", "Blender Grease Pencil Shadow Depth of Field Blur", "Shadow bikin bayangan 2D otomatis yang bisa diarahin pakai objek lampu/empty; Blur bikin objek Grease Pencil ngeblur lembut (bisa ikut fokus kamera!)."),
            ("Colorize, Pixelate, Swirl, Wave & Flip", "Blender Grease Pencil Pixelate Wave Distortion Effect", "Ubah goresan jadi ala game retro 8-bit (Pixelate), sepia/duotone (Colorize), pusaran (Swirl), atau bergelombang kena angin/air (Wave)!"),
        ],
    },
    "STRIP": {
        "title": "Tab Strip Properties (Pengaturan Klip Video/Suara di Video Sequencer)",
        "en_keyword": "Blender Video Sequencer Strip Properties Transform Speed",
        "gaul_summary": (
            "Muncul pas lu lagi ngedit video di Video Sequencer! Mengatur posisi gambar klip, potong pinggir (Crop), transparansi (Opacity), "
            "blend mode, kecepatan pemutaran, sampai volume dan pitch suara."
        ),
        "cara_pakai": (
            "1. Klik salah satu batang klip (Strip) di timeline Video Sequencer.\n"
            "2. Buka bagian 'Transform' buat geser/zoom posisi video, 'Compositing' buat Opacity fade-in/out, atau 'Sound' buat gedein suara & nyalain 'Display Waveform'!"
        ),
        "sections": [
            ("Compositing & Transform (Blend, Opacity, Position, Scale, Rotation, Crop)", "Blender VSE Strip Transform Crop Opacity", "Ngatur cara klip numpuk di atas klip bawahnya, geser posisi X/Y, perbesar/perkecil video, dan potong tepiannya."),
            ("Video, Time & Sound (Strobe, Reverse, Volume, Pitch, Waveform)", "Blender VSE Reverse Video Audio Waveform Volume", "Centang 'Reverse Frames' buat muter video mundur; centang 'Display Waveform' di klip suara biar gelombang suaranya kelihatan gampang dipotong pas ketukan musik!"),
            ("Proxy & Timecode", "Blender VSE Proxy Render Smooth Playback", "Kalau preview edit video 4K patah-patah ngelag, aktifin Proxy 25% atau 50% biar muternya langsung enteng licin!"),
        ],
    },
    "STRIP_MODIFIER": {
        "title": "Tab Strip Modifier Properties (Filter Warna & Suara di Video Editing)",
        "en_keyword": "Blender VSE Strip Modifiers Color Balance Curves Equalizer",
        "gaul_summary": (
            "Mirip Modifier objek 3D, tapi khusus buat potongan video atau audio di Video Sequencer! "
            "Dipakai buat color grading (terangin video gelap, benerin warna kuning/biru, naikin kontras) atau ngerapiin frekuensi suara (Equalizer/Echo)."
        ),
        "cara_pakai": (
            "1. Pilih klip video atau audio di Video Sequencer.\n"
            "2. Klik 'Add Strip Modifier' -> pilih 'Curves' / 'Color Balance' / 'White Balance' buat video, atau 'Sound Equalizer' buat audio!"
        ),
        "sections": [
            ("Color Grading Modifiers (Color Balance, Curves, Brightness/Contrast, White Balance, Hue Correct, Tone Map)", "Blender VSE Color Grading Modifiers Tutorial", "Koreksi warna gelap/terang (Lift/Gamma/Gain) dan suasana warna video tanpa ngerusak file rekaman asli."),
            ("Compositor & Mask Strip Modifiers", "Blender VSE Compositor Strip Modifier Mask", "Masukin node Compositor langsung ke klip VSE atau bolongin sebagian area video pakai Mask!"),
            ("Audio Strip Modifiers (Sound Equalizer, Pitch, Echo)", "Blender VSE Sound Equalizer Pitch Echo", "Perjelas suara vokal, ubah tinggi-rendah nada suara, atau tambah gema tanpa perlu keluar dari Blender."),
        ],
    },
}
