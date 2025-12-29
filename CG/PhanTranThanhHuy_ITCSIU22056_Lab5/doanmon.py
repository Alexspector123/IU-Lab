#!/usr/bin/python3
import math
from py3d.core.base import Base
from py3d.core_ext.camera import Camera
from py3d.core_ext.mesh import Mesh
from py3d.core_ext.renderer import Renderer
from py3d.core_ext.scene import Scene
from py3d.core_ext.texture import Texture
from py3d.geometry.box import BoxGeometry
from py3d.geometry.parametric import ParametricGeometry
from py3d.geometry.rectangle import RectangleGeometry
from py3d.geometry.sphere import SphereGeometry
from py3d.material.surface import SurfaceMaterial
from py3d.material.texture import TextureMaterial
from py3d.extras.movement_rig import MovementRig
from py3d.extras.text_texture import TextTexture

outer_radius = 2.5     
inner_radius = 1.7     
gate_width = 0.5       
arc_angle = math.pi     
u_segments = 32       
v_segments = 16        

def arc_gate_outer_surface(u, v):
    theta = u * arc_angle 
    width_pos = (v - 0.5) * gate_width
    
    x = outer_radius * math.cos(theta)
    y = outer_radius * math.sin(theta)
    z = width_pos
    return [x, y, z]

def arc_gate_inner_surface(u, v):
    theta = u * arc_angle
    width_pos = (v - 0.5) * gate_width
    
    x = inner_radius * math.cos(theta)
    y = inner_radius * math.sin(theta)
    z = width_pos
    return [x, y, z]

def arc_gate_top_surface(u, v):
    theta = u * arc_angle
    radius_pos = inner_radius + v * (outer_radius - inner_radius)
    
    x = radius_pos * math.cos(theta)
    y = radius_pos * math.sin(theta)
    z = gate_width / 2
    return [x, y, z]

def arc_gate_bottom_surface(u, v):
    theta = u * arc_angle
    radius_pos = inner_radius + v * (outer_radius - inner_radius)
    
    x = radius_pos * math.cos(theta)
    y = radius_pos * math.sin(theta)
    z = -gate_width / 2
    return [x, y, z]

def create_gate_meshes(scene, pos_x=0, pos_y=0, pos_z=0, gate_depth=gate_width, color=[0.6, 0.4, 0.2]):
    # --- Gate Material ---
    gate_material = SurfaceMaterial(property_dict={
        "baseColor": color,
        "doubleSide": True,
        "useVertexColors": False
    })

    meshes = []
    # --- Outer Surface ---
    outer_geometry = ParametricGeometry(
        u_start=0, u_end=1,
        u_resolution=u_segments,
        v_start=0, v_end=1,
        v_resolution=v_segments,
        surface_function=arc_gate_outer_surface
    )
    outer_mesh = Mesh(outer_geometry, gate_material)
    outer_mesh.set_position([pos_x, pos_y + 1, pos_z])
    meshes.append(outer_mesh)

    # --- Inner Surface ---
    inner_geometry = ParametricGeometry(
        u_start=0, u_end=1,
        u_resolution=u_segments,
        v_start=0, v_end=1,
        v_resolution=v_segments,
        surface_function=arc_gate_inner_surface
    )
    inner_mesh = Mesh(inner_geometry, gate_material)
    inner_mesh.set_position([pos_x, pos_y + 1, pos_z])
    meshes.append(inner_mesh)

    # --- Top Surface ---
    top_geometry = ParametricGeometry(
        u_start=0, u_end=1,
        u_resolution=u_segments,
        v_start=0, v_end=1,
        v_resolution=8,
        surface_function=arc_gate_top_surface
    )
    top_mesh = Mesh(top_geometry, gate_material)
    top_mesh.set_position([pos_x, pos_y + 1, pos_z])
    meshes.append(top_mesh)

    # --- Bottom Surface ---
    bottom_geometry = ParametricGeometry(
        u_start=0, u_end=1,
        u_resolution=u_segments,
        v_start=0, v_end=1,
        v_resolution=8,
        surface_function=arc_gate_bottom_surface
    )
    bottom_mesh = Mesh(bottom_geometry, gate_material)
    bottom_mesh.set_position([pos_x, pos_y + 1, pos_z])
    meshes.append(bottom_mesh)

    height_offset = 2.0
    outer_mesh.set_position([pos_x, pos_y + 1 + height_offset/2, pos_z])
    inner_mesh.set_position([pos_x, pos_y + 1 + height_offset/2, pos_z])
    top_mesh.set_position([pos_x, pos_y + 1 + height_offset/2, pos_z])
    bottom_mesh.set_position([pos_x, pos_y + 1 + height_offset/2, pos_z])

    # --- Left Pillar ---
    thickness = outer_radius - inner_radius + 0.5
    left_pillar_geometry = BoxGeometry(
        width=thickness,
        height=outer_radius + height_offset,
        depth=gate_depth
    )
    left_pillar = Mesh(left_pillar_geometry, gate_material)
    left_pillar.set_position([
        pos_x - outer_radius + thickness/2,
        pos_y + (outer_radius)/2 + 1,
        pos_z
    ])
    meshes.append(left_pillar)

    # --- Right Pillar ---
    right_pillar_geometry = BoxGeometry(
        width=thickness,
        height=outer_radius + height_offset,
        depth=gate_depth
    )
    right_pillar = Mesh(right_pillar_geometry, gate_material)
    right_pillar.set_position([
        pos_x + outer_radius - thickness/2,
        pos_y + (outer_radius)/2 + 1,
        pos_z
    ])
    meshes.append(right_pillar)

    # --- Add to scene ---
    for mesh in meshes:
        scene.add(mesh)
    return meshes

