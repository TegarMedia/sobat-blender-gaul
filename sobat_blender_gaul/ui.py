# SPDX-License-Identifier: GPL-3.0-or-later
"""UI Panels di Seluruh 20 Tab Properties, Right-Click Menu Global, Live Inspector & Pencari YouTube/Google."""

from __future__ import annotations

import textwrap
import bpy
from bpy.types import AddonPreferences, Menu, Panel

from . import engine_gaul_translator as tr_engine
from .engine_inspector import inspect_hovered_ui_element
from .kamus_constraints_physics import (
    CONSTRAINT_CATALOG,
    PHYSICS_CATALOG,
    SHADERFX_CATALOG,
    STRIP_MODIFIER_CATALOG,
)
from .kamus_fitur_global import GLOBAL_BLENDER_FEATURES, build_smart_english_query
from .kamus_modifiers import ASSET_MODIFIER_CATALOG, MODIFIER_CATALOG, MODIFIER_PARAM_GAUL
from .kamus_render_mat_data import OBJECT_DATA_GUIDES, PRINCIPLED_BSDF_GAUL, RENDER_ENGINE_GUIDES
from .kamus_tabs import TAB_GUIDES

BASE_MOD_SKIP = {
    "rna_type", "name", "type", "show_viewport", "show_render", "show_in_editmode",
    "show_on_cage", "show_expanded", "is_active", "use_pin_to_last",
    "is_override_data", "use_apply_on_spline", "execution_time", "persistent_uid",
}
BASE_CON_SKIP = {
    "rna_type", "name", "type", "show_expanded", "is_override_data",
    "is_valid", "error_location", "error_rotation", "active",
}


def _region_wrap_width(default_w: int = 42) -> int:
    try:
        reg = getattr(bpy.context, "region", None)
        if reg and reg.width > 120:
            ui_sc = bpy.context.preferences.view.ui_scale or 1.0
            return max(24, min(78, int((reg.width / ui_sc - 58) / 6.4)))
    except Exception:
        pass
    return default_w


def _wrap_box(layout: bpy.types.UILayout, text: str, width: int = 0, icon: str = "NONE") -> None:
    eff_w = _region_wrap_width(width or 42)
    first = True
    for raw in (text or "").splitlines():
        lines = textwrap.wrap(raw.strip(), width=eff_w) or []
        for ln in lines:
            row = layout.row(align=True)
            row.scale_y = 0.82
            row.label(text=ln, icon=icon if first else ("BLANK1" if icon != "NONE" else "NONE"))
            first = False


def _draw_yt_google_buttons(layout: bpy.types.UILayout, en_keyword: str, compact: bool = False) -> None:
    row = layout.row(align=True)
    if not compact:
        row.scale_y = 1.15
    op_yt = row.operator(
        "sobatgaul.search_web",
        text="YouTube" if compact else "Cari di YouTube (EN)",
        icon="PLAY",
    )
    op_yt.query = en_keyword
    op_yt.engine = "YOUTUBE"
    op_yt.smart_translate = False

    op_gg = row.operator(
        "sobatgaul.search_web",
        text="Google" if compact else "Cari di Google (EN)",
        icon="URL",
    )
    op_gg.query = en_keyword.replace("tutorial", "how to use explained")
    op_gg.engine = "GOOGLE"
    op_gg.smart_translate = False


def draw_button_context_menu_extension(self: Menu, context: bpy.types.Context) -> None:
    """Ditambahkan ke menu Klik Kanan SEMUA tombol & angka di seluruh Blender!"""
    info = inspect_hovered_ui_element(context)
    if not info:
        return

    layout = self.layout
    layout.separator()
    short_title = info["title"]
    if len(short_title) > 36:
        short_title = short_title[:33] + "..."

    layout.label(text=f"Sobat Gaul: {short_title}", icon="BOOKMARKS")
    layout.operator("sobatgaul.inspect_hovered_popup", text="Baca Penjelasan Gaul Lengkap (Alt+Q)", icon="LIGHT")

    op_yt = layout.operator("sobatgaul.button_quick_search", text="Langsung Cari di YouTube (English)", icon="PLAY")
    op_yt.engine = "YOUTUBE"

    op_gg = layout.operator("sobatgaul.button_quick_search", text="Cari Penjelasan di Google (English)", icon="URL")
    op_gg.engine = "GOOGLE"


