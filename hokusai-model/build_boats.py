"""
Procedural model of the oshiokuri-bune (fast cargo boats) from Hokusai's
"The Great Wave off Kanagawa". Run with:
    blender --background --python build_boats.py
Exports:
    oshiokuri_boat.glb      - one boat with crouching crew and oars
    great_wave_boats.glb    - the three boats arranged as in the print
    preview.png             - quick render for checking
"""
import bpy, bmesh, math, os
from mathutils import Vector, Euler

OUT = os.path.dirname(os.path.abspath(__file__))

# ---------- dimensions (metres, X = length, bow at +X) ----------
L = 12.0      # overall length
W = 1.05      # max half-beam at gunwale
D = 0.75      # depth amidships
N_SEC = 48    # hull sections along length


def reset():
    bpy.ops.wm.read_factory_settings(use_empty=True)


def mat(name, rgb, rough=0.7):
    m = bpy.data.materials.new(name)
    m.use_nodes = True
    b = m.node_tree.nodes["Principled BSDF"]
    b.inputs["Base Color"].default_value = (*rgb, 1)
    b.inputs["Roughness"].default_value = rough
    return m


def half_beam(t):
    if t < 0.4:
        return W * (0.78 + 0.22 * math.sin(math.pi / 2 * t / 0.4))
    u = (t - 0.4) / 0.6
    return max(W * (1 - u ** 2) ** 0.75, 0.025)


def bottom_z(t):
    bow = 1.1 * D * max(0.0, (t - 0.55) / 0.45) ** 2.0
    stern = 0.12 * D * max(0.0, (0.08 - t) / 0.08) ** 2
    return bow + stern


def sheer_z(t):
    bow = 0.75 * D * max(0.0, (t - 0.5) / 0.5) ** 2.2
    stern = 0.12 * D * max(0.0, (0.15 - t) / 0.15) ** 2
    return D + bow + stern


def x_of(t):
    return -L / 2 + t * L


def section(t):
    """Wasen-style hard-chine profile: flat bottom (shiki) + flared sides (tana)."""
    w, zb, zs = half_beam(t), bottom_z(t), sheer_z(t)
    wb = 0.58 * w
    wm = wb + (w - wb) * 0.55
    zm = zb + (zs - zb) * 0.42
    half = [(0, zb), (wb, zb), (wm, zm), (w, zs)]
    pts = [(-y, z) for y, z in reversed(half[1:])] + half
    return [(x_of(t), y, z) for y, z in pts]


def build_hull(m_hull):
    bm = bmesh.new()
    rings = []
    for i in range(N_SEC + 1):
        t = i / N_SEC
        rings.append([bm.verts.new(p) for p in section(t)])
    n = len(rings[0])
    for a, b in zip(rings, rings[1:]):
        for j in range(n - 1):
            bm.faces.new((a[j], a[j + 1], b[j + 1], b[j]))
    bm.faces.new(list(reversed(rings[0])))   # transom
    bm.faces.new(rings[-1])                   # bow tip cap
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    me = bpy.data.meshes.new("Hull")
    bm.to_mesh(me)
    bm.free()
    ob = bpy.data.objects.new("Hull", me)
    bpy.context.collection.objects.link(ob)
    me.materials.append(m_hull)
    # open top: delete faces we don't want? Hull is open at the top already
    # (sections are U-shaped), so just give it plank thickness.
    sol = ob.modifiers.new("Solidify", "SOLIDIFY")
    sol.thickness = 0.045
    sol.offset = 1
    sub = ob.modifiers.new("Bevel", "BEVEL")
    sub.width = 0.01
    sub.segments = 2
    for f in me.polygons:
        f.use_smooth = False
    return ob


def box(name, loc, size, m, rot=(0, 0, 0)):
    bpy.ops.mesh.primitive_cube_add(size=1, location=loc, rotation=rot)
    ob = bpy.context.active_object
    ob.name = name
    ob.scale = size
    ob.data.materials.append(m)
    return ob


def cyl(name, loc, r, depth, m, rot=(0, 0, 0), verts=10):
    bpy.ops.mesh.primitive_cylinder_add(vertices=verts, radius=r, depth=depth,
                                        location=loc, rotation=rot)
    ob = bpy.context.active_object
    ob.name = name
    ob.data.materials.append(m)
    return ob