def add_gate_roof(scene, pos_x=0, pos_y=0, pos_z=0, gate_width=0.5):
    roof_material = SurfaceMaterial(property_dict={
        "baseColor": [0.7, 0.2, 0.2],
        "doubleSide": True
    })

    # --- Main Roof (mái lớn) ---
    main_roof_width = outer_radius*2 + 1.0
    main_roof_height = 0.5
    main_roof_depth = gate_width + 1.0
    main_roof = Mesh(BoxGeometry(width=main_roof_width, height=main_roof_height, depth=main_roof_depth), roof_material)
    main_roof.set_position([pos_x, pos_y + outer_radius + 2.5, pos_z])
    scene.add(main_roof)

    # --- Top Roof (mái nhỏ trên) ---
    top_roof_width = outer_radius
    top_roof_height = 0.3
    top_roof_depth = gate_width + 0.5
    top_roof = Mesh(BoxGeometry(width=top_roof_width, height=top_roof_height, depth=top_roof_depth), roof_material)
    top_roof.set_position([pos_x, pos_y + outer_radius + 3.0, pos_z])
    scene.add(top_roof)

    return main_roof, top_roof

def add_railing_fence(scene, floor_center_x, floor_center_y, floor_center_z, floor_width, floor_depth, post_height=2.0, post_thickness=0.2, post_spacing=1.0, material_post=None, material_top=None, material_bar=None):
    if material_post is None:
        material_post = SurfaceMaterial(property_dict={"baseColor": [1.0, 0.84, 0.0], "doubleSide": True})  # vàng
    if material_top is None:
        material_top = SurfaceMaterial(property_dict={"baseColor": [1.0, 0.0, 0.0], "doubleSide": True})  # đỏ
    if material_bar is None:
        material_bar = SurfaceMaterial(property_dict={"baseColor": [1.0, 0.84, 0.0], "doubleSide": True})  # vàng

    meshes = []
    x_positions = [floor_center_x - floor_width/2 + i*post_spacing for i in range(int(floor_width/post_spacing)+1)]
    for x in x_positions:
        post_front = Mesh(BoxGeometry(width=post_thickness, height=post_height, depth=post_thickness), material_post)
        post_front.set_position([x, floor_center_y + post_height/2, floor_center_z + floor_depth/2])
        scene.add(post_front)
        meshes.append(post_front)

        top_front = Mesh(BoxGeometry(width=post_thickness, height=0.2, depth=post_thickness), material_top)
        top_front.set_position([x, floor_center_y + post_height + 0.1, floor_center_z + floor_depth/2])
        scene.add(top_front)
        meshes.append(top_front)

        post_back = Mesh(BoxGeometry(width=post_thickness, height=post_height, depth=post_thickness), material_post)
        post_back.set_position([x, floor_center_y + post_height/2, floor_center_z - floor_depth/2])
        scene.add(post_back)
        meshes.append(post_back)

        top_back = Mesh(BoxGeometry(width=post_thickness, height=0.2, depth=post_thickness), material_top)
        top_back.set_position([x, floor_center_y + post_height + 0.1, floor_center_z - floor_depth/2])
        scene.add(top_back)
        meshes.append(top_back)

    # Left & Right (dọc Z)
    z_positions = [floor_center_z - floor_depth/2 + i*post_spacing for i in range(int(floor_depth/post_spacing)+1)]
    for z in z_positions:
        # Left
        post_left = Mesh(BoxGeometry(width=post_thickness, height=post_height, depth=post_thickness), material_post)
        post_left.set_position([floor_center_x - floor_width/2, floor_center_y + post_height/2, z])
        scene.add(post_left)
        meshes.append(post_left)
        top_left = Mesh(BoxGeometry(width=post_thickness, height=0.2, depth=post_thickness), material_top)
        top_left.set_position([floor_center_x - floor_width/2, floor_center_y + post_height + 0.1, z])
        scene.add(top_left)
        meshes.append(top_left)

        # Right
        post_right = Mesh(BoxGeometry(width=post_thickness, height=post_height, depth=post_thickness), material_post)
        post_right.set_position([floor_center_x + floor_width/2, floor_center_y + post_height/2, z])
        scene.add(post_right)
        meshes.append(post_right)
        top_right = Mesh(BoxGeometry(width=post_thickness, height=0.2, depth=post_thickness), material_top)
        top_right.set_position([floor_center_x + floor_width/2, floor_center_y + post_height + 0.1, z])
        scene.add(top_right)
        meshes.append(top_right)

    # --- Nối các cột bằng thanh ngang ---
    # Front & Back horizontal bars
    bar_height = floor_center_y + post_height*0.2
    bar_thickness = post_thickness * 6
    front_bar = Mesh(BoxGeometry(width=floor_width, height=bar_thickness, depth=bar_thickness), material_bar)
    front_bar.set_position([floor_center_x, bar_height, floor_center_z + floor_depth/2])
    scene.add(front_bar)
    meshes.append(front_bar)

    back_bar = Mesh(BoxGeometry(width=floor_width, height=bar_thickness, depth=bar_thickness), material_bar)
    back_bar.set_position([floor_center_x, bar_height, floor_center_z - floor_depth/2])
    scene.add(back_bar)
    meshes.append(back_bar)

    # Left & Right horizontal bars
    left_bar = Mesh(BoxGeometry(width=bar_thickness, height=bar_thickness, depth=floor_depth), material_bar)
    left_bar.set_position([floor_center_x - floor_width/2, bar_height, floor_center_z])
    scene.add(left_bar)
    meshes.append(left_bar)

    right_bar = Mesh(BoxGeometry(width=bar_thickness, height=bar_thickness, depth=floor_depth), material_bar)
    right_bar.set_position([floor_center_x + floor_width/2, bar_height, floor_center_z])
    scene.add(right_bar)
    meshes.append(right_bar)

    return meshes