def _draw_top_bar_and_global_search(layout: bpy.types.UILayout, context: bpy.types.Context) -> None:
    wm_s = getattr(context.window_manager, "sobat_gaul", None)
    if wm_s is None:
        return

    # Baris Status Mode Hover + Shortcut Hint
    top = layout.box()
    row = top.row(align=True)
    active = tr_engine.is_hover_active()
    row.operator(
        "sobatgaul.toggle_hover",
        text="Hover Bahasa Gaul: AKTIF (Arahin Kursor!)" if active else "Hover Bahasa Gaul: MATI (Klik Nyalain)",
        icon="CHECKBOX_HLT" if active else "CHECKBOX_DEHLT",
        depress=active,
    )
    sub = top.row(align=True)
    sub.scale_y = 0.8
    sub.label(text="Tips: Arahin kursor ke tombol apa aja, atau Klik Kanan / Alt+Q buat cari YouTube!", icon="INFO")

    # Baris Pencarian Global Semua Fitur Blender (Indo / Inggris -> YouTube & Google)
    sbox = layout.box()
    hrow = sbox.row(align=True)
    hrow.prop(
        wm_s,
        "show_global_search",
        text="Cari Semua Fitur Blender (Google & YouTube)",
        icon="TRIA_DOWN" if wm_s.show_global_search else "TRIA_RIGHT",
        emboss=False,
    )
    if wm_s.show_global_search:
        sbox.prop(wm_s, "search_query", text="", icon="VIEWZOOM")
        q_raw = wm_s.search_query.strip()
        smart_en_yt = build_smart_english_query(q_raw, for_youtube=True)
        smart_en_gg = build_smart_english_query(q_raw, for_youtube=False)

        kw_row = sbox.row(align=True)
        kw_row.scale_y = 0.82
        kw_row.label(text=f"Keyword EN: {smart_en_yt}", icon="WORLD")
        cp = kw_row.operator("sobatgaul.copy_keyword", text="", icon="COPYDOWN")
        cp.keyword = smart_en_yt

        act = sbox.row(align=True)
        act.scale_y = 1.25
        oy = act.operator("sobatgaul.search_web", text="Langsung Cari YouTube", icon="PLAY")
        oy.query = q_raw or "Blender beginner tutorial"
        oy.engine = "YOUTUBE"
        oy.smart_translate = True

        og = act.operator("sobatgaul.search_web", text="Cari di Google", icon="URL")
        og.query = q_raw or "Blender beginner guide"
        og.engine = "GOOGLE"
        og.smart_translate = True

        # Tampilkan hasil kamus fitur yang cocok dengan ketikan user!
        if q_raw:
            ql = q_raw.lower()
            matches: list[tuple[str, str, str, str]] = []

            for info in MODIFIER_CATALOG.values():
                hay = f"{info['name']} {info['category']} {info['fungsi']} {info['en_keyword']}".lower()
                if ql in hay:
                    matches.append((f"Modifier ({info['category']})", info["name"], info["en_keyword"], info["fungsi"]))

            for info in ASSET_MODIFIER_CATALOG.values():
                hay = f"{info['name']} {info['category']} {info['fungsi']} {info['en_keyword']}".lower()
                if ql in hay:
                    matches.append(("Modifier Asset", info["name"], info["en_keyword"], info["fungsi"]))

            for info in CONSTRAINT_CATALOG.values():
                hay = f"{info['name']} {info['category']} {info['fungsi']}".lower()
                if ql in hay:
                    matches.append((f"Constraint ({info['category']})", info["name"], info["en_keyword"], info["fungsi"]))

            for cat, en_name, en_kw, indo_tags, gaul_desc in GLOBAL_BLENDER_FEATURES:
                hay = f"{cat} {en_name} {en_kw} {indo_tags} {gaul_desc}".lower()
                if ql in hay:
                    matches.append((cat, en_name, en_kw, gaul_desc))

            if matches:
                sbox.label(text=f"Ditemukan {len(matches)} fitur yang cocok:", icon="BOOKMARKS")
                for cat, name, kw, desc in matches[:8]:
                    card = sbox.box()
                    r = card.row(align=True)
                    r.label(text=f"[{cat}] {name}", icon="DOT")
                    _draw_yt_google_buttons(r, kw, compact=True)
                    _wrap_box(card, desc, width=50)


