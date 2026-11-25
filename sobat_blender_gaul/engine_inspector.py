# SPDX-License-Identifier: GPL-3.0-or-later
"""Smart UI Button Context Inspector & English Keyword Builder untuk Seluruh Fitur Blender."""

from __future__ import annotations

import urllib.parse
import bpy

from .engine_gaul_translator import explain_raw_gaul
from .kamus_constraints_physics import CONSTRAINT_CATALOG, SHADERFX_CATALOG, STRIP_MODIFIER_CATALOG
from .kamus_modifiers import ASSET_MODIFIER_CATALOG, MODIFIER_CATALOG, MODIFIER_PARAM_GAUL
from .kamus_render_mat_data import PRINCIPLED_BSDF_GAUL
from .kamus_tabs import TAB_GUIDES

_BSDF_MAP = {name: (kw, fungsi, cara) for name, kw, fungsi, cara in PRINCIPLED_BSDF_GAUL}


def make_youtube_url(en_query: str) -> str:
    clean = " ".join((en_query or "Blender 3D tutorial").split())
    return "https://www.youtube.com/results?search_query=" + urllib.parse.quote_plus(clean)


def make_google_url(en_query: str) -> str:
    clean = " ".join((en_query or "Blender 3D how to use").split())
    return "https://www.google.com/search?q=" + urllib.parse.quote_plus(clean)


def _clean_struct_label(rna_name: str, rna_id: str) -> str:
    label = (rna_name or rna_id or "").strip()
    for drop in ("Settings", "Properties", "Data"):
        if label.endswith(f" {drop}") and len(label) > len(drop) + 3:
            pass
    return label


