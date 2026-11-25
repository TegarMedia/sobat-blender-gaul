# SPDX-License-Identifier: GPL-3.0-or-later
"""Universal RNA, Operator, Enum & Asset Gaul Tooltip Compiler untuk Blender 5.2."""

from __future__ import annotations

import re
import bpy

from .asset_tooltips import ASSET_AND_BRUSH_DESCS
from .kamus_constraints_physics import CONSTRAINT_CATALOG, SHADERFX_CATALOG
from .kamus_modifiers import ASSET_MODIFIER_CATALOG, MODIFIER_CATALOG, MODIFIER_PROP_TOOLTIPS
from .kamus_tabs import TAB_ICON_TOOLTIPS

DOMAIN_NAME = "sobat_blender_gaul_i18n"
_IS_REGISTERED = False
_SAVED_PREFS: dict[str, object] = {}
_COMPILED_CACHE: dict[str, str] = {}

FOOTER_HINT = "💡 Klik Kanan tombol ini -> Cari Video YouTube / Google (Keyword Inggris)"

# Curated high-frequency tooltips across Render, Output, Object, Camera, Light, Mesh, Material, Physics, Tools
CURATED_CORE_TOOLTIPS: dict[str, str] = {
    # Transform & Object
    "Location of the object": (
        "Fungsi: Posisi koordinat objek (Kiri-Kanan X, Depan-Belakang Y, Atas-Bawah Z) di ruang 3D.\n"
        "Cara Pakai: Geser angkanya atau pencet 'G' di layar 3D buat mindahin objek (Alt+G buat balikin ke titik tengah 0,0,0!)."
    ),
    "Rotation in Eulers": (
        "Fungsi: Sudut kemiringan/putaran objek dalam satuan derajat pada sumbu X, Y, dan Z.\n"
        "Cara Pakai: Geser angkanya atau pencet 'R' di layar 3D buat muter objek (Alt+R buat ngeriset putaran balik tegak!)."
    ),
    "Scaling factor in X, Y, and Z": (
        "Fungsi: Ukuran besar-kecilnya skala objek pada sumbu X, Y, dan Z (standar normal = 1.0).\n"
        "Cara Pakai: Habis ubah ukuran di Object Mode, biasain pencet Ctrl+A -> 'Scale' biar modifier kayak Bevel gak miring gepeng!"
    ),
    "Parent object": (
        "Fungsi: Menentukan siapa 'Induk' dari objek ini — kalau induknya pindah/muter, objek anak otomatis ikut terbawa!\n"
        "Cara Pakai: Pilih nama objek induk di sini, atau di layar 3D pilih Anak dulu -> Shift+Klik Induk -> pencet Ctrl+P!"
    ),
    "Make object only catch shadows to be composited onto another footage": (
        "Fungsi: Shadow Catcher (Cycles) — bikin objek lantai jadi transparan tak terlihat, TAPI tetep nangkep bayangan gelap di atasnya!\n"
        "Cara Pakai: Centang ini di objek lantai waktu lu mau nempelin objek 3D ke atas foto/video dunia nyata!"
    ),
    "Render objects as a holdout or matte, creating a hole in the image with zero Alpha": (
        "Fungsi: Holdout — menyulap objek ini jadi 'pembolong hitam transparan' (Alpha 0) buat nutupin objek di belakangnya.\n"
        "Cara Pakai: Centang ini (pastikan Film -> Transparent juga aktif!) buat teknik compositing menaruh objek 3D di balik tiang video asli."
    ),
    "Display the object as a wireframe, solid, textured or just bounds": (
        "Fungsi: Mengatur gaya tampilan objek ini khusus di layar kerja (tanpa mengubah hasil Render akhir!).\n"
        "Cara Pakai: Ganti ke 'Wire' pada objek pemotong Boolean supaya lu bisa ngelihat tembus ke bagian lubang di dalamnya!"
    ),

    # Render & Sampling
    "Engine to use for rendering": (
        "Fungsi: Memilih mesin pengolah gambar utama: EEVEE (cepat real-time) atau Cycles (cahaya pantul fisik super realistis).\n"
        "Cara Pakai: Pakai EEVEE buat kerja cepat/stylized, atau pilih Cycles (+ Device GPU Compute) buat hasil kaca & cahaya kelas film!"
    ),
    "Device to use for rendering": (
        "Fungsi: Menentukan apakah proses render Cycles dikerjakan oleh prosesor (CPU) atau kartu grafis (GPU Compute).\n"
        "Cara Pakai: Ganti ke 'GPU Compute' kalau laptop/PC lu punya VGA (NVIDIA RTX/GTX, AMD, Apple Silicon) biar render berkali-kali lebih ngebut!"
    ),
    "Number of samples to render for each pixel": (
        "Fungsi: Jumlah perhitungan titik cahaya per piksel — makin besar angkanya gambar makin halus tajam, tapi waktu render makin lama!\n"
        "Cara Pakai: Di Cycles cukup isi 128–512 bareng fitur Denoise aktif; di EEVEE cukup 64–128 udah mulus banget!"
    ),
    "Denoise the rendered image": (
        "Fungsi: Penghilang bintik-bintik semut kasar (noise) otomatis pakai kecerdasan AI sesudah render selesai!\n"
        "Cara Pakai: WAJIB DICENTANG di Cycles supaya walaupun pakai Samples rendah, hasil fotonya langsung mulus bening!"
    ),
    "World background is transparent, for compositing the render over another background": (
        "Fungsi: Film Transparent — menghapus langit background jadi bolong transparan kotak-kotak catur!\n"
        "Cara Pakai: Centang ini + simpan hasil render pakai format 'PNG' (Color: RGBA) biar dapet gambar objek tanpa background!"
    ),
    "Simulate shutter blur for moving objects and camera": (
        "Fungsi: Motion Blur — memberi efek buram gerakan alami pada benda/roda yang bergerak cepat seperti di kamera film asli.\n"
        "Cara Pakai: Centang ini saat render animasi supaya gerakan cepat terasa mulus sinematik dan gak kaku patah-patah."
    ),
    "Keep render data around for faster re-renders and animation renders, at the cost of increased memory usage": (
        "Fungsi: Persistent Data — menyimpan tekstur & geometri tetap di memori VGA supaya gak perlu loading ulang tiap ganti frame animasi!\n"
        "Cara Pakai: Centang ini waktu mau render animasi banyak frame di Cycles biar hemat waktu drastis!"
    ),

    # Output
    "Number of horizontal pixels in the rendered image": (
        "Fungsi: Resolution X — lebar mendatar gambar/video hasil render dalam satuan piksel.\n"
        "Cara Pakai: Isi 1920 buat Full HD mendatar (YouTube), 1080 buat vertikal (TikTok/Reels/Shorts), atau 3840 buat 4K!"
    ),
    "Number of vertical pixels in the rendered image": (
        "Fungsi: Resolution Y — tinggi tegak gambar/video hasil render dalam satuan piksel.\n"
        "Cara Pakai: Isi 1080 buat Full HD mendatar (1920x1080), atau 1920 buat video vertikal HP (1080x1920)!"
    ),
    "Percentage scale for render resolution": (
        "Fungsi: Skala persentase ukuran resolusi render (100% = ukuran penuh sesuai X & Y di atas).\n"
        "Cara Pakai: Turunin ke 50% waktu lagi ngetes cahaya/animasi biar proses rendernya 4x lebih cepat!"
    ),
    "Directory/name to save animations, # characters define the position and padding of frame numbers": (
        "Fungsi: Lokasi folder & nama file di komputer tempat Blender menyimpan hasil render animasi lu.\n"
        "Cara Pakai: Klik ikon map folder di kanan -> pilih folder tujuan lu sebelum pencet Render Animation (Ctrl+F12)!"
    ),
    "File format to save the rendered images as": (
        "Fungsi: Format penyimpanan hasil render (PNG, JPEG, OpenEXR, atau FFmpeg Video buat MP4).\n"
        "Cara Pakai: Pilih 'PNG' buat foto (atau urutan gambar animasi yang aman anti gagal mati lampu), atau 'FFmpeg Video' buat langsung jadi video!"
    ),

    # Camera & Light
    "Perspective Camera focal length value in millimeters": (
        "Fungsi: Focal Length — ukuran zoom lensa kamera dalam milimeter (persis lensa kamera DSLR/Mirrorless asli!).\n"
        "Cara Pakai: 24mm = sudut lebar dramatis; 50mm = normal mata manusia; 85mm–135mm = fokus tele sinematik cakep buat produk/wajah!"
    ),
    "Use Depth of Field": (
        "Fungsi: Mengaktifkan efek fokus lensa kamera dimana subjek utama tajam tapi background di belakangnya ngeblur lembut (Bokeh)!\n"
        "Cara Pakai: Centang kotak ini -> buka panahnya -> pilih subjek utama di 'Focus on Object' -> kecilin angka 'F-Stop' (misal 0.5–1.4)!"
    ),
    "F-Stop ratio (lower numbers give more defocus, higher numbers give a sharper image)": (
        "Fungsi: Bukaan diafragma lensa (F-Stop) penentu seberapa kuat blur background kamera (Depth of Field).\n"
        "Cara Pakai: Makin KECIL angkanya (misal 0.3–1.4), background makin NGEBLUR bokeh parah! Makin gede (8–16), depan-belakang tajam semua."
    ),
    "F-Stop ratio (lower numbers give a shallower depth of field)": (
        "Fungsi: Bukaan diafragma lensa penentu seberapa kuat blur background kamera (Depth of Field).\n"
        "Cara Pakai: Makin KECIL angkanya (misal 0.3–1.4), background makin NGEBLUR parah! Makin besar (misal 8–16), depan-belakang tajam semua."
    ),
    "Camera far clipping distance": (
        "Fungsi: Clip End — jarak pandang terjauh mata kamera sebelum benda-benda jauh dipotong hilang.\n"
        "Cara Pakai: Kalau gunung/kota di kejauhan kelihatan terpotong bolong di kamera, naikin angka ini dari 100m jadi 1000m atau 5000m!"
    ),
    "Light energy emitted over the entire area of the light in all directions": (
        "Fungsi: Power (Watt) — seberapa terang pancaran cahaya dari lampu ini.\n"
        "Cara Pakai: Naikkan angkanya kalau ruangan masih gelap (semakin besar ukuran objek ruangan lu, semakin besar Watt yang dibutuhkan!)."
    ),
    "Shadow ray tracing sample radius, larger values give softer shadows": (
        "Fungsi: Radius / Ukuran bola lampu — penentu utama apakah bayangan jatuh terlihat TAJAM KERAS atau HALUS LEMBUT!\n"
        "Cara Pakai: Kecilkan (0.01m) buat bayangan terik tajam; besarkan (0.5m–2m) buat bayangan lembut mewah ala lampu softbox studio!"
    ),

    # Operators populer
    "Render and display faces smooth, using interpolated vertex normals": (
        "Fungsi: Shade Smooth — menyulap tampilan poligon kotak-kotak kasar jadi kelihatan licin mulus tanpa nambah jumlah titik!\n"
        "Cara Pakai: Klik tombol ini di objek melengkung (bola/karakter). Kalau tepian siku jadi ikutan belang, pakai 'Shade Auto Smooth'!"
    ),
    "Render and display faces uniform, using face normals": (
        "Fungsi: Shade Flat — mengembalikan tampilan tiap keping poligon jadi tegas kotak-kotak sesuai bentuk aslinya.\n"
        "Cara Pakai: Klik ini buat melihat struktur poligon asli atau gaya visual Low-Poly."
    ),
}