def _draw_modifier_tab_extras(layout: bpy.types.UILayout, context: bpy.types.Context) -> None:
    wm_s = getattr(context.window_manager, "sobat_gaul", None)
    ob = context.object

    # 1. KAMUS MODIFIER SEBELUM KLIK (Pilih Kategori -> Baca Fungsi & Cara Pakai -> Klik Pasang / YouTube!)
    if wm_s is not None:
        cat_box = layout.box()
        crow = cat_box.row(align=True)
        crow.prop(
            wm_s,
            "show_modifier_catalog",
            text="Kamus Semua Modifier (Baca Dulu Sebelum Klik!)",
            icon="TRIA_DOWN" if wm_s.show_modifier_catalog else "TRIA_RIGHT",
            emboss=False,
        )
        if wm_s.show_modifier_catalog:
            cat_box.prop(wm_s, "modifier_category_filter", text="Kategori")
            cat_box.prop(wm_s, "modifier_filter_text", text="", icon="VIEWZOOM")
            chosen_cat = wm_s.modifier_category_filter
            ftxt = wm_s.modifier_filter_text.strip().lower()

            combined_items: list[tuple[str, dict[str, str], bool]] = []
            for mid, minfo in MODIFIER_CATALOG.items():
                if chosen_cat != "ALL" and minfo["category"] != chosen_cat:
                    continue
                if ftxt and ftxt not in f"{minfo['name']} {minfo['fungsi']} {minfo['cara_pakai']}".lower():
                    continue
                combined_items.append((mid, minfo, False))

            for aname, ainfo in ASSET_MODIFIER_CATALOG.items():
                if chosen_cat != "ALL" and ainfo["category"] != chosen_cat:
                    continue
                if ftxt and ftxt not in f"{ainfo['name']} {ainfo['fungsi']} {ainfo['cara_pakai']}".lower():
                    continue
                combined_items.append((aname, ainfo, True))

            cat_box.label(text=f"Menampilkan {len(combined_items)} Modifier:", icon="MODIFIER")
            for key_id, minfo, is_asset in combined_items[:18]:
                mbox = cat_box.box()
                hdr = mbox.row(align=True)
                hdr.label(text=f"{minfo['name']} ({minfo['category']})", icon="MODIFIER_DATA")
                if ob is not None:
                    add_op = hdr.operator("sobatgaul.quick_add_modifier", text="+ Pasang", icon="ADD")
                    if is_asset:
                        add_op.is_asset = True
                        add_op.asset_name = key_id
                    else:
                        add_op.is_asset = False
                        add_op.mod_type = key_id

                _wrap_box(mbox, f"Fungsi: {minfo['fungsi']}", width=50)
                _wrap_box(mbox, f"Cara Pakai: {minfo['cara_pakai']}", width=50)
                if minfo.get("tips"):
                    _wrap_box(mbox, f"Tips: {minfo['tips']}", width=50)
                _draw_yt_google_buttons(mbox, minfo["en_keyword"], compact=False)

            if len(combined_items) > 18:
                cat_box.label(text=f"...ketik nama di kotak filter atas untuk melihat {len(combined_items) - 18} lainnya.", icon="INFO")

    # 2. BEDAH LENGKAP MODIFIER YANG SEDANG TERPASANG DI OBJEK INI (Sampe ke Input Variablenya!)
    if ob is not None and len(ob.modifiers) > 0:
        live_box = layout.box()
        live_box.label(text=f"Bedah Modifier Aktif di '{ob.name}' ({len(ob.modifiers)} terpasang):", icon="MODIFIER_ON")
        show_params = wm_s.show_active_params if wm_s else True
        if wm_s:
            live_box.prop(wm_s, "show_active_params", text="Tampilkan Penjelasan Semua Input Variable di Dalamnya")

        for mod in ob.modifiers:
            mcard = live_box.box()
            mtype = mod.type
            is_ng = mtype == "NODES" and getattr(mod, "node_group", None) is not None
            ng_name = mod.node_group.name if is_ng else ""

            if is_ng and (ng_name in ASSET_MODIFIER_CATALOG or ("Array (Asset)" if ng_name == "Array" else "") in ASSET_MODIFIER_CATALOG):
                akey = "Array (Asset)" if ng_name == "Array" else ng_name
                cat_entry = ASSET_MODIFIER_CATALOG[akey]
                en_kw = cat_entry["en_keyword"]
                fungsi_txt = cat_entry["fungsi"]
                cara_txt = cat_entry["cara_pakai"]
            elif mtype in MODIFIER_CATALOG:
                cat_entry = MODIFIER_CATALOG[mtype]
                en_kw = cat_entry["en_keyword"]
                fungsi_txt = cat_entry["fungsi"]
                cara_txt = cat_entry["cara_pakai"]
            else:
                en_kw = f"Blender {ng_name or mod.name} Modifier tutorial"
                fungsi_txt = f"Modifier Geometry Nodes '{ng_name or mod.name}'."
                cara_txt = "Atur nilai input di panel modifier bawah untuk mengubah hasil bentuk secara langsung."

            top_r = mcard.row(align=True)
            top_r.label(text=f"{mod.name} [{ng_name if is_ng else mtype}]", icon="DOT")
            _draw_yt_google_buttons(top_r, en_kw, compact=True)
            _wrap_box(mcard, f"Fungsi: {fungsi_txt}", width=50)
            _wrap_box(mcard, f"Cara: {cara_txt}", width=50)

            # Bedah setiap input variable di dalam modifier ini!
            if show_params:
                if is_ng and hasattr(mod.node_group, "interface"):
                    for item in mod.node_group.interface.items_tree:
                        if getattr(item, "item_type", "") == "SOCKET" and getattr(item, "in_out", "") == "INPUT":
                            sname = item.name
                            if sname in {"Geometry", "Mesh"}:
                                continue
                            sdesc = getattr(item, "description", "")
                            sf, _ = tr_engine.explain_raw_gaul(sdesc, label=sname)
                            pr = mcard.row(align=True)
                            pr.scale_y = 0.85
                            pr.label(text=f"• {sname}:", icon="RIGHTARROW_THIN")
                            _draw_yt_google_buttons(pr, f"Blender {ng_name} {sname} tutorial", compact=True)
                            _wrap_box(mcard, f"   {sf}", width=52)
                else:
                    for p in mod.bl_rna.properties:
                        if p.identifier in BASE_MOD_SKIP:
                            continue
                        pname = p.name or p.identifier
                        if p.identifier in MODIFIER_PARAM_GAUL:
                            p_gaul = MODIFIER_PARAM_GAUL[p.identifier]
                        else:
                            p_gaul, _ = tr_engine.explain_raw_gaul(p.description, p.type, "NONE", pname)
                        pr = mcard.row(align=True)
                        pr.scale_y = 0.85
                        pr.label(text=f"• {pname}:", icon="RIGHTARROW_THIN")
                        _draw_yt_google_buttons(pr, f"Blender {mod.bl_rna.name} {pname} tutorial", compact=True)
                        _wrap_box(mcard, f"   {p_gaul}", width=52)


