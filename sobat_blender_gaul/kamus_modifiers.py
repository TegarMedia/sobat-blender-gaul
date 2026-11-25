# SPDX-License-Identifier: GPL-3.0-or-later
"""Kamus Lengkap Bahasa Indonesia Gaul untuk SELURUH 83 Modifier Bawaan + Modifier Asset Baru Blender 5.2."""

from __future__ import annotations

# Format:
# MODIFIER_CATALOG[mod_id] = {
#     "name": Nama Inggris di UI Blender,
#     "category": Kategori di menu Add Modifier,
#     "orig_desc": Deskripsi bahasa Inggris persis dari Blender 5.2 RNA (untuk hover menu Add Modifier!),
#     "en_keyword": Keyword bahasa Inggris siap pakai buat YouTube / Google,
#     "fungsi": Penjelasan fungsi pakai bahasa gaul pemula,
#     "cara_pakai": Langkah simpel cara pakainya,
#     "tips": Tips anti-bingung buat pemula,
# }

MODIFIER_CATALOG: dict[str, dict[str, str]] = {
    # =========================================================================
    # GENERATE MODIFIERS (Pembuat & Pengganda Bentuk — Paling Sering Dipakai!)
    # =========================================================================
    "ARRAY": {
        "name": "Array",
        "category": "Generate",
        "orig_desc": "Create copies of the shape with offsets",
        "en_keyword": "Blender Array Modifier tutorial",
        "fungsi": "Tukang fotokopi berderet! Ngegandain 1 objek jadi berbaris rapi (kayak anak tangga, pagar, rel kereta, atau batu bata) otomatis.",
        "cara_pakai": "Pasang Array -> naikin 'Count' buat jumlah kopiannya -> atur arah gesernya di 'Relative Offset' (X/Y/Z).",
        "tips": "Kalau mau bikin barisan melingkar (kayak kelopak bunga/velg mobil), matiin Relative Offset terus nyalain 'Object Offset' pakai objek Empty yang diputar!",
    },
    "BEVEL": {
        "name": "Bevel",
        "category": "Generate",
        "orig_desc": "Generate sloped corners by adding geometry to the mesh's edges or vertices",
        "en_keyword": "Blender Bevel Modifier tutorial",
        "fungsi": "Bikin sudut/pinggiran objek yang tadinya tajem kayak silet jadi tumpul atau melengkung mulus biar kelihatan realistis & nangkep kilap cahaya!",
        "cara_pakai": "Pasang Bevel -> atur 'Amount' (lebar tumpulannya, kecilin aja misal 0.02m) -> naikin 'Segments' (ke 3–5) biar lengkungannya bulet mulus!",
        "tips": "WAJIB INGAT: Kalau hasil Bevel lu miring/gepeng sebelah, pencet Ctrl+A di Object Mode -> pilih 'Scale' dulu! Nyalain juga 'Harden Normals' kalau pakai Shade Auto Smooth.",
    },
    "BOOLEAN": {
        "name": "Boolean",
        "category": "Generate",
        "orig_desc": "Use another shape to cut, combine or perform a difference operation",
        "en_keyword": "Blender Boolean Modifier tutorial",
        "fungsi": "Mesin pelubang & penggabung bentuk! Pakai 1 objek lain buat motong/melubangi objek ini (kayak bikin lubang jendela di tembok) atau ngelem dua objek jadi satu.",
        "cara_pakai": "Bikin objek pemotong -> taruh menembus objek utama -> klik objek utama & pasang Boolean -> pilih 'Difference' (potong) atau 'Union' (gabung) -> klik pipet di kolom 'Object' ke objek pemotong, lalu sembunyiin objek pemotongnya (pencet H)!",
        "tips": " kalau hasil potongannya bolong error/hilang, coba ganti 'Solver' dari Exact ke 'Float' (atau Manifold), dan pastikan objek gak punya titik dobel (Merge by Distance).",
    },
    "BUILD": {
        "name": "Build",
        "category": "Generate",
        "orig_desc": "Cause the faces of the mesh object to appear or disappear one after the other over time",
        "en_keyword": "Blender Build Modifier animation tutorial",
        "fungsi": "Efek sulap muncul satu-satu! Bikin kepingan poligon objek lu merakit dirinya sendiri sedikit demi sedikit seiring jalannya animasi.",
        "cara_pakai": "Pasang Build -> atur 'Start Frame' (mulai muncul) & 'Length' (berapa frame sampe utuh) -> pencet Spacebar di timeline buat nonton animasinya! Centang 'Randomize' kalau mau munculnya acak keren.",
        "tips": "Urutan munculnya bisa lu atur rapi dari bawah ke atas pakai menu Mesh -> Sort Elements di Edit Mode.",
    },
    "DECIMATE": {
        "name": "Decimate",
        "category": "Generate",
        "orig_desc": "Reduce the geometry density",
        "en_keyword": "Blender Decimate Modifier reduce polygons tutorial",
        "fungsi": "Diet poligon instan! Nurunin jumlah titik/segitiga objek yang keberatan (misal hasil Sculpting jutaan titik) biar enteng tanpa banyak ngerusak bentuk luarnya.",
        "cara_pakai": "Pasang Decimate -> biarin mode 'Collapse' -> kecilin angka 'Ratio' pelan-pelan (misal dari 1.0 ke 0.2 artinya sisa 20% poligon aja) sambil pantau Face Count di bawahnya!",
        "tips": "Mode 'Un-Subdivide' enak banget buat ngebalikin model yang terlanjur di-Subdivide, sedangkan 'Planar' bagus buat objek kotak datar.",
    },
    "EDGE_SPLIT": {
        "name": "Edge Split",
        "category": "Generate",
        "orig_desc": "Split away joined faces at the edges",
        "en_keyword": "Blender Edge Split Modifier tutorial",
        "fungsi": "Memisahkan sambungan poligon di sudut yang tajam supaya bayangan halus (Shade Smooth) gak belepotan di tepi kotak/silinder.",
        "cara_pakai": "Pasang Edge Split -> atur 'Edge Angle' (sudut lebih tajam dari angka ini bakal dipisah tegas) atau tandain garis manual pakai Mark Sharp.",
        "tips": "Di Blender 5.2 modern, buat ngerapiin bayangan tanpa beneran merobek titik mesh, lebih disaranin pakai modifier 'Smooth by Angle' di menu Normals!",
    },
    "NODES": {
        "name": "Geometry Nodes",
        "category": "Generate",
        "orig_desc": "",
        "en_keyword": "Blender Geometry Nodes Modifier beginner tutorial",
        "fungsi": "Otak prosedural serba bisa di Blender! Bikin sistem otomatis pakai sambungan kabel Node — mulai dari nyebar hutan ribuan pohon, gedung otomatis, sampai efek VFX canggih.",
        "cara_pakai": "Pasang Geometry Nodes -> klik tombol '+ New' atau pilih Node Group yang udah ada -> buka workspace 'Geometry Nodes' buat ngerangkai node-nya!",
        "tips": "Semua input yang lu colok ke 'Group Input' di Geometry Nodes bakal otomatis nongol jadi tombol slider praktis di kotak modifier ini!",
    },
    "MASK": {
        "name": "Mask",
        "category": "Generate",
        "orig_desc": "Dynamically hide vertices based on a vertex group or armature",
        "en_keyword": "Blender Mask Modifier hide mesh under clothes tutorial",
        "fungsi": "Penyembunyi bagian badan! Nyembunyiin area titik tertentu berdasarkan Vertex Group atau tulang tanpa perlu ngehapus permanen.",
        "cara_pakai": "Bikin Vertex Group berisi titik badan yang ketutup baju -> pasang Mask -> pilih nama Vertex Group-nya -> klik tombol panah bolak-balik (<-> Invert) kalau mau nyembunyiin grup tersebut!",
        "tips": "Wajib banget dipakai karakter 3D berbusana supaya kulit badan gak tembus keluar (clipping) lewat baju waktu karakter lari/joget!",
    },
    "MIRROR": {
        "name": "Mirror",
        "category": "Generate",
        "orig_desc": "Mirror along the local X, Y and/or Z axes, over the object origin",
        "en_keyword": "Blender Mirror Modifier beginner tutorial",
        "fungsi": "Cermin ajaib penghemat waktu 50%! Lu cukup ngedit separuh sisi objek (misal separuh muka/mobil/pedang), sisi sebelahnya otomatis kebentuk kembar persis!",
        "cara_pakai": "Hapus separuh sisi objek di Edit Mode -> pasang Mirror -> pilih Axis (biasanya X) -> WAJIB centang 'Clipping' supaya titik tengah nempel rapet gak bisa robek nyebrang!",
        "tips": "Cermin selalu ngambil patokan dari 'Titik Oranye' (Origin) objek lu! Kalau mau cerminnya ngikut benda lain, isi kolom 'Mirror Object' pakai Empty.",
    },
    "MESH_TO_VOLUME": {
        "name": "Mesh to Volume",
        "category": "Generate",
        "orig_desc": "",
        "en_keyword": "Blender Mesh to Volume clouds tutorial",
        "fungsi": "Nyulap model 3D padat jadi gumpalan asap/awan empuk! Dipasang di objek Volume kosong terus ngambil bentuk dari objek Mesh pilihan lu.",
        "cara_pakai": "Pencet Shift+A -> Volume -> Empty -> pasang modifier 'Mesh to Volume' -> pilih objek Mesh sumber di kolom 'Object' -> atur Density & Voxel Amount!",
        "tips": "Kombinasi maut bikin awan Ghibli/realistis: tambahin modifier 'Volume Displace' tepat di bawah 'Mesh to Volume' pakai tekstur Clouds!",
    },
    "MULTIRES": {
        "name": "Multiresolution",
        "category": "Generate",
        "orig_desc": "Subdivide the mesh in a way that allows editing the higher subdivision levels",
        "en_keyword": "Blender Multiresolution Sculpting Modifier tutorial",
        "fungsi": "Kakaknya Subdivision Surface khusus buat **Sculpting (Memahat)**! Memecah poligon jadi super halus berlevel-level supaya lu bisa ngukir pori-pori kulit, tapi bisa balik ke level rendah kapan aja.",
        "cara_pakai": "Pasang Multiresolution di model dasar rapi -> klik tombol 'Subdivide' beberapa kali -> pindah ke Sculpt Mode & mulai memahat detail halus!",
        "tips": "Jangan klik Apply! Kehebatan Multires justru karena lu bisa nurunin 'Levels Viewport' biar enteng pas animasi, tapi 'Render' tetep di level tertinggi!",
    },
    "REMESH": {
        "name": "Remesh",
        "category": "Generate",
        "orig_desc": "Generate new mesh topology based on the current shape",
        "en_keyword": "Blender Remesh Modifier Voxel Blocks tutorial",
        "fungsi": "Daur ulang jaring poligon! Ngelebur seluruh permukaan objek (termasuk beberapa bagian terpisah) jadi satu kulit baru yang kerapatan kotak-kotaknya seragam.",
        "cara_pakai": "Pasang Remesh -> pilih mode 'Voxel' buat gabungin bentuk mulus (kecilkan 'Voxel Size' biar makin detail, hati-hati jangan langsung 0.001 nanti nge-hang!), atau mode 'Blocks' buat efek kotak-kotak Minecraft!",
        "tips": "Selesai Boolean banyak potongan berantakan? Kasih Remesh + Smooth Corrective biar nyatu mulus kayak besi cor!",
    },
    "SCREW": {
        "name": "Screw",
        "category": "Generate",
        "orig_desc": "Lathe around an axis, treating the input mesh as a profile",
        "en_keyword": "Blender Screw Modifier bottle vase spring tutorial",
        "fungsi": "Mesin bubut putar 360 derajat! Cukup gambar 1 garis siluet pinggir (profil separuh gelas, botol, guci, pion catur, atau per pegas), langsung diputar jadi objek 3D bulat utuh!",
        "cara_pakai": "Gambar garis siluet di sebelah kanan titik tengah -> pasang Screw -> pilih Axis putar (biasanya Z) -> naikin 'Steps' biar melingkarnya halus! Isi angka 'Screw' & naikin 'Iterations' kalau mau jadi ulir baut/per pegas!",
        "tips": "Kalau bayangan permukaan gelasnya item kebalik (merah di Face Orientation), centang 'Flip' di bagian Normals pada modifier Screw!",
    },
    "SKIN": {
        "name": "Skin",
        "category": "Generate",
        "orig_desc": "Create a solid shape from vertices and edges, using the vertex radius to define the thickness",
        "en_keyword": "Blender Skin Modifier tree character base mesh tutorial",
        "fungsi": "Pembungkus daging instan dari garis tulang! Cukup bikin rangka garis tipis (kayak orang-orangan lidi atau ranting pohon), Skin otomatis ngebungkus garis itu jadi pipa daging bervolume!",
        "cara_pakai": "Bikin garis dari titik-titik di Edit Mode -> pasang Skin -> di Edit Mode pilih titik lalu pencet **Ctrl + A** (bukan S!) terus geser mouse buat nggedein/ngecilin ketebalan daging di titik itu!",
        "tips": "Pasang 'Subdivision Surface' tepat di bawah modifier Skin biar hasilnya langsung bulet mulus kayak batang pohon atau karakter kartun!",
    },
    "SOLIDIFY": {
        "name": "Solidify",
        "category": "Generate",
        "orig_desc": "Make the surface thick",
        "en_keyword": "Blender Solidify Modifier thickness tutorial",
        "fungsi": "Pemberi ketebalan daging/dinding! Objek 3D standar (kayak Plane atau mangkok terbuka) itu aslinya setipis kertas 0mm; Solidify ngasih ketebalan nyata jadi kayak tembok, baju, kaca helm, atau kulit mangkok.",
        "cara_pakai": "Pasang Solidify -> geser angka 'Thickness' buat tebelnya -> atur 'Offset' (-1 menebal ke dalam, +1 menebal ke luar, 0 tengah-tengah) -> centang 'Even Thickness' biar sudut siku-sikunya gak mencong tipis!",
        "tips": "Trik Outline Kartun Anime (Inverted Hull): Pasang Solidify, kasih material hitam Emissive (Material Offset = 1), centang 'Flip' Normals + Backface Culling!",
    },
    "SUBSURF": {
        "name": "Subdivision Surface",
        "category": "Generate",
        "orig_desc": "Split the faces into smaller parts, giving it a smoother appearance",
        "en_keyword": "Blender Subdivision Surface Modifier tutorial",
        "fungsi": "MODIFIER PALING LEGENDARIS (Shortcut: Ctrl+1 / Ctrl+2)! Memecah kotak-kotak kaku kasar jadi lipatan poligon super mulus & membulat organik!",
        "cara_pakai": "Pasang Subdivision Surface -> atur 'Levels Viewport' cukup di angka 1 atau 2 (dan 'Render' di 2 atau 3, JANGAN langsung 6 nanti PC meledak hang!) -> klik kanan objek di layar lalu pilih 'Shade Smooth'!",
        "tips": "Kalau bentuk kotak lu malah menciut jadi bulet kayak bakso, masuk Edit Mode terus tambah Loop Cut (Ctrl+R) di deket pinggirannya (Supporting Loops) atau pakai Edge Crease (Shift+E)!",
    },
    "TRIANGULATE": {
        "name": "Triangulate",
        "category": "Generate",
        "orig_desc": "Convert all polygons to triangles",
        "en_keyword": "Blender Triangulate Modifier game export baking tutorial",
        "fungsi": "Memotong semua bidang segi-empat (Quad) atau segi-banyak (N-Gon) jadi segitiga rapi tanpa ngubah bentuk objek.",
        "cara_pakai": "Tinggal pasang paling bawah di tumpukan modifier (centang 'Keep Normals' biar bayangan gak berubah) sebelum export model ke Game Engine (Unreal/Unity) atau Substance Painter!",
        "tips": "Kenapa penting buat game? Biar cara pemotongan segitiganya konsisten antara Blender dan software baking tekstur!",
    },
    "VOLUME_TO_MESH": {
        "name": "Volume to Mesh",
        "category": "Generate",
        "orig_desc": "",
        "en_keyword": "Blender Volume to Mesh Modifier tutorial",
        "fungsi": "Kebalikannya Mesh to Volume! Mengubah gumpalan kabut/asap/VDB Volume jadi model jaring poligon padat (Mesh) yang bisa dikasih material biasa atau di-3D print.",
        "cara_pakai": "Bikin objek Mesh apa aja -> pasang 'Volume to Mesh' -> pilih objek Volume sumbernya -> atur 'Threshold' (batas kepadatan) & 'Voxel Amount' buat detailnya.",
        "tips": "Naikin 'Adaptivity' sedikit kalau mau area yang rata punya lebih sedikit segitiga biar lebih ringan.",
    },
    "WELD": {
        "name": "Weld",
        "category": "Generate",
        "orig_desc": "Find groups of vertices closer than dist and merge them together",
        "en_keyword": "Blender Weld Modifier merge vertices tutorial",
        "fungsi": "Tukang las titik otomatis! Nyari titik-titik (vertex) yang jaraknya dempet banget terus dilebur jadi satu titik tunggal.",
        "cara_pakai": "Taruh modifier Weld di bawah Array, Screw, atau Boolean -> naikin sedikit angka 'Distance' (misal 0.001m) sampai sambungan antar bagian nyatu mulus!",
        "tips": "Penyelamat hidup kalau habis pakai Screw atau Mirror terus di sambungannya ada garis belang gara-gara titik belum nyatu!",
    },
    "WIREFRAME": {
        "name": "Wireframe",
        "category": "Generate",
        "orig_desc": "Convert faces into thickened edges",
        "en_keyword": "Blender Wireframe Modifier cage sci-fi tutorial",
        "fungsi": "Nyulap seluruh garis jaring poligon objek jadi pipa besi rangka kawat (kayak jaring keranjang sampah, menara sutet, sangkar burung, atau hologram sci-fi)!",
        "cara_pakai": "Pasang Wireframe -> atur 'Thickness' buat tebel besinya! Mau kulit aslinya tetep ada di balik rangka? Matiin centang 'Replace Original' terus bedain warnanya pakai 'Material Offset'!",
        "tips": "Centang 'Even Thickness' biar ketebalan pipa besinya rata konsisten di semua belokan.",
    },

    # =========================================================================
    # DEFORM MODIFIERS (Pembengkok, Pelentur & Penempel Bentuk)
    # =========================================================================
    "ARMATURE": {
        "name": "Armature",
        "category": "Deform",
        "orig_desc": "Deform the shape using an armature object",
        "en_keyword": "Blender Armature Modifier rigging weight paint tutorial",
        "fungsi": "Penghubung daging model 3D ke kerangka tulang (Rig)! Supaya waktu tulangnya digerakin di Pose Mode, badan/baju karakter ikut menekuk hidup.",
        "cara_pakai": "Biasanya otomatis kepasang waktu lu pencet Ctrl+P -> 'With Automatic Weights' dari Mesh ke tulang! Kalau pasang manual, tinggal pilih objek kerangkanya di kolom 'Object'.",
        "tips": "Centang 'Preserve Volume' supaya siku dan lutut karakter gak kempes menciut waktu ditekuk ekstrim atau diputar!",
    },
    "CAST": {
        "name": "Cast",
        "category": "Deform",
        "orig_desc": "Shift the shape towards a predefined primitive",
        "en_keyword": "Blender Cast Modifier cube to sphere tutorial",
        "fungsi": "Mencetak/mendorong bentuk objek apapun supaya berubah mendekati bentuk Bola (Sphere), Tabung (Cylinder), atau Kotak (Cuboid)!",
        "cara_pakai": "Pastikan objek punya cukup banyak titik (Subdivide dulu!) -> pasang Cast -> pilih 'Cast Type' (misal Sphere) -> geser 'Factor' (0 = bentuk asli, 1 = jadi bola sempurna!).",
        "tips": "'Factor' ini bisa dianimasiin pakai keyframe (pencet I) buat efek morphing objek berubah bentuk jadi bola secara mulus!",
    },
    "CURVE": {
        "name": "Curve",
        "category": "Deform",
        "orig_desc": "Bend the mesh using a curve object",
        "en_keyword": "Blender Curve Modifier along path tutorial",
        "fungsi": "Membengkokkan objek lurus supaya meliuk ngikutin jalur garis lengkung (Curve) — wajib banget buat bikin rantai melingkar, jalan tol berbelok, sabuk, kabel, atau rel!",
        "cara_pakai": "Taruh objek & objek Bezier Curve di titik Origin yang SAMA persis -> pasang Curve Modifier di objek (di bawah Array kalau berderet!) -> pilih garisnya di 'Curve Object' -> coba ganti 'Deform Axis' (X/-X/Y) kalau arahnya melenceng!",
        "tips": "Masalah #1 pemula di Curve Modifier: objek melayang jauh berantakan! Solusinya: samain posisi Origin objek dan Origin Curve di satu titik yang sama (Shift+S -> Selection to Cursor)!",
    },
    "DISPLACE": {
        "name": "Displace",
        "category": "Deform",
        "orig_desc": "Offset vertices based on a texture",
        "en_keyword": "Blender Displace Modifier terrain rock texture tutorial",
        "fungsi": "Pembuat permukaan timbul-tenggelam beneran! Mendorong titik-titik poligon naik/turun mengikuti gelap-terangnya gambar tekstur (cocok buat bikin gunung, batu karang, ombak, atau ukiran timbul).",
        "cara_pakai": "Subdivide objek dulu biar titiknya banyak! -> pasang Displace -> klik '+ New' -> klik ikon paling kanan buat loncat ke Tab Texture & pilih misal 'Clouds' -> balik ke Modifier & atur 'Strength'!",
        "tips": "Makin banyak titik poligon (pasang Subdivision Surface DI ATAS Displace!), makin tajam dan halus detail tonjolan teksturnya!",
    },
    "HOOK": {
        "name": "Hook",
        "category": "Deform",
        "orig_desc": "Deform specific points using another object",
        "en_keyword": "Blender Hook Modifier rope curve animation tutorial",
        "fungsi": "Kait pancing penarik titik! Mengikat beberapa titik di Edit Mode ke sebuah objek luar (misal Empty), jadi lu bisa narik-ulur ujung kabel atau kain langsung dari Object Mode!",
        "cara_pakai": "Cara tercepat: Masuk Edit Mode -> pilih titik yang mau dikait -> pencet **Ctrl + H** -> pilih 'Hook to New Object'! Otomatis muncul Empty pegangan + modifier Hook!",
        "tips": "Enak banget dipakai di ujung Bezier Curve buat bikin kabel goyang atau tali busur panah yang ditarik tangan karakter!",
    },
    "LAPLACIANDEFORM": {
        "name": "Laplacian Deform",
        "category": "Deform",
        "orig_desc": "Deform based a series of anchor points",
        "en_keyword": "Blender Laplacian Deform Modifier tutorial",
        "fungsi": "Pembengkok pintar yang tetep ngejaga detail ukiran permukaan (kayak sisik naga atau urat otot) tetap utuh waktu bagian badannya ditekuk pakai titik jangkar (Anchors).",
        "cara_pakai": "Bikin Vertex Group berisi titik jangkar penahan & penarik -> pilih di 'Anchors Vertex Group' -> klik tombol 'Bind' -> gerakin titik jangkar pakai modifier Hook!",
        "tips": "Klik 'Bind' waktu bentuk masih di posisi awal normal sebelum titik jangkarnya digeser.",
    },
    "LATTICE": {
        "name": "Lattice",
        "category": "Deform",
        "orig_desc": "Deform using the shape of a lattice object",
        "en_keyword": "Blender Lattice Modifier cartoon eye squash stretch tutorial",
        "fungsi": "Kandang karet pembengkok! Masukin objek rumit ke dalam kotak jaring 'Lattice', terus cukup tarik sudut kandang Lattice-nya buat melengkungin seluruh isi objek dengan mulus!",
        "cara_pakai": "Pencet Shift+A -> Lattice, gedein di Object Mode sampe membungkus objek lu -> klik objek utama -> pasang Lattice Modifier -> pilih kandangnya di kolom 'Object' -> edit bentuk kandang Lattice di Edit Mode!",
        "tips": "Trik Rahasia Animator Kartun: Bola mata lonjong/gepeng di film animasi tetep bisa melirik mulus tanpa keluar kelopak mata berkat Lattice Modifier!",
    },
    "MESH_DEFORM": {
        "name": "Mesh Deform",
        "category": "Deform",
        "orig_desc": "Deform using a different mesh, which acts as a deformation cage",
        "en_keyword": "Blender Mesh Deform cage rigging tutorial",
        "fungsi": "Mirip Lattice, tapi kandang karet pembungkusnya bebas pakai model Mesh low-poly bentuk apa aja buatan lu sendiri!",
        "cara_pakai": "Bikin mesh kasar tertutup (cage) yang ngebungkus penuh karakter/baju detail lu -> pasang Mesh Deform di model detail -> pilih cage di 'Object' -> klik tombol 'Bind'!",
        "tips": "Sering dipakai studio profesional buat ngegerakin baju berlapis-lapis yang super rumit cukup dengan menggerakkan 1 kandang baju low-poly!",
    },
    "SHRINKWRAP": {
        "name": "Shrinkwrap",
        "category": "Deform",
        "orig_desc": "Project the shape onto another object",
        "en_keyword": "Blender Shrinkwrap Modifier sticker retopology clothes tutorial",
        "fungsi": "Plastik vakum penempel permukaan! Memaksa titik-titik objek ini nempel plek ketiplek mengikuti lekukan permukaan objek lain (kayak nempel stiker/decal ke bodi mobil melengkung, sabuk di perut, atau Retopology!).",
        "cara_pakai": "Pasang Shrinkwrap -> pilih objek tujuan tempat nempel di kolom 'Target' -> naikin sedikit angka 'Offset' (misal 0.002m) biar stiker/bajunya gak tenggelam kedap-kedip (Z-fighting) sama permukaan target!",
        "tips": "Coba ganti 'Wrap Method' ke 'Project' (centang Negative & Positive) kalau mau nembak stiker lurus ke permukaan melengkung!",
    },
    "SIMPLE_DEFORM": {
        "name": "Simple Deform",
        "category": "Deform",
        "orig_desc": "Deform the shape by twisting, bending, tapering or stretching",
        "en_keyword": "Blender Simple Deform Twist Bend Taper Stretch tutorial",
        "fungsi": "4 jurus bengkok instan dalam 1 tombol: **Twist** (plintir kayak permen/bor), **Bend** (lengkungin jadi busur/lingkaran), **Taper** (runcingin atas/bawah), & **Stretch** (gepeng-melar)!",
        "cara_pakai": "Pastikan objek punya banyak potongan garis (Loop Cut / Subdivide) biar bisa melengkung! -> pasang Simple Deform -> pilih tab Twist/Bend/Taper/Stretch -> ganti Axis (X/Y/Z) & geser Angle/Factor!",
        "tips": "Kalau arah lengkung Bend bikin pusing muter aneh, bikin objek Empty (Shift+A -> Empty), taruh di tengah, lalu pilih Empty itu di kolom 'Origin' pada Simple Deform — tinggal putar Empty-nya!",
    },
    "SMOOTH": {
        "name": "Smooth",
        "category": "Deform",
        "orig_desc": "Smooth the mesh by flattening the angles between adjacent faces",
        "en_keyword": "Blender Smooth Modifier mesh vertices tutorial",
        "fungsi": "Setrika perata poligon! Menggeser posisi titik-titik yang menonjol tajam supaya permukaannya makin rata dan lembut (TANPA nambah jumlah poligon baru).",
        "cara_pakai": "Pasang Smooth -> atur 'Factor' (kekuatan setrika) dan naikin 'Repeat' (berapa kali disetrika ulang) sampai kerutannya hilang.",
        "tips": "Isi kolom 'Vertex Group' kalau lu cuma mau nyetrika halus bagian sambungan leher aja tanpa bikin hidung karakter ikut rata!",
    },
    "CORRECTIVE_SMOOTH": {
        "name": "Smooth Corrective",
        "category": "Deform",
        "orig_desc": "Smooth the mesh while still preserving the volume",
        "en_keyword": "Blender Corrective Smooth rigging elbow knee tutorial",
        "fungsi": "Pelembut pintar penjaga bentuk! Ngerapiin lipatan patah-patah yang jelek (terutama di ketiak, siku, atau selangkangan waktu tulang karakter ditekuk) sambil tetep menjaga bentuk asli model.",
        "cara_pakai": "Taruh 'Smooth Corrective' tepat DI BAWAH modifier Armature -> centang 'Only Smooth' biar area yang lagi gak ketekuk gak ikut berubah -> naikin 'Repeat' secukupnya!",
        "tips": "Senjata rahasia rigger biar lipatan sendi karakter kelihatan lentur alami tanpa harus capek benerin Weight Paint berjam-jam!",
    },
    "LAPLACIANSMOOTH": {
        "name": "Smooth Laplacian",
        "category": "Deform",
        "orig_desc": "Reduce the noise on a mesh surface with minimal changes to its shape",
        "en_keyword": "Blender Laplacian Smooth 3D scan noise tutorial",
        "fungsi": "Penghalus bintik kasar (noise) tingkat lanjut! Menghilangkan gerigi kasar (misal dari hasil 3D Scan) tapi berusaha keras menjaga siluet bentuk utamanya gak menciut kurus.",
        "cara_pakai": "Pasang Smooth Laplacian -> geser kecil 'Lambda Factor' & 'Repeat' sampai bintik kasarnya hilang tapi fitur wajah/sudut pentingnya tetap terjaga.",
        "tips": "Sangat berguna buat bersihin hasil 3D photogrammetry atau hasil konversi Volume to Mesh.",
    },
    "SURFACE_DEFORM": {
        "name": "Surface Deform",
        "category": "Deform",
        "orig_desc": "Transfer motion from another mesh",
        "en_keyword": "Blender Surface Deform clothes on cloth proxy tutorial",
        "fungsi": "Penumpang gerak permukaan! Ngikat objek detail (kayak kancing baju, kantong, sabuk, atau baju berlapis) ke selembar kain tipis supaya ikut berkibar bareng tanpa perlu ikutan dihitung berat-berat di simulasi!",
        "cara_pakai": "Pasang Surface Deform di objek detail -> pilih lembaran mesh penggeraknya di kolom 'Target' -> klik tombol **'Bind'** -> waktu targetnya gerak/simulasi Cloth, objek detail otomatis nempel ngikut!",
        "tips": "Cara paling ringan simulasi baju detail: simulasikan kain polos low-poly aja pakai Cloth, terus tempelin baju berenda/kancing tinggi poligon pakai Surface Deform!",
    },
    "WARP": {
        "name": "Warp",
        "category": "Deform",
        "orig_desc": "Warp parts of a mesh to a new location in a very flexible way thanks to 2 specified objects",
        "en_keyword": "Blender Warp Modifier bulge deform tutorial",
        "fungsi": "Penarik benjolan di antara 2 titik objek! Menggeser sebagian permukaan mesh dari posisi 'Object From' menuju 'Object To' dengan pinggiran melengkung mulus.",
        "cara_pakai": "Bikin 2 Empty (From & To) -> pasang Warp di mesh berpoligon rapat -> isi From & To -> geser 'Object To' buat bikin efek tonjolan berjalan di bawah kulit/karpet!",
        "tips": "Atur bentuk lengkungan tonjolannya di bagian 'Falloff' (Smooth, Sphere, Sharp, atau Custom Curve).",
    },
    "WAVE": {
        "name": "Wave",
        "category": "Deform",
        "orig_desc": "Adds a ripple-like motion to an object's geometry",
        "en_keyword": "Blender Wave Modifier water ripple flag animation tutorial",
        "fungsi": "Pembuat gelombang riak otomatis! Bikin permukaan objek bergelombang naik-turun terus-menerus kayak riak tetesan air, bendera berkibar ringan, atau gerakan ular.",
        "cara_pakai": "Subdivide objek dulu biar banyak segmen -> pasang Wave -> pencet Play (Spacebar)! Atur 'Height' (tinggi ombak), 'Width' (lebar jarak antar ombak), dan 'Speed' (kecepatan rambat)!",
        "tips": "Matikan salah satu centang X atau Y di bagian Motion kalau lu mau gelombangnya jalan satu arah lurus (kayak bendera/ombak pantai), bukan melingkar dari tengah!",
    },
    "VOLUME_DISPLACE": {
        "name": "Volume Displace",
        "category": "Deform",
        "orig_desc": "Deform volume based on noise or other vector fields",
        "en_keyword": "Blender Volume Displace realistic clouds tutorial",
        "fungsi": "Pengacak pinggiran awan Volume! Mengacak bentuk objek Volume pakai tekstur Clouds/Noise supaya pinggirannya kribo berbulu alami kayak awan sungguhan di langit!",
        "cara_pakai": "Tambahkan di objek Volume (di bawah Mesh to Volume) -> klik '+ New' buat bikin tekstur -> ganti tipe tekstur ke 'Clouds' -> atur 'Strength' di modifier!",
        "tips": "Pakai 2 tumpuk Volume Displace (satu ukuran besar buat siluet gumpalan, satu ukuran kecil buat serabut tipis pinggirannya) biar awannya kelihatan super nyata!",
    },

    # =========================================================================
    # NORMALS & EDIT MODIFIERS (Perapi Cahaya, UV & Data Titik)
    # =========================================================================
    "NORMAL_EDIT": {
        "name": "Normal Edit",
        "category": "Normals",
        "orig_desc": "Modify the direction of the surface normals",
        "en_keyword": "Blender Normal Edit Modifier stylized foliage tree tutorial",
        "fungsi": "Pengarah pantulan cahaya palsu! Memutar arah 'Normal' (arah hadap cahaya) permukaan tanpa ngubah bentuk titiknya — WAJIB banget buat bikin daun pohon anime/Ghibli kelihatan empuk menyatu!",
        "cara_pakai": "Buat daun pohon: pasang Normal Edit -> pilih mode 'Radial' (nyebar bulat dari tengah pohon) atau 'Directional' ke arah lampu!",
        "tips": "Ini rahasia nomor #1 kenapa dedaunan pohon 3D ala game Genshin Impact / film Ghibli kelihatan lembut gak kotak-kotak padahal dari lembaran poligon tipis!",
    },
    "WEIGHTED_NORMAL": {
        "name": "Weighted Normal",
        "category": "Normals",
        "orig_desc": "Modify the direction of the surface normals using a weighting method",
        "en_keyword": "Blender Weighted Normal Bevel hard surface tutorial",
        "fungsi": "Pengkilap permukaan robot/mesin (Hard-Surface)! Bikin bidang datar gede tetep memantulkan cahaya lurus sempurna tanpa melengkung belang gara-gara sudut Bevel.",
        "cara_pakai": "Pasang Bevel (Segments=1 atau 2) -> pasang 'Smooth by Angle' -> taruh 'Weighted Normal' paling bawah & centang 'Keep Sharp'! Permukaan mesin langsung rata kinclong!",
        "tips": "Pasangan sejati Bevel Modifier saat bikin mobil, senjata, gedung, atau gadget!",
    },
    "DATA_TRANSFER": {
        "name": "Data Transfer",
        "category": "Edit",
        "orig_desc": "Transfer several types of data (vertex groups, UV maps, vertex colors, custom normals) from one mesh to another",
        "en_keyword": "Blender Data Transfer Modifier custom normals weight paint tutorial",
        "fungsi": "Mesin fotokopi data jeroan antar objek! Nyalin Weight Paint tulang (Vertex Groups), arah kilap cahaya (Custom Normals), atau UV Map dari objek A yang rapi ke objek B!",
        "cara_pakai": "Contoh nyalin Weight Paint badan ke baju baru: klik Baju -> pasang Data Transfer -> pilih Badan di 'Source' -> centang 'Vertex Data' -> klik tombol 'Vertex Groups' -> klik **'Generate Data Layers'** -> Apply!",
        "tips": "Trik hemat waktu berjam-jam: tiap bikin baju baru buat karakter yang udah ber-rigging, tinggal salin bobot tulangnya dari kulit badan pakai Data Transfer!",
    },
    "MESH_CACHE": {
        "name": "Mesh Cache",
        "category": "Edit",
        "orig_desc": "Deform the mesh using an external frame-by-frame vertex transform cache",
        "en_keyword": "Blender Mesh Cache MDD PC2 tutorial",
        "fungsi": "Pemutar rekaman gerakan titik (.mdd / .pc2) dari software 3D luar (kayak simulasi baju dari Marvelous Designer) ke objek Mesh di Blender.",
        "cara_pakai": "Pastikan jumlah titik objek sama persis -> pasang Mesh Cache -> pilih format MDD/PC2 -> arahin File Path ke file cache animasinya.",
        "tips": "Untuk pipeline modern antar software 3D sekarang lebih sering pakai 'Mesh Sequence Cache' dengan file Alembic (.abc).",
    },
    "MESH_SEQUENCE_CACHE": {
        "name": "Mesh Sequence Cache",
        "category": "Edit",
        "orig_desc": "Deform the mesh or curve using an external mesh cache in Alembic format",
        "en_keyword": "Blender Mesh Sequence Cache Alembic USD tutorial",
        "fungsi": "Pemutar animasi cache file **Alembic (.abc)** atau **USD** dari simulasi luar (Houdini, Marvelous Designer, EmberGen) secara mulus tiap frame.",
        "cara_pakai": "Otomatis terpasang saat lu klik File -> Import -> Alembic (.abc)! Di dalamnya lu bisa ngatur kecepatan waktu atau ganti Object Path.",
        "tips": "Sangat berguna buat memutar ulang simulasi air/kain berat yang sudah di-export jadi file Alembic ringan.",
    },
    "UV_PROJECT": {
        "name": "UV Project",
        "category": "Edit",
        "orig_desc": "Project the UV map coordinates from the negative Z axis of another object",
        "en_keyword": "Blender UV Project Modifier camera decal sticker tutorial",
        "fungsi": "Proyektor bioskop buat gambar tekstur! Nembakin koordinat UV gambar lurus dari arah kamera atau objek Empty ke permukaan 3D (enak buat geser-geser stiker/grafiti atau Camera Projection!).",
        "cara_pakai": "Pasang UV Project -> pilih UV Map yang dipakai -> tambahin Projector -> pilih Kamera atau Empty penembaknya (pastikan Aspect X/Y sesuai ukuran foto!).",
        "tips": "Sering dipakai buat animasi wajah 2D Lego/kartun: muka gambar 2D bisa digeser-geser posisinya di kepala 3D cuma dengan menggeser Empty!",
    },
    "UV_WARP": {
        "name": "UV Warp",
        "category": "Edit",
        "orig_desc": "Transform the UV map using the difference between two objects",
        "en_keyword": "Blender UV Warp 2D eye mouth rig tutorial",
        "fungsi": "Penggeser gambar tekstur pakai tulang/Empty! Menggeser, memutar, atau membesar-kecilkan posisi UV tekstur berdasarkan jarak gerak dari Object From ke Object To.",
        "cara_pakai": "Pasang UV Warp -> pilih UV Map mata/mulut 2D -> isi 'Object From' (tulang diam dasar) & 'Object To' (tulang penggerak) -> gerakin tulang penggerak buat ganti ekspresi/lirikan mata 2D!",
        "tips": "Andalan utama karakter anime/game chibi yang matanya pakai gambar tekstur 2D supaya bisa kedip dan ngelirik pakai Rig!",
    },
    "VERTEX_WEIGHT_EDIT": {
        "name": "Vertex Weight Edit",
        "category": "Edit",
        "orig_desc": "Modify of the weights of a vertex group",
        "en_keyword": "Blender Vertex Weight Edit Modifier tutorial",
        "fungsi": "Pengolah kurva bobot Vertex Group secara live! Bisa mempertajam, membalik, atau menambah/menghapus titik ke dalam Vertex Group pakai kurva atau tekstur.",
        "cara_pakai": "Pilih nama 'Vertex Group' -> atur Falloff Type (misal Smooth/Custom Curve) atau masukin Mask Texture buat memodifikasi bobot grup secara dinamis.",
        "tips": "Sering dikombinasikan sebelum modifier Displace, Mask, atau Particle supaya efeknya berubah dinamis.",
    },
    "VERTEX_WEIGHT_MIX": {
        "name": "Vertex Weight Mix",
        "category": "Edit",
        "orig_desc": "Mix the weights of two vertex groups",
        "en_keyword": "Blender Vertex Weight Mix Modifier tutorial",
        "fungsi": "Pencampur dua Vertex Group! Menggabungkan, mengurangi, atau mengalikan isi bobot dari Grup B ke dalam Grup A (mirip Blend Mode layer di Photoshop).",
        "cara_pakai": "Pilih 'Vertex Group A' (target yang mau diubah) dan 'Vertex Group B' (pencampurnya) -> pilih 'Mix Mode' (Add = tambah, Subtract = kurangi, Multiply = irisan).",
        "tips": "Taruh DI ATAS modifier yang memakai Vertex Group A supaya hasil campurannya langsung terbaca oleh modifier di bawahnya!",
    },
    "VERTEX_WEIGHT_PROXIMITY": {
        "name": "Vertex Weight Proximity",
        "category": "Edit",
        "orig_desc": "Set the vertex group weights based on the distance to another target object",
        "en_keyword": "Blender Vertex Weight Proximity dynamic effect tutorial",
        "fungsi": "Sensor jarak otomatis! Mengubah nilai bobot Vertex Group berdasarkan seberapa DEKAT permukaan objek ini dengan objek Target lain!",
        "cara_pakai": "Bikin Vertex Group (isi semua titik bobot 1.0) -> pasang Vertex Weight Proximity -> pilih grupnya & pilih 'Target Object' -> atur jarak 'Lowest' & 'Highest' -> pakai grup itu di Displace/Mask/Geometry Nodes di bawahnya!",
        "tips": "Keren banget buat efek tanah otomatis amblas/menyala pas dideketin kaki karakter atau bola lewat!",
    },

    # =========================================================================
    # PHYSICS MODIFIERS (Jembatan Urutan Simulasi Fisika di Modifier Stack)
    # =========================================================================
    "CLOTH": {
        "name": "Cloth",
        "category": "Physics",
        "orig_desc": "Physic simulation for cloth",
        "en_keyword": "Blender Cloth Modifier stack order tutorial",
        "fungsi": "Representasi simulasi Kain (Cloth) di dalam tumpukan Modifier! Semua tombol pengaturannya ada di **Tab Physics**, tapi urutannya diatur di sini!",
        "cara_pakai": "Tips Urutan Emas: Taruh Armature DI ATAS Cloth, dan taruh Subdivision Surface + Solidify DI BAWAH Cloth biar simulasi ringan tapi hasilnya mulus dan tebal!",
        "tips": "Klik tombol loncat ke Tab Physics buat ngatur bahan kain (Silk/Cotton), Self Collisions, Pin Group, dan Pressure!",
    },
    "COLLISION": {
        "name": "Collision",
        "category": "Physics",
        "orig_desc": "For colliders participating in physics simulation, control which level in the modifier stack is used as the collision surface",
        "en_keyword": "Blender Collision Modifier physics tutorial",
        "fungsi": "Penanda tumbukan fisika di tumpukan Modifier! Supaya objek ini bisa nahan kain (Cloth), Soft Body, dan Partikel biar gak tembus.",
        "cara_pakai": "Kalau objek badan ini punya Armature, pastikan Collision ditaruh DI BAWAH Armature supaya tumbukannya ngikut gerakan badan karakter! Detailnya atur di Tab Physics.",
        "tips": "Kalau kain masih agak melayang jauh dari badan, buka Tab Physics -> Collision -> kecilin angka 'Thickness Outer' (misal ke 0.002).",
    },
    "DYNAMIC_PAINT": {
        "name": "Dynamic Paint",
        "category": "Physics",
        "orig_desc": "Turn objects into paint canvases and brushes, creating color attributes, image sequences, or displacement",
        "en_keyword": "Blender Dynamic Paint footprints rain ripples tutorial",
        "fungsi": "Sistem Kanvas & Kuas sentuh otomatis! Bikin objek meninggalkan jejak cat warna, basah air hujan, riak ombak, atau jejak kaki penyok di salju saat bersentuhan.",
        "cara_pakai": "Pengaturan lengkapnya ada di **Tab Physics -> Dynamic Paint** (set lantai jadi 'Canvas' dan sepatu/bola jadi 'Brush').",
        "tips": "Pastikan objek Canvas punya cukup banyak titik poligon kalau pakai format Vertex (atau pakai Image Sequence kalau low-poly).",
    },
    "EXPLODE": {
        "name": "Explode",
        "category": "Physics",
        "orig_desc": "Break apart the mesh faces and let them follow particles",
        "en_keyword": "Blender Explode Modifier shatter object tutorial",
        "fungsi": "Peledak kepingan poligon! Memecah permukaan objek berkeping-keping lalu menerbangkannya mengikuti lontaran sistem Partikel!",
        "cara_pakai": "WAJIB pasang **Particle System** dulu di objek ini (atau lewat menu Object -> Quick Effects -> Quick Explode!) -> baru pasang modifier Explode DI BAWAH Particle System!",
        "tips": "Tambahin modifier 'Solidify' tepat di bawah Explode biar serpihan pecahannya punya ketebalan kayak pecahan kaca/tembok beneran!",
    },
    "FLUID": {
        "name": "Fluid",
        "category": "Physics",
        "orig_desc": "Physics simulation for fluids, like water, oil and smoke",
        "en_keyword": "Blender Fluid Simulation water smoke fire tutorial",
        "fungsi": "Jembatan simulasi cairan (Air/Madu) dan gas (Asap/Api Mantaflow). Semua pengaturan Domain, Flow, dan Bake ada di **Tab Physics**!",
        "cara_pakai": "Buat pemula yang mau langsung jadi dalam 3 detik: klik objek -> buka menu atas **Object -> Quick Effects -> Quick Smoke** atau **Quick Liquid**, terus pencet Play!",
        "tips": "Kalau simulasi air/asap gak nongol pas ganti settingan, buka Tab Physics -> bagian Cache -> ganti Type ke 'Modular' atau 'Replay' lalu klik Free/Bake.",
    },
    "OCEAN": {
        "name": "Ocean",
        "category": "Physics",
        "orig_desc": "Generate a moving ocean surface",
        "en_keyword": "Blender Ocean Modifier realistic sea waves foam tutorial",
        "fungsi": "Generator lautan berombak instan! Langsung nyulap satu objek apa aja jadi hamparan ombak samudra realistis lengkap dengan data buih putih (Foam)!",
        "cara_pakai": "Pasang Ocean -> naikin 'Resolution Viewport/Render' biar tajam -> buat animasi ombak gerak: klik titik di samping angka **'Time'** di frame 1 (pencet I), pindah ke frame 250, naikin Time jadi 8, pencet I lagi!",
        "tips": "Centang bagian 'Foam' dan isi Data Layer Name (misal 'foam'), lalu panggil pakai node Attribute('foam') di Shader Editor buat ngasih buih putih di puncak ombak!",
    },
    "PARTICLE_INSTANCE": {
        "name": "Particle Instance",
        "category": "Physics",
        "orig_desc": "Duplicate mesh at the location of particles",
        "en_keyword": "Blender Particle Instance Modifier trails tutorial",
        "fungsi": "Pengganda sekaligus pelentur objek mengikuti jejak partikel dari objek lain (bahkan bisa memanjang melengkung mengikuti ekor lintasan partikel!).",
        "cara_pakai": "Pasang di objek yang mau digandain -> pilih objek pemilik partikel di kolom 'Object' -> centang 'Create Along Paths' kalau mau objeknya melengkung di sepanjang garis rambut/jejak partikel.",
        "tips": "Uniknya dibanding Render As Object biasa: objeknya beneran ikut melengkung (deform) mengikuti belokan jalur partikel!",
    },
    "PARTICLE_SYSTEM": {
        "name": "Particle System",
        "category": "Physics",
        "orig_desc": "Spawn particles from the shape",
        "en_keyword": "Blender Particle System stack order tutorial",
        "fungsi": "Penanda posisi Particle System di dalam tumpukan Modifier (pengaturan lengkapnya ada di **Tab Particles**!).",
        "cara_pakai": "Kalau objek lu pakai Subdivision Surface atau Mirror, centang 'Use Modifier Stack' di Tab Particles -> Emission -> Source supaya partikel keluar mengikuti bentuk yang sudah dihaluskan!",
        "tips": "Urutan di sini menentukan apakah partikel keluar dari bentuk sebelum atau sesudah modifier lain dijalankan.",
    },
    "SOFT_BODY": {
        "name": "Soft Body",
        "category": "Physics",
        "orig_desc": "Simulate soft deformable objects",
        "en_keyword": "Blender Soft Body jelly bounce physics tutorial",
        "fungsi": "Penanda simulasi benda kenyal/membal (agar-agar, bola karet kempes, jiggle) di tumpukan Modifier. Pengaturan lengkapnya ada di **Tab Physics**!",
        "cara_pakai": "Buka Tab Physics -> kalau mau objek jatuh membal di lantai, matiin centang 'Goal' lalu nyalain 'Edges' (naikin nilai Bending biar gak letoy kempes rata)!",
        "tips": "Taruh Subdivision Surface DI BAWAH Soft Body supaya perhitungan fisika tetap ngebut ringan tapi tampilan luarnya mulus!",
    },
    "SURFACE": {
        "name": "Surface",
        "category": "Physics",
        "orig_desc": "",
        "en_keyword": "Blender Physics Collision Surface Modifier",
        "fungsi": "Modifier internal otomatis milik Blender yang muncul sendiri saat objek diaktifkan sebagai penahan tumbukan (Collision/Deflection) untuk menyimpan kecepatan gerak permukaan.",
        "cara_pakai": "Tidak perlu dipasang manual — otomatis dikelola Blender waktu lu menyalakan Collision atau Brush fisika di Tab Physics.",
        "tips": "Biarkan posisinya sesuai urutan permukaan yang ingin dijadikan batas tabrakan.",
    },

    # =========================================================================
    # GREASE PENCIL MODIFIERS (Modifier Khusus Objek Gambar 2D/3D Grease Pencil)
    # =========================================================================
    "LINEART": {
        "name": "Line Art",
        "category": "Grease Pencil",
        "orig_desc": "Generate Line Art from scene geometries",
        "en_keyword": "Blender Grease Pencil Line Art anime outline tutorial",
        "fungsi": "TINTA KOMIK/ANIME OTOMATIS! Ngegambar garis tepi tinta 2D yang super rapi mengikuti siluet objek 3D atau satu Collection penuh dilihat dari sudut pandang Kamera!",
        "cara_pakai": "Pastikan sudah ada Kamera di scene! -> Pencet Shift+A -> Grease Pencil -> Empty (atau langsung Collection Line Art!) -> di modifier Line Art pilih Source Type (Collection/Object), Layer, dan Material tinta hitamnya!",
        "tips": "Hasil garis Line Art selalu dihitung dari sudut pandang **Active Camera**, jadi cek hasilnya lewat Numpad 0 (Camera View)!",
    },
    "GREASE_PENCIL_ARRAY": {
        "name": "Array (Grease Pencil)",
        "category": "Grease Pencil",
        "orig_desc": "Duplicate strokes into an array",
        "en_keyword": "Blender Grease Pencil Array Modifier tutorial",
        "fungsi": "Menggandakan goresan gambar 2D Grease Pencil berderet otomatis lengkap dengan variasi acak posisi, putaran, dan ukuran!",
        "cara_pakai": "Pasang di objek Grease Pencil -> atur 'Count' & 'Relative/Constant Offset' untuk menduplikasi gambar.",
        "tips": "Buka sub-panel 'Randomize' buat bikin barisan rumput/pagar gambar tangan kelihatan sedikit beda-beda alami!",
    },
    "GREASE_PENCIL_BUILD": {
        "name": "Build (Grease Pencil)",
        "category": "Grease Pencil",
        "orig_desc": "Grease Pencil build modifier",
        "en_keyword": "Blender Grease Pencil Build Modifier handwriting animation tutorial",
        "fungsi": "ANIMASI MENULIS / MENGGAMBAR SENDIRI! Bikin goresan tangan Grease Pencil muncul tergambar dari ujung awal sampai akhir seolah lagi dilukis live!",
        "cara_pakai": "Gambar sesuatu pakai Grease Pencil -> pasang Build -> pilih Mode 'Sequential' (satu goresan kelar baru lanjut berikutnya) atau 'Concurrent' (barengan) -> pencet Play!",
        "tips": "Favorit banget buat bikin video explainer papan tulis, tanda tangan bergerak, atau efek sketsa hidup!",
    },
    "GREASE_PENCIL_DASH": {
        "name": "Dot Dash",
        "category": "Grease Pencil",
        "orig_desc": "Generate dot-dash styled strokes",
        "en_keyword": "Blender Grease Pencil Dot Dash Modifier tutorial",
        "fungsi": "Mengubah garis sambung utuh jadi garis putus-putus atau titik-garis otomatis (kayak jalur peta harta karun atau garis potong gunting)!",
        "cara_pakai": "Pasang Dot Dash -> atur panjang garis ('Dash') dan jarak celah kosongnya ('Gap') -> animasiin nilai 'Segment Offset' biar garis putus-putusnya kelihatan jalan berbaris!",
        "tips": "Kamu bisa nambah beberapa segmen pola berbeda biar ritme titik-garisnya bervariasi.",
    },
    "GREASE_PENCIL_ENVELOPE": {
        "name": "Envelope",
        "category": "Grease Pencil",
        "orig_desc": "Create an envelope shape",
        "en_keyword": "Blender Grease Pencil Envelope Modifier tutorial",
        "fungsi": "Menghubungkan titik-titik goresan yang berjauhan dengan jaring garis jaring laba-laba / kaligrafi bayangan artistik.",
        "cara_pakai": "Pasang Envelope -> atur nilai 'Spread' (seberapa jauh jangkauan titik yang saling disambungkan) dan 'Thickness'.",
        "tips": "Keren banget buat efek sketsa arsitektur kasar atau bayangan komik cross-hatching instan!",
    },
    "GREASE_PENCIL_LENGTH": {
        "name": "Length",
        "category": "Grease Pencil",
        "orig_desc": "Grease Pencil length modifier",
        "en_keyword": "Blender Grease Pencil Length overshoot sketchy lines tutorial",
        "fungsi": "Memanjangkan atau memendekkan ujung pangkal (Start) dan ujung akhir (End) setiap goresan tinta gambar!",
        "cara_pakai": "Naikin 'Start' & 'End' sedikit ke angka positif buat bikin ujung garis lebih lewat menyilang ala sketsa arsitek tangan!",
        "tips": "Dikombinasikan sama Line Art bikin render 3D berasa gambar pensil sketsa manual beneran!",
    },
    "GREASE_PENCIL_MIRROR": {
        "name": "Mirror (Grease Pencil)",
        "category": "Grease Pencil",
        "orig_desc": "Duplicate strokes like a mirror",
        "en_keyword": "Blender Grease Pencil Mirror Modifier tutorial",
        "fungsi": "Mencerminkan goresan gambar Grease Pencil kiri-kanan (X/Y/Z) secara simetris otomatis!",
        "cara_pakai": "Pilih sumbu cermin (biasanya X) -> gambar sebelah wajah/ornamen di Draw Mode, sisi sebelahnya langsung ikut tergambar!",
        "tips": "Bisa pilih objek Empty di kolom 'Object' kalau titik tengah cerminnya mau digeser-geser.",
    },
    "GREASE_PENCIL_MULTIPLY": {
        "name": "Multiple Strokes",
        "category": "Grease Pencil",
        "orig_desc": "Generate multiple strokes around original strokes",
        "en_keyword": "Blender Grease Pencil Multiple Strokes tutorial",
        "fungsi": "Menggandakan 1 garis tunggal jadi beberapa garis paralel bersebelahan (kayak garis kembar jalan raya atau efek goresan kuas bercabang).",
        "cara_pakai": "Atur 'Duplicates' (jumlah garis kembar) dan 'Distance' (lebar jarak antar garisnya).",
        "tips": "Mainkan kurva Fade/Split untuk efek garis sketsa berlapis.",
    },
    "GREASE_PENCIL_OUTLINE": {
        "name": "Outline (Grease Pencil)",
        "category": "Grease Pencil",
        "orig_desc": "Convert stroke to outline",
        "en_keyword": "Blender Grease Pencil Outline Modifier tutorial",
        "fungsi": "Mengubah 1 goresan tebal jadi garis pinggir mengelilingi luar ketebalan goresan tersebut.",
        "cara_pakai": "Pasang Outline -> atur 'Thickness' buat tebal garis pinggir barunya dan pilih 'Outline Material' kalau mau warnanya beda.",
        "tips": "Enak buat bikin stiker ber-border ganda di Grease Pencil.",
    },
    "GREASE_PENCIL_SIMPLIFY": {
        "name": "Simplify (Grease Pencil)",
        "category": "Grease Pencil",
        "orig_desc": "Simplify stroke reducing number of points",
        "en_keyword": "Blender Grease Pencil Simplify Modifier tutorial",
        "fungsi": "Mengurangi jumlah titik pada goresan Grease Pencil yang terlalu rapat supaya file ringan dan garis lebih luwes mudah diedit.",
        "cara_pakai": "Pilih Mode 'Adaptive' -> naikin sedikit 'Factor' sampai titik berlebihan berkurang tanpa merusak bentuk gambar.",
        "tips": "Pasang di bawah Line Art kalau garis hasil Line Art punya terlalu banyak titik berdempetan.",
    },
    "GREASE_PENCIL_SUBDIV": {
        "name": "Subdivide (Grease Pencil)",
        "category": "Grease Pencil",
        "orig_desc": "Grease Pencil subdivide modifier",
        "en_keyword": "Blender Grease Pencil Subdivide Modifier tutorial",
        "fungsi": "Menambah titik perantara dan menghaluskan belokan garis Grease Pencil yang patah-patah kaku.",
        "cara_pakai": "Naikin 'Levels' (1 atau 2) dengan tipe Catmull-Clark supaya sudut garis jadi melengkung mulus.",
        "tips": "Pasang SEBELUM modifier Noise supaya getaran garis Noise punya cukup banyak titik untuk bergoyang!",
    },
    "GREASE_PENCIL_ARMATURE": {
        "name": "Armature (Grease Pencil)",
        "category": "Grease Pencil",
        "orig_desc": "Deform stroke points using armature object",
        "en_keyword": "Blender Grease Pencil Armature rigging 2D animation tutorial",
        "fungsi": "Menggerakkan gambar 2D Grease Pencil pakai kerangka tulang (Armature) buat bikin animasi karakter 2D rigging!",
        "cara_pakai": "Pilih objek tulang di kolom 'Object' dan pastikan goresan sudah punya Vertex Group sesuai nama tulang.",
        "tips": "Kamu bisa menggabungkan animasi frame-by-frame gambar tangan dengan tulang Armature sekaligus!",
    },
    "GREASE_PENCIL_HOOK": {
        "name": "Hook (Grease Pencil)",
        "category": "Grease Pencil",
        "orig_desc": "Deform stroke points using objects",
        "en_keyword": "Blender Grease Pencil Hook Modifier tutorial",
        "fungsi": "Menarik bagian tertentu dari garis Grease Pencil menggunakan objek Empty atau tulang luar.",
        "cara_pakai": "Pilih objek penarik di 'Object' dan batasi bagian garis yang ketarik pakai Vertex Group atau Falloff Radius.",
        "tips": "Praktis buat narik ujung tali atau ekspresi alis gambar 2D.",
    },
    "GREASE_PENCIL_LATTICE": {
        "name": "Lattice (Grease Pencil)",
        "category": "Grease Pencil",
        "orig_desc": "Deform strokes using a lattice object",
        "en_keyword": "Blender Grease Pencil Lattice Modifier tutorial",
        "fungsi": "Membengkokkan dan melenturkan seluruh gambar Grease Pencil di dalam kandang karet Lattice.",
        "cara_pakai": "Buat objek Lattice membungkus gambar -> pilih Lattice di kolom 'Object' -> tarik titik-titik Lattice di Edit Mode!",
        "tips": "Enak banget buat ngasih efek perspektif palsu atau pantulan membal pada karakter gambar 2D!",
    },
    "GREASE_PENCIL_NOISE": {
        "name": "Noise (Grease Pencil)",
        "category": "Grease Pencil",
        "orig_desc": "Generate noise wobble in Grease Pencil strokes",
        "en_keyword": "Blender Grease Pencil Noise Modifier boiling line effect tutorial",
        "fungsi": "EFEK GARIS HIDUP BERGETAR (Boiling Lines)! Mengacak tipis posisi/tebal/transparansi garis tiap beberapa frame biar animasi berasa digambar tangan hidup ala kartun indie!",
        "cara_pakai": "Pasang Noise -> kecilin 'Position' dikit aja (misal 0.02) -> centang **'Randomize'** -> atur 'Step' ke 4 (biar getarnya ganti tiap 4 frame, gak terlalu kejang cepat)!",
        "tips": "Ini kunci nomor #1 kenapa garis Line Art 3D bisa kelihatan kayak lukisan tangan 2D tradisional yang bernyawa!",
    },
    "GREASE_PENCIL_OFFSET": {
        "name": "Offset (Grease Pencil)",
        "category": "Grease Pencil",
        "orig_desc": "Change stroke location, rotation, or scale",
        "en_keyword": "Blender Grease Pencil Offset Modifier tutorial",
        "fungsi": "Menggeser posisi, memutar, atau mengubah ukuran goresan Grease Pencil (atau per-layer) secara non-permanen.",
        "cara_pakai": "Atur Location/Rotation/Scale, atau buka bagian Randomize buat mengacak posisi tiap goresan.",
        "tips": "Filter pakai panel 'Influence -> Layer' kalau cuma mau menggeser 1 layer gambar tertentu aja!",
    },
    "GREASE_PENCIL_SHRINKWRAP": {
        "name": "Shrinkwrap (Grease Pencil)",
        "category": "Grease Pencil",
        "orig_desc": "Project the shape onto another object",
        "en_keyword": "Blender Grease Pencil Shrinkwrap draw on 3D mesh tutorial",
        "fungsi": "Menempelkan goresan gambar 2D Grease Pencil supaya melengkung pas menempel di permukaan objek 3D (kayak gambar alis/luka/grafiti nempel di muka 3D)!",
        "cara_pakai": "Pilih objek 3D tempat nempel di kolom 'Target' -> atur 'Offset' sedikit di atas 0 biar tintanya gak tenggelam ke dalam kulit 3D!",
        "tips": "Wajib dipakai untuk gaya campuran 2D-3D (kayak Spider-Verse / Arcane details) waktu ngegambar garis ekspresi di atas kepala 3D!",
    },
    "GREASE_PENCIL_SMOOTH": {
        "name": "Smooth (Grease Pencil)",
        "category": "Grease Pencil",
        "orig_desc": "Smooth Grease Pencil strokes",
        "en_keyword": "Blender Grease Pencil Smooth Modifier tutorial",
        "fungsi": "Menghaluskan lekukan garis, ketebalan, atau tekanan tinta Grease Pencil yang bergerigi akibat tangan gemetar waktu menggambar.",
        "cara_pakai": "Atur 'Factor' dan 'Repeat', serta centang apakah mau menghaluskan Position, Strength, atau Thickness.",
        "tips": "Bisa dikombinasikan sesudah Line Art atau gambar mouse supaya lengkungannya seluwes pakai pen tablet mahal!",
    },
    "GREASE_PENCIL_THICKNESS": {
        "name": "Thickness (Grease Pencil)",
        "category": "Grease Pencil",
        "orig_desc": "Change stroke thickness",
        "en_keyword": "Blender Grease Pencil Thickness Modifier custom curve tutorial",
        "fungsi": "Mengatur tebal-tipis garis Grease Pencil secara global atau pakai kurva custom (misal runcing tajam di kedua ujung pangkal-akhir seperti kuas kaligrafi)!",
        "cara_pakai": "Atur 'Thickness Factor', dan centang 'Custom Curve' buat membentuk profil ujung garis runcing dan tengah tebal!",
        "tips": "Trik bikin garis Line Art makin estetik: pasang Thickness pakai Custom Curve melengkung biar ujung garisnya meruncing dinamis!",
    },
    "GREASE_PENCIL_COLOR": {
        "name": "Hue/Saturation (Grease Pencil)",
        "category": "Grease Pencil",
        "orig_desc": "Change hue/saturation/value of the strokes",
        "en_keyword": "Blender Grease Pencil Hue Saturation Modifier tutorial",
        "fungsi": "Menggeser rona warna (Hue), kepekatan warna (Saturation), dan terang-gelap (Value) goresan gambar Grease Pencil tanpa ngubah material aslinya.",
        "cara_pakai": "Geser Hue (0.5 = warna asli), Saturation (0 = hitam putih), atau Value (terang-gelap); batasi ke 1 Layer di sub-panel Influence kalau perlu.",
        "tips": "Cepat banget buat nyesuaiin warna karakter 2D waktu adegan berubah dari siang terang ke malam biru gelap!",
    },
    "GREASE_PENCIL_OPACITY": {
        "name": "Opacity (Grease Pencil)",
        "category": "Grease Pencil",
        "orig_desc": "Change the opacity of the strokes",
        "en_keyword": "Blender Grease Pencil Opacity Modifier fade tutorial",
        "fungsi": "Mengatur tingkat tembus pandang (transparansi) goresan atau isi warna Grease Pencil — gampang dianimasiin buat efek fade-in / fade-out!",
        "cara_pakai": "Geser 'Opacity Factor' (1.0 = jelas pekat, 0.0 = hilang transparan).",
        "tips": "Pilih mode 'Hardness' kalau mau melembutkan pinggiran goresan kuas.",
    },
    "GREASE_PENCIL_TINT": {
        "name": "Tint (Grease Pencil)",
        "category": "Grease Pencil",
        "orig_desc": "Tint the color of the strokes",
        "en_keyword": "Blender Grease Pencil Tint Modifier gradient tutorial",
        "fungsi": "Melapisi goresan Grease Pencil dengan campuran warna solid atau gradasi warna (Color Ramp)!",
        "cara_pakai": "Pilih warna 'Color' (atau ganti Type ke 'Gradient') -> naikkan 'Factor' buat menentukan seberapa kuat sapuan warna tint-nya.",
        "tips": "Mode Gradient bikin lu bisa mewarnai satu objek gambar pakai gradasi senja mulus dalam sekali klik!",
    },
    "GREASE_PENCIL_TEXTURE": {
        "name": "Texture Mapping (Grease Pencil)",
        "category": "Grease Pencil",
        "orig_desc": "Change stroke UV texture values",
        "en_keyword": "Blender Grease Pencil Texture Mapping Modifier tutorial",
        "fungsi": "Menggeser, memutar, dan mengubah skala koordinat UV tekstur kuas di sepanjang goresan Grease Pencil.",
        "cara_pakai": "Atur UV Offset, Rotation, dan Scale pada goresan bertekstur (misal goresan tekstur kapur/arang).",
        "tips": "Animasikan UV Offset untuk membuat pola tekstur di dalam garis tampak mengalir!",
    },
    "GREASE_PENCIL_TIME": {
        "name": "Time Offset (Grease Pencil)",
        "category": "Grease Pencil",
        "orig_desc": "Offset keyframes",
        "en_keyword": "Blender Grease Pencil Time Offset loop animation tutorial",
        "fungsi": "Mesin pemutar ulang animasi 2D! Bisa mengulang terus-menerus (Loop) gambar animasi pendek (kayak api berkobar, rambut tertiup angin, kedip), mempercepat, atau membalik urutannya!",
        "cara_pakai": "Bikin 3–5 frame gambar animasi -> pasang Time Offset -> centang 'Keep Loop' dan atur Custom Range frame awal-akhir gambarnya!",
        "tips": "Hemat tenaga gila-gilaan buat animator 2D: cukup gambar 4 frame api bergerak, Time Offset otomatis me-loop sepanjang film!",
    },
    "GREASE_PENCIL_VERTEX_WEIGHT_PROXIMITY": {
        "name": "Vertex Weight Proximity (Grease Pencil)",
        "category": "Grease Pencil",
        "orig_desc": "Generate vertex weights based on distance to object",
        "en_keyword": "Blender Grease Pencil Vertex Weight Proximity tutorial",
        "fungsi": "Mengatur bobot Vertex Group pada titik goresan Grease Pencil berdasarkan jarak ke objek Target (misal garis otomatis menebal saat didekati objek).",
        "cara_pakai": "Pilih Vertex Group dan Target Object, atur jarak minimum/maksimum, lalu gunakan Vertex Group tersebut di modifier Thickness atau Opacity di bawahnya!",
        "tips": "Bagus buat bikin garis fokus dinamis saat kamera mendekat ke bagian tertentu.",
    },
    "GREASE_PENCIL_VERTEX_WEIGHT_ANGLE": {
        "name": "Vertex Weight Angle (Grease Pencil)",
        "category": "Grease Pencil",
        "orig_desc": "Generate vertex weights based on stroke angle",
        "en_keyword": "Blender Grease Pencil Vertex Weight Angle calligraphy tutorial",
        "fungsi": "Mengatur bobot Vertex Group berdasarkan arah kemiringan sudut goresan — bikin efek pena kaligrafi otomatis (garis vertikal tebal, garis horizontal tipis)!",
        "cara_pakai": "Pilih Vertex Group target -> atur sudut 'Angle' -> pasangkan Vertex Group itu pada modifier Thickness di bawahnya!",
        "tips": "Langsung ngasih nuansa kuas tinta tradisional pada garis Line Art otomatis!",
    },
}