# Kamus frasa panjang -> pendek bahasa Indonesia gaul 3D (diurutkan dari frasa terpanjang saat kompilasi)
_PHRASE_MAP: list[tuple[str, str]] = [
    ("f-stop", "bukaan lensa (F-Stop)"),
    ("z-axis", "sumbu Z (atas-bawah)"),
    ("x-axis", "sumbu X (kiri-kanan)"),
    ("y-axis", "sumbu Y (depan-belakang)"),
    ("vertex group", "grup titik (Vertex Group)"),
    ("vertex groups", "grup titik (Vertex Groups)"),
    ("uv map", "peta tekstur (UV Map)"),
    ("uv maps", "peta tekstur (UV Maps)"),
    ("shape key", "kunci perubahan bentuk (Shape Key)"),
    ("shape keys", "kunci perubahan bentuk (Shape Keys)"),
    ("bounding box", "kotak batas luar (Bounding Box)"),
    ("data-block", "blok data"),
    ("data-blocks", "blok data"),
    ("world space", "koordinat dunia (World Space)"),
    ("local space", "koordinat lokal objek (Local Space)"),
    ("object space", "koordinat objek"),
    ("tangent space", "ruang permukaan (Tangent Space)"),
    ("screen space", "ruang layar kamera"),
    ("custom normals", "arah pantul cahaya custom (Normals)"),
    ("face normals", "arah hadap bidang (Face Normals)"),
    ("vertex normals", "arah pantul titik (Vertex Normals)"),
    ("surface normal", "arah tegak lurus permukaan (Normal)"),
    ("surface normals", "arah tegak lurus permukaan (Normals)"),
    ("depth of field", "efek fokus blur kamera (Depth of Field)"),
    ("motion blur", "efek buram gerak (Motion Blur)"),
    ("ambient occlusion", "bayangan celah sempit (Ambient Occlusion)"),
    ("global illumination", "pantulan cahaya alami (Global Illumination)"),
    ("ray tracing", "pelacakan pantulan sinar (Ray Tracing)"),
    ("light bounces", "pantulan cahaya"),
    ("color ramp", "gradasi warna (Color Ramp)"),
    ("grease pencil", "gambar Grease Pencil"),
    ("hair curves", "helai rambut (Hair Curves)"),
    ("guide curves", "kurva rambut panduan"),
    ("control points", "titik kontrol"),
    ("control point", "titik kontrol"),
    ("active object", "objek yang lagi dipilih"),
    ("target object", "objek sasaran (Target)"),
    ("focal length", "zoom lensa (Focal Length)"),
    ("frame rate", "kecepatan frame per detik (FPS)"),
    ("start frame", "frame mulai"),
    ("end frame", "frame selesai"),
    ("current frame", "frame saat ini"),
    ("self collision", "tabrakan antar lipatan sendiri"),
    ("rigid body", "benda padat fisika (Rigid Body)"),
    ("soft body", "benda kenyal fisika (Soft Body)"),
    ("force field", "medan gaya/angin (Force Field)"),
    ("modifier stack", "tumpukan urutan Modifier"),
    ("in edit mode", "saat di Edit Mode"),
    ("in object mode", "saat di Object Mode"),
    ("in pose mode", "saat di Pose Mode"),
    ("in sculpt mode", "saat di Sculpt Mode"),
    ("in the viewport", "di layar kerja Viewport"),
    ("when rendering", "waktu proses Render akhir"),
    ("during render", "waktu proses Render"),
    ("based on", "berdasarkan"),
    ("relative to", "relatif terhadap"),
    ("instead of", "sebagai ganti dari"),
    ("according to", "sesuai dengan"),
    ("used to", "dipakai buat"),
    ("used for", "dipakai buat"),
    ("whether to", "nentuin apakah mau"),
    ("determines whether", "nentuin apakah"),
    ("specifies how", "nentuin gimana cara"),
    ("controls how", "ngatur gimana cara"),
    ("number of", "jumlah"),
    ("amount of", "banyaknya / seberapa kuat"),
    ("maximum number of", "jumlah maksimal"),
    ("minimum number of", "jumlah minimal"),
    ("distance between", "jarak antara"),
    ("angle between", "sudut kemiringan antara"),
]