def sphere(name, loc, scale, m, rot=(0, 0, 0), seg=12):
    bpy.ops.mesh.primitive_uv_sphere_add(segments=seg, ring_count=seg // 2,
                                         radius=1, location=loc, rotation=rot)
    ob = bpy.context.active_object
    ob.name = name
    ob.scale = scale
    ob.data.materials.append(m)
    bpy.ops.object.shade_smooth()
    return ob


def rower(loc, facing, M):
    """Crouched oarsman in indigo, white tenugui headband - as in the print."""
    x, y, z = loc
    parts = []
    lean = math.radians(40) * facing
    parts.append(sphere("Torso", (x, y, z + 0.32), (0.22, 0.18, 0.30), M["indigo"],
                        rot=(0, lean, 0)))
    hx = x + 0.17 * facing
    parts.append(sphere("Head", (hx, y, z + 0.58), (0.11, 0.11, 0.12), M["skin"]))
    bpy.ops.mesh.primitive_torus_add(major_radius=0.105, minor_radius=0.03,
                                     location=(hx, y, z + 0.61),
                                     major_segments=14, minor_segments=6)
    band = bpy.context.active_object
    band.data.materials.append(M["white"])
    parts.append(band)
    # arms reaching to the gunwale
    for s in (-1, 1):
        parts.append(cyl("Arm", (x + 0.12 * facing, y + s * 0.2, z + 0.32), 0.05, 0.38,
                         M["indigo"], rot=(s * math.radians(50), math.radians(70) * facing, 0), verts=8))
    return parts


def build_boat(name, M, crew=True):
    parts = [build_hull(M["hull"])]

    # gunwale rails (top strakes, slightly darker wood)
    for side in (-1, 1):
        pts = []
        for i in range(N_SEC + 1):
            t = i / N_SEC
            pts.append(Vector((x_of(t), side * half_beam(t), sheer_z(t) + 0.03)))
        cu = bpy.data.curves.new("Rail", "CURVE")
        cu.dimensions = "3D"
        cu.bevel_depth = 0.045
        cu.bevel_resolution = 1
        sp = cu.splines.new("POLY")
        sp.points.add(len(pts) - 1)
        for p, v in zip(sp.points, pts):
            p.co = (*v, 1)
        ob = bpy.data.objects.new("Rail", cu)
        bpy.context.collection.objects.link(ob)
        cu.materials.append(M["wood_dark"])
        parts.append(ob)

    # thwarts / cross beams (funabari)
    for t in (0.12, 0.27, 0.42, 0.57, 0.70):
        w = half_beam(t)
        parts.append(box("Thwart", (x_of(t), 0, sheer_z(t) - 0.08),
                         (0.14, 2 * w + 0.1, 0.07), M["wood_dark"]))

    # floor boards
    for t0, t1 in ((0.05, 0.55),):
        xa, xb = x_of(t0), x_of(t1)
        parts.append(box("Floor", ((xa + xb) / 2, 0, 0.09),
                         (xb - xa, 1.0, 0.03), M["hull"]))

    # stem post sweeping up at the bow
    tip = Vector((x_of(1.0), 0, sheer_z(1.0)))
    parts.append(cyl("Stem", tip + Vector((0.05, 0, 0.15)), 0.05, 0.45, M["wood_dark"],
                     rot=(0, math.radians(20), 0), verts=8))
    # transom board
    parts.append(box("Transom", (x_of(0.0) - 0.02, 0, (D + 0.1) / 2 + 0.05),
                     (0.06, 2 * half_beam(0.0), D), M["wood_dark"]))
    # bow railing frame seen on the upper-right boat (tatami rack / yagura)
    tr = 0.80
    xr, zr = x_of(tr), sheer_z(tr)
    for s in (-1, 1):
        parts.append(cyl("Post", (xr, s * 0.35, zr + 0.25), 0.03, 0.5, M["wood_dark"], verts=6))
    parts.append(cyl("Bar", (xr, 0, zr + 0.48), 0.03, 0.8, M["wood_dark"],
                     rot=(math.radians(90), 0, 0), verts=6))

    if crew:
        # 8 crouching oarsmen in two rows, as in the print
        for t in (0.18, 0.31, 0.44, 0.56):
            x = x_of(t)
            z = 0.1
            for s in (-1, 1):
                parts += rower((x, s * 0.42, z), facing=-1, M=M)
        # oars (ro / kai) over the sides, angled into the water
        for t in (0.2, 0.36, 0.52):
            w = half_beam(t)
            for s in (-1, 1):
                pivot = Vector((x_of(t), s * w, sheer_z(t)))
                d = Vector((-0.3, s * 0.75, -0.6)).normalized()
                rot = d.to_track_quat("Z", "Y").to_euler()
                parts.append(cyl("Oar", pivot + d * 0.8, 0.03, 2.6, M["wood_dark"],
                                 rot=rot, verts=6))
                parts.append(box("Blade", pivot + d * 2.2, (0.04, 0.18, 0.6),
                                 M["wood_dark"], rot=rot))

    # apply modifiers / convert curves, then join into one object
    bpy.ops.object.select_all(action="DESELECT")
    for ob in parts:
        ob.select_set(True)
    bpy.context.view_layer.objects.active = parts[0]
    bpy.ops.object.convert(target="MESH")
    bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)
    bpy.ops.object.join()
    boat = bpy.context.active_object
    boat.name = name
    boat.data.name = name
    return boat