def _draw_context_specific_extras(tab_key: str, layout: bpy.types.UILayout, context: bpy.types.Context) -> None:
    ob = context.object

    if tab_key == "MODIFIER":
        _draw_modifier_tab_extras(layout, context)
        return

    if tab_key == "RENDER" and context.scene:
        eng = context.scene.render.engine
        if eng in RENDER_ENGINE_GUIDES:
            eg = RENDER_ENGINE_GUIDES[eng]
            box = layout.box()
            box.label(text=f"Mesin Render Aktif: {eg['name']}", icon="SCENE")
            _wrap_box(box, f"Fungsi: {eg['fungsi']}", width=50)
            _wrap_box(box, f"Cara Pakai: {eg['cara_pakai']}", width=50)
            _draw_yt_google_buttons(box, eg["en_keyword"])

    elif tab_key == "MATERIAL":
        box = layout.box()
        box.label(text="Kamus Semua Input Principled BSDF (Cat Material Utama):", icon="MATERIAL")
        for sname, kw, f_txt, c_txt in PRINCIPLED_BSDF_GAUL:
            sb = box.box()
            r = sb.row(align=True)
            r.label(text=sname, icon="NODE_SOCKET_RGBA")
            _draw_yt_google_buttons(r, f"{kw} tutorial", compact=True)
            _wrap_box(sb, f"Fungsi: {f_txt}", width=50)
            _wrap_box(sb, f"Cara: {c_txt}", width=50)

    elif tab_key == "DATA" and ob is not None:
        od = OBJECT_DATA_GUIDES.get(ob.type)
        if od:
            box = layout.box()
            box.label(text=f"Objek Terpilih ({ob.type}): {od['title']}", icon="OUTLINER_DATA_MESH")
            _wrap_box(box, od["gaul"], width=50)
            _draw_yt_google_buttons(box, f"{od['en_keyword']} tutorial")
            for it_name, it_kw, it_desc in od["items"]:
                ib = box.box()
                r = ib.row(align=True)
                r.label(text=it_name, icon="DOT")
                _draw_yt_google_buttons(r, f"{it_kw} tutorial", compact=True)
                _wrap_box(ib, it_desc, width=50)

    elif tab_key in {"CONSTRAINT", "BONE_CONSTRAINT"}:
        cons = []
        if tab_key == "BONE_CONSTRAINT" and getattr(context, "active_pose_bone", None):
            cons = list(context.active_pose_bone.constraints)
        elif ob is not None:
            cons = list(ob.constraints)

        if cons:
            box = layout.box()
            box.label(text=f"Bedah Constraint Aktif ({len(cons)} terpasang):", icon="CONSTRAINT")
            for con in cons:
                cb = box.box()
                cinfo = CONSTRAINT_CATALOG.get(con.type)
                cname = cinfo["name"] if cinfo else con.name
                ckw = cinfo["en_keyword"] if cinfo else f"Blender {con.bl_rna.name} tutorial"
                r = cb.row(align=True)
                r.label(text=f"{con.name} [{cname}]", icon="DOT")
                _draw_yt_google_buttons(r, ckw, compact=True)
                if cinfo:
                    _wrap_box(cb, f"Fungsi: {cinfo['fungsi']}", width=50)
                    _wrap_box(cb, f"Cara: {cinfo['cara_pakai']}", width=50)
                for p in con.bl_rna.properties:
                    if p.identifier in BASE_CON_SKIP:
                        continue
                    pf, _ = tr_engine.explain_raw_gaul(p.description, p.type, "NONE", p.name)
                    _wrap_box(cb, f"• {p.name}: {pf}", width=50)

    elif tab_key == "PHYSICS":
        box = layout.box()
        box.label(text="Kamus Semua Sistem Simulasi Fisika Blender:", icon="PHYSICS")
        for pinfo in PHYSICS_CATALOG.values():
            pb = box.box()
            r = pb.row(align=True)
            r.label(text=pinfo["name"], icon="DOT")
            _draw_yt_google_buttons(r, pinfo["en_keyword"], compact=True)
            _wrap_box(pb, f"Fungsi: {pinfo['fungsi']}", width=50)
            _wrap_box(pb, f"Cara: {pinfo['cara_pakai']}", width=50)

    elif tab_key == "SHADERFX" and ob is not None and hasattr(ob, "shader_effects") and len(ob.shader_effects) > 0:
        box = layout.box()
        box.label(text="Efek Visual Grease Pencil Aktif:", icon="SHADERFX")
        for fx in ob.shader_effects:
            finfo = SHADERFX_CATALOG.get(fx.type)
            if finfo:
                fb = box.box()
                r = fb.row(align=True)
                r.label(text=finfo["name"], icon="DOT")
                _draw_yt_google_buttons(r, finfo["en_keyword"], compact=True)
                _wrap_box(fb, f"Fungsi: {finfo['fungsi']}", width=50)
                _wrap_box(fb, f"Cara: {finfo['cara_pakai']}", width=50)

    elif tab_key == "STRIP_MODIFIER":
        box = layout.box()
        box.label(text="Kamus Semua Strip Modifier Video & Audio:", icon="MODIFIER")
        for sinfo in STRIP_MODIFIER_CATALOG.values():
            sb = box.box()
            r = sb.row(align=True)
            r.label(text=sinfo["name"], icon="DOT")
            _draw_yt_google_buttons(r, f"{sinfo['en_keyword']} tutorial", compact=True)
            _wrap_box(sb, f"Fungsi: {sinfo['fungsi']}", width=50)