# =============================================================================
# BLENDER 5.2 ESSENTIALS NODE-GROUP ASSET MODIFIERS (Smooth by Angle, Array Baru, Hair, dll!)
# =============================================================================
ASSET_MODIFIER_CATALOG: dict[str, dict[str, str]] = {
    "Smooth by Angle": {
        "name": "Smooth by Angle",
        "category": "Normals",
        "orig_desc": "Set the sharpness of mesh edges based on the angle between the neighboring faces",
        "en_keyword": "Blender Smooth by Angle Modifier Auto Smooth tutorial",
        "fungsi": "PENGGANTI AUTO SMOOTH DI BLENDER MODERN! Bikin permukaan lengkung silinder kelihatan halus mulus, TAPI sudut siku-siku tajamnya tetep tegas gak belepotan bayangan!",
        "cara_pakai": "Cara cepat: Klik kanan objek -> pilih 'Shade Auto Smooth' (otomatis masang modifier ini!), atau pasang dari Add Modifier -> Normals -> Smooth by Angle -> atur batas sudut 'Angle' (standar 30°).",
        "tips": "Centang 'Ignore Sharpness' kalau mau mengabaikan garis biru Mark Sharp lama yang terlanjur ada di mesh.",
    },
    "Array (Asset)": {
        "name": "Array (Geometry Nodes Baru)",
        "category": "Generate",
        "orig_desc": "Create copies of the geometry with linear, radial, or curve distribution",
        "en_keyword": "Blender New Array Modifier Radial Curve Linear tutorial",
        "fungsi": "Versi upgrade modern dari Array di Blender 5.x! Langsung bisa bikin barisan Lurus (Linear), Melingkar (Circular/Radial!), atau Mengikuti Garis (Curve) tanpa ribet pakai Empty!",
        "cara_pakai": "Pasang Array dari menu Generate -> pilih Shape (Line, Circle, atau Curve) -> atur Count/Distance dan bahkan bisa langsung acak rotasi/ukurannya di Randomize!",
        "tips": "Jauh lebih praktis dari Array (Legacy) waktu mau bikin meja bundar berkursi keliling atau pagar melengkung!",
    },
    "Curve to Tube": {
        "name": "Curve to Tube",
        "category": "Generate",
        "orig_desc": "Turn curves into tube meshes with customizable profile and caps",
        "en_keyword": "Blender Curve to Tube Modifier cable pipe tutorial",
        "fungsi": "Penyulap garis Curve tipis jadi pipa, kabel, selang, atau tiang 3D lengkap dengan tutup ujung (Caps) dan ketebalan yang bisa diatur!",
        "cara_pakai": "Gambar Bezier Curve -> pasang 'Curve to Tube' -> atur Radius (tebal pipa), Resolution, dan tutup ujungnya!",
        "tips": "Enak banget dipakai bareng Draw Curve tool buat ngegambar kabel menjuntai menempel di lantai/tembok!",
    },
    "Scatter on Surface": {
        "name": "Scatter on Surface",
        "category": "Generate",
        "orig_desc": "Scatter referenced geometry on a surface mesh",
        "en_keyword": "Blender Scatter on Surface Modifier grass rocks tutorial",
        "fungsi": "PENYEBAR RUMPUT, BATU & POHON INSTAN! Menyebarkan ribuan objek/koleksi di atas permukaan tanah lengkap dengan jarak anti-tabrakan (Minimum Distance) dan ukuran acak!",
        "cara_pakai": "Klik objek tanah -> pasang 'Scatter on Surface' -> pilih objek rumput/batu di kolom 'Object' (atau satu folder di 'Collection') -> atur 'Density' & nyalain 'Randomize' biar ukuran dan arah hadapnya alami!",
        "tips": "Naikin 'Minimum Distance' supaya batu/pohon yang disebar gak saling numpuk tembus satu sama lain!",
    },
    "Cloth Dynamics (Experimental)": {
        "name": "Cloth Dynamics (Experimental)",
        "category": "Physics",
        "orig_desc": "Simulate dynamic cloth behavior using Geometry Nodes simulation zones",
        "en_keyword": "Blender Geometry Nodes Cloth Dynamics Modifier tutorial",
        "fungsi": "Simulasi kain generasi baru berbasis Geometry Nodes di Blender 5.2!",
        "cara_pakai": "Pasang di mesh berpoligon cukup rapat lalu tekan Spacebar untuk menjalankan simulasi secara real-time.",
        "tips": "Cocok buat eksperimen kain prosedural yang langsung nyambung dengan tumpukan Geometry Nodes.",
    },
    "Generate Hair Curves": {
        "name": "Generate Hair Curves",
        "category": "Hair & Assets",
        "orig_desc": "Generates new hair curves on a surface mesh",
        "en_keyword": "Blender Hair Curves System Generate Hair tutorial",
        "fungsi": "Penumbuh helai rambut/bulu baru secara otomatis di atas permukaan kulit kepala atau badan karakter!",
        "cara_pakai": "Pilih objek Curves rambut -> pastikan Surface Object & UV Map sudah terisi -> atur Density (kerapatan) dan Hair Length (panjang rambut).",
        "tips": "Pastikan model kepala/badan sudah punya UV Map yang tidak tumpang-tindih supaya akar rambut menempel rapi!",
    },
    "Interpolate Hair Curves": {
        "name": "Interpolate Hair Curves",
        "category": "Hair & Assets",
        "orig_desc": "Interpolates existing guide curves on a surface mesh",
        "en_keyword": "Blender Interpolate Hair Curves grooming tutorial",
        "fungsi": "Pengisi ribuan anak rambut otomatis di sela-sela sedikit helai rambut panduan (Guide Curves) yang sudah lu sisir di Sculpt Mode!",
        "cara_pakai": "Sisir sedikit rambut utama pakai kuas Comb -> pasang Interpolate Hair Curves buat menebalkan rambut jadi lebat alami mengikuti arah sisiran!",
        "tips": "Gunakan Density Mask / Vertex Group untuk membatasi garis batas tumbuh rambut (hairline) di dahi dan tengkuk.",
    },
    "Clump Hair Curves": {
        "name": "Clump Hair Curves",
        "category": "Hair & Assets",
        "orig_desc": "Clumps together existing hair curves using guide curves",
        "en_keyword": "Blender Clump Hair Curves grooming tutorial",
        "fungsi": "Mengelompokkan ujung-ujung helai rambut supaya mengumpul meruncing alami per ikatan kecil (gak megar satu-satu kayak sapu ijuk)!",
        "cara_pakai": "Pasang sesudah Interpolate Hair Curves -> atur Factor, Shape, dan Guide Distance untuk menentukan besar kecilnya gumpalan helai rambut.",
        "tips": "Rambut manusia dan bulu hewan di dunia nyata hampir selalu punya sedikit efek Clump!",
    },
    "Curl Hair Curves": {
        "name": "Curl Hair Curves",
        "category": "Hair & Assets",
        "orig_desc": "Deforms existing hair curves into curls using guide curves",
        "en_keyword": "Blender Curl Hair Curves curly hair tutorial",
        "fungsi": "Mengubah helai rambut lurus menjadi ikal bergelombang atau keriting spiral!",
        "cara_pakai": "Atur Radius (lebar lingkaran ikal) dan Frequency (seberapa rapat putaran keritingnya dari pangkal ke ujung).",
        "tips": "Naikin 'Subdivision' di dalam modifier ini kalau lengkungan keritingnya masih terlihat agak patah-patah.",
    },
    "Frizz Hair Curves": {
        "name": "Frizz Hair Curves",
        "category": "Hair & Assets",
        "orig_desc": "Deforms hair curves using a random vector per point to frizz them",
        "en_keyword": "Blender Frizz Hair Curves realistic flyaway hair tutorial",
        "fungsi": "Memberi efek anak rambut agak kusut/acak halus (flyaways) biar rambut gak kelihatan kaku kayak plastik CGI!",
        "cara_pakai": "Kasih angka Distance kecil aja dan atur Shape supaya bagian akar tetap rapi tapi makin ke ujung makin natural.",
        "tips": "Sedikit Frizz + lampu belakang (Rim Light) bikin render rambut kelihatan super nyata!",
    },
    "Braid Hair Curves": {
        "name": "Braid Hair Curves",
        "category": "Hair & Assets",
        "orig_desc": "Deforms existing hair curves into braids using guide curves",
        "en_keyword": "Blender Braid Hair Curves tutorial",
        "fungsi": "Menganyam helai-helai rambut mengikuti garis panduan menjadi kepangan rambut (braids) lengkap dengan karet ikat ujungnya!",
        "cara_pakai": "Atur Radius, Frequency kepangan, dan bagian Flare untuk ujung rambut di bawah ikatan kepang.",
        "tips": "Gunakan kurva panduan (Guide Curves) yang cukup panjang untuk alur kepangan yang rapi.",
    },
    "Hair Curves Noise": {
        "name": "Hair Curves Noise",
        "category": "Hair & Assets",
        "orig_desc": "Deforms hair curves using a noise texture",
        "en_keyword": "Blender Hair Curves Noise grooming tutorial",
        "fungsi": "Memberi gelombang acak lembut di sepanjang batang rambut memakai pola Noise supaya alur sisiran terlihat organik.",
        "cara_pakai": "Atur Distance (kuatnya gelombang) dan Scale (besar kecilnya ombak tekstur noise).",
        "tips": "Berbeda dengan Frizz yang mengacak per titik tajam, Noise membuat alunan gelombang yang lebih halus.",
    },
    "Trim Hair Curves": {
        "name": "Trim Hair Curves",
        "category": "Hair & Assets",
        "orig_desc": "Trims or scales hair curves to a certain length",
        "en_keyword": "Blender Trim Hair Curves haircut length tutorial",
        "fungsi": "Gunting pangkas rambut otomatis! Memotong atau menyamakan variasi panjang pendek ujung helai rambut.",
        "cara_pakai": "Atur Length atau Factor, dan tambahkan Random Offset supaya potongan ujung rambut gak rata kaku seperti penggaris.",
        "tips": "Enak dipakai buat eksperimen panjang potongan rambut tanpa merusak sisiran asli!",
    },
    "Smooth Hair Curves": {
        "name": "Smooth Hair Curves",
        "category": "Hair & Assets",
        "orig_desc": "Smoothes the shape of hair curves",
        "en_keyword": "Blender Smooth Hair Curves tutorial",
        "fungsi": "Menghaluskan lekukan batang rambut yang patah atau tertekuk tajam.",
        "cara_pakai": "Atur Weight dan Iterations secukupnya sampai lengkungan helai rambut terlihat luwes.",
        "tips": "Aktifkan Preserve Length kalau gak mau panjang rambut menyusut waktu dihaluskan.",
    },
    "Roll Hair Curves": {
        "name": "Roll Hair Curves",
        "category": "Hair & Assets",
        "orig_desc": "Rolls up hair curves starting from their tips",
        "en_keyword": "Blender Roll Hair Curves fur curls tutorial",
        "fungsi": "Menggulung helai rambut melingkar mulai dari ujungnya ke arah dalam (cocok buat bulu domba, janggut ikal, atau gulungan rambut klasik).",
        "cara_pakai": "Atur Roll Length dan Roll Radius untuk mengatur besar gulungan di ujung rambut.",
        "tips": "Tambahkan sedikit variasi acak supaya tiap gulungan tidak seragam kaku.",
    },
    "Set Hair Curve Profile": {
        "name": "Set Hair Curve Profile",
        "category": "Hair & Assets",
        "orig_desc": "Sets the radius attribute of hair curves according to a profile shape",
        "en_keyword": "Blender Set Hair Curve Profile thickness tutorial",
        "fungsi": "Mengatur ketebalan sehelai rambut dari akar (tebal) meruncing halus ke ujung rambut (tipis) supaya pas dirender gak kelihatan kayak kabel tebal!",
        "cara_pakai": "WAJIB ADA di tumpukan paling bawah modifier rambut! Kecilin 'Radius' (misal 0.0005 m) dan atur 'Shape' supaya ujung rambut meruncing halus!",
        "tips": "Kalau rambut karakter lu kelihatan tebal kaku kayak mie lidi waktu dirender, 99% penyebabnya angka Radius di sini belum dikecilin!",
    },
}