def materials():
    return {
        "hull": mat("Hull_Wood", (0.86, 0.74, 0.55)),       # pale tan of the print
        "wood_dark": mat("Wood_Trim", (0.55, 0.42, 0.28)),
        "indigo": mat("Indigo_Cloth", (0.06, 0.17, 0.42), 0.9),  # Prussian-blue robes
        "skin": mat("Skin", (0.80, 0.62, 0.45)),
        "white": mat("Tenugui_White", (0.95, 0.95, 0.92)),
    }


def export(path, objs):
    bpy.ops.object.select_all(action="DESELECT")
    for o in objs:
        o.select_set(True)
    bpy.ops.export_scene.gltf(filepath=path, export_format="GLB",
                              use_selection=True, export_apply=True)
    print("WROTE", path)


# ---------- 1) single boat ----------
reset()
M = materials()
boat = build_boat("Oshiokuri_Bune", M)
export(os.path.join(OUT, "oshiokuri_boat.glb"), [boat])

# ---------- 2) three boats posed like the print ----------
b1 = boat
b1.name = "Boat_Left"            # under the great wave, bow rising to the left
b1.location = (-9, 3, 1.5)
b1.rotation_euler = Euler((math.radians(-10), math.radians(-25), math.radians(170)))
b2 = build_boat("Boat_Center", M)  # foreground, sliding down a trough
b2.location = (0, -2, -1.0)
b2.rotation_euler = Euler((math.radians(8), math.radians(10), math.radians(-12)))
b3 = build_boat("Boat_Right", M)   # far right, riding up a crest
b3.location = (7, 6, 2.5)
b3.rotation_euler = Euler((math.radians(-5), math.radians(-20), math.radians(-160)))
export(os.path.join(OUT, "great_wave_boats.glb"), [b1, b2, b3])

# ---------- preview render ----------
scn = bpy.context.scene
scn.render.engine = "BLENDER_EEVEE" if "BLENDER_EEVEE" in [e.identifier for e in bpy.types.RenderSettings.bl_rna.properties["engine"].enum_items] else "BLENDER_EEVEE_NEXT"
scn.view_settings.view_transform = "Standard"
scn.render.resolution_x, scn.render.resolution_y = 1600, 900
world = bpy.data.worlds.new("W")
world.use_nodes = True
world.node_tree.nodes["Background"].inputs[0].default_value = (0.93, 0.89, 0.80, 1)
scn.world = world
bpy.ops.object.light_add(type="SUN", rotation=(math.radians(40), 0, math.radians(30)))
bpy.context.active_object.data.energy = 4
bpy.ops.object.camera_add(location=(4, -26, 12))
cam = bpy.context.active_object
direction = Vector((-1, 2, 1)) - cam.location
cam.rotation_euler = direction.to_track_quat("-Z", "Y").to_euler()
cam.data.lens = 40
scn.camera = cam
scn.render.filepath = os.path.join(OUT, "preview.png")
bpy.ops.render.render(write_still=True)
print("WROTE preview")