_WORD_MAP: dict[str, str] = {
    "a": "",
    "above": "di atas",
    "below": "di bawah",
    "numbers": "angka",
    "defocus": "efek blur bokeh",
    "sharper": "lebih tajam",
    "smoother": "lebih mulus",
    "softer": "lebih lembut",
    "harder": "lebih tegas",
    "brighter": "lebih terang",
    "darker": "lebih gelap",
    "stronger": "lebih kuat",
    "weaker": "lebih lemah",
    "thicker": "lebih tebal",
    "thinner": "lebih tipis",
    "wider": "lebih lebar",
    "closer": "lebih dekat",
    "further": "lebih jauh",
    "slower": "lebih pelan",
    "uses": "memakai",
    "whether": "apakah",
    "whose": "yang",
    "add": "tambahin",
    "added": "ditambahin",
    "adding": "nambahin",
    "adjust": "atur",
    "adjusts": "ngatur",
    "adjusted": "diatur",
    "affect": "ngaruh ke",
    "affected": "dipengaruhi",
    "affects": "mempengaruhi",
    "align": "sejajarin",
    "aligned": "disejajarin",
    "all": "semua",
    "allow": "izinkan",
    "allows": "bikin lu bisa",
    "along": "di sepanjang",
    "alpha": "transparansi (Alpha)",
    "also": "juga",
    "always": "selalu",
    "amount": "jumlah/besaran",
    "an": "sebuah",
    "and": "dan",
    "angle": "sudut",
    "angles": "sudut-sudut",
    "animate": "animasiin",
    "animated": "beranimasi",
    "animation": "animasi",
    "apply": "terapkan",
    "applied": "diterapkan",
    "area": "area/luas",
    "armature": "kerangka tulang (Armature)",
    "around": "di sekeliling",
    "array": "barisan duplikat",
    "as": "sebagai",
    "assign": "pasang/masukin",
    "assigned": "dipasang",
    "at": "pada",
    "attach": "tempelin",
    "attached": "nempel",
    "attenuation": "redaman jarak",
    "attribute": "atribut data",
    "attributes": "atribut data",
    "auto": "otomatis",
    "automatic": "otomatis",
    "automatically": "secara otomatis",
    "available": "yang tersedia",
    "average": "rata-rata",
    "axes": "sumbu-sumbu (X/Y/Z)",
    "axis": "sumbu",
    "background": "latar belakang",
    "bake": "rekam permanen (Bake)",
    "baked": "hasil Bake",
    "base": "dasar",
    "be": "jadi",
    "before": "sebelum",
    "after": "sesudah",
    "behavior": "perilaku",
    "bend": "tekukan/lengkungan",
    "between": "di antara",
    "bevel": "sudut tumpul (Bevel)",
    "bind": "ikat (Bind)",
    "blend": "campur/haluskan",
    "blending": "pencampuran",
    "blur": "efek buram (Blur)",
    "bone": "tulang",
    "bones": "tulang-tulang",
    "border": "batas pinggir",
    "both": "kedua",
    "bounce": "pantulan",
    "bounces": "pantulan",
    "boundary": "garis batas tepi",
    "box": "kotak",
    "brightness": "tingkat terang",
    "brush": "kuas",
    "brushes": "kuas-kuas",
    "by": "dengan",
    "cache": "simpanan memori (Cache)",
    "calculate": "hitung",
    "calculated": "dihitung",
    "calculation": "perhitungan",
    "camera": "kamera",
    "can": "bisa",
    "canvas": "kanvas permukaan",
    "cast": "pancarkan/bentuk",
    "cell": "sel/kotak",
    "center": "titik tengah",
    "change": "ubah",
    "changes": "mengubah",
    "channel": "saluran (channel)",
    "channels": "saluran",
    "child": "anak objek",
    "children": "anak-anak partikel/objek",
    "choose": "pilih",
    "clamp": "batasi mentok (Clamp)",
    "clamping": "pembatasan nilai",
    "clear": "bersihkan/hapus",
    "clip": "batas potong",
    "clipping": "batas potong/kunci tengah",
    "cloth": "kain",
    "collection": "folder grup (Collection)",
    "collision": "tumbukan/tabrakan",
    "collisions": "tabrakan",
    "color": "warna",
    "colors": "warna-warna",
    "combine": "gabungin",
    "compute": "hitung",
    "cone": "kerucut",
    "connect": "sambungin",
    "connected": "tersambung",
    "constant": "tetap/konstan",
    "constraint": "aturan pengikat (Constraint)",
    "constraints": "aturan pengikat",
    "contrast": "kontras tajam",
    "control": "kendalikan/atur",
    "controls": "mengatur",
    "convert": "ubah konversi",
    "coordinate": "koordinat",
    "coordinates": "koordinat",
    "copy": "salin/tiru",
    "copies": "kopian duplikat",
    "corner": "pojok sudut",
    "corners": "pojokan sudut",
    "count": "jumlah hitungan",
    "crease": "lipatan tajam",
    "create": "bikin",
    "creates": "bikin",
    "creating": "membuat",
    "current": "saat ini",
    "curvature": "kelengkungan",
    "curve": "garis lengkung (Curve)",
    "curves": "garis-garis lengkung",
    "custom": "custom buatan sendiri",
    "cut": "potong",
    "cuts": "potongan",
    "damping": "redaman gerak",
    "data": "data",
    "default": "bawaan standar",
    "define": "nentuin",
    "defined": "ditentukan",
    "defines": "nentuin",
    "deform": "bengkokin/ubah bentuk",
    "deformation": "perubahan bentuk",
    "deforms": "mengubah bentuk",
    "degree": "derajat",
    "degrees": "derajat",
    "delete": "hapus",
    "density": "kerapatan/kepadatan",
    "depth": "kedalaman",
    "detail": "ketajaman detail",
    "details": "detail halus",
    "determine": "nentuin",
    "diffuse": "warna dasar menyebar (Diffuse)",
    "direct": "langsung",
    "direction": "arah",
    "directional": "searah",
    "disable": "matiin",
    "disabled": "dimatikan",
    "displace": "dorong timbul-tenggelam",
    "displacement": "tonjolan permukaan",
    "display": "tampilin",
    "displayed": "ditampilin",
    "distance": "jarak",
    "distortion": "distorsi lengkung",
    "distribution": "pola sebaran",
    "divide": "bagi",
    "domain": "kotak wilayah simulasi (Domain)",
    "drag": "hambatan udara",
    "draw": "gambar",
    "duplicate": "gandakan/duplikat",
    "duplicates": "hasil duplikat",
    "dynamic": "dinamis otomatis",
    "each": "setiap",
    "edge": "garis tepi (Edge)",
    "edges": "garis-garis tepi (Edges)",
    "edit": "ubah/edit",
    "editing": "pengeditan",
    "effect": "efek",
    "effects": "efek-efek",
    "effector": "penghalang/pemicu",
    "element": "elemen",
    "elements": "elemen-elemen",
    "emission": "pancaran cahaya/partikel",
    "emit": "pancarkan",
    "enable": "nyalain/aktifkan",
    "enabled": "aktif menyala",
    "enables": "mengaktifkan",
    "end": "ujung akhir",
    "energy": "energi/terang",
    "environment": "lingkungan langit",
    "error": "selisih/error",
    "evaluate": "hitung evaluasi",
    "even": "rata seragam",
    "every": "setiap",
    "exact": "presisi akurat",
    "exclude": "kecualikan",
    "existing": "yang udah ada",
    "expand": "lebarkan",
    "export": "ekspor simpan keluar",
    "exposure": "terang cahaya kamera (Exposure)",
    "external": "file luar",
    "extra": "tambahan",
    "extrude": "tarik tebalkan (Extrude)",
    "face": "bidang poligon (Face)",
    "faces": "bidang-bidang poligon (Faces)",
    "factor": "faktor kekuatan",
    "fade": "memudar halus",
    "falloff": "gradasi melemah di pinggir (Falloff)",
    "far": "jauh",
    "fast": "cepat",
    "faster": "lebih ngebut",
    "field": "medan area",
    "file": "file",
    "fill": "isi/tutup penuh",
    "film": "sensor film kamera",
    "filter": "saring/haluskan",
    "final": "hasil akhir",
    "find": "cari",
    "first": "pertama",
    "fit": "paskan ukuran",
    "fixed": "tetap",
    "flat": "datar tegas",
    "flip": "balikkan arah",
    "flow": "aliran sumber (Flow)",
    "fluid": "cairan/asap (Fluid)",
    "focus": "titik fokus tajam",
    "follow": "ikutin",
    "following": "mengikuti",
    "font": "gaya huruf (Font)",
    "for": "buat",
    "force": "dorongan gaya",
    "format": "format",
    "frame": "bingkai waktu (Frame)",
    "frames": "frame animasi",
    "free": "bebaskan/hapus",
    "frequency": "kerapatan gelombang",
    "friction": "gaya gesek kesat",
    "from": "dari",
    "front": "depan",
    "full": "penuh",
    "gamma": "kecerahan tengah (Gamma)",
    "gap": "celah jarak",
    "gas": "asap/api (Gas)",
    "general": "umum",
    "generate": "buat otomatis",
    "generated": "hasil buatan otomatis",
    "generates": "membuat otomatis",
    "geometry": "bentuk geometri 3D",
    "give": "ngasih",
    "given": "yang ditentukan",
    "giving": "sehingga ngasih",
    "glass": "kaca bening",
    "global": "global menyeluruh",
    "glossy": "pantulan mengkilap (Glossy)",
    "glow": "cahaya berpendar (Glow)",
    "goal": "posisi awal pegangan (Goal)",
    "gradient": "gradasi warna",
    "gravity": "tarikan gravitasi",
    "grid": "jaring kotak-kotak (Grid)",
    "group": "grup kelompok",
    "groups": "grup-grup",
    "guide": "panduan jalur",
    "guides": "garis panduan",
    "hair": "rambut/bulu",
    "handle": "gagang titik lengkung",
    "hard": "keras tajam",
    "hardness": "ketegasan pinggir",
    "height": "tinggi",
    "hide": "sembunyiin",
    "hidden": "tersembunyi",
    "high": "tinggi",
    "higher": "makin tinggi",
    "highest": "paling tinggi",
    "highlight": "kilap terang",
    "hole": "lubang",
    "holes": "lubang-lubang",
    "horizontal": "mendatar kiri-kanan",
    "how": "gimana/seberapa",
    "hue": "rona jenis warna (Hue)",
    "if": "kalau",
    "ignore": "abaikan",
    "image": "gambar/foto",
    "images": "gambar-gambar",
    "import": "masukin file luar",
    "in": "di dalam",
    "include": "ikut sertakan",
    "increase": "naikkan/tambah",
    "increased": "bertambah",
    "index": "nomor urut (Index)",
    "indirect": "pantulan tak langsung",
    "individual": "masing-masing terpisah",
    "influence": "kekuatan pengaruh",
    "inflow": "keran penyembur terus-menerus",
    "initial": "awal mula",
    "inner": "bagian dalam",
    "input": "masukan (Input)",
    "inside": "di bagian dalam",
    "instance": "objek kopian hemat memori (Instance)",
    "instances": "kopian-kopian objek",
    "intensity": "kekuatan/intensitas",
    "interactive": "interaktif langsung",
    "interface": "tampilan antarmuka",
    "interpolate": "isi perantara mulus",
    "interpolation": "penghalusan transisi",
    "intersect": "irisan perpotongan",
    "intersection": "garis perpotongan",
    "into": "menjadi / ke dalam",
    "invert": "balikkan kebalikannya",
    "inverted": "dibalik",
    "is": "adalah",
    "island": "potongan pulau UV",
    "iterations": "jumlah pengulangan proses",
    "join": "gabungkan",
    "joined": "tergabung",
    "keep": "pertahankan/jaga",
    "keyframe": "titik rekam animasi (Keyframe)",
    "keyframes": "titik-titik animasi",
    "large": "besar",
    "larger": "makin besar",
    "last": "terakhir",
    "lattice": "kandang pembengkok (Lattice)",
    "layer": "lapisan (Layer)",
    "layers": "lapisan-lapisan",
    "left": "kiri",
    "length": "panjang",
    "lens": "lensa kamera",
    "less": "lebih sedikit",
    "level": "tingkatan level",
    "levels": "tingkatan level",
    "lifetime": "umur hidup partikel",
    "light": "cahaya lampu",
    "lighting": "pencahayaan",
    "lights": "lampu-lampu",
    "limit": "batas kunci",
    "limits": "batas-batas",
    "line": "garis",
    "linear": "lurus stabil",
    "lines": "garis-garis",
    "link": "sambungkan",
    "liquid": "cairan air",
    "list": "daftar",
    "load": "muat buka",
    "local": "lokal objek",
    "location": "lokasi posisi",
    "lock": "kunci gembok",
    "locked": "dikunci",
    "look": "gaya tampilan warna",
    "loop": "putaran ulang/melingkar",
    "low": "rendah",
    "lower": "makin kecil/rendah",
    "lowest": "paling rendah",
    "main": "utama",
    "maintain": "pertahankan",
    "make": "bikin",
    "makes": "membuat",
    "manual": "manual",
    "map": "peta pemetaan",
    "mapping": "pemetaan koordinat",
    "margin": "jarak tepi aman (Margin)",
    "mark": "tandai",
    "mask": "masker pelindung/pembatas",
    "mass": "berat massa benda (kg)",
    "match": "samakan",
    "material": "material cat permukaan",
    "materials": "material-material",
    "max": "maksimal",
    "maximum": "batas maksimal",
    "mean": "rata-rata",
    "memory": "memori RAM/VRAM",
    "merge": "lebur satukan",
    "merged": "dilebur menyatu",
    "mesh": "jaring model 3D (Mesh)",
    "meshes": "model-model Mesh",
    "metallic": "sifat logam mengkilap",
    "method": "metode cara kerja",
    "middle": "tengah",
    "min": "minimal",
    "minimum": "batas minimal",
    "mirror": "cermin simetris",
    "mist": "kabut jarak jauh (Mist)",
    "mix": "campuran",
    "mode": "mode",
    "model": "model 3D",
    "modifier": "efek Modifier",
    "modifiers": "efek-efek Modifier",
    "modify": "ubah/modifikasi",
    "more": "lebih banyak",
    "motion": "gerakan",
    "move": "geser pindahkan",
    "movement": "pergerakan",
    "moving": "bergerak",
    "multiple": "banyak sekaligus",
    "multiplier": "pengali kekuatan",
    "multiply": "kalikan",
    "name": "nama",
    "near": "dekat",
    "nearest": "paling dekat",
    "negative": "arah negatif (-)",
    "neighbor": "tetangga sebelah",
    "neighboring": "bersebelahan",
    "neighbors": "titik tetangga",
    "new": "baru",
    "next": "berikutnya",
    "no": "tanpa",
    "node": "kotak Node",
    "nodes": "rangkaian Nodes",
    "noise": "bintik/pola acak (Noise)",
    "none": "kosong/tidak ada",
    "normal": "arah hadap permukaan (Normal)",
    "normals": "arah pantul cahaya (Normals)",
    "not": "tidak",
    "number": "angka/jumlah",
    "object": "objek",
    "objects": "objek-objek",
    "occlusion": "bayangan terhalang",
    "of": "dari",
    "off": "mati",
    "offset": "jarak geser (Offset)",
    "on": "di atas / aktif",
    "one": "satu",
    "only": "hanya/cuma",
    "opacity": "kepekatan (kebalikan transparan)",
    "open": "buka",
    "operation": "jenis operasi",
    "operator": "aksi perintah",
    "optional": "opsional tambahan",
    "options": "pilihan opsi",
    "or": "atau",
    "order": "urutan",
    "orientation": "arah orientasi",
    "origin": "titik pusat oranye (Origin)",
    "original": "bentuk aslinya",
    "other": "lainnya",
    "out": "keluar",
    "outer": "bagian luar",
    "outline": "garis tepi luar",
    "output": "keluaran hasil (Output)",
    "outside": "di luar",
    "over": "di atas / selama",
    "overall": "keseluruhan",
    "overlap": "tumpang-tindih tabrakan",
    "override": "timpa paksa (Override)",
    "owner": "objek pemilik ini",
    "paint": "lukis cat",
    "panel": "kotak panel",
    "parent": "induk objek (Parent)",
    "part": "bagian",
    "particle": "butir partikel",
    "particles": "butiran partikel",
    "parts": "bagian-bagian",
    "pass": "lapisan informasi render (Pass)",
    "passes": "lapisan-lapisan render",
    "passive": "diam menahan (Passive)",
    "path": "jalur lintasan / lokasi file",
    "paths": "jalur-jalur",
    "pattern": "pola corak",
    "per": "tiap",
    "percentage": "persentase (%)",
    "performance": "kecepatan performa",
    "physics": "simulasi fisika",
    "pick": "ambil/pilih",
    "pin": "jepit kunci (Pin)",
    "pivot": "titik poros putar (Pivot)",
    "pixel": "titik piksel gambar",
    "pixels": "piksel-piksel",
    "place": "taruh tempatkan",
    "plane": "bidang datar",
    "play": "putar jalankan",
    "playback": "pemutaran animasi",
    "point": "titik",
    "points": "titik-titik",
    "pole": "arah hadap lutut/siku (Pole)",
    "polygon": "bidang poligon",
    "polygons": "bidang-bidang poligon",
    "pose": "gaya gerak tulang (Pose)",
    "position": "posisi",
    "positions": "posisi-posisi",
    "positive": "arah positif (+)",
    "power": "daya terang/kekuatan",
    "precision": "ketelitian presisi",
    "preserve": "jaga tetap utuh",
    "preset": "settingan siap pakai (Preset)",
    "pressure": "tekanan angin/pena",
    "prevent": "mencegah supaya gak",
    "preview": "tampilan pratinjau cepat",
    "previous": "sebelumnya",
    "primitive": "bentuk dasar 3D",
    "profile": "bentuk profil pinggiran",
    "project": "tembak proyeksikan",
    "projection": "proyeksi tembakan",
    "properties": "pengaturan properti",
    "property": "properti pengaturan",
    "proportional": "proporsional merata",
    "quality": "kualitas ketelitian",
    "radius": "jari-jari ukuran lebar (Radius)",
    "random": "acak natural",
    "randomize": "acak variasinya",
    "randomness": "tingkat keacakan",
    "range": "rentang batas",
    "rate": "laju kecepatan",
    "ratio": "perbandingan rasio",
    "ray": "sinar cahaya",
    "rays": "sinar-sinar cahaya",
    "real": "nyata",
    "recalculate": "hitung ulang",
    "receive": "menerima",
    "reduce": "kurangi pangkas",
    "reducing": "mengurangi",
    "reference": "acuan referensi",
    "reflection": "pantulan cermin",
    "refraction": "pembiasan tembus kaca",
    "region": "area wilayah",
    "relative": "relatif proporsional",
    "remesh": "susun ulang jaring poligon",
    "remove": "hapus buang",
    "render": "proses gambar akhir (Render)",
    "rendered": "hasil Render",
    "rendering": "proses Render",
    "repeat": "ulangi",
    "replace": "ganti timpa",
    "reset": "kembalikan ke awal (Reset)",
    "resolution": "ketajaman resolusi",
    "rest": "posisi diam awal (Rest)",
    "restore": "pulihkan kembali",
    "restrict": "batasi kunci",
    "result": "hasil akhir",
    "reverse": "putar balik arah",
    "right": "kanan",
    "rim": "pinggiran tepi",
    "ripple": "riak gelombang",
    "roll": "gulungan miring tulang",
    "root": "pangkal akar",
    "rotate": "putar",
    "rotated": "diputar",
    "rotation": "putaran (Rotation)",
    "roughness": "kekasaran/keburaman kilap",
    "round": "membulat halus",
    "same": "sama",
    "sample": "sampel titik hitung",
    "samples": "jumlah sampel ketajaman",
    "sampling": "pengambilan sampel cahaya",
    "saturation": "kepekatan warna (Saturation)",
    "save": "simpan",
    "scale": "ukuran skala",
    "scaled": "diubah ukurannya",
    "scaling": "perubahan ukuran skala",
    "scatter": "sebarkan merata",
    "scattered": "disebarkan",
    "scene": "adegan dunia 3D (Scene)",
    "screen": "layar",
    "sculpt": "pahat ukir (Sculpt)",
    "seam": "garis jahitan potong UV",
    "second": "detik / kedua",
    "seconds": "detik",
    "seed": "angka acak variasi (Seed)",
    "segment": "potongan ruas garis",
    "segments": "jumlah ruas potongan",
    "select": "pilih seleksi",
    "selected": "yang dipilih",
    "selection": "area yang dipilih",
    "self": "dirinya sendiri",
    "sensor": "sensor kamera",
    "separate": "pisahkan tersendiri",
    "sequence": "urutan gambar beruntun",
    "set": "atur tetapkan",
    "sets": "mengatur",
    "setting": "pengaturan",
    "settings": "pengaturan-pengaturan",
    "shade": "gaya bayangan permukaan",
    "shader": "peracik material cahaya (Shader)",
    "shading": "pewarnaan & bayangan",
    "shadow": "bayangan gelap",
    "shadows": "bayangan-bayangan",
    "shape": "bentuk",
    "sharp": "tajam tegas",
    "sharpness": "ketajaman sudut",
    "shear": "miringkan jajargenjang",
    "shell": "kulit dinding",
    "shift": "geser",
    "show": "tampilkan",
    "shrink": "ciutkan mengecil",
    "side": "sisi",
    "sides": "sisi-sisi",
    "simple": "sederhana langsung",
    "simplify": "sederhanakan kurangi beban",
    "simulate": "simulasikan",
    "simulation": "simulasi fisika",
    "single": "satu tunggal",
    "size": "ukuran besar",
    "skin": "kulit daging",
    "sky": "langit",
    "slide": "geser meluncur",
    "slider": "penggeser angka",
    "slow": "agak berat dihitung",
    "small": "kecil",
    "smaller": "makin kecil",
    "smoke": "asap",
    "smooth": "halus mulus",
    "smoothing": "penghalusan",
    "smoothness": "kehalusan",
    "snap": "tempel magnet presisi (Snap)",
    "soft": "lembut empuk",
    "softness": "kelembutan",
    "solid": "padat utuh",
    "solver": "mesin penghitung (Solver)",
    "sound": "suara audio",
    "source": "sumber asal",
    "space": "ruang koordinat",
    "spawn": "munculkan",
    "specific": "tertentu spesifik",
    "specified": "yang dipilih",
    "specify": "tentukan",
    "specular": "pantulan kilap cahaya",
    "speed": "kecepatan gerak",
    "sphere": "bola bulat",
    "spin": "putar melingkar",
    "spline": "garis kurva (Spline)",
    "split": "pisahkan belah",
    "spot": "lampu sorot kerucut",
    "spread": "lebar sebaran",
    "spring": "pegas membal",
    "stability": "kestabilan",
    "stabilize": "stabilkan anti-gemetar",
    "stack": "tumpukan urutan",
    "start": "awal mulai",
    "state": "kondisi",
    "step": "langkah lompatan",
    "steps": "jumlah langkah",
    "stiffness": "kekakuan bahan (makin tinggi makin kaku)",
    "still": "tetap",
    "stop": "berhenti",
    "store": "simpan",
    "straight": "lurus",
    "strand": "helai rambut",
    "strands": "helai-helai rambut",
    "strength": "kekuatan efek",
    "stretch": "tarik melar",
    "strip": "potongan klip (Strip)",
    "stroke": "goresan kuas/garis",
    "strokes": "goresan-goresan",
    "style": "gaya tampilan",
    "subdivide": "pecah perhalus poligon",
    "subdivision": "pembagian penghalus poligon",
    "subdivisions": "level penghalusan poligon",
    "substeps": "sub-langkah akurasi fisika",
    "subsurface": "tembus cahaya bawah kulit (SSS)",
    "subtract": "kurangi lubangi",
    "sun": "cahaya matahari",
    "surface": "permukaan kulit objek",
    "surfaces": "permukaan-permukaan",
    "symmetry": "cermin simetris kiri-kanan",
    "system": "sistem",
    "tangent": "garis singgung arah permukaan",
    "taper": "meruncing mengecil",
    "target": "objek sasaran (Target)",
    "temperature": "suhu warna/panas",
    "tension": "tegangan tarikan",
    "text": "tulisan teks",
    "texture": "gambar corak (Texture)",
    "textures": "tekstur-tekstur",
    "than": "daripada",
    "that": "yang",
    "the": "",
    "their": "miliknya",
    "them": "mereka",
    "then": "lalu",
    "these": "ini",
    "thick": "tebal",
    "thickness": "ketebalan",
    "thin": "tipis",
    "this": "ini",
    "threshold": "ambang batas pemicu",
    "through": "menembus lewat",
    "tile": "kotak ubin proses",
    "time": "waktu",
    "timeline": "garis waktu animasi",
    "tint": "campuran sapuan warna",
    "tip": "ujung lancip",
    "tips": "ujung-ujung",
    "to": "ke / untuk",
    "toggle": "tombol nyala-mati",
    "tool": "alat kerja",
    "tools": "alat-alat",
    "top": "bagian atas",
    "topology": "susunan jaring poligon",
    "total": "total keseluruhan",
    "towards": "menuju ke arah",
    "track": "lacak ikuti arah",
    "tracking": "pelacakan gerak",
    "transform": "posisi/rotasi/skala (Transform)",
    "transformation": "perubahan posisi/rotasi/skala",
    "transformations": "perubahan posisi/rotasi/skala",
    "transforms": "mengubah posisi/rotasi/skala",
    "transition": "perpindahan halus",
    "translation": "pergeseran posisi",
    "transmission": "tembus cahaya kaca/air",
    "transparency": "ketembusan pandang",
    "transparent": "tembus pandang transparan",
    "triangle": "poligon segitiga",
    "triangles": "poligon-poligon segitiga",
    "trim": "potong pangkas",
    "tube": "pipa tabung",
    "turbulence": "pusaran angin acak",
    "turn": "ubah/putar",
    "twist": "plintiran putar",
    "two": "dua",
    "type": "jenis tipe",
    "uniform": "seragam merata",
    "union": "gabung lebur jadi satu",
    "unit": "satuan ukuran",
    "units": "satuan ukuran",
    "unwrap": "bentangkan kulit UV",
    "up": "arah atas",
    "update": "perbarui",
    "upper": "batas atas",
    "use": "pakai/aktifkan",
    "used": " yang dipakai",
    "using": "dengan memakai",
    "uv": "koordinat tekstur UV",
    "value": "angka nilai / terang warna",
    "values": "nilai-nilai angka",
    "variation": "variasi acak",
    "vector": "arah & nilai (Vector X/Y/Z)",
    "velocity": "kecepatan lontar",
    "vertex": "titik sudut (Vertex)",
    "vertical": "tegak atas-bawah",
    "vertices": "titik-titik sudut (Vertices)",
    "verts": "titik-titik (Verts)",
    "video": "video",
    "view": "pandangan layar",
    "viewport": "layar kerja 3D Viewport",
    "visibility": "keterlihatan (muncul/sembunyi)",
    "visible": "terlihat muncul",
    "viscosity": "kekentalan cairan",
    "volume": "isi ruang/kabut 3D (Volume)",
    "vortex": "pusaran angin puyuh",
    "voxel": "kotak piksel 3D (Voxel)",
    "wall": "dinding",
    "warp": "tarik lengkungkan",
    "water": "air",
    "wave": "gelombang ombak",
    "waves": "gelombang-gelombang",
    "way": "cara",
    "weight": "bobot kekuatan (Weight)",
    "weights": "bobot pengaruh",
    "weld": "las gabung titik",
    "when": "kapan/saat",
    "where": "di mana",
    "which": "yang mana",
    "while": "sambil",
    "white": "putih",
    "whole": "seluruh utuh",
    "width": "lebar",
    "wind": "tiupan angin",
    "wire": "rangka garis kawat",
    "wireframe": "rangka jaring kawat (Wireframe)",
    "with": "dengan",
    "within": "di dalam batas",
    "without": "tanpa",
    "world": "dunia langit (World)",
    "wrap": "bungkus tempelkan",
    "zero": "angka nol (0)",
}