def add_middle_room(scene, center_x, center_y, center_z,
             room_width, room_depth, room_height,
             wall_thickness=0.2,
             door_width=1.2, door_count=3,
             arc_radius=0.6,
             material_wall=None, material_roof=None, material_arc=None):
    
    if material_wall is None:
        material_wall = SurfaceMaterial(property_dict={"baseColor":[0.7,0.7,0.7], "doubleSide": True})
    if material_roof is None:
        material_roof = SurfaceMaterial(property_dict={"baseColor":[0.6, 0.4, 0.2], "doubleSide": True})
    if material_arc is None:
        material_arc = SurfaceMaterial(property_dict={"baseColor":[0.7,0.7,0.7], "doubleSide": True})

    meshes = []

    door_spacing = (room_width - door_count * door_width) / (door_count + 1)
    x_start = center_x - room_width/2

    for i in range(door_count):
        gate_x = x_start + door_spacing*(i+1) + door_width*i + door_width/2
        create_gate_meshes(scene, pos_x=gate_x, pos_y=center_y, pos_z=center_z + room_depth/2,
                           gate_depth=wall_thickness, color=[0.7,0.7,0.7])
        
    # --- Front wall ---
    front_wall = Mesh(BoxGeometry(width=room_width/6, height=room_height + arc_radius, depth=wall_thickness), material_wall)
    front_wall.set_position([center_x*2, center_y + (room_height + arc_radius)/2, center_z - room_depth/2 + 6])
    scene.add(front_wall)
    meshes.append(front_wall)
    front_wall = Mesh(BoxGeometry(width=room_width/7, height=room_height + arc_radius, depth=wall_thickness), material_wall)
    front_wall.set_position([center_x/2 - 4, center_y + (room_height + arc_radius)/2, center_z - room_depth/2 + 6])
    scene.add(front_wall)
    meshes.append(front_wall)
    front_wall = Mesh(BoxGeometry(width=room_width, height=room_height/5, depth=wall_thickness), material_wall)
    front_wall.set_position([center_x/2 + 3.5, center_y + (room_height + arc_radius), center_z - room_depth/2 + 6])
    scene.add(front_wall)
    meshes.append(front_wall)

    # --- Back wall ---
    back_wall = Mesh(BoxGeometry(width=room_width, height=room_height + arc_radius, depth=wall_thickness), material_wall)
    back_wall.set_position([center_x, center_y + (room_height + arc_radius)/2, center_z - room_depth/2])
    scene.add(back_wall)
    meshes.append(back_wall)

    # --- Left wall ---
    left_wall = Mesh(BoxGeometry(width=wall_thickness, height=room_height + arc_radius, depth=room_depth), material_wall)
    left_wall.set_position([center_x - room_width/2, center_y + (room_height + arc_radius)/2, center_z])
    scene.add(left_wall)
    meshes.append(left_wall)

    # --- Right wall ---
    right_wall = Mesh(BoxGeometry(width=wall_thickness, height=room_height + arc_radius, depth=room_depth), material_wall)
    right_wall.set_position([center_x + room_width/2, center_y + (room_height + arc_radius)/2, center_z])
    scene.add(right_wall)
    meshes.append(right_wall)

    # --- Roof ---
    roof_thickness = 0.3
    roof = Mesh(BoxGeometry(width=room_width, height=roof_thickness, depth=room_depth), material_roof)
    roof.set_position([center_x, center_y + room_height + arc_radius + roof_thickness/2, center_z])
    scene.add(roof)
    meshes.append(roof)

    return meshes

