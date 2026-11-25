# SPDX-License-Identifier: GPL-3.0-or-later
"""Sobat Blender Gaul — Hover Tooltip Bahasa Gaul di Seluruh Properties + Cari YouTube & Google (Keyword Inggris)."""

from __future__ import annotations

import bpy
from bpy.app.handlers import persistent
from bpy.props import BoolProperty, EnumProperty, PointerProperty, StringProperty
from bpy.types import PropertyGroup

from . import engine_gaul_translator, operators, ui

bl_info = {
    "name": "Sobat Blender Gaul — Kamus Properties & Cari Tutorial",
    "author": "Sobat Blender Gaul",
    "version": (1, 0, 0),
    "blender": (4, 2, 0),
    "location": "Hover Semua Tombol Properties | Klik Kanan Tombol Apa Saja | Alt+Q | Properties & N-Panel",
    "description": "Penjelasan Bahasa Indonesia Gaul pemula saat kursor hover di seluruh Tab Properties & Modifier + tombol cari YouTube/Google dengan keyword Bahasa Inggris",
    "category": "Interface",
}

_KEYMAPS: list[tuple[bpy.types.KeyMap, bpy.types.KeyMapItem]] = []


class SOBATGAUL_PG_wm_settings(PropertyGroup):
    hover_enabled: BoolProperty(
        name="Mode Hover Bahasa Gaul",
        description="Aktifkan penjelasan Bahasa Indonesia Gaul otomatis saat kursor menunjuk tombol atau menu",
        default=True,
    )
    show_global_search: BoolProperty(
        name="Buka Pencarian Fitur",
        description="Buka kotak pencarian seluruh fitur Blender ke YouTube dan Google",
        default=True,
    )
    search_query: StringProperty(
        name="Cari Fitur (Indo / Inggris)",
        description="Ketik fitur apa saja pakai Bahasa Indonesia (misal: tumpulin sudut, bolongin, kain, kaca) atau Bahasa Inggris (misal: Bevel, Subsurf)",
        default="",
    )
    show_tab_overview: BoolProperty(
        name="Tampilkan Panduan Tab Ini",
        description="Buka ringkasan fungsi dan bedah bagian-bagian di tab Properties yang sedang aktif",
        default=False,
    )
    show_modifier_catalog: BoolProperty(
        name="Buka Kamus Modifier Sebelum Klik",
        description="Lihat penjelasan fungsi dan cara pakai semua Modifier sebelum memasangnya ke objek",
        default=True,
    )
    modifier_category_filter: EnumProperty(
        name="Kategori Modifier",
        description="Saring daftar modifier berdasarkan kategorinya di menu Add Modifier",
        items=(
            ("ALL", "Semua Kategori", "Tampilkan semua modifier yang ada di Blender"),
            ("Generate", "Generate (Pembuat Bentuk)", "Array, Bevel, Boolean, Mirror, Solidify,Subdivision Surface, dll"),
            ("Deform", "Deform (Pembengkok Bentuk)", "Armature, Curve, Displace, Lattice, Shrinkwrap, Simple Deform, dll"),
            ("Normals", "Normals (Perapi Cahaya)", "Smooth by Angle, Weighted Normal, Normal Edit"),
            ("Edit", "Edit (Data Titik & UV)", "Data Transfer, UV Project, UV Warp, Vertex Weight"),
            ("Physics", "Physics (Simulasi Fisika)", "Cloth, Collision, Fluid, Ocean, Soft Body, Dynamic Paint"),
            ("Hair & Assets", "Hair & Assets (Rambut Baru)", "Generate/Interpolate/Clump/Curl/Frizz Hair Curves"),
            ("Grease Pencil", "Grease Pencil (2D/Line Art)", "Line Art, Noise, Build, Thickness, Tint, Time Offset, dll"),
        ),
        default="Generate",
    )
    modifier_filter_text: StringProperty(
        name="Filter Nama/Fungsi Modifier",
        description="Ketik nama modifier atau fungsinya (misal: cermin, halus, tebal, bevel)",
        default="",
    )
    show_active_params: BoolProperty(
        name="Bedah Semua Input Variable",
        description="Tampilkan penjelasan Bahasa Gaul untuk setiap angka/tombol input di dalam modifier yang sedang aktif",
        default=True,
    )


@persistent
def _on_load_post(_dummy):
    # Pastikan preferensi tooltip tetap sinkron sesudah membuka file .blend baru
    if engine_gaul_translator.is_hover_active():
        try:
            prefs = bpy.context.preferences.view
            prefs.language = "en_US"
            prefs.use_translate_tooltips = True
            prefs.use_translate_interface = False
        except Exception:
            pass


def _register_keymaps() -> None:
    wm = bpy.context.window_manager
    if wm is None or wm.keyconfigs.addon is None:
        return
    km = wm.keyconfigs.addon.keymaps.new(name="Screen", space_type="EMPTY")
    kmi = km.keymap_items.new(
        "sobatgaul.inspect_hovered_popup",
        type="Q",
        value="PRESS",
        alt=True,
    )
    _KEYMAPS.append((km, kmi))


def _unregister_keymaps() -> None:
    for km, kmi in _KEYMAPS:
        try:
            km.keymap_items.remove(kmi)
        except Exception:
            pass
    _KEYMAPS.clear()


def register():
    bpy.utils.register_class(SOBATGAUL_PG_wm_settings)
    bpy.types.WindowManager.sobat_gaul = PointerProperty(type=SOBATGAUL_PG_wm_settings)

    operators.register()
    ui.register()
    _register_keymaps()

    engine_gaul_translator.enable_hover_translations()

    if _on_load_post not in bpy.app.handlers.load_post:
        bpy.app.handlers.load_post.append(_on_load_post)


def unregister():
    if _on_load_post in bpy.app.handlers.load_post:
        bpy.app.handlers.load_post.remove(_on_load_post)

    engine_gaul_translator.disable_hover_translations(restore_prefs=True)

    _unregister_keymaps()
    ui.unregister()
    operators.unregister()

    if hasattr(bpy.types.WindowManager, "sobat_gaul"):
        del bpy.types.WindowManager.sobat_gaul
    bpy.utils.unregister_class(SOBATGAUL_PG_wm_settings)