def inspect_hovered_ui_element(context: bpy.types.Context) -> dict[str, str] | None:
    """Membaca elemen UI apa pun yang sedang ditunjuk kursor (baik di Properties maupun di seluruh Blender!)."""
    btn_prop = getattr(context, "button_prop", None)
    btn_ptr = getattr(context, "button_pointer", None)
    btn_op = getattr(context, "button_operator", None)

    # -------------------------------------------------------------------------
    # KASUS 1: Tombol Operator / Menu Item (misal di dalam Add Modifier, Extrude, Shade Smooth, dll)
    # -------------------------------------------------------------------------
    if btn_op is not None:
        op_rna = getattr(btn_op, "bl_rna", None)
        op_id = op_rna.identifier if op_rna else ""
        op_name = (op_rna.name if op_rna else "") or op_id
        op_desc = (op_rna.description if op_rna else "") or ""

        # Cek khusus menu Add Modifier SEBELUM diklik!
        if op_id == "OBJECT_OT_modifier_add":
            mtype = getattr(btn_op, "type", "")
            if mtype in MODIFIER_CATALOG:
                info = MODIFIER_CATALOG[mtype]
                return {
                    "title": f"{info['name']} Modifier",
                    "category": f"Modifier ({info['category']})",
                    "en_keyword_yt": info["en_keyword"],
                    "en_keyword_gg": info["en_keyword"].replace("tutorial", "how to use explained"),
                    "fungsi": info["fungsi"],
                    "cara_pakai": info["cara_pakai"],
                    "tips": info.get("tips", ""),
                }

        # Cek khusus Asset Modifier Blender 5.2 (Smooth by Angle, Scatter on Surface, Array baru, Hair!)
        if op_id == "OBJECT_OT_modifier_add_node_group":
            rel = getattr(btn_op, "relative_asset_identifier", "") or ""
            asset_name = rel.rsplit("/", 1)[-1] if "/" in rel else rel
            key = "Array (Asset)" if asset_name == "Array" else asset_name
            if key in ASSET_MODIFIER_CATALOG:
                info = ASSET_MODIFIER_CATALOG[key]
                return {
                    "title": f"{info['name']} Modifier",
                    "category": f"Asset Modifier ({info['category']})",
                    "en_keyword_yt": info["en_keyword"],
                    "en_keyword_gg": info["en_keyword"].replace("tutorial", "how to use"),
                    "fungsi": info["fungsi"],
                    "cara_pakai": info["cara_pakai"],
                    "tips": info.get("tips", ""),
                }
            if asset_name:
                f_gaul, c_gaul = explain_raw_gaul(op_desc, label=asset_name)
                return {
                    "title": f"{asset_name} (Node Modifier)",
                    "category": "Geometry Nodes Asset Modifier",
                    "en_keyword_yt": f"Blender {asset_name} Modifier tutorial",
                    "en_keyword_gg": f"Blender {asset_name} Modifier how to use",
                    "fungsi": f_gaul,
                    "cara_pakai": c_gaul,
                    "tips": "Atur parameter input di kotak Modifier sesudah dipasang ke objek.",
                }

        # Cek menu Add Constraint
        if op_id in {"OBJECT_OT_constraint_add", "POSE_OT_constraint_add"}:
            ctype = getattr(btn_op, "type", "")
            if ctype in CONSTRAINT_CATALOG:
                info = CONSTRAINT_CATALOG[ctype]
                return {
                    "title": f"{info['name']} Constraint",
                    "category": f"Constraint ({info['category']})",
                    "en_keyword_yt": info["en_keyword"],
                    "en_keyword_gg": info["en_keyword"].replace("tutorial", "explained"),
                    "fungsi": info["fungsi"],
                    "cara_pakai": info["cara_pakai"],
                    "tips": "",
                }

        # Cek menu Add Visual Effect (ShaderFX)
        if op_id == "OBJECT_OT_shaderfx_add":
            fxtype = getattr(btn_op, "type", "")
            if fxtype in SHADERFX_CATALOG:
                info = SHADERFX_CATALOG[fxtype]
                return {
                    "title": f"{info['name']} Visual Effect",
                    "category": "Grease Pencil Effects",
                    "en_keyword_yt": info["en_keyword"],
                    "en_keyword_gg": info["en_keyword"].replace("tutorial", "explained"),
                    "fungsi": info["fungsi"],
                    "cara_pakai": info["cara_pakai"],
                    "tips": "Aktifkan mode Rendered di 3D Viewport supaya efek visual langsung terlihat.",
                }

        # Cek tombol Active Tool di Toolbar (T)
        if op_id == "WM_OT_tool_set_by_id":
            tname = getattr(btn_op, "name", "") or ""
            pretty_tool = tname.replace("builtin.", "").replace("builtin_brush.", "").replace("_", " ").title()
            if pretty_tool:
                return {
                    "title": f"{pretty_tool} Tool",
                    "category": "Active Tool",
                    "en_keyword_yt": f"Blender {pretty_tool} Tool tutorial",
                    "en_keyword_gg": f"Blender {pretty_tool} Tool how to use",
                    "fungsi": f"Alat interaktif '{pretty_tool}' untuk mengedit atau memanipulasi objek langsung di viewport.",
                    "cara_pakai": "Klik ikon alat ini, lalu klik-tahan-geser di objek atau gunakan gizmo yang muncul. Pengaturan lengkapnya ada di Tab Active Tool paling atas Properties!",
                    "tips": "",
                }

        # Operator umum apa pun di seluruh Blender!
        prefix_cat = op_id.split("_OT_", 1)[0].replace("_", " ").title() if "_OT_" in op_id else "Operator"
        f_gaul, c_gaul = explain_raw_gaul(op_desc, label=op_name)
        en_base = f"Blender {prefix_cat} {op_name}".strip()
        return {
            "title": op_name,
            "category": f"{prefix_cat} Action",
            "en_keyword_yt": f"{en_base} tutorial",
            "en_keyword_gg": f"{en_base} how to use",
            "fungsi": f_gaul,
            "cara_pakai": c_gaul,
            "tips": "",
        }

    # -------------------------------------------------------------------------
    # KASUS 2: Input Variable / Slider / Checkbox / Dropdown / Node Socket (`button_prop` + `button_pointer`)
    # -------------------------------------------------------------------------
    if btn_prop is not None:
        prop_id = btn_prop.identifier
        prop_name = btn_prop.name or prop_id
        prop_desc = btn_prop.description or ""
        prop_type = btn_prop.type
        prop_sub = "COLOR" if (prop_type == "FLOAT" and "color" in prop_name.lower()) else ("ANGLE" if getattr(btn_prop, "unit", "NONE") == "ROTATION" else "NONE")

        owner_name = ""
        owner_id = ""
        if btn_ptr is not None and hasattr(btn_ptr, "bl_rna"):
            owner_name = btn_ptr.bl_rna.name or ""
            owner_id = btn_ptr.bl_rna.identifier or ""

        # Cek NodeSocket (misal Principled BSDF di Tab Material atau Shader/Geometry Nodes!)
        if btn_ptr is not None and hasattr(btn_ptr, "node") and getattr(btn_ptr, "node", None) is not None:
            node = btn_ptr.node
            sock_name = getattr(btn_ptr, "name", prop_name)
            node_label = getattr(node, "label", "") or getattr(node, "bl_label", "") or getattr(node, "name", "Shader Node")
            if sock_name in _BSDF_MAP and "Principled" in node_label:
                kw, f_bsdf, c_bsdf = _BSDF_MAP[sock_name]
                return {
                    "title": f"Principled BSDF › {sock_name}",
                    "category": "Material Shader Input",
                    "en_keyword_yt": f"{kw} tutorial",
                    "en_keyword_gg": f"{kw} explained",
                    "fungsi": f_bsdf,
                    "cara_pakai": c_bsdf,
                    "tips": "",
                }
            f_gaul, c_gaul = explain_raw_gaul(prop_desc, prop_type, prop_sub, sock_name)
            return {
                "title": f"{node_label} › {sock_name}",
                "category": "Node Input",
                "en_keyword_yt": f"Blender {node_label} {sock_name} node tutorial",
                "en_keyword_gg": f"Blender {node_label} {sock_name} how to use",
                "fungsi": f_gaul,
                "cara_pakai": c_gaul,
                "tips": "",
            }

        # Cek khusus Tab Context Selector di SpaceProperties
        if owner_id == "SpaceProperties" and prop_id == "context":
            cur_tab = getattr(btn_ptr, "context", "")
            if cur_tab in TAB_GUIDES:
                tg = TAB_GUIDES[cur_tab]
                return {
                    "title": tg["title"],
                    "category": "Properties Tab",
                    "en_keyword_yt": f"{tg['en_keyword']} tutorial",
                    "en_keyword_gg": f"{tg['en_keyword']} guide",
                    "fungsi": tg["gaul_summary"],
                    "cara_pakai": tg["cara_pakai"],
                    "tips": "",
                }

        # Cek kalau di dalam Modifier (termasuk Geometry Nodes Asset Modifier!)
        if btn_ptr is not None and isinstance(btn_ptr, bpy.types.Modifier):
            mod_type = getattr(btn_ptr, "type", "")
            if mod_type == "NODES" and getattr(btn_ptr, "node_group", None):
                ng_name = btn_ptr.node_group.name
                owner_clean = f"{ng_name} Modifier"
            elif mod_type in MODIFIER_CATALOG:
                owner_clean = f"{MODIFIER_CATALOG[mod_type]['name']} Modifier"
            else:
                owner_clean = owner_name or "Modifier"

            f_gaul, c_gaul = explain_raw_gaul(prop_desc, prop_type, prop_sub, prop_name)
            if prop_id in MODIFIER_PARAM_GAUL:
                f_gaul = MODIFIER_PARAM_GAUL[prop_id]

            return {
                "title": f"{owner_clean} › {prop_name}",
                "category": "Modifier Input Variable",
                "en_keyword_yt": f"Blender {owner_clean} {prop_name} tutorial",
                "en_keyword_gg": f"Blender {owner_clean} {prop_name} how to use",
                "fungsi": f_gaul,
                "cara_pakai": c_gaul,
                "tips": MODIFIER_CATALOG.get(mod_type, {}).get("tips", ""),
            }

        # Cek kalau di dalam Constraint
        if btn_ptr is not None and isinstance(btn_ptr, bpy.types.Constraint):
            con_type = getattr(btn_ptr, "type", "")
            con_label = CONSTRAINT_CATALOG.get(con_type, {}).get("name", owner_name or "Constraint")
            f_gaul, c_gaul = explain_raw_gaul(prop_desc, prop_type, prop_sub, prop_name)
            return {
                "title": f"{con_label} Constraint › {prop_name}",
                "category": "Constraint Input Variable",
                "en_keyword_yt": f"Blender {con_label} Constraint {prop_name} tutorial",
                "en_keyword_gg": f"Blender {con_label} Constraint {prop_name} explained",
                "fungsi": f_gaul,
                "cara_pakai": c_gaul,
                "tips": "",
            }

        # Semua properti lainnya di seluruh tab Properties & seluruh Blender!
        owner_clean = _clean_struct_label(owner_name, owner_id)
        f_gaul, c_gaul = explain_raw_gaul(prop_desc, prop_type, prop_sub, prop_name)

        # Bila properti bertipe ENUM, jelaskan juga opsi yang sedang terpilih sekarang!
        extra_tip = ""
        if prop_type == "ENUM" and btn_ptr is not None and hasattr(btn_prop, "enum_items"):
            try:
                cur_val = getattr(btn_ptr, prop_id, None)
                if isinstance(cur_val, str) and cur_val in btn_prop.enum_items:
                    ei = btn_prop.enum_items[cur_val]
                    if ei.description:
                        ef, _ = explain_raw_gaul(ei.description, label=ei.name)
                        extra_tip = f"Opsi aktif sekarang ('{ei.name}'): {ef}"
            except Exception:
                pass

        title_full = f"{owner_clean} › {prop_name}" if owner_clean else prop_name
        en_core = f"Blender {owner_clean} {prop_name}".strip()
        return {
            "title": title_full,
            "category": owner_clean or "Blender Property",
            "en_keyword_yt": f"{en_core} tutorial",
            "en_keyword_gg": f"{en_core} how to use explained",
            "fungsi": f_gaul,
            "cara_pakai": c_gaul,
            "tips": extra_tip,
        }

    # -------------------------------------------------------------------------
    # KASUS 3: Fallback — Bila dipanggil di area kosong dalam Properties Editor
    # -------------------------------------------------------------------------
    space = getattr(context, "space_data", None)
    if space is not None and getattr(space, "type", "") == "PROPERTIES":
        tab_ctx = getattr(space, "context", "")
        if tab_ctx in TAB_GUIDES:
            tg = TAB_GUIDES[tab_ctx]
            return {
                "title": tg["title"],
                "category": "Tab Properties Aktif",
                "en_keyword_yt": f"{tg['en_keyword']} tutorial",
                "en_keyword_gg": f"{tg['en_keyword']} guide",
                "fungsi": tg["gaul_summary"],
                "cara_pakai": tg["cara_pakai"],
                "tips": "Arahin kursor tepat di atas tombol/angka lalu tekan Alt+Q atau Klik Kanan buat bedah per-tombol!",
            }

    return None