def draw_tab_guide_panel(layout: bpy.types.UILayout, context: bpy.types.Context, tab_key: str) -> None:
    _draw_top_bar_and_global_search(layout, context)

    tg = TAB_GUIDES.get(tab_key)
    if tg:
        wm_s = getattr(context.window_manager, "sobat_gaul", None)
        gbox = layout.box()
        grow = gbox.row(align=True)
        show_ov = wm_s.show_tab_overview if wm_s else True
        if wm_s:
            grow.prop(
                wm_s,
                "show_tab_overview",
                text=tg["title"],
                icon="TRIA_DOWN" if show_ov else "TRIA_RIGHT",
                emboss=False,
            )
        else:
            grow.label(text=tg["title"], icon="BOOKMARKS")

        if show_ov:
            _wrap_box(gbox, tg["gaul_summary"], width=50, icon="BOOKMARKS")
            cbox = gbox.box()
            cbox.label(text="Cara Pakai Cepat:", icon="TOOL_SETTINGS")
            _wrap_box(cbox, tg["cara_pakai"], width=50)
            _draw_yt_google_buttons(gbox, f"{tg['en_keyword']} tutorial")

            # Breakdown setiap sub-panel / bagian di dalam tab ini!
            sec_col = gbox.column(align=True)
            sec_col.label(text="Bedah Setiap Bagian di Tab Ini:", icon="LINENUMBERS_ON")
            for sec_title, sec_kw, sec_desc in tg.get("sections", []):
                sb = gbox.box()
                sr = sb.row(align=True)
                sr.label(text=sec_title, icon="DOT")
                _draw_yt_google_buttons(sr, f"{sec_kw} tutorial", compact=True)
                _wrap_box(sb, sec_desc, width=50)

    _draw_context_specific_extras(tab_key, layout, context)


