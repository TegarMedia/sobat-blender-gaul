# SPDX-License-Identifier: GPL-3.0-or-later
"""Operators untuk Pencarian YouTube & Google (Keyword Inggris), Popup Kartu Gaul, & Toggle Hover."""

from __future__ import annotations

import textwrap
import webbrowser
import bpy
from bpy.props import BoolProperty, EnumProperty, StringProperty
from bpy.types import Operator

from . import engine_gaul_translator as tr_engine
from .engine_inspector import inspect_hovered_ui_element, make_google_url, make_youtube_url
from .kamus_fitur_global import build_smart_english_query


def _open_browser_url(url: str) -> None:
    try:
        bpy.ops.wm.url_open(url=url)
    except Exception:
        webbrowser.open(url)


def _draw_wrapped_text(layout: bpy.types.UILayout, text: str, width: int = 68, icon: str = "NONE") -> None:
    first = True
    for raw_line in (text or "").splitlines():
        wrapped = textwrap.wrap(raw_line.strip(), width=width) or [""]
        for ln in wrapped:
            if not ln:
                continue
            row = layout.row(align=True)
            row.scale_y = 0.88
            row.label(text=ln, icon=icon if first else "BLANK1" if icon != "NONE" else "NONE")
            first = False


class SOBATGAUL_OT_search_web(Operator):
    """Fungsi: Cari tutorial fitur Blender ini di YouTube atau Google menggunakan Keyword Bahasa Inggris!\nCara Pakai: Klik tombol ini untuk langsung membuka hasil pencarian di browser."""

    bl_idname = "sobatgaul.search_web"
    bl_label = "Cari Tutorial (Keyword Inggris)"

    query: StringProperty(
        name="English Keyword",
        description="Kata kunci bahasa Inggris yang dipakai untuk mencari tutorial di YouTube / Google",
        default="",
    )
    engine: EnumProperty(
        name="Mesin Pencari",
        items=(
            ("YOUTUBE", "YouTube", "Langsung cari video tutorial di YouTube pakai keyword bahasa Inggris"),
            ("GOOGLE", "Google", "Cari penjelasan & artikel/video di Google pakai keyword bahasa Inggris"),
        ),
        default="YOUTUBE",
    )
    smart_translate: BoolProperty(
        name="Smart Indo->English",
        default=False,
    )

    def execute(self, _context):
        for_yt = self.engine == "YOUTUBE"
        final_q = build_smart_english_query(self.query, for_youtube=for_yt) if self.smart_translate else self.query.strip()
        if not final_q:
            final_q = "Blender 3D beginner tutorial"
        if "blender" not in final_q.lower():
            final_q = f"Blender {final_q}"

        url = make_youtube_url(final_q) if for_yt else make_google_url(final_q)
        _open_browser_url(url)
        target_name = "YouTube" if for_yt else "Google"
        self.report({"INFO"}, f"Membuka {target_name} dengan keyword Inggris: '{final_q}'")
        return {"FINISHED"}


class SOBATGAUL_OT_button_quick_search(Operator):
    """Fungsi: Langsung cari fitur/tombol yang baru kamu Klik Kanan ini di YouTube atau Google pakai Keyword Bahasa Inggris!\nCara Pakai: Klik menu ini untuk langsung membuka video atau artikel tutorialnya."""

    bl_idname = "sobatgaul.button_quick_search"
    bl_label = "Cari Fitur Ini (Keyword Inggris)"

    engine: EnumProperty(
        name="Mesin Pencari",
        items=(
            ("YOUTUBE", "YouTube", "Langsung buka pencarian video tutorial di YouTube"),
            ("GOOGLE", "Google", "Langsung buka pencarian penjelasan di Google"),
        ),
        default="YOUTUBE",
    )

    @classmethod
    def poll(cls, context):
        return (
            getattr(context, "button_prop", None) is not None
            or getattr(context, "button_operator", None) is not None
        )

    def execute(self, context):
        info = inspect_hovered_ui_element(context)
        if not info:
            self.report({"WARNING"}, "Arahkan kursor tepat di atas tombol atau angka fitur dulu ya!")
            return {"CANCELLED"}

        for_yt = self.engine == "YOUTUBE"
        kw = info["en_keyword_yt"] if for_yt else info["en_keyword_gg"]
        url = make_youtube_url(kw) if for_yt else make_google_url(kw)
        _open_browser_url(url)
        self.report({"INFO"}, f"Mencari di {'YouTube' if for_yt else 'Google'}: '{kw}'")
        return {"FINISHED"}