def add_top_room(scene, center_x, center_y, center_z,
             room_width, room_depth, room_height,
             wall_thickness=0.2,
             door_width=1.2, door_count=3,
             arc_radius=0.6,
             material_wall=None, material_roof=None, material_arc=None):
    
    if material_wall is None:
        material_wall = SurfaceMaterial(property_dict={"baseColor":[0.7,0.7,0.7], "doubleSide": True})
    if material_roof is None:
        material_roof = SurfaceMaterial(property_dict={"baseColor":[0.6, 0.4, 0.2], "doubleSide": True})
    if material_arc is None:
        material_arc = SurfaceMaterial(property_dict={"baseColor":[0.7,0.7,0.7], "doubleSide": True})

    meshes = []

    door_spacing = (room_width - door_count * door_width) / (door_count + 1)
    x_start = center_x - room_width/2

    for i in range(door_count):
        gate_x = x_start + door_spacing*(i+1) + door_width*i + door_width/2
        create_gate_meshes(scene, pos_x=gate_x, pos_y=center_y, pos_z=center_z + room_depth/2,
                           gate_depth=wall_thickness, color=[0.7,0.7,0.7])
        
    # --- Front wall ---
    front_wall = Mesh(BoxGeometry(width=room_width/3 - 0.5, height=room_height + arc_radius, depth=wall_thickness), material_wall)
    front_wall.set_position([center_x*2 - 4, center_y + (room_height + arc_radius)/2, center_z - room_depth/2 + 3])
    scene.add(front_wall)
    meshes.append(front_wall)
    front_wall = Mesh(BoxGeometry(width=room_width/3 - 5, height=room_height + arc_radius, depth=wall_thickness), material_wall)
    front_wall.set_position([center_x/2, center_y + (room_height + arc_radius)/2, center_z - room_depth/2 + 3])
    scene.add(front_wall)
    meshes.append(front_wall)
    front_wall = Mesh(BoxGeometry(width=room_width, height=room_height/6, depth=wall_thickness), material_wall)
    front_wall.set_position([center_x/2 + 3.5, center_y + (room_height + arc_radius), center_z - room_depth/2 + 3])
    scene.add(front_wall)
    meshes.append(front_wall)

    # --- Back wall ---
    back_wall = Mesh(BoxGeometry(width=room_width, height=room_height + arc_radius, depth=wall_thickness), material_wall)
    back_wall.set_position([center_x, center_y + (room_height + arc_radius)/2, center_z - room_depth/2])
    scene.add(back_wall)
    meshes.append(back_wall)

    # --- Left wall ---
    left_wall = Mesh(BoxGeometry(width=wall_thickness, height=room_height + arc_radius, depth=room_depth), material_wall)
    left_wall.set_position([center_x - room_width/2, center_y + (room_height + arc_radius)/2, center_z])
    scene.add(left_wall)
    meshes.append(left_wall)

    # --- Right wall ---
    right_wall = Mesh(BoxGeometry(width=wall_thickness, height=room_height + arc_radius, depth=room_depth), material_wall)
    right_wall.set_position([center_x + room_width/2, center_y + (room_height + arc_radius)/2, center_z])
    scene.add(right_wall)
    meshes.append(right_wall)

    # --- Roof ---
    roof_thickness = 0.3
    roof = Mesh(BoxGeometry(width=room_width, height=roof_thickness, depth=room_depth), material_roof)
    roof.set_position([center_x, center_y + room_height + arc_radius + roof_thickness/2, center_z])
    scene.add(roof)
    meshes.append(roof)

    return meshes
