# file: doan_mon.py
import math
from py3d.core_ext.mesh import Mesh
from py3d.geometry.box import BoxGeometry
from py3d.geometry.parametric import ParametricGeometry
from py3d.material.phong import PhongMaterial

# --- 1. Custom Material & Global Settings ---
class SurfaceMaterial(PhongMaterial):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("number_of_light_sources", 2)
        kwargs.setdefault("use_shadow", True)
        super().__init__(*args, **kwargs)

outer_radius = 2.5     
inner_radius = 1.7     
gate_width = 0.5       
arc_angle = math.pi    
u_segments = 32       
v_segments = 16        

# --- 2. Math Helpers ---
def arc_gate_outer_surface(u, v):
    theta = u * arc_angle 
    width_pos = (v - 0.5) * gate_width
    return [outer_radius * math.cos(theta), outer_radius * math.sin(theta), width_pos]

def arc_gate_inner_surface(u, v):
    theta = u * arc_angle
    width_pos = (v - 0.5) * gate_width
    return [inner_radius * math.cos(theta), inner_radius * math.sin(theta), width_pos]

def arc_gate_top_surface(u, v):
    theta = u * arc_angle
    radius_pos = inner_radius + v * (outer_radius - inner_radius)
    return [radius_pos * math.cos(theta), radius_pos * math.sin(theta), gate_width / 2]

def arc_gate_bottom_surface(u, v):
    theta = u * arc_angle
    radius_pos = inner_radius + v * (outer_radius - inner_radius)
    return [radius_pos * math.cos(theta), radius_pos * math.sin(theta), -gate_width / 2]

# --- 3. Component Builders ---
def create_gate_meshes(scene, pos_x, pos_y, pos_z, gate_depth=gate_width, color=[0.6, 0.4, 0.2]):
    gate_material = SurfaceMaterial(property_dict={"baseColor": color, "doubleSide": True})
    meshes = []
    
    # Arches
    geoms = [
        ParametricGeometry(0,1,u_segments, 0,1,v_segments, arc_gate_outer_surface),
        ParametricGeometry(0,1,u_segments, 0,1,v_segments, arc_gate_inner_surface),
        ParametricGeometry(0,1,u_segments, 0,1,8, arc_gate_top_surface),
        ParametricGeometry(0,1,u_segments, 0,1,8, arc_gate_bottom_surface)
    ]
    
    height_offset = 2.0
    for geo in geoms:
        m = Mesh(geo, gate_material)
        m.set_position([pos_x, pos_y + 1 + height_offset/2, pos_z])
        meshes.append(m)

    # Pillars
    thickness = outer_radius - inner_radius + 0.5
    pillar_geo = BoxGeometry(thickness, outer_radius + height_offset, gate_depth)
    
    left = Mesh(pillar_geo, gate_material)
    left.set_position([pos_x - outer_radius + thickness/2, pos_y + (outer_radius)/2 + 1, pos_z])
    meshes.append(left)
    
    right = Mesh(pillar_geo, gate_material)
    right.set_position([pos_x + outer_radius - thickness/2, pos_y + (outer_radius)/2 + 1, pos_z])
    meshes.append(right)

    for m in meshes: scene.add(m)
    return meshes

def add_railing_fence(scene, cx, cy, cz, w, d, ph=2.0, pt=0.2, ps=1.0):
    mat_post = SurfaceMaterial(property_dict={"baseColor": [1.0, 0.84, 0.0], "doubleSide": True})
    mat_top = SurfaceMaterial(property_dict={"baseColor": [1.0, 0.0, 0.0], "doubleSide": True})
    mat_bar = SurfaceMaterial(property_dict={"baseColor": [1.0, 0.84, 0.0], "doubleSide": True})

    def add_box(geo, mat, x, y, z):
        m = Mesh(geo, mat)
        m.set_position([x, y, z])
        scene.add(m)

    # Front/Back posts
    x_pos = [cx - w/2 + i*ps for i in range(int(w/ps)+1)]
    for x in x_pos:
        add_box(BoxGeometry(pt, ph, pt), mat_post, x, cy + ph/2, cz + d/2)
        add_box(BoxGeometry(pt, 0.2, pt), mat_top, x, cy + ph + 0.1, cz + d/2)
        add_box(BoxGeometry(pt, ph, pt), mat_post, x, cy + ph/2, cz - d/2)
        add_box(BoxGeometry(pt, 0.2, pt), mat_top, x, cy + ph + 0.1, cz - d/2)

    # Left/Right posts
    z_pos = [cz - d/2 + i*ps for i in range(int(d/ps)+1)]
    for z in z_pos:
        add_box(BoxGeometry(pt, ph, pt), mat_post, cx - w/2, cy + ph/2, z)
        add_box(BoxGeometry(pt, 0.2, pt), mat_top, cx - w/2, cy + ph + 0.1, z)
        add_box(BoxGeometry(pt, ph, pt), mat_post, cx + w/2, cy + ph/2, z)
        add_box(BoxGeometry(pt, 0.2, pt), mat_top, cx + w/2, cy + ph + 0.1, z)

    # Bars
    bar_h = cy + ph*0.2
    bar_t = pt * 6
    add_box(BoxGeometry(w, bar_t, bar_t), mat_bar, cx, bar_h, cz + d/2)
    add_box(BoxGeometry(w, bar_t, bar_t), mat_bar, cx, bar_h, cz - d/2)
    add_box(BoxGeometry(bar_t, bar_t, d), mat_bar, cx - w/2, bar_h, cz)
    add_box(BoxGeometry(bar_t, bar_t, d), mat_bar, cx + w/2, bar_h, cz)