class SOBATGAUL_OT_inspect_hovered_popup(Operator):
    """Fungsi: Buka Kartu Pintar Bahasa Gaul untuk membedah Fungsi & Cara Pakai tombol yang ditunjuk kursor + tombol YouTube/Google!\nCara Pakai: Arahkan kursor ke tombol mana pun lalu tekan Alt+Q atau pilih dari Klik Kanan."""

    bl_idname = "sobatgaul.inspect_hovered_popup"
    bl_label = "Kartu Pintar Sobat Blender Gaul"

    custom_keyword: StringProperty(
        name="Keyword Inggris",
        description="Kamu juga bisa mengedit kata kunci bahasa Inggris ini sebelum klik Cari YouTube / Google",
        default="",
    )

    _info: dict[str, str] | None = None

    def invoke(self, context, _event):
        self._info = inspect_hovered_ui_element(context)
        if not self._info:
            self.report({"INFO"}, "Arahkan kursor ke salah satu tombol, slider, atau tab Properties dulu terus tekan Alt+Q!")
            return {"CANCELLED"}
        self.custom_keyword = self._info["en_keyword_yt"]
        return context.window_manager.invoke_props_dialog(self, width=470)

    def draw(self, _context):
        layout = self.layout
        info = self._info
        if not info:
            layout.label(text="Tidak ada tombol yang terdeteksi di bawah kursor.", icon="INFO")
            return

        # Header Nama Fitur
        header = layout.box()
        row = header.row(align=True)
        row.label(text=info["title"], icon="LIGHT")
        sub = header.row(align=True)
        sub.scale_y = 0.8
        sub.label(text=f"Kategori: {info['category']}", icon="TAG")

        # Fungsi Gaul
        box_f = layout.box()
        box_f.label(text="Fungsi (Bahasa Gaul Pemula):", icon="BOOKMARKS")
        _draw_wrapped_text(box_f, info["fungsi"], width=66)

        # Cara Pakai
        box_c = layout.box()
        box_c.label(text="Cara Pakai:", icon="TOOL_SETTINGS")
        _draw_wrapped_text(box_c, info["cara_pakai"], width=66)

        # Tips Tambahan
        if info.get("tips"):
            box_t = layout.box()
            box_t.label(text="Tips Anti-Bingung:", icon="SOLO_ON")
            _draw_wrapped_text(box_t, info["tips"], width=66)

        # Kotak Pencarian YouTube & Google (Keyword Bahasa Inggris)
        box_s = layout.box()
        box_s.label(text="Masih Bingung? Cari Video & Artikel (Keyword Inggris):", icon="VIEWZOOM")
        box_s.prop(self, "custom_keyword", text="Keyword")
        btn_row = box_s.row(align=True)
        btn_row.scale_y = 1.35

        op_yt = btn_row.operator("sobatgaul.search_web", text="Langsung Cari di YouTube", icon="PLAY")
        op_yt.query = self.custom_keyword
        op_yt.engine = "YOUTUBE"
        op_yt.smart_translate = False

        op_gg = btn_row.operator("sobatgaul.search_web", text="Cari di Google", icon="URL")
        op_gg.query = self.custom_keyword
        op_gg.engine = "GOOGLE"
        op_gg.smart_translate = False

    def execute(self, _context):
        return {"FINISHED"}