class Example(Base):
    def initialize(self):
        print("Initializing program...")
        self.renderer = Renderer()
        self.scene = Scene()
        self.camera = Camera(aspect_ratio=800/600)
        self.sky_camera = Camera(aspect_ratio=512/512) 
        self.sky_camera.set_position([0, 20, 0]) 
        self.sky_camera.look_at([0, 0, 0])
        self.rig = MovementRig()
        self.rig.add(self.camera)
        self.rig.add(self.sky_camera)
        self.scene.add(self.rig)
        self.rig.set_position([0, 2, 6])

        # --- Sky ---
        sky_geometry = SphereGeometry(radius=50)
        sky_material = TextureMaterial(texture=Texture(file_name="textures/sky.jpg"))
        sky = Mesh(sky_geometry, sky_material)
        self.scene.add(sky)

        # --- Grass ---
        grass_geometry = RectangleGeometry(width=100, height=100)
        grass_material = TextureMaterial(
            texture=Texture(file_name="textures/grass.jpg"),
            property_dict={"repeatUV": [50, 50]}
        )
        grass = Mesh(grass_geometry, grass_material)
        grass.rotate_x(-math.pi/2)
        self.scene.add(grass)

        spacing = 7
        for i in range(3):
            create_gate_meshes(self.scene, pos_x=i*spacing, pos_y=0, pos_z=0, gate_depth=10.0)

        box_material = SurfaceMaterial(property_dict={
            "baseColor": [0.6, 0.4, 0.2],
            "doubleSide": True
        })

        box1_geometry = BoxGeometry(width=2, height=5, depth=9)
        box1 = Mesh(box1_geometry, box_material)
        box1.set_position([spacing/2, 1.5, 0])
        self.scene.add(box1)

        box2_geometry = BoxGeometry(width=2, height=5, depth=9)
        box2 = Mesh(box2_geometry, box_material)
        box2.set_position([spacing + spacing/2, 1.5, 0])
        self.scene.add(box2)

        create_gate_meshes(self.scene, pos_x=3.5 * spacing, pos_y=0, pos_z=0, gate_depth=10.0)
        box_3 = Mesh(BoxGeometry(width=spacing, height=5, depth=9), box_material)
        box_3.set_position([2*spacing + spacing - 1.25, 1.5, 0])
        self.scene.add(box_3)
        create_gate_meshes(self.scene, pos_x=-1.5 * spacing, pos_y=0, pos_z=0, gate_depth=10.0)
        box_4 = Mesh(BoxGeometry(width=spacing - 1.55, height=5, depth=9), box_material)
        box_4.set_position([-spacing + 1.75, 1.5, 0])
        self.scene.add(box_4)

        box_5 = Mesh(BoxGeometry(width=spacing*1.25, height=5, depth=9), box_material)
        box_5.set_position([4.5*spacing - 1, 1.5, 0])
        self.scene.add(box_5)
        box_6 = Mesh(BoxGeometry(width=spacing, height=5, depth=9), box_material)
        box_6.set_position([-spacing*2.5 + 1, 1.5, 0])
        self.scene.add(box_6)


        floor1 = Mesh(BoxGeometry(
            width=spacing*8, 
            height=1, 
            depth=9), 
            box_material)
        floor1.set_position([        
            7, 4.5, 0
            ])
        self.scene.add(floor1)

        add_railing_fence(
            scene=self.scene,
            floor_center_x=7,
            floor_center_y=4.5,
            floor_center_z=0,
            floor_width=spacing*8,
            floor_depth=9,
            post_height=1.3,
            post_thickness=0.2,
            post_spacing=5.0
        )

        add_middle_room(
            scene=self.scene,
            center_x=7,
            center_y=4.5,
            center_z=0,
            room_width=3*6 - 1.0,
            room_depth=6,
            room_height=4,
            wall_thickness=0.2,
            door_width=1.2,
            door_count=3
        )

        middle_room_y = 4.5
        room_width = 3*6 - 1.0
        room_depth = 6
        room_height = 4
        add_railing_fence(
            scene=self.scene,
            floor_center_x=7,
            floor_center_y=middle_room_y + room_height + 1,
            floor_center_z=0,
            floor_width=room_width,
            floor_depth=room_depth,
            post_height=1.3,
            post_thickness=0.2,
            post_spacing=5.0
        )

        top_room_y = middle_room_y + room_height + 1.3  # + chiều cao railing
        add_top_room(
            scene=self.scene,
            center_x=7,
            center_y=top_room_y,
            center_z=0,
            room_width=room_width * 0.5,
            room_depth=room_depth * 0.5,
            room_height=room_height,
            wall_thickness=0.2,
            door_width=1.2,
            door_count=1
        )
        small_box_width = room_width * 0.3
        small_box_depth = room_depth * 0.3
        small_box_height = room_height / 5
        dark_brown = [0.4, 0.25, 0.1]

        small_box_material = SurfaceMaterial(property_dict={
            "baseColor": dark_brown,
            "doubleSide": True
        })
        small_box = Mesh(BoxGeometry(width=small_box_width, height=small_box_height, depth=small_box_depth),
                        small_box_material)
        small_box.set_position([7, top_room_y + room_height + small_box_height/2 + 1, 0])
        self.scene.add(small_box)

        roof_width = room_width * 0.7
        roof_depth = room_depth * 0.7
        roof_height = small_box_height * 2.5
        roof_material = SurfaceMaterial(property_dict={
            "baseColor": [0.4, 0.25, 0.1],
            "doubleSide": True
        })

        def pyramid_roof(u, v):
            x = -roof_width/2 + u * roof_width
            z = -roof_depth/2 + v * roof_depth
            h = roof_height * (1 - max(abs(u-0.5)*2, abs(v-0.5)*2))
            y = h
            return [x, y, z]

        roof_mesh = Mesh(
            ParametricGeometry(u_start=0, u_end=1, u_resolution=20, v_start=0, v_end=1, v_resolution=20, surface_function=pyramid_roof),
            roof_material
        )
        roof_mesh.set_position([7, top_room_y + room_height + small_box_height, 0])
        self.scene.add(roof_mesh)

    def update(self):
        self.rig.update(self.input, self.delta_time)
        self.renderer.render(self.scene, self.sky_camera)
        self.renderer.render(self.scene, self.camera)

# --- RUN PROGRAM ---
Example(screen_size=[800, 600]).run()