_TOKEN_RE = re.compile(r"[A-Za-z']+|[^A-Za-z']+")
_SORTED_PHRASES = sorted(_PHRASE_MAP, key=lambda kv: len(kv[0]), reverse=True)
_PHRASE_RE = re.compile(
    r"\b(?:" + "|".join(re.escape(p) for p, _ in _SORTED_PHRASES) + r")\b",
    re.IGNORECASE,
)
_PHRASE_LOOKUP = {p.lower(): rep for p, rep in _SORTED_PHRASES}


def translate_english_to_gaul_sentence(en_text: str, label_hint: str = "") -> str:
    """Menerjemahkan kalimat deskripsi RNA bahasa Inggris menjadi Bahasa Indonesia Gaul yang gampang dipahami pemula."""
    txt = (en_text or "").strip().rstrip(".")
    if not txt:
        if label_hint:
            return f"Mengatur opsi atau nilai '{label_hint}' pada fitur ini"
        return "Mengatur nilai atau opsi pada fitur Blender ini"

    # 1. Ganti frasa multi-kata terlebih dahulu (1-pass cepat dengan regex)
    step1 = _PHRASE_RE.sub(lambda m: _PHRASE_LOOKUP[m.group(0).lower()], txt)

    # 2. Terjemahkan per-kata sambil mempertahankan angka, simbol, X/Y/Z, singkatan huruf besar (UV, IK, HDR, RGB, VDB)
    parts = _TOKEN_RE.findall(step1)
    out_parts: list[str] = []
    for tok in parts:
        if tok[0].isalpha():
            # Pertahankan singkatan teknis pendek huruf kapital seperti UV, IK, FK, RGB, RGBA, HDRI, VDB, GPU, CPU, X, Y, Z
            if tok.isupper() and len(tok) <= 5 and tok not in {"THE", "AND", "FOR", "USE", "ALL", "OFF", "ADD", "SET", "NEW"}:
                out_parts.append(tok)
                continue
            low = tok.lower()
            if low in _WORD_MAP:
                rep = _WORD_MAP[low]
                if rep:
                    out_parts.append(rep)
                continue
        out_parts.append(tok)

    sentence = "".join(out_parts)
    sentence = re.sub(r"\s{2,}", " ", sentence).strip(" ,;-")
    if sentence:
        sentence = sentence[0].upper() + sentence[1:]
    return sentence or f"Mengatur '{label_hint or 'fitur ini'}'"