# =============================================================================
# TOOLTIP KHUSUS PARAMETER / INPUT VARIABLE MODIFIER PALING PENTING (Hover Langsung!)
# Key = deskripsi bahasa Inggris persis dari Blender 5.2 RNA
# =============================================================================
MODIFIER_PROP_TOOLTIPS: dict[str, str] = {
    # Header tombol Modifier umum (Viewport, Render, Edit Mode, On Cage)
    "Add a procedural operation/effect to the active object": (
        "Fungsi: Buka daftar menu Modifier buat nambahin efek pembentuk otomatis ke objek lu (kayak Bevel, Mirror, Subdivision, Boolean, dll).\n"
        "Cara Pakai: Klik tombol ini -> arahin kursor ke nama modifier yang mau diintip buat baca penjelasan gaulnya!"
    ),
    "Display modifier in viewport": (
        "Fungsi: Tombol nyala/mati tampilan efek modifier ini di layar kerja 3D Viewport.\n"
        "Cara Pakai: Matiin ikon layar ini sementara kalau scene lu mulai berat ngelag waktu ngedit (pas render akhir tetep nyala kok selama ikon kamera aktif!)."
    ),
    "Use modifier during render": (
        "Fungsi: Nentuin apakah efek modifier ini ikut dihitung waktu lu pencet Render gambar/video akhir (F12).\n"
        "Cara Pakai: Biarin nyala biru kalau mau efeknya muncul di hasil foto/video akhir; matiin kalau cuma buat bantuan ngedit doang."
    ),
    "Display modifier in Edit mode": (
        "Fungsi: Biar efek modifier ini tetep kelihatan nyala walaupun lu lagi masuk ke Edit Mode (Tab)!\n"
        "Cara Pakai: Klik ikon kotak bertitik ini kalau lu mau ngedit titik sambil langsung ngelihat hasil Mirror/Subdivision/Curve-nya secara live."
    ),
    "Adjust edit cage to modifier result": (
        "Fungsi: Menempelkan jaring titik Edit Mode langsung ke permukaan hasil modifier (On Cage).\n"
        "Cara Pakai: Nyalain bareng ikon Edit Mode kalau lu mau titik-titik yang lu klik nempel pas di kulit mulus hasil Subdivision, bukan melayang di kotak luarnya."
    ),
    "Move modifier to the very end of the stack and keep it there": (
        "Fungsi: Paku pengunci posisi paling bawah! Memaksa modifier ini selalu nongkrong di urutan paling akhir walaupun lu nambah modifier baru.\n"
        "Cara Pakai: Cocok dinyalain di modifier 'Smooth by Angle' atau 'Weighted Normal' yang emang bagusnya selalu di urutan terakhir."
    ),

    # Bevel Modifier inputs
    "Number of segments for round edges/verts": (
        "Fungsi: Jumlah lipatan/potongan garis di sudut Bevel.\n"
        "Cara Pakai: Angka 1 = sudut miring tegas (chamfer); naikin ke 3–5 = sudut melengkung bulet mulus! Jangan kebanyakan (>12) biar poligon gak bengkak berat."
    ),
    "Bevel amount": (
        "Fungsi: Lebar seberapa jauh pinggiran sudut objek ditumpulin/dipotong oleh Bevel.\n"
        "Cara Pakai: Geser pelan pake Shift+Drag biar halus! Kalau objek kecil tapi Bevel mentok gak berubah, coba matiin 'Clamp Overlap' atau kecilin angkanya."
    ),
    "The profile shape (0.5 = round)": (
        "Fungsi: Bentuk cekung/cembung lengkungan sudut Bevel.\n"
        "Cara Pakai: 0.5 = melengkung bulat normal; mendekati 0 = melesak cekung ke dalam; 1.0 = siku lancip balik ke kotak."
    ),
    "Match normals of new faces to adjacent faces": (
        "Fungsi: Harden Normals — merapikan pantulan cahaya di bidang datar sekitar Bevel supaya rata kinclong gak melengkung belang!\n"
        "Cara Pakai: Centang ini kalau bikin objek mekanik/kotak halus (pastikan objek juga udah dikasih Shade Auto Smooth / Smooth by Angle)."
    ),
    "Prefer to slide along edges to having even widths": (
        "Fungsi: Clamp Overlap — rem pengaman supaya potongan Bevel berhenti sebelum garisnya saling tabrakan tumpuk rusuh!\n"
        "Cara Pakai: Biarin tercentang biar aman! Matiin cuma kalau nilai Amount lu terasa macet gak mau nambah lebar."
    ),
    "Pattern to use for mitered outer edges": (
        "Fungsi: Miter Outer — bentuk sambungan pertemuan di pojok luar tiga garis Bevel.\n"
        "Cara Pakai: Ganti dari 'Sharp' ke 'Arc' supaya pojokan siku pertemuan Bevel punya jaring quad yang jauh lebih rapi dan mulus!"
    ),

    # Subdivision Surface inputs
    "Number of subdivisions to perform": (
        "Fungsi: Levels Viewport — seberapa halus lipatan pembagian poligon yang ditampilin di layar kerja sekarang.\n"
        "Cara Pakai: Cukup isi angka 1 atau 2 aja! Hati-hati tiap naik 1 angka jumlah poligon dikali 4x lipat (angka 5–6 bisa bikin komputer nge-freeze!)."
    ),
    "Number of subdivisions to perform when rendering": (
        "Fungsi: Render Levels — tingkat kehalusan poligon khusus saat diproses jadi gambar/video Render akhir (F12).\n"
        "Cara Pakai: Biasanya diisi 2 atau 3 supaya pas ngedit enteng (Viewport=1), tapi pas dirender hasilnya super mulus!"
    ),
    "Select type of subdivision algorithm": (
        "Fungsi: Pilih cara membagi poligon: 'Catmull-Clark' (membulat halus mulus) atau 'Simple' (nambah banyak titik kotak TANPA melengkungin bentuk asli!).\n"
        "Cara Pakai: Pakai 'Catmull-Clark' buat ngalusin model; pakai 'Simple' kalau cuma butuh nambah titik buat Displace/Sculpting tapi bentuk kotak mau tetep tajam!"
    ),

    # Mirror Modifier inputs
    "Enable axis mirror": (
        "Fungsi: Pilih sumbu arah pencerminan (X = kiri-kanan, Y = depan-belakang, Z = atas-bawah).\n"
        "Cara Pakai: Klik tombol X, Y, atau Z (bisa nyala lebih dari satu sekaligus, misal X+Y buat bikin 4 kaki meja langsung dari 1 kaki!)."
    ),
    "Prevent vertices from going through the mirror during transform": (
        "Fungsi: Clipping — lem magnet penahan garis tengah cermin!\n"
        "Cara Pakai: WAJIB DICENTANG pas bikin wajah/badan/mobil simetris supaya titik sambungan tengah nempel rapet gak bisa robek atau tembus nyebrang!"
    ),
    "Distance from axis within which mirrored vertices are merged": (
        "Fungsi: Merge Distance — jarak toleransi seberapa dekat titik kiri dan kanan di garis tengah bakal dilebur jadi satu titik.\n"
        "Cara Pakai: Biarin kecil (0.001 m); kalau titik yang deket tengah malah gak sengaja ketarik nempel, kecilin lagi angkanya."
    ),
    "Object to use as mirror": (
        "Fungsi: Mirror Object — menjadikan objek lain (biasanya Empty) sebagai posisi & arah kaca cerminnya!\n"
        "Cara Pakai: Klik pipet lalu klik objek Empty kalau titik tengah objek lu gak di pusat dunia, atau kalau mau bikin cermin miring!"
    ),
    "Cuts the mesh across the mirror plane": (
        "Fungsi: Bisect — pisau pemotong otomatis tepat di garis cermin!\n"
        "Cara Pakai: Nyalain sumbu X/Y/Z di Bisect kalau lu males ngehapus separuh sisi objek manual — bagian yang lewat cermin langsung dipotong bersih!"
    ),

    # Solidify Modifier inputs
    "Thickness of the shell": (
        "Fungsi: Ketebalan dinding/kulit baru yang dibuat oleh Solidify.\n"
        "Cara Pakai: Geser angkanya sesuai tebal bahan yang lu mau (misal 0.003m buat kain/kaca tipis, 0.15m buat tembok rumah)."
    ),
    "Offset the thickness from the center": (
        "Fungsi: Arah menebalnya dinding: ke arah dalam (-1.0), ke tengah dua arah (0.0), atau menebal keluar (+1.0).\n"
        "Cara Pakai: Kalau bikin baju/helm di luar kepala karakter, ganti Offset ke +1.0 supaya menebalnya ke arah LUAR dan gak nembus masuk kulit!"
    ),
    "Maintain thickness by adjusting for sharp corners (slow, disable when not needed)": (
        "Fungsi: Even Thickness — menjaga ketebalan dinding di belokan sudut siku-siku tetap rata gak menipis gepeng!\n"
        "Cara Pakai: Wajib centang ini kalau objek lu berbentuk kotak/ruangan/sudut tegas biar tebal pojokannya presisi!"
    ),
    "Create edge loops between the inner and outer surfaces on face edges (slow, disable when not needed)": (
        "Fungsi: Fill — menutup celah pinggiran antara kulit luar dan kulit dalam supaya gak bolong kopong.\n"
        "Cara Pakai: Biarkan tercentang supaya pinggiran objek tebal lu tertutup rapi."
    ),

    # Boolean Modifier inputs
    "Operation to perform on the mesh": (
        "Fungsi: Jenis operasi Boolean: Difference (lubangi/kurangi), Union (lebur gabung jadi satu), atau Intersect (ambil bagian irisannya aja).\n"
        "Cara Pakai: Pilih 'Difference' buat melubangi tembok/mesin, atau 'Union' buat menyatukan dua bentuk terpisah sebelum di-Sculpt/Bevel!"
    ),
    "Method for calculating booleans": (
        "Fungsi: Mesin penghitung potongan Boolean (Float / Exact / Manifold).\n"
        "Cara Pakai: 'Exact' paling akurat buat objek tumpang-tindih rapi; ganti ke 'Float' (jauh lebih ngebut!) atau 'Manifold' kalau objek lu tiba-tiba hilang/bolong saat dipotong!"
    ),
    "Mesh object to use for Boolean operation": (
        "Fungsi: Objek pemotong atau penggabung yang dipakai untuk operasi Boolean ini.\n"
        "Cara Pakai: Klik ikon pipet suntik terus klik objek pemotong di layar 3D (jangan lupa sembunyiin objek pemotong pakai H atau ubah Display As -> Wire!)."
    ),

    # Array Modifier inputs
    "Number of duplicates to make": (
        "Fungsi: Count — jumlah total barisan kopian objek (termasuk 1 objek aslinya).\n"
        "Cara Pakai: Isi misalnya 5 kalau mau ada 5 objek berjejer rapi."
    ),
    "Array length calculation method": (
        "Fungsi: Fit Type — cara nentuin banyaknya barisan Array.\n"
        "Cara Pakai: 'Fixed Count' = tentuin jumlah bijinya manual; 'Fit Length' = isi sepanjang sekian meter; 'Fit Curve' = otomatis ngisi penuh sepanjang garis Bezier Curve!"
    ),
}