class SOBATGAUL_OT_toggle_hover(Operator):
    """Fungsi: Nyalakan atau matikan Hover Tooltip Bahasa Indonesia Gaul di seluruh tombol Blender.\nCara Pakai: Klik tombol ini kapan saja buat mengaktifkan atau mematikan mode Hover Bahasa Gaul."""

    bl_idname = "sobatgaul.toggle_hover"
    bl_label = "Toggle Mode Hover Bahasa Gaul"

    def execute(self, context):
        wm_settings = getattr(context.window_manager, "sobat_gaul", None)
        if tr_engine.is_hover_active():
            tr_engine.disable_hover_translations(restore_prefs=True)
            if wm_settings is not None:
                wm_settings.hover_enabled = False
            self.report({"INFO"}, "Mode Hover Bahasa Gaul: DIMATIKAN (kembali ke tooltip standar).")
        else:
            count = tr_engine.enable_hover_translations()
            if wm_settings is not None:
                wm_settings.hover_enabled = True
            self.report({"INFO"}, f"Mode Hover Bahasa Gaul: AKTIF ({count:,} fitur & input siap dijelasin!)")
        return {"FINISHED"}


class SOBATGAUL_OT_quick_add_modifier(Operator):
    """Fungsi: Pasang modifier ini langsung ke objek yang sedang kamu pilih di 3D Viewport!\nCara Pakai: Pilih objek dulu di layar 3D lalu klik tombol '+ Pasang' ini."""

    bl_idname = "sobatgaul.quick_add_modifier"
    bl_label = "Pasang Modifier Ini ke Objek"
    bl_options = {"REGISTER", "UNDO"}

    mod_type: StringProperty(name="Modifier Type", default="BEVEL")
    is_asset: BoolProperty(name="Is Asset Modifier", default=False)
    asset_name: StringProperty(name="Asset Name", default="")

    @classmethod
    def poll(cls, context):
        return context.object is not None

    def execute(self, context):
        try:
            if self.is_asset and self.asset_name:
                raw_name = "Array" if self.asset_name == "Array (Asset)" else self.asset_name
                bpy.ops.object.modifier_add_node_group(
                    asset_library_type="ESSENTIALS",
                    asset_library_identifier="",
                    relative_asset_identifier=f"nodes/geometry_nodes_essentials.blend/NodeTree/{raw_name}",
                )
                self.report({"INFO"}, f"Berhasil memasang modifier '{raw_name}' ke {context.object.name}!")
            else:
                bpy.ops.object.modifier_add(type=self.mod_type)
                self.report({"INFO"}, f"Berhasil memasang modifier '{self.mod_type}' ke {context.object.name}!")
            return {"FINISHED"}
        except Exception as exc:
            self.report({"WARNING"}, f"Modifier ini tidak cocok untuk tipe objek {context.object.type}: {exc}")
            return {"CANCELLED"}


class SOBATGAUL_OT_copy_keyword(Operator):
    """Fungsi: Salin keyword bahasa Inggris fitur ini ke Clipboard.\nCara Pakai: Klik ikon salin ini lalu Paste (Ctrl+V) di mana saja."""

    bl_idname = "sobatgaul.copy_keyword"
    bl_label = "Copy Keyword Inggris"

    keyword: StringProperty(default="")

    def execute(self, context):
        context.window_manager.clipboard = self.keyword
        self.report({"INFO"}, f"Keyword Inggris disalin: '{self.keyword}'")
        return {"FINISHED"}


CLASSES = (
    SOBATGAUL_OT_search_web,
    SOBATGAUL_OT_button_quick_search,
    SOBATGAUL_OT_inspect_hovered_popup,
    SOBATGAUL_OT_toggle_hover,
    SOBATGAUL_OT_quick_add_modifier,
    SOBATGAUL_OT_copy_keyword,
)


def register():
    for cls in CLASSES:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(CLASSES):
        bpy.utils.unregister_class(cls)