def build_widget_cara_pakai(
    kind: str,
    prop_type: str = "",
    prop_subtype: str = "NONE",
    prop_name: str = "",
    owner_name: str = "",
) -> str:
    """Menghasilkan panduan 'Cara Pakai' praktis sesuai jenis input variable / tombol di UI Blender."""
    if kind == "OPERATOR":
        return "Klik tombol ini buat langsung ngejalanin aksinya."
    if kind == "ENUM_ITEM":
        return f"Klik pilihan '{prop_name}' ini di menu dropdown kalau lu mau mode ini yang aktif."
    if kind == "BRUSH":
        return "Pilih kuas ini -> atur Radius (pencet F) & Strength (Shift+F) -> sapukan di permukaan model!"
    if kind == "ASSET":
        return "Klik buat masang aset/modifier ini ke objek lu, lalu atur angka inputnya di panel Modifier!"
    if kind == "STRUCT":
        return f"Buka panel {prop_name or owner_name} ini lalu atur parameter di dalamnya sesuai kebutuhan."

    if prop_type == "BOOLEAN":
        return "Centang kotak ini buat NYALAIN fiturnya, atau matiin centangnya kalau gak pengen efeknya aktif."
    if prop_type == "ENUM":
        return "Klik kotak pilihan (dropdown) ini buat ganti mode/metode yang paling pas sama kebutuhan lu."
    if prop_type == "POINTER":
        return "Klik kolom ini (atau pakai ikon pipet suntik) buat milih objek/data sasaran yang mau dipakai."
    if prop_type == "STRING":
        low_n = prop_name.lower()
        if "group" in low_n or "uv" in low_n or "layer" in low_n or "bone" in low_n or "attribute" in low_n:
            return "Klik kolom ini terus pilih nama dari daftar yang tersedia di objek lu."
        if "path" in low_n or "file" in low_n or "directory" in low_n:
            return "Klik ikon map folder di sebelah kanan buat milih lokasi file/folder di komputer lu."
        return "Klik kolom teks ini lalu ketik nama atau nilai yang diinginkan, akhiri dengan Enter."
    if prop_type == "INT":
        return "Klik panah kiri/kanan atau ketik angkanya langsung (jangan isi kelewat gede kalau bikin berat!)."
    if prop_type == "FLOAT":
        if prop_subtype in {"COLOR", "COLOR_GAMMA"}:
            return "Klik kotak warna ini terus pilih warna yang lu suka di roda warna (atau ambil pakai pipet)."
        if prop_subtype in {"FACTOR", "PERCENTAGE"}:
            return "Geser slider kiri-kanan (0 = mati/minimal, makin ke kanan makin kuat; tahan Shift biar halusan!)."
        if prop_subtype == "ANGLE":
            return "Geser angka derajat kemiringan/putarannya (tahan Shift sambil geser biar presisi!)."
        return "Klik-tahan-geser angkanya kiri-kanan buat ngatur nilainya (tahan Shift biar gesernya pelan presisi!)."
    if prop_type == "COLLECTION":
        return "Gunakan daftar item di panel ini (klik '+' buat nambah baru atau '-' buat hapus)."

    return "Arahin & ubah nilainya sesuai efek visual yang lu pengen di layar 3D."


def format_full_tooltip(fungsi: str, cara_pakai: str, include_footer: bool = True) -> str:
    f_clean = fungsi.strip()
    c_clean = cara_pakai.strip()
    if not f_clean.lower().startswith("fungsi:"):
        f_clean = f"Fungsi: {f_clean}"
    if not c_clean.lower().startswith("cara pakai:"):
        c_clean = f"Cara Pakai: {c_clean}"
    if include_footer:
        return f"{f_clean}\n{c_clean}\n{FOOTER_HINT}"
    return f"{f_clean}\n{c_clean}"


def compile_all_blender_tooltips(force_full_scan: bool = False) -> dict[str, str]:
    """Mengompilasi 100% seluruh deskripsi RNA Properties, Modifiers, Constraints, Operators & Assets ke Bahasa Gaul!"""
    if _COMPILED_CACHE and not force_full_scan:
        return _COMPILED_CACHE

    if not force_full_scan:
        try:
            from .precompiled_tooltips import PRECOMPILED_TOOLTIPS
            if PRECOMPILED_TOOLTIPS:
                _COMPILED_CACHE.update(PRECOMPILED_TOOLTIPS)
                return _COMPILED_CACHE
        except Exception:
            pass

    result: dict[str, str] = {}

    # 1. Masukkan semua Curated Tooltips (Prioritas Tertinggi — Penjelasan Manual Super Gaul!)
    for en_desc, gaul_tip in TAB_ICON_TOOLTIPS.items():
        if en_desc:
            result[en_desc] = f"{gaul_tip}\n{FOOTER_HINT}"

    for mod in MODIFIER_CATALOG.values():
        d = mod.get("orig_desc", "")
        if d:
            result[d] = format_full_tooltip(mod["fungsi"], mod["cara_pakai"])

    for amod in ASSET_MODIFIER_CATALOG.values():
        d = amod.get("orig_desc", "")
        if d:
            result[d] = format_full_tooltip(amod["fungsi"], amod["cara_pakai"])

    for c_item in CONSTRAINT_CATALOG.values():
        d = c_item.get("orig_desc", "")
        if d:
            result[d] = format_full_tooltip(c_item["fungsi"], c_item["cara_pakai"])

    for fx_item in SHADERFX_CATALOG.values():
        d = fx_item.get("orig_desc", "")
        if d:
            result[d] = format_full_tooltip(fx_item["fungsi"], fx_item["cara_pakai"])

    for en_desc, gaul_tip in MODIFIER_PROP_TOOLTIPS.items():
        if en_desc:
            result[en_desc] = f"{gaul_tip}\n{FOOTER_HINT}"

    for en_desc, gaul_tip in CURATED_CORE_TOOLTIPS.items():
        if en_desc:
            result[en_desc] = f"{gaul_tip}\n{FOOTER_HINT}"

    # 2. Masukkan seluruh Asset Node Groups & Essentials Brushes dari Blender 5.2
    for en_desc, (kind, label) in ASSET_AND_BRUSH_DESCS.items():
        if en_desc and en_desc not in result:
            fungsi = translate_english_to_gaul_sentence(en_desc, label)
            cara = build_widget_cara_pakai("SOCKET" if kind == "SOCKET" else kind, "FLOAT" if kind == "SOCKET" else "", "NONE", label)
            result[en_desc] = format_full_tooltip(fungsi, cara)

    # 3. Sapu BERSIH 100% seluruh bpy.types (semua tab Properties sampe ke akar-akarnya: setiap struct, property, enum!)
    for tname in dir(bpy.types):
        cls = getattr(bpy.types, tname, None)
        rna = getattr(cls, "bl_rna", None)
        if rna is None:
            continue

        owner_label = rna.name or tname
        s_desc = rna.description
        if s_desc and s_desc not in result:
            fungsi = translate_english_to_gaul_sentence(s_desc, owner_label)
            cara = build_widget_cara_pakai("STRUCT", prop_name=owner_label, owner_name=owner_label)
            result[s_desc] = format_full_tooltip(fungsi, cara)

        for prop in rna.properties:
            p_desc = prop.description
            p_type = prop.type
            p_name = prop.name or prop.identifier
            p_sub = "COLOR" if (p_type == "FLOAT" and "color" in p_name.lower()) else ("ANGLE" if getattr(prop, "unit", "NONE") == "ROTATION" else "NONE")

            if p_desc and p_desc not in result:
                fungsi = translate_english_to_gaul_sentence(p_desc, p_name)
                cara = build_widget_cara_pakai("PROP", p_type, p_sub, p_name, owner_label)
                result[p_desc] = format_full_tooltip(fungsi, cara)

            if p_type == "ENUM" and hasattr(prop, "enum_items"):
                for ei in prop.enum_items:
                    e_desc = ei.description
                    if e_desc and e_desc not in result:
                        e_name = ei.name or ei.identifier
                        fungsi = translate_english_to_gaul_sentence(e_desc, e_name)
                        cara = build_widget_cara_pakai("ENUM_ITEM", "ENUM", "NONE", e_name, p_name)
                        result[e_desc] = format_full_tooltip(fungsi, cara)

    # 4. Sapu BERSIH 100% seluruh Operators di bpy.ops (semua tombol & tool di seluruh Blender!)
    for mod_name in dir(bpy.ops):
        if mod_name.startswith("_"):
            continue
        submod = getattr(bpy.ops, mod_name, None)
        if submod is None:
            continue
        for fn_name in dir(submod):
            if fn_name.startswith("_"):
                continue
            try:
                op_rna = getattr(submod, fn_name).get_rna_type()
                op_desc = op_rna.description
                if op_desc and op_desc not in result:
                    fungsi = translate_english_to_gaul_sentence(op_desc, op_rna.name)
                    cara = build_widget_cara_pakai("OPERATOR", prop_name=op_rna.name)
                    result[op_desc] = format_full_tooltip(fungsi, cara)
            except Exception:
                pass

    _COMPILED_CACHE.update(result)
    return _COMPILED_CACHE


def explain_raw_gaul(en_desc: str, prop_type: str = "", prop_subtype: str = "NONE", label: str = "") -> tuple[str, str]:
    """Mengembalikan pasangan (fungsi_gaul, cara_pakai_gaul) untuk ditampilkan di Popup Card / Panel."""
    compiled = compile_all_blender_tooltips()
    if en_desc and en_desc in compiled:
        lines = compiled[en_desc].splitlines()
        f_line = lines[0].replace("Fungsi:", "").strip() if lines else ""
        c_line = lines[1].replace("Cara Pakai:", "").strip() if len(lines) > 1 else ""
        return f_line, c_line

    f_gaul = translate_english_to_gaul_sentence(en_desc, label)
    c_gaul = build_widget_cara_pakai("PROP" if prop_type else "OPERATOR", prop_type, prop_subtype, label)
    return f_gaul, c_gaul


def enable_hover_translations() -> int:
    """Mendaftarkan kamus Hover Bahasa Gaul ke Blender tanpa mengubah nama tombol bahasa Inggris!"""
    global _IS_REGISTERED
    tips = compile_all_blender_tooltips()

    # Daftarkan untuk en_US, eo, dan id_ID supaya selalu aktif mulus tanpa konflik file .mo kaku
    per_locale = {("*", k): v for k, v in tips.items()}
    translations_dict = {
        "en_US": per_locale,
        "eo": per_locale,
        "id_ID": per_locale,
    }

    if _IS_REGISTERED:
        try:
            bpy.app.translations.unregister(DOMAIN_NAME)
        except Exception:
            pass
        _IS_REGISTERED = False

    bpy.app.translations.register(DOMAIN_NAME, translations_dict)
    _IS_REGISTERED = True

    try:
        prefs = bpy.context.preferences.view
        if not _SAVED_PREFS:
            _SAVED_PREFS["language"] = prefs.language
            _SAVED_PREFS["use_translate_tooltips"] = prefs.use_translate_tooltips
            _SAVED_PREFS["use_translate_interface"] = prefs.use_translate_interface
            _SAVED_PREFS["use_translate_new_dataname"] = prefs.use_translate_new_dataname

        # Pakai en_US + translate_tooltips=True + translate_interface=False:
        # 1) Label UI tetap bahasa Inggris standar (cocok buat keyword YouTube/Google!)
        # 2) 100% hover tooltip memakai Bahasa Indonesia Gaul kita (0 bentrok .mo bawaan!)
        prefs.language = "en_US"
        prefs.use_translate_tooltips = True
        prefs.use_translate_interface = False
        prefs.use_translate_new_dataname = False
    except Exception:
        pass

    return len(tips)


def disable_hover_translations(restore_prefs: bool = True) -> None:
    """Mematikan kamus Hover Bahasa Gaul dan mengembalikan pengaturan bahasa asli user."""
    global _IS_REGISTERED
    if _IS_REGISTERED:
        try:
            bpy.app.translations.unregister(DOMAIN_NAME)
        except Exception:
            pass
        _IS_REGISTERED = False

    if restore_prefs and _SAVED_PREFS:
        try:
            prefs = bpy.context.preferences.view
            if "language" in _SAVED_PREFS:
                prefs.language = str(_SAVED_PREFS["language"])
            if "use_translate_tooltips" in _SAVED_PREFS:
                prefs.use_translate_tooltips = bool(_SAVED_PREFS["use_translate_tooltips"])
            if "use_translate_interface" in _SAVED_PREFS:
                prefs.use_translate_interface = bool(_SAVED_PREFS["use_translate_interface"])
            if "use_translate_new_dataname" in _SAVED_PREFS:
                prefs.use_translate_new_dataname = bool(_SAVED_PREFS["use_translate_new_dataname"])
        except Exception:
            pass


def is_hover_active() -> bool:
    return _IS_REGISTERED