# Daftar nama input parameter populer modifier (dipakai di Panel Bedah Modifier Aktif!)
MODIFIER_PARAM_GAUL: dict[str, str] = {
    "count": "Jumlah total duplikat objek dalam barisan Array.",
    "fit_type": "Cara nentuin panjang Array: jumlah tetap (Fixed Count), panjang meter (Fit Length), atau ngikut panjang garis (Fit Curve).",
    "use_relative_offset": "Geser jarak tiap kopian berdasarkan kelipatan ukuran lebar objek itu sendiri (1.0 = nempel pas sebelahan!).",
    "relative_offset_displace": "Jarak geser relatif X/Y/Z (isi 1.0 supaya tiap kopian nempel pas di pinggir kopian sebelumnya).",
    "use_constant_offset": "Geser jarak tiap kopian pakai ukuran meter/cm pasti, gak peduli ukuran objeknya seberapa.",
    "constant_offset_displace": "Jarak geser tetap (meter/cm) antar kopian di sumbu X/Y/Z.",
    "use_object_offset": "Gunakan posisi/putaran objek lain (misal Empty) buat bikin Array melingkar atau mengecil bertahap!",
    "offset_object": "Objek acuan (biasanya Empty) untuk mengatur putaran/geseran Object Offset.",
    "use_merge_vertices": "Otomatis ngelem titik sambungan antar kopian Array yang saling nempel biar nyatu mulus.",
    "width": "Lebar area sudut yang ditumpulkan oleh Bevel (kecilkan angkanya kalau sudut objek berantakan tabrakan!).",
    "segments": "Jumlah lipatan garis penghalus sudut (1 = miring rata tegas, 3–5 = melengkung bulat halus!).",
    "profile": "Bentuk lengkungan sudut: 0.5 bulat normal, <0.5 cekung ke dalam, 1.0 siku tajam.",
    "limit_method": "Filter garis mana aja yang kena Bevel: Angle (berdasarkan tajam sudut), Weight, atau Vertex Group.",
    "angle_limit": "Batas kemiringan sudut minimum supaya garisnya kena Bevel (standar 30 derajat).",
    "harden_normals": "Ratakan arah pantulan cahaya bidang datar di sekitar Bevel biar permukaan mesin kelihatan mulus mengkilap!",
    "clamp_overlap": "Rem pengaman biar lebar Bevel berhenti otomatis sebelum garisnya saling tabrakan tumpuk.",
    "miter_outer": "Pola pertemuan pojok luar Bevel (ganti ke 'Arc' biar topologi pojokannya jauh lebih rapi!).",
    "operation": "Mode Boolean: Difference (lubangi), Union (gabung lebur), atau Intersect (ambil irisannya aja).",
    "solver": "Mesin hitung Boolean: Exact (presisi tinggi), Float (cepat & toleran), atau Manifold (khusus mesh tertutup rapat).",
    "object": "Objek target/acuan yang dipakai oleh modifier ini (klik ikon pipet buat milih langsung di layar!).",
    "collection": "Folder grup Collection yang seluruh isinya dipakai oleh modifier ini.",
    "levels": "Tingkat kehalusan pembagian poligon di layar kerja Viewport (cukup 1–2 biar enteng!).",
    "render_levels": "Tingkat kehalusan pembagian poligon waktu Render akhir F12 (biasanya 2–3).",
    "subdivision_type": "Catmull-Clark = bikin halus membulat; Simple = perbanyak titik tanpa ngubah bentuk kotak tajam.",
    "use_axis": "Sumbu aktif (X / Y / Z) tempat pencerminan dijalankan.",
    "use_bisect_axis": "Otomatis memotong bagian mesh yang kelewat menyeberangi garis tengah cermin.",
    "use_flip_axis": "Membalik sisi mana yang dipertahankan waktu fitur Bisect memotong objek.",
    "mirror_object": "Objek luar (misal Empty) yang dipakai sebagai titik tengah & arah kaca cermin.",
    "use_clip": "Kunci titik di garis tengah cermin supaya nempel rapat dan gak bisa ketarik robek!",
    "merge_threshold": "Jarak maksimal (meter) agar titik berdekatan langsung dilebur jadi satu titik tunggal.",
    "thickness": "Ketebalan dinding/rangka baru yang dihasilkan oleh modifier.",
    "offset": "Posisi pergeseran ketebalan/jarak tempel terhadap permukaan asli (-1 ke dalam, 0 tengah, +1 ke luar).",
    "use_even_offset": "Jaga ketebalan dinding tetap seragam rata di belokan sudut siku-siku (Even Thickness).",
    "use_rim": "Tutup celah pinggiran antara kulit luar dan kulit dalam supaya objek tebal gak bolong.",
    "use_rim_only": "Hanya buat pinggiran tebalnya saja, hapus permukaan depan & belakangnya.",
    "deform_method": "Mode bengkok Simple Deform: Twist (plintir), Bend (tekuk melengkung), Taper (meruncing), Stretch (melar).",
    "deform_axis": "Sumbu utama (X, Y, atau Z) arah pembengkokan dijalankan.",
    "angle": "Besarnya sudut putaran/lengkungan dalam satuan derajat.",
    "factor": "Kekuatan pengaruh efek (biasanya 0 = gak ngaruh, 1 = efek penuh 100%).",
    "strength": "Kuatnya dorongan atau tarikan efek modifier pada titik-titik objek.",
    "target": "Objek sasaran tempat modifier ini menempel atau mengambil bentuk.",
    "wrap_method": "Cara menempelkan Shrinkwrap: Nearest Surface Point (terdekat), Project (tembak lurus), atau Target Normal Project (paling mulus!).",
    "wrap_mode": "Posisi tempel terhadap permukaan target (On Surface, Outside, Above Surface, dll).",
    "vertex_group": "Batasi efek modifier ini supaya CUMA bekerja pada titik-titik di dalam Vertex Group pilihan lu!",
    "invert_vertex_group": "Balikkan pengaruh Vertex Group (yang tadinya kena jadi aman, yang aman malah kena efek).",
    "voxel_size": "Ukuran kotak resolusi Remesh/Volume — makin KECIL makin detail tajam, tapi jangan kekecilan biar gak nge-hang!",
    "adaptivity": "Kurangi jumlah poligon di bagian yang datar rata supaya hasil lebih ringan hemat memori.",
    "ratio": "Persentase sisa poligon di Decimate (1.0 = utuh 100%, 0.1 = dipangkas sisa 10% aja).",
    "iterations": "Berapa kali proses penghalusan/perhitungan diulang berturut-turut.",
    "steps": "Jumlah potongan segmen putaran di layar Viewport (makin tinggi makin bulat halus).",
    "screw_offset": "Jarak naik per satu putaran penuh (isi > 0 buat bikin per pegas atau ulir sekrup!).",
}