# Pembuatan Panel Otomatis untuk SELURUH 19 Context di SpaceProperties + 1 Panel Active Tool + 1 N-Panel 3D Viewport!
_PROP_CONTEXT_MAP: list[tuple[str, str]] = [
    ("render", "RENDER"),
    ("output", "OUTPUT"),
    ("view_layer", "VIEW_LAYER"),
    ("scene", "SCENE"),
    ("world", "WORLD"),
    ("collection", "COLLECTION"),
    ("object", "OBJECT"),
    ("modifier", "MODIFIER"),
    ("particle", "PARTICLES"),
    ("physics", "PHYSICS"),
    ("constraint", "CONSTRAINT"),
    ("data", "DATA"),
    ("bone", "BONE"),
    ("bone_constraint", "BONE_CONSTRAINT"),
    ("material", "MATERIAL"),
    ("texture", "TEXTURE"),
    ("shaderfx", "SHADERFX"),
    ("strip", "STRIP"),
    ("strip_modifier", "STRIP_MODIFIER"),
]

GENERATED_PROP_PANELS: list[type] = []

for _bl_ctx, _tab_key in _PROP_CONTEXT_MAP:
    def _make_panel(bl_ctx: str, tab_key: str) -> type:
        cls_name = f"SOBATGAUL_PT_props_{bl_ctx}"

        def _draw(self, context):
            draw_tab_guide_panel(self.layout, context, tab_key)

        attrs = {
            "bl_label": "Sobat Blender Gaul — Panduan & Cari YouTube/Google",
            "bl_idname": cls_name,
            "bl_space_type": "PROPERTIES",
            "bl_region_type": "WINDOW",
            "bl_context": bl_ctx,
            "bl_order": -10 if tab_key == "MODIFIER" else 999,
            "bl_options": set() if tab_key == "MODIFIER" else {"DEFAULT_CLOSED"},
            "draw": _draw,
        }
        return type(cls_name, (Panel,), attrs)

    GENERATED_PROP_PANELS.append(_make_panel(_bl_ctx, _tab_key))