def add_room_structure(scene, cx, cy, cz, rw, rd, rh, wall_th=0.2, doors=3, is_top=False):
    mat_wall = SurfaceMaterial(property_dict={"baseColor":[0.7,0.7,0.7], "doubleSide": True})
    mat_roof = SurfaceMaterial(property_dict={"baseColor":[0.6, 0.4, 0.2], "doubleSide": True})
    
    # Doors
    door_w = 1.2
    spacing = (rw - doors * door_w) / (doors + 1)
    x_start = cx - rw/2
    for i in range(doors):
        gx = x_start + spacing*(i+1) + door_w*i + door_w/2
        create_gate_meshes(scene, gx, cy, cz + rd/2, wall_th, [0.7,0.7,0.7])
    
    arc_rad = 0.6
    
    # --- FIXED SECTION BELOW ---
    
    # Back Wall
    back_mesh = Mesh(BoxGeometry(rw, rh + arc_rad, wall_th), mat_wall)
    back_mesh.set_position([cx, cy + (rh+arc_rad)/2, cz - rd/2])
    scene.add(back_mesh)

    # Left Wall
    left_mesh = Mesh(BoxGeometry(wall_th, rh + arc_rad, rd), mat_wall)
    left_mesh.set_position([cx - rw/2, cy + (rh+arc_rad)/2, cz])
    scene.add(left_mesh)

    # Right Wall
    right_mesh = Mesh(BoxGeometry(wall_th, rh + arc_rad, rd), mat_wall)
    right_mesh.set_position([cx + rw/2, cy + (rh+arc_rad)/2, cz])
    scene.add(right_mesh)

    # Roof
    roof_mesh = Mesh(BoxGeometry(rw, 0.3, rd), mat_roof)
    roof_mesh.set_position([cx, cy + rh + arc_rad + 0.15, cz])
    scene.add(roof_mesh)

# --- 4. MAIN BUILD FUNCTION ---
def build_doan_mon(scene, x, z):
    """
    Builds the Doan Mon gate at specific x, z coordinates.
    Original code was centered roughly at x=7, z=0.
    We calculate offsets to move the whole structure.
    """
    dx = x - 7
    dz = z
    
    spacing = 7
    box_material = SurfaceMaterial(property_dict={"baseColor": [0.6, 0.4, 0.2], "doubleSide": True})

    # Base Arches
    for i in range(3):
        create_gate_meshes(scene, i*spacing + dx, 0, 0 + dz, 10.0)

    # Base Walls/Boxes
    def add_box(w, h, d, px, py, pz):
        m = Mesh(BoxGeometry(w, h, d), box_material)
        m.set_position([px + dx, py, pz + dz])
        scene.add(m)

    add_box(2, 5, 9, spacing/2, 1.5, 0)
    add_box(2, 5, 9, spacing + spacing/2, 1.5, 0)
    
    create_gate_meshes(scene, 3.5 * spacing + dx, 0, 0 + dz, 10.0)
    add_box(spacing, 5, 9, 2*spacing + spacing - 1.25, 1.5, 0)
    
    create_gate_meshes(scene, -1.5 * spacing + dx, 0, 0 + dz, 10.0)
    add_box(spacing - 1.55, 5, 9, -spacing + 1.75, 1.5, 0)
    add_box(spacing*1.25, 5, 9, 4.5*spacing - 1, 1.5, 0)
    add_box(spacing, 5, 9, -spacing*2.5 + 1, 1.5, 0)

    # Floor 1
    add_box(spacing*8, 1, 9, 7, 4.5, 0)

    # Railing 1
    add_railing_fence(scene, 7+dx, 4.5, 0+dz, spacing*8, 9, 1.3, 0.2, 5.0)

    # Middle Room
    add_room_structure(scene, 7+dx, 4.5, 0+dz, 3*6 - 1.0, 6, 4, 0.2, 3)

    # Railing 2
    middle_room_y = 4.5
    room_w = 3*6 - 1.0
    room_d = 6
    room_h = 4
    add_railing_fence(scene, 7+dx, middle_room_y + room_h + 1, 0+dz, room_w, room_d, 1.3, 0.2, 5.0)

    # Top Room
    top_room_y = middle_room_y + room_h + 1.3
    add_room_structure(scene, 7+dx, top_room_y, 0+dz, room_w*0.5, room_d*0.5, room_h, 0.2, 1)

    # Top Decoration
    small_w, small_d, small_h = room_w * 0.3, room_d * 0.3, room_h / 5
    dark_mat = SurfaceMaterial(property_dict={"baseColor": [0.4, 0.25, 0.1], "doubleSide": True})
    sb = Mesh(BoxGeometry(small_w, small_h, small_d), dark_mat)
    sb.set_position([7+dx, top_room_y + room_h + small_h/2 + 1, 0+dz])
    scene.add(sb)

    # Parametric Roof
    roof_w, roof_d, roof_h = room_w * 0.7, room_d * 0.7, small_h * 2.5
    
    def pyramid_roof(u, v):
        x_local = -roof_w/2 + u * roof_w
        z_local = -roof_d/2 + v * roof_d
        h = roof_h * (1 - max(abs(u-0.5)*2, abs(v-0.5)*2))
        return [x_local, h, z_local]

    roof_mesh = Mesh(
        ParametricGeometry(0, 1, 20, 0, 1, 20, pyramid_roof),
        dark_mat
    )
    roof_mesh.set_position([7+dx, top_room_y + room_h + small_h, 0+dz])
    scene.add(roof_mesh)