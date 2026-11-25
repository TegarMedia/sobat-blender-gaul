# SPDX-License-Identifier: GPL-3.0-or-later
"""Katalog Pencarian Global Semua Fitur Blender (Indo Gaul <-> Keyword Inggris) untuk Cari YouTube & Google."""

from __future__ import annotations

# Kamus sinonim bahasa Indonesia sehari-hari -> istilah bahasa Inggris resmi Blender!
# Jadi kalau pemula ngetik "bolongin", "halusin", "tumpulin", "kaca", "tulang", sistem otomatis tahu istilah Inggrisnya!
INDO_TO_ENGLISH_TERMS: list[tuple[str, str]] = [
    ("tumpulin sudut", "Bevel Modifier"),
    ("sudut tumpul", "Bevel"),
    ("pinggiran halus", "Bevel"),
    ("halusin objek", "Subdivision Surface Shade Smooth"),
    ("mulusin", "Subdivision Surface Smooth"),
    ("bolongin", "Boolean Difference Modifier"),
    ("lubangin", "Boolean Difference Modifier"),
    ("potong objek", "Boolean Knife Bisect"),
    ("gabungin objek", "Join Boolean Union"),
    ("cermin", "Mirror Modifier Symmetrize"),
    ("simetris", "Mirror Modifier Symmetry"),
    ("tebelin", "Solidify Modifier Extrude"),
    ("kasih ketebalan", "Solidify Modifier"),
    ("gandain berbaris", "Array Modifier Duplicate"),
    ("fotokopi", "Array Duplicate Linked"),
    ("baris melingkar", "Radial Array Modifier"),
    ("tempel permukaan", "Shrinkwrap Modifier Snap to Face"),
    ("stiker", "Shrinkwrap Decal UV Project"),
    ("bengkokin", "Simple Deform Bend Curve Modifier"),
    ("plintir", "Simple Deform Twist"),
    ("melengkung ikut garis", "Curve Modifier Follow Path"),
    ("pipa kabel", "Bezier Curve Bevel Depth Curve to Tube"),
    ("bikin gelas botol", "Screw Modifier Spin"),
    ("rangka kawat", "Wireframe Modifier"),
    ("kurangin poligon", "Decimate Remesh Retopology"),
    ("berat ngelag", "Decimate Simplify Optimize Viewport"),
    ("tulang", "Armature Rigging Bones"),
    ("gerakin karakter", "Rigging Inverse Kinematics Weight Paint"),
    ("lutut siku nekuk", "Inverse Kinematics IK Pole Target"),
    ("ekspresi wajah", "Shape Keys Facial Rigging"),
    ("kedip senyum", "Shape Keys"),
    ("rambut bulu", "Hair Curves Grooming Particle Hair"),
    ("rumput pohon", "Scatter on Surface Geometry Nodes"),
    ("kain baju", "Cloth Simulation Physics Pin Group"),
    ("bantal gembung", "Cloth Pressure Pillow"),
    ("bendera berkibar", "Cloth Simulation Wind Force Field"),
    ("benda jatuh pecah", "Rigid Body Cell Fracture Physics"),
    ("air cairan tumpah", "Fluid Simulation Mantaflow Liquid"),
    ("asap api ledakan", "Fluid Simulation Smoke Fire Mantaflow"),
    ("awan kabut", "Mesh to Volume Displace Volumetric Fog"),
    ("laut ombak", "Ocean Modifier Foam"),
    ("kaca bening", "Glass Material Transmission Roughness IOR"),
    ("besi emas logam", "Metallic Roughness Principled BSDF"),
    ("lampu bersinar neon", "Emission Shader Glare Bloom Compositor"),
    ("kulit manusia", "Subsurface Scattering Skin Shader"),
    ("kartun anime garis", "Grease Pencil Line Art Cel Toon Shader"),
    ("kamera blur bokeh", "Camera Depth of Field Aperture F-Stop"),
    ("kamera ikut gerak", "Damped Track Follow Path Camera Constraint"),
    ("background transparan", "Render Film Transparent PNG"),
    ("bintik bintik semut", "Cycles Denoise Sampling Noise Threshold"),
    ("render lama lambat", "Cycles GPU Compute Persistent Data Optimize"),
    ("tekstur melar", "UV Unwrap Mark Seam Apply Scale"),
    ("kupas uv", "UV Unwrapping Mark Seam"),
    ("pahat ukir", "Sculpt Mode Remesh Dyntopo Multiresolution"),
    ("tarik permukaan", "Extrude Region Tool"),
    ("potong garis keliling", "Loop Cut and Slide Ctrl R"),
    ("sisip kotak dalam", "Inset Faces Tool"),
    ("pisau potong", "Knife Tool"),
    ("jembatan sambung lubang", "Bridge Edge Loops Fill Grid Fill"),
    ("titik tengah pivot", "Set Origin to Geometry 3D Cursor"),
]


# Daftar Lengkap Fitur-Fitur Seluruh Blender (di luar maupun di dalam Properties!)
# Format: (kategori, nama_inggris, keyword_inggris, kata_kunci_indo, penjelasan_gaul)
GLOBAL_BLENDER_FEATURES: list[tuple[str, str, str, str, str]] = [
    # --- MODELING TOOLS (Edit Mode) ---
    ("Modeling Tool", "Extrude Region (E)", "Blender Extrude Region Manifold tool tutorial", "tarik tumbuh panjangan extrude dinding", "Narik keluar permukaan/garis/titik buat numbuhin cabang bentuk 3D baru (pencet E di Edit Mode, atau Alt+E buat Extrude Manifold/Along Normals!)."),
    ("Modeling Tool", "Inset Faces (I)", "Blender Inset Faces tool tutorial", "sisip bingkai kotak dalam jendela inset", "Bikin kotak poligon lebih kecil di dalam permukaan yang dipilih — wajib buat bikin kusen jendela, layar TV, atau panel tombol (pencet I di Edit Mode)!"),
    ("Modeling Tool", "Bevel Tool (Ctrl+B)", "Blender Bevel Tool Edit Mode Ctrl B tutorial", "tumpulin sudut garis manual bevel", "Numpulin garis tertentu secara langsung di Edit Mode: pilih garis -> pencet Ctrl+B -> geser mouse & putar scroll roda mouse buat nambah segmen halusnya!"),
    ("Modeling Tool", "Loop Cut and Slide (Ctrl+R)", "Blender Loop Cut and Slide Ctrl R tutorial", "potong melingkar garis bagi segmen loop cut", "Motong garis sabuk melingkari badan objek! Pencet Ctrl+R -> putar scroll mouse buat nambah jumlah garis potongan -> klik kiri -> geser posisinya!"),
    ("Modeling Tool", "Knife Tool (K)", "Blender Knife Tool Bisect cut mesh tutorial", "pisau iris potong bebas gambar garis", "Pisau bedah bebas buat ngiris garis bentuk apa aja langsung di atas permukaan poligon (pencet K -> klik-klik titik irisannya -> pencet Enter buat konfirmasi!)."),
    ("Modeling Tool", "Poly Build Tool", "Blender Poly Build Retopology tool tutorial", "bangun poligon satu satu retopology", "Alat favorit buat Retopology! Klik-tarik garis buat langsung numbuhin kepingan poligon baru mengikuti kulit patung Sculpt (aktifin Snap to Face!)."),
    ("Modeling Tool", "Spin Tool", "Blender Spin Tool pipe corner 90 degree tutorial", "putar lengkung siku pipa gelas spin", "Memutar permukaan/profil mengelilingi 3D Cursor — jagoan buat bikin belokan pipa siku 90 derajat yang mulus!"),
    ("Modeling Tool", "Bridge Edge Loops", "Blender Bridge Edge Loops connect holes tutorial", "jembatan sambung dua lubang pipa bridge", "Menyambungkan dua lingkaran pinggiran lubang yang berhadapan langsung jadi lorong/jembatan terhubung rapi (Ctrl+E -> Bridge Edge Loops)!"),
    ("Modeling Tool", "Grid Fill & Fill (F)", "Blender Grid Fill vs Fill N-Gon tutorial", "tutup lubang permukaan rata rapi grid fill", "Pencet F buat nutup lubang cepat, atau Face -> Grid Fill buat menutup lubang lingkaran langsung jadi jaring kotak-kotak (Quad) super rapi!"),
    ("Modeling Tool", "Merge by Distance (M)", "Blender Merge by Distance remove doubles tutorial", "hapus titik dobel numpuk las gabung", "OBAT NOMOR #1 MODEL RUSAK! Pilih semua titik (A) di Edit Mode -> pencet M -> 'By Distance' buat menghapus titik kembar menumpuk yang bikin bayangan/Bevel error!"),
    ("Modeling Tool", "Proportional Editing (O)", "Blender Proportional Editing O shortcut tutorial", "tarik lembut ikut melengkung bukit magnet", "Pencet tombol 'O' di Edit Mode! Waktu lu narik 1 titik, titik-titik tetangga di sekitarnya ikut ketarik lembut kayak karet (putar scroll mouse buat gedein lingkaran pengaruhnya)!"),
    ("Modeling Tool", "Apply Scale & Transforms (Ctrl+A)", "Blender Apply Scale Ctrl A why important tutorial", "reset skala ukuran satu biar bevel uv bener", "ATURAN WAJIB PEMULA: Habis nge-Scale di Object Mode, pencet Ctrl+A -> 'Scale'! Kalau lupa, Bevel bakal miring sebelah dan UV Unwrap bakal gepeng!"),
    ("Modeling Tool", "Set Origin (Right Click -> Set Origin)", "Blender Set Origin 3D Cursor Pivot Point tutorial", "pindah titik tengah oranye engsel putar", "Mindahin titik pusat oranye objek (misal pindahin ke pinggir engsel pintu lewat 3D Cursor supaya pintunya muter di engsel, bukan muter di tengah daun pintu!)."),
    ("Modeling Tool", "Snap (Shift+Tab)", "Blender Snapping Vertex Face Increment tutorial", "magnet tempel presisi titik permukaan", "Magnet presisi buat nempelin titik ke titik (Vertex), objek ke lantai permukaan (Face Project), atau geser per kotak grid!"),

    # --- SCULPTING TOOLS ---
    ("Sculpting", "Draw / Clay Strips / Crease / Grab / Smooth Brushes", "Blender Sculpting Brushes Beginner Guide tutorial", "pahat ukir kuas tanah liat wajah karakter", "Kuas utama mematung: Clay Strips (nambah daging), Crease (bikin garis lipatan tajam), Grab (tarik bentuk besar pakai G), Smooth (tahan Shift kapan aja buat mulusin!), Inflate (gembungin)."),
    ("Sculpting", "Voxel Remesh (Ctrl+R di Sculpt Mode)", "Blender Sculpt Mode Voxel Remesh Shift R tutorial", "lebur jaring poligon pahat tambah detail", "Tekan Shift+R buat milih ukuran kotak detail, lalu Ctrl+R di Sculpt Mode buat melebur patung jadi jaring baru yang siap dipahat makin detail!"),
    ("Sculpting", "Dynamic Topology (Dyntopo)", "Blender Dyntopo Dynamic Topology Sculpting tutorial", "otomatis nambah segitiga pas kuas lewat", "Otomatis memecah segitiga kecil HANYA di bagian yang disentuh kuas aja — enak buat sketsa bentuk bebas dari satu bola!"),
    ("Sculpting", "Mask & Face Sets", "Blender Sculpt Masking Face Sets Pose Brush tutorial", "pelindung area kunci warna bagian pahat", "Lukis Mask hitam (M) buat mengunci area supaya gak kena pahatan (Ctrl+I buat balik, Alt+M buat hapus mask), atau bagi per-bagian warna pakai Face Sets!"),

    # --- UV & TEXTURING ---
    ("UV & Texturing", "Mark Seam & Unwrap (U)", "Blender UV Unwrapping Mark Seam Beginner tutorial", "garis gunting jahitan baju kupas tekstur", "Pilih garis tempat lipatan tersembunyi di Edit Mode -> klik kanan 'Mark Seam' (garis merah) -> pilih semua (A) -> pencet U -> Unwrap buat ngebentangin kulit 3D jadi datar 2D!"),
    ("UV & Texturing", "Smart UV Project & Cube Projection", "Blender Smart UV Project Cube Projection quick unwrap", "unwrap otomatis cepat kotak gedung mesin", "Malas pasang Mark Seam satu-satu buat objek kotak/gedung/meja? Pencet U -> 'Smart UV Project' atau 'Cube Projection' beres dalam 2 detik!"),
    ("UV & Texturing", "Texture Paint Mode", "Blender Texture Paint directly on 3D model tutorial", "lukis cat gambar langsung di badan model 3D", "Melukis warna, karat, kotoran, atau gambar tangan pakai kuas langsung di atas bodi model 3D lu maupun di kanvas 2D!"),

    # --- SHADING & NODES ---
    ("Shading & Nodes", "Shader Editor & Node Wrangler (Ctrl+T)", "Blender Shader Editor Node Wrangler PBR Texture setup", "pasang tekstur pbr kasar normal kabel node", "Aktifin add-on bawaan 'Node Wrangler', klik Principled BSDF lalu pencet **Ctrl+Shift+T** -> pilih semua file foto tekstur PBR lu sekaligus, otomatis terpasang lengkap!"),
    ("Shading & Nodes", "Color Ramp Node", "Blender Color Ramp Node Shader tutorial", "atur kontras warna gradasi toon cel shader", "Node paling sakti di Shader Editor! Mengubah hitam-putih tekstur jadi warna gradasi bebas atau bikin bayangan patah tegas ala kartun Anime (mode Constant)!"),
    ("Shading & Nodes", "Noise / Voronoi / Wave / Musgrave Procedural Nodes", "Blender Procedural Materials Noise Voronoi tutorial", "tekstur otomatis batu marmer kayu air karat", "Bikin corak batu, air, kayu, marmer, karat, atau kulit jeruk 100% dari matematika Node tanpa perlu download foto tekstur sama sekali!"),

    # --- GEOMETRY NODES ---
    ("Geometry Nodes", "Distribute Points on Faces + Instance on Points", "Blender Geometry Nodes Scatter Instances tutorial", "sebar ribuan pohon rumput batu instance", "Duo node paling terkenal di Geometry Nodes buat menanam ribuan rumput, bunga, kerikil, atau lampu kota secara super enteng!"),
    ("Geometry Nodes", "Simulation Zone & Repeat Zone", "Blender Geometry Nodes Simulation Zone Repeat Zone", "simulasi fisika partikel perulangan node", "Membuat simulasi partikel custom, jejak gerak (trails), pertumbuhan akar tanaman, atau perulangan fraktal di dalam Geometry Nodes."),

    # --- ANIMATION & RIGGING ---
    ("Animation & Rigging", "Keyframes (I), Timeline, Graph Editor & Dope Sheet", "Blender Keyframe Animation Graph Editor Beginner tutorial", "rekam gerakan animasi kurva halus melambat", "Pencet 'I' buat ngunci posisi di frame awal, pindah frame, geser objek, pencet 'I' lagi! Buka Graph Editor buat ngatur gerakan melambat mulus (Ease In/Out) atau memantul!"),
    ("Animation & Rigging", "Parent With Automatic Weights (Ctrl+P)", "Blender Rigging Parent With Automatic Weights tutorial", "sambungin badan ke tulang otomatis", "Klik model badan karakter dulu -> Shift+Klik kerangka tulang Armature -> pencet **Ctrl+P -> With Automatic Weights**! Badan langsung ikut nekuk pas tulang digerakin!"),
    ("Animation & Rigging", "Weight Paint Mode", "Blender Weight Paint Fix Rigging Deformation tutorial", "lukis bobot merah biru tulang ketarik salah", "Kalau pas kaki ditekuk rok/paha sebelahnya malah ikut ketarik melar, masuk ke Weight Paint Mode (Merah = ikut 100%, Biru = diam 0%) buat ngerapiin pengaruh tiap tulang!"),
    ("Animation & Rigging", "Rigify Auto-Rigging", "Blender Rigify Human Character Rigging tutorial", "rig otomatis manusia lengkap jari wajah ik", "Add-on bawaan Blender yang langsung membuatkan kerangka tulang manusia/hewan super lengkap (sudah ada kontrol IK/FK kaki tangan & jari!) tanpa ngerakit dari nol!"),

    # --- COMPOSITING & POST-PROCESSING ---
    ("Compositing", "Glare Node (Efek Cahaya Bloom / Fog Glow!)", "Blender Compositor Glare Fog Glow Bloom Blender 5 tutorial", "cahaya berpendar silau bintang bloom neon", "PENTING DI BLENDER MODERN: Efek pendaran cahaya lampu neon bersinar (Bloom) sekarang dipasang lewat **Compositor -> tambah node 'Glare' (tipe Fog Glow / Bloom)** + nyalain Viewport Compositor 'Always'!"),
    ("Compositing", "Cryptomatte, Lens Distortion & Color Balance", "Blender Compositing Beginner Post Processing tutorial", "edit warna akhir efek lensa pasca render", "Polesan akhir sesudah render langsung di dalam Blender supaya gambar kelihatan sinematik tajam tanpa perlu pindah aplikasi lain!"),
]


def build_smart_english_query(raw_text: str, for_youtube: bool = True) -> str:
    """Mengubah ketikan user (baik bahasa Indonesia gaul maupun Inggris) menjadi keyword Inggris Blender yang akurat!"""
    q = (raw_text or "").strip()
    if not q:
        return "Blender 3D beginner properties modifiers tutorial"

    q_low = q.lower()
    matched_en: list[str] = []

    for indo_phrase, en_term in INDO_TO_ENGLISH_TERMS:
        if indo_phrase in q_low:
            matched_en.append(en_term)

    # Cek kata per kata sederhana bila user mengetik campuran Indo
    word_map = {
        "cara": "",
        "pakai": "",
        "fungsi": "",
        "buat": "",
        "bikin": "",
        "gimana": "",
        "apa": "",
        "itu": "",
        "di": "",
        "halus": "smooth",
        "tumpul": "bevel",
        "lubang": "boolean difference",
        "potong": "cut boolean bisect",
        "cermin": "mirror",
        "tebal": "solidify thickness",
        "kaca": "glass transmission",
        "besi": "metallic",
        "logam": "metallic",
        "cahaya": "lighting emission",
        "bayangan": "shadow",
        "kamera": "camera",
        "lampu": "light",
        "kain": "cloth physics",
        "baju": "clothing cloth",
        "air": "water fluid liquid",
        "asap": "smoke mantaflow",
        "api": "fire mantaflow",
        "rambut": "hair curves",
        "rumput": "grass scatter",
        "tulang": "armature rigging bone",
        "wajah": "facial shape keys",
        "tekstur": "texture uv mapping",
        "warna": "material color shader",
        "animasi": "animation keyframe",
        "pahat": "sculpting",
        "garis": "curve line art",
        "lambat": "optimize faster render",
        "bintik": "denoise noise",
    }

    if matched_en:
        core = " ".join(dict.fromkeys(matched_en))
    else:
        tokens = []
        for tok in q.split():
            tl = tok.lower().strip(",.?!:;()[]")
            if tl in word_map:
                rep = word_map[tl]
                if rep:
                    tokens.append(rep)
            else:
                tokens.append(tok)
        core = " ".join(tokens).strip() or q

    if "blender" not in core.lower():
        core = f"Blender {core}"

    suffix = "tutorial" if for_youtube else "how to use explained"
    if suffix.split()[0] not in core.lower():
        core = f"{core} {suffix}"
    return " ".join(core.split())