class SOBATGAUL_PT_tool_tab(Panel):
    """Muncul di Tab paling atas Properties (Active Tool & Workspace)!"""

    bl_label = "Sobat Blender Gaul — Panduan Alat Aktif & Cari Tutorial"
    bl_idname = "SOBATGAUL_PT_tool_tab"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Tool"
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        draw_tab_guide_panel(self.layout, context, "TOOL")


class SOBATGAUL_PT_view3d_npanel(Panel):
    """Panel cepat di Sidebar N-Panel 3D Viewport supaya bisa cari fitur Blender kapan aja!"""

    bl_label = "Sobat Blender Gaul"
    bl_idname = "SOBATGAUL_PT_view3d_npanel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Sobat Gaul"

    def draw(self, context):
        layout = self.layout
        _draw_top_bar_and_global_search(layout, context)
        _draw_modifier_tab_extras(layout, context)


class SOBATGAUL_Preferences(AddonPreferences):
    bl_idname = __package__

    def draw(self, context):
        layout = self.layout
        box = layout.box()
        box.label(text="Sobat Blender Gaul — Pengaturan & Cara Pakai Cepat:", icon="BOOKMARKS")
        _wrap_box(
            box,
            "1. Arahkan kursor (Hover) ke tombol, angka, dropdown, atau daftar Add Modifier apa pun di Properties buat langsung baca Fungsi & Cara Pakai dalam Bahasa Indonesia Gaul!\n"
            "2. Nama tombol sengaja dijaga tetap Bahasa Inggris asli supaya kamu gampang mengikuti tutorial internasional.\n"
            "3. Klik Kanan di tombol MANA PUN di seluruh Blender (atau tekan Alt+Q saat hover) buat membuka Kartu Pintar atau langsung mencari di YouTube & Google dengan Keyword Bahasa Inggris!",
            width=78,
        )
        active = tr_engine.is_hover_active()
        layout.operator(
            "sobatgaul.toggle_hover",
            text="Matikan Hover Bahasa Gaul" if active else "Aktifkan Hover Bahasa Gaul Sekarang",
            icon="CHECKBOX_HLT" if active else "CHECKBOX_DEHLT",
        )


STATIC_CLASSES = (
    SOBATGAUL_PT_tool_tab,
    SOBATGAUL_PT_view3d_npanel,
    SOBATGAUL_Preferences,
)


def register():
    for pcls in GENERATED_PROP_PANELS:
        bpy.utils.register_class(pcls)
    for cls in STATIC_CLASSES:
        bpy.utils.register_class(cls)
    if hasattr(bpy.types, "UI_MT_button_context_menu"):
        bpy.types.UI_MT_button_context_menu.append(draw_button_context_menu_extension)


def unregister():
    if hasattr(bpy.types, "UI_MT_button_context_menu"):
        try:
            bpy.types.UI_MT_button_context_menu.remove(draw_button_context_menu_extension)
        except Exception:
            pass
    for cls in reversed(STATIC_CLASSES):
        bpy.utils.unregister_class(cls)
    for pcls in reversed(GENERATED_PROP_PANELS):
        bpy.utils.unregister_class(pcls)
