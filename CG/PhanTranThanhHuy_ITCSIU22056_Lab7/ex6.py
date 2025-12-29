#!/usr/bin/python3
import math
import random

from py3d.core.base import Base
from py3d.core_ext.camera import Camera
from py3d.core_ext.mesh import Mesh
from py3d.core_ext.renderer import Renderer
from py3d.core_ext.scene import Scene
from py3d.core_ext.texture import Texture
from py3d.core_ext.object3d import Object3D

from py3d.geometry.box import BoxGeometry
from py3d.geometry.rectangle import RectangleGeometry
from py3d.geometry.sphere import SphereGeometry

from py3d.material.texture import TextureMaterial
from py3d.material.phong import PhongMaterial
from py3d.material.material import Material

from py3d.light.ambient import AmbientLight
from py3d.light.directional import DirectionalLight

from py3d.extras.movement_rig import MovementRig
from py3d.extras.text_texture import TextTexture

from doanmon import build_doan_mon

# ---------------------------------------------------------
# Wrapper: Phong + shadows, filter unsupported keys
# ---------------------------------------------------------
class SurfaceMaterial(PhongMaterial):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("number_of_light_sources", 2)  # ambient + sun
        kwargs.setdefault("use_shadow", True)

        pd = kwargs.get("property_dict")
        if pd is not None:
            pd = dict(pd)
            # py3d's PhongMaterial may not support these; drop to avoid errors
            pd.pop("specularColor", None)
            pd.pop("shininess", None)
            kwargs["property_dict"] = pd

        super().__init__(*args, **kwargs)


class Example(Base):

    # ---------- helper: trees ----------
    def make_tree(self, x, z, small=False):
        trunk_h = 0.9 if small else 1.2
        crown_r = 0.6 if small else 0.8

        trunk = Mesh(
            BoxGeometry(0.25, trunk_h, 0.25),
            SurfaceMaterial(property_dict={"baseColor": [0.45, 0.28, 0.15]}),
        )
        trunk.set_position([x, trunk_h / 2, z])
        self.scene.add(trunk)

        crown = Mesh(
            SphereGeometry(crown_r),
            SurfaceMaterial(property_dict={"baseColor": [0.15, 0.65, 0.15]}),
        )
        crown.set_position([x, trunk_h + crown_r * 0.7, z])
        self.scene.add(crown)

    # ---------- helper: building type picker ----------
    def pick_building_type(self, dist_from_center):
        """
        Return 'skyscraper', 'apartment', or 'house' with distance-based probabilities.
        Core: more towers; mid: more apartments; outer: more houses.
        """
        if dist_from_center < 30:
            probs = (0.6, 0.3, 0.1)   # S, A, H
        elif dist_from_center < 70:
            probs = (0.25, 0.45, 0.30)
        else:
            probs = (0.05, 0.25, 0.70)

        r = random.random()
        if r < probs[0]:
            return "skyscraper"
        elif r < probs[0] + probs[1]:
            return "apartment"
        else:
            return "house"

    # ---------- helper: skyscraper ----------
    def make_skyscraper(self, cx, cz, cell_w, cell_d):
        """Tall tower with stacked segments, footprint inside a single cell."""
        floor_h = 0.8
        floors = random.randint(14, 22)
        total_h = floors * floor_h

        min_side = 0.6 * min(cell_w, cell_d)
        base_w = min_side
        base_d = min_side

        tower_root = Object3D()
        tower_root.set_position([cx, 0, cz])
        self.scene.add(tower_root)

        base_color = [
            0.35,
            0.4 + 0.1 * random.random(),
            0.6 + 0.15 * random.random(),
        ]

        # lower body
        seg1_h = total_h * 0.6
        seg1 = Mesh(
            BoxGeometry(base_w, seg1_h, base_d),
            SurfaceMaterial(property_dict={"baseColor": base_color}),
        )
        seg1.set_position([0, seg1_h / 2, 0])
        tower_root.add(seg1)

        # horizontal floor bands
        band_count = int(floors * 0.6)
        if band_count > 0:
            step = seg1_h / band_count
            band_thick = step * 0.12
            for k in range(2, band_count, 2):
                y = k * step
                band = Mesh(
                    BoxGeometry(base_w * 1.01, band_thick, base_d * 1.01),
                    SurfaceMaterial(property_dict={"baseColor": [0.25, 0.3, 0.35]}),
                )
                band.set_position([0, y, 0])
                tower_root.add(band)

        # upper body
        seg2_w = base_w * 0.7
        seg2_d = base_d * 0.7
        seg2_h = total_h * 0.3
        seg2_color = [c * 0.9 for c in base_color]
        seg2 = Mesh(
            BoxGeometry(seg2_w, seg2_h, seg2_d),
            SurfaceMaterial(property_dict={"baseColor": seg2_color}),
        )
        seg2.set_position([0, seg1_h + seg2_h / 2, 0])
        tower_root.add(seg2)

        # top volume / penthouse
        top_w = seg2_w * 0.5
        top_d = seg2_d * 0.5
        top_h = total_h * 0.1
        top_color = [min(1.0, c * 1.1) for c in base_color]
        top = Mesh(
            BoxGeometry(top_w, top_h, top_d),
            SurfaceMaterial(property_dict={"baseColor": top_color}),
        )
        top.set_position([0, seg1_h + seg2_h + top_h / 2, 0])
        tower_root.add(top)

    # ---------- helper: apartment ----------
    def make_apartment(self, cx, cz, cell_w, cell_d):
        """Mid-rise apartment block with simple balconies + facade strips."""
        floor_h = 0.7
        floors = random.randint(5, 9)
        h = floors * floor_h

        body_w = 0.7 * cell_w
        body_d = 0.55 * cell_d

        color = [0.7, 0.7 - 0.1 * random.random(), 0.65]
        body = Mesh(
            BoxGeometry(body_w, h, body_d),
            SurfaceMaterial(property_dict={"baseColor": color}),
        )
        body.set_position([cx, h / 2, cz])
        self.scene.add(body)

        roof = Mesh(
            BoxGeometry(body_w * 0.98, 0.2, body_d * 0.98),
            SurfaceMaterial(property_dict={"baseColor": [c * 0.9 for c in color]}),
        )
        roof.set_position([cx, h + 0.1, cz])
        self.scene.add(roof)

        # balconies front/back
        balcony_depth = 0.6
        balcony_h = 0.15
        balcony_color = [0.85, 0.85, 0.88]
        for sign in (-1, 1):
            balcony = Mesh(
                BoxGeometry(body_w * 0.75, balcony_h, balcony_depth),
                SurfaceMaterial(property_dict={"baseColor": balcony_color}),
            )
            balcony.set_position(
                [cx, h * 0.45, cz + sign * (body_d / 2 + balcony_depth / 2)]
            )
            self.scene.add(balcony)

        # front glass strips (fake windows)
        strip_w = 0.2 * body_w
        for sx in (-0.35, 0.35):
            strip = Mesh(
                BoxGeometry(strip_w, h * 0.9, 0.04),
                SurfaceMaterial(property_dict={"baseColor": [0.5, 0.6, 0.75]}),
            )
            strip.set_position([
                cx + sx * body_w,
                h * 0.55,
                cz + body_d / 2 + 0.02,
            ])
            self.scene.add(strip)

    # ---------- helper: house ----------
    def make_house(self, cx, cz, cell_w, cell_d):
        """Low-rise house with small trees nearby (village / suburbs)."""
        body_w = 0.6 * cell_w
        body_d = 0.55 * cell_d
        h = random.uniform(1.6, 2.3)

        body_color = random.choice([
            [0.9, 0.75, 0.65],
            [0.82, 0.82, 0.7],
            [0.78, 0.86, 0.93],
        ])
        body = Mesh(
            BoxGeometry(body_w, h, body_d),
            SurfaceMaterial(property_dict={"baseColor": body_color}),
        )
        body.set_position([cx, h / 2, cz])
        self.scene.add(body)

        roof_h = 0.5
        roof_color = [0.6, 0.15, 0.15]
        roof = Mesh(
            BoxGeometry(body_w * 1.05, roof_h, body_d * 1.05),
            SurfaceMaterial(property_dict={"baseColor": roof_color}),
        )
        roof.set_position([cx, h + roof_h / 2, cz])
        self.scene.add(roof)

        # simple front windows
        win_w = body_w * 0.18
        win_h = h * 0.3
        for sx in (-0.3, 0.3):
            win = Mesh(
                BoxGeometry(win_w, win_h, 0.03),
                SurfaceMaterial(property_dict={"baseColor": [0.6, 0.75, 0.9]}),
            )
            win.set_position([
                cx + sx * body_w * 0.6,
                h * 0.6,
                cz + body_d / 2 + 0.02,
            ])
            self.scene.add(win)

        # two little trees in the yard
        self.make_tree(cx + body_w * 0.6, cz + body_d * 0.2, small=True)
        self.make_tree(cx - body_w * 0.6, cz - body_d * 0.2, small=True)

    # ---------- helper: vehicles ----------
    def add_vehicle(self, axis, lane_coord, start_pos, direction=1, vtype=None):
        """
        axis: "x" (east-west) or "z" (north-south)
        lane_coord: z (for x-axis) or x (for z-axis)
        start_pos: initial x or z
        direction: +1 or -1 along axis
        """
        if vtype is None:
            vtype = random.choice(["car", "car", "car", "truck", "bus"])

        if vtype == "car":
            length, width, height = 4.0, 2.0, 1.2
            body_color = random.choice([
                [0.9, 0.1, 0.1],
                [0.1, 0.1, 0.9],
                [0.1, 0.6, 0.2],
                [0.9, 0.8, 0.1],
            ])
            roof_color = [c * 0.8 for c in body_color]
        elif vtype == "truck":
            length, width, height = 7.0, 2.5, 2.0
            body_color = [0.8, 0.8, 0.82]
            roof_color = [0.7, 0.7, 0.72]
        else:  # bus
            length, width, height = 9.0, 2.7, 2.5
            body_color = [0.9, 0.85, 0.2]
            roof_color = [0.95, 0.95, 0.85]

        root = Object3D()
        y = height / 2 + self.road_height / 2 + 0.02

        if axis == "x":
            root.set_position([start_pos, y, lane_coord])
        else:
            root.set_position([lane_coord, y, start_pos])

        self.scene.add(root)

        # build geometry: lower body + upper cabin
        lower_h = height * 0.6
        upper_h = height * 0.4

        if axis == "x":
            lower_geom = BoxGeometry(length, lower_h, width)
            upper_geom = BoxGeometry(length * 0.6, upper_h, width * 0.9)
        else:
            lower_geom = BoxGeometry(width, lower_h, length)
            upper_geom = BoxGeometry(width * 0.9, upper_h, length * 0.6)

        lower = Mesh(
            lower_geom,
            SurfaceMaterial(property_dict={"baseColor": body_color}),
        )
        upper = Mesh(
            upper_geom,
            SurfaceMaterial(property_dict={"baseColor": roof_color}),
        )

        lower.set_position([0.0, lower_h / 2, 0.0])
        upper.set_position([0.0, lower_h + upper_h / 2, 0.0])

        root.add(lower)
        root.add(upper)

        self.vehicles.append({
            "axis": axis,
            "lane": lane_coord,
            "pos": start_pos,
            "dir": direction,
            "speed": random.uniform(7.0, 11.0),
            "y": y,
            "node": root,
            "cleared_center": False
        })

    def init_vehicles(self):
        self.vehicles = []

        # central east–west road (z = 0)
        z_main = 0.0
        lane_offset = 1.8

        # eastbound: left -> right
        for offset in (-60, -30, 0):
            self.add_vehicle(
                axis="x",
                lane_coord=z_main - lane_offset,
                start_pos=-80.0 + offset,
                direction=1,
            )

        # westbound: right -> left
        for offset in (0, 30, 60):
            self.add_vehicle(
                axis="x",
                lane_coord=z_main + lane_offset,
                start_pos=80.0 - offset,
                direction=-1,
            )

        # central north–south road (x = 0)
        x_main = 0.0
        lane_offset = 1.8

        # southbound: -z -> +z
        for offset in (-60, -30, 0):
            self.add_vehicle(
                axis="z",
                lane_coord=x_main - lane_offset,
                start_pos=-80.0 + offset,
                direction=1,
            )

        # northbound: +z -> -z
        for offset in (0, 30, 60):
            self.add_vehicle(
                axis="z",
                lane_coord=x_main + lane_offset,
                start_pos=80.0 - offset,
                direction=-1,
            )

    # ---------- helper: pedestrians ----------
    def add_pedestrian(self, axis, lane_coord, start_pos, direction=1):
        """
        Small person: box body + sphere head walking along sidewalk.
        axis, lane_coord, start_pos similar to vehicles.
        """
        root = Object3D()
        if axis == "x":
            root.set_position([start_pos, 0.0, lane_coord])
        else:
            root.set_position([lane_coord, 0.0, start_pos])
        self.scene.add(root)

        body_h = 1.1
        body = Mesh(
            BoxGeometry(0.4, body_h, 0.3),
            SurfaceMaterial(property_dict={"baseColor": [0.2, 0.3, 0.7]}),
        )
        body.set_position([0.0, body_h / 2, 0.0])
        root.add(body)

        head = Mesh(
            SphereGeometry(0.25),
            SurfaceMaterial(property_dict={"baseColor": [0.95, 0.8, 0.6]}),
        )
        head.set_position([0.0, body_h + 0.25, 0.0])
        root.add(head)

        self.pedestrians.append({
            "axis": axis,
            "lane": lane_coord,
            "pos": start_pos,
            "dir": direction,
            "speed": random.uniform(0.3, 0.7),
            "node": root,
        })

    def init_pedestrians(self):
        self.pedestrians = []
        sidewalk_offset = self.road_width / 2 + 0.9

        # along each east–west road: people walking east/west
        for z in self.road_z:
            for offset in (-70, -30, 10, 50):
                self.add_pedestrian("x", z - sidewalk_offset, offset, direction=1)
                self.add_pedestrian("x", z + sidewalk_offset, -offset, direction=-1)

        # along each north–south road: people walking north/south
        for x in self.road_x:
            for offset in (-70, -30, 10, 50):
                self.add_pedestrian("z", x - sidewalk_offset, offset, direction=1)
                self.add_pedestrian("z", x + sidewalk_offset, -offset, direction=-1)

    # ---------- helper: traffic lights ----------
    def build_traffic_lights(self):
        self.intersection_lights = []

        post_h = 5.0
        post_color = [0.2, 0.2, 0.2]
        bulb_size = 0.6

        # posts OUTSIDE crosswalks at the central intersection only
        r = self.road_width / 2 + self.crosswalk_width + 1.0
        y_post = post_h / 2
        y_bulb = post_h - 0.7

        corners = [
            (-r, -r),
            ( r, -r),
            (-r,  r),
            ( r,  r),
        ]

        for ix, iz in self.intersections:
            intersection = {
                "pos": (ix, iz),
                "ns_red": [], "ns_yellow": [], "ns_green": [],
                "ew_red": [], "ew_yellow": [], "ew_green": []
            }

            for (dx, dz) in corners:
                x, z = ix + dx, iz + dz

                # post
                post = Mesh(BoxGeometry(0.2, post_h, 0.2),
                            SurfaceMaterial(property_dict={"baseColor": post_color}))
                post.set_position([x, y_post, z])
                self.scene.add(post)

                # N–S bulbs
                ns_red = Mesh(BoxGeometry(bulb_size, bulb_size, bulb_size),
                            SurfaceMaterial(property_dict={"baseColor": [0.2,0,0]}))
                ns_yellow = Mesh(BoxGeometry(bulb_size, bulb_size, bulb_size),
                                SurfaceMaterial(property_dict={"baseColor": [0.2,0.2,0]}))
                ns_green = Mesh(BoxGeometry(bulb_size, bulb_size, bulb_size),
                                SurfaceMaterial(property_dict={"baseColor": [0,0.2,0]}))

                ns_red.set_position([x, y_bulb, z - 0.6])
                ns_yellow.set_position([x, y_bulb - (bulb_size + 0.2), z - 0.6])
                ns_green.set_position([x, y_bulb - 2*(bulb_size + 0.2), z - 0.6])
                self.scene.add(ns_red); self.scene.add(ns_yellow); self.scene.add(ns_green)
                intersection["ns_red"].append(ns_red)
                intersection["ns_yellow"].append(ns_yellow)
                intersection["ns_green"].append(ns_green)

                # E–W bulbs
                ew_red = Mesh(BoxGeometry(bulb_size, bulb_size, bulb_size),
                            SurfaceMaterial(property_dict={"baseColor": [0.2,0,0]}))
                ew_yellow = Mesh(BoxGeometry(bulb_size, bulb_size, bulb_size),
                                SurfaceMaterial(property_dict={"baseColor": [0.2,0.2,0]}))
                ew_green = Mesh(BoxGeometry(bulb_size, bulb_size, bulb_size),
                                SurfaceMaterial(property_dict={"baseColor": [0,0.2,0]}))

                ew_red.set_position([x - 0.6, y_bulb, z])
                ew_yellow.set_position([x - 0.6, y_bulb - (bulb_size + 0.2), z])
                ew_green.set_position([x - 0.6, y_bulb - 2*(bulb_size + 0.2), z])
                self.scene.add(ew_red); self.scene.add(ew_yellow); self.scene.add(ew_green)
                intersection["ew_red"].append(ew_red)
                intersection["ew_yellow"].append(ew_yellow)
                intersection["ew_green"].append(ew_green)

            self.intersection_lights.append(intersection)

    # ---------- helper: vehicle update with queueing ----------
    def update_vehicles(self, dt, ns_green, ew_green):
        # group vehicles by lane+direction
        lanes = {}
        for v in self.vehicles:
            key = (v["axis"], v["lane"], v["dir"])
            lanes.setdefault(key, []).append(v)

        intersection_half = 4.0 
        stop_line = -intersection_half

        for (axis, lane, d), group in lanes.items():
            # sort front-to-back along movement direction
            group.sort(key=lambda v: v["pos"] * d, reverse=True)

            ahead_pos = None
            for v in group:
                pos = v["pos"]
                speed = v["speed"]

                allowed = ew_green if axis == "x" else ns_green

                new_pos = pos + d * speed * dt
                region = self.classify_position(pos, intersection_half)

                # ---------- Green Light ----------
                if allowed and region == "before":
                    if pos * d < stop_line * d and new_pos * d >= stop_line * d:
                        v["cleared_center"] = True

                # red light: clamp at stop line near center
                must_stop = False
                if not allowed and not v["cleared_center"]:
                    if region == "before":
                        # chặn tại stop line
                        if pos * d < stop_line * d and new_pos * d >= stop_line * d:
                            new_pos = stop_line
                            must_stop = True
                        # giữ xe đứng yên nếu đã sát line
                        if abs(pos - stop_line) < 0.4:
                            new_pos = stop_line
                            must_stop = True

                # check if this step crosses map boundary
                wrapped = False
                if new_pos > 110.0:
                    new_pos = -110.0
                    wrapped = True
                    v["cleared_center"] = False
                elif new_pos < -110.0:
                    new_pos = 110.0
                    wrapped = True
                    v["cleared_center"] = False

                # keep safe distance from vehicle in front,
                # BUT only if this car did not just wrap around
                min_gap = 6.0  # center-to-center gap
                if ahead_pos is not None and not wrapped and not must_stop:
                    if d > 0:
                        max_pos = ahead_pos - min_gap
                        if new_pos > max_pos:
                            new_pos = max_pos
                    else:
                        min_pos = ahead_pos + min_gap
                        if new_pos < min_pos:
                            new_pos = min_pos

                v["pos"] = new_pos

                if axis == "x":
                    x, z = new_pos, lane
                else:
                    x, z = lane, new_pos

                v["node"].set_position([x, v["y"], z])

                # If this car wrapped, it is now at the *back* of the lane,
                # so we do NOT treat it as "ahead" for the others this frame.
                if not wrapped:
                    ahead_pos = new_pos

    # ---------- helper: pedestrians update ----------
    def update_pedestrians(self, dt):
        curb_offset = 0.5 
        crosswalk_distance = 1.5
        
        for p in self.pedestrians:
            pos = p["pos"]
            lane = p["lane"]
            axis = p["axis"]

            nearest_ix = min(self.intersections, key=lambda ix_iz: (pos - (ix_iz[0] if axis=="x" else ix_iz[1]))**2)
            ix, iz = nearest_ix

            if axis == "x":
                cross_pos = ix 
            else:
                cross_pos = iz

            distance_to_cross = abs(pos - cross_pos)

            if distance_to_cross < crosswalk_distance:
                crossing_direction_green = (self.t_ns_green if axis=="x" else self.t_ew_green)
                crossing_direction_yellow = (self.t_ns_yellow if axis=="x" else self.t_ew_yellow)

                if crossing_direction_green:
                    p["waiting"] = True
                    pos = cross_pos - math.copysign(curb_offset, pos - cross_pos)
                else:
                    p["waiting"] = False
                    pos += p["speed"] * dt
            else:
                pos += p["speed"] * dt

            # wrap around
            if p["pos"] > 115.0:
                p["pos"] = -115.0
            elif p["pos"] < -115.0:
                p["pos"] = 115.0

            p["pos"] = pos

            x, z = (pos, lane) if axis=="x" else (lane, pos)
            p["node"].set_position([x, 0.0, z])

    # ---------- helper: tree–intersection proximity ----------
    def is_near_intersection(self, x, z, margin):
        for ix, iz in self.intersections:
            if abs(x - ix) <= margin and abs(z - iz) <= margin:
                return True
        return False

    # ---------- helper: vehicles axis ----------
    def classify_position(self, pos_val, intersection_half=4.0):
        if pos_val < -intersection_half:
            return "before"
        elif pos_val > intersection_half:
            return "after"
        else:
            return "inside"
    
    # ---------- helper: airplane ----------
    def make_airplane(self):
        # Create Root Node
        self.plane_root = Object3D()
        
        # Material: White/Silver so shadows show up nicely
        plane_mat = SurfaceMaterial(property_dict={
            "baseColor": [0.9, 0.9, 1.0],
            "doubleSide": True
        })

        # --- 1. Fuselage (The Body) ---
        # Long along the Z axis
        fuselage = Mesh(BoxGeometry(width=1, height=1, depth=6), plane_mat)
        self.plane_root.add(fuselage)

        # --- 2. Main Wings ---
        # Wide along X axis
        wings = Mesh(BoxGeometry(width=8, height=0.2, depth=2), plane_mat)
        # Move wings slightly forward (negative Z is usually "forward" in OpenGL)
        wings.set_position([0, 0, -1]) 
        self.plane_root.add(wings)

        # --- 3. Vertical Tail ---
        # Tall, at the back (positive Z)
        tail_v = Mesh(BoxGeometry(width=0.4, height=2, depth=1.5), plane_mat)
        tail_v.set_position([0, 1, 2.5])
        self.plane_root.add(tail_v)

        # --- 4. Horizontal Tail ---
        # Wide, at the back
        tail_h = Mesh(BoxGeometry(width=3, height=0.2, depth=1.5), plane_mat)
        tail_h.set_position([0, 0.5, 2.5])
        self.plane_root.add(tail_h)

        # Add the whole group to the main scene
        self.scene.add(self.plane_root)
    # ==========================================================
    # initialize
    # ==========================================================
    def initialize(self):
        random.seed(1)

        self.renderer = Renderer()
        self.scene = Scene()

        # Cameras
        self.camera = Camera(aspect_ratio=800 / 600)
        self.rig = MovementRig(units_per_second=12)
        self.rig.add(self.camera)
        self.scene.add(self.rig)
        self.rig.set_position([0, 12, 45])
        self.camera.look_at([0, 0, 0])

        self.sky_camera = Camera(aspect_ratio=1.0)
        self.sky_camera.set_position([0, 80, 0])
        self.sky_camera.look_at([0, 0, 0])
        self.scene.add(self.sky_camera)

        # Lighting
        self.ambient_light = AmbientLight(color=[0.3, 0.3, 0.35])
        self.scene.add(self.ambient_light)

        self.sun_light = DirectionalLight(
            color=[1.0, 1.0, 0.9],
            direction=[-1, -1, -1],
        )
        self.scene.add(self.sun_light)

        self.renderer.enable_shadows(self.sun_light, strength=0.85)

        # Traffic light cycle
        self.traffic_cycle = 14.0       # total seconds per cycle
        self.traffic_ns_green_time = 3.0  # first half: NS green, EW red

        # ---- Traffic light timings ----
        self.t_ns_green = self.traffic_ns_green_time
        self.t_ns_yellow = 0.5
        self.t_ew_green = self.traffic_cycle - self.traffic_ns_green_time
        self.t_ew_yellow = 0.5

        self.traffic_cycle = (
            self.t_ns_green +
            self.t_ns_yellow +
            self.t_ew_green +
            self.t_ew_yellow
        )

        # Sky
        sky = Mesh(
            SphereGeometry(200),
            TextureMaterial(Texture(file_name="textures/sky.jpg")),
        )
        self.scene.add(sky)

        # Ground
        city_half = 100.0
        ground_material = PhongMaterial(
            texture=Texture(file_name="textures/grass.jpg"),
            number_of_light_sources=2,
            use_shadow=True,
        )
        ground = Mesh(
            RectangleGeometry(2 * city_half, 2 * city_half),
            ground_material,
        )
        ground.rotate_x(-math.pi / 2)
        ground.set_position([0, 0, 0])
        self.scene.add(ground)

        # Sun sphere (visual only)
        sun_geom = SphereGeometry(radius=3.0)
        vs_code = """
        uniform mat4 modelMatrix;
        uniform mat4 viewMatrix;
        uniform mat4 projectionMatrix;
        in vec3 vertexPosition;
        void main()
        {
            gl_Position = projectionMatrix * viewMatrix * modelMatrix
                          * vec4(vertexPosition, 1.0);
        }
        """
        fs_code = """
        out vec4 fragColor;
        void main()
        {
            fragColor = vec4(1.0, 0.9, 0.0, 1.0);
        }
        """
        sun_mat = Material(vs_code, fs_code)
        sun_mat.locate_uniforms()
        self.sun = Mesh(sun_geom, sun_mat)
        self.sun.set_position([0, 60, 0])
        self.scene.add(self.sun)

        # Label
        label_tex = TextTexture(
            text="City / Village Scene",
            system_font_name="Arial Bold",
            font_size=72,
            font_color=[1, 1, 1],
            image_width=1024,
            image_height=128,
            align_horizontal=0.5,
            align_vertical=0.5,
            image_border_width=4,
            image_border_color=[0, 0, 0],
        )
        self.label = Mesh(
            RectangleGeometry(6.0, 0.7),
            TextureMaterial(label_tex),
        )
        self.label.set_position([0, 18, -15])
        self.scene.add(self.label)

        # ========= Roads =========
        self.road_width = 8.0
        self.road_height = 0.04
        road_color = [0.12, 0.12, 0.12]

        # Road centers
        self.road_x = [-60, -30, 0, 30, 60]
        self.road_z = [-60, -30, 0, 30, 60]

        # North–south roads
        for x in self.road_x:
            road = Mesh(
                BoxGeometry(self.road_width, self.road_height, 2 * city_half),
                SurfaceMaterial(property_dict={"baseColor": road_color}),
            )
            road.set_position([x, self.road_height / 2, 0])
            self.scene.add(road)

        # East–west roads
        for z in self.road_z:
            road = Mesh(
                BoxGeometry(2 * city_half, self.road_height, self.road_width),
                SurfaceMaterial(property_dict={"baseColor": road_color}),
            )
            road.set_position([0, self.road_height / 2, z])
            self.scene.add(road)

        # Pre-compute all intersections (for crosswalks / tree clearing)
        self.intersections = [(rx, rz) for rx in self.road_x for rz in self.road_z]

        # Central plaza where roads cross at origin
        plaza = Mesh(
            BoxGeometry(18, 0.05, 18),
            SurfaceMaterial(property_dict={"baseColor": [0.32, 0.32, 0.35]}),
        )
        plaza.set_position([0, 0.05 / 2, 0])
        self.scene.add(plaza)

        # ---- Crosswalks at every intersection ----
        self.crosswalk_width = 2.0
        cw_w = self.crosswalk_width
        cw_len = self.road_width - 1.5
        zebra_mat = SurfaceMaterial(property_dict={"baseColor": [0.92, 0.92, 0.92]})

        for ix, iz in self.intersections:
            # across north–south road: west & east sides
            cw = Mesh(RectangleGeometry(cw_w, cw_len), zebra_mat)
            cw.rotate_x(-math.pi / 2)
            cw.set_position([ix - self.road_width / 2 - cw_w / 2, 0.051, iz])
            self.scene.add(cw)

            cw = Mesh(RectangleGeometry(cw_w, cw_len), zebra_mat)
            cw.rotate_x(-math.pi / 2)
            cw.set_position([ix + self.road_width / 2 + cw_w / 2, 0.051, iz])
            self.scene.add(cw)

            # across east–west road: south & north sides
            cw = Mesh(RectangleGeometry(cw_len, cw_w), zebra_mat)
            cw.rotate_x(-math.pi / 2)
            cw.set_position([ix, 0.051, iz - self.road_width / 2 - cw_w / 2])
            self.scene.add(cw)

            cw = Mesh(RectangleGeometry(cw_len, cw_w), zebra_mat)
            cw.rotate_x(-math.pi / 2)
            cw.set_position([ix, 0.051, iz + self.road_width / 2 + cw_w / 2])
            self.scene.add(cw)

        # ---- Lane markings for all roads (center dashed line) ----
        mark_mat = SurfaceMaterial(property_dict={"baseColor": [0.9, 0.9, 0.9]})
        # along every east–west road
        for z in self.road_z:
            for x in range(-90, 91, 8):
                dash = Mesh(RectangleGeometry(2.0, 0.4), mark_mat)
                dash.rotate_x(-math.pi / 2)
                dash.set_position([x, 0.051, z])
                self.scene.add(dash)
        # along every north–south road
        for x in self.road_x:
            for z in range(-90, 91, 8):
                dash = Mesh(RectangleGeometry(0.4, 2.0), mark_mat)
                dash.rotate_x(-math.pi / 2)
                dash.set_position([x, 0.051, z])
                self.scene.add(dash)

        # Traffic lights only at central intersection
        self.build_traffic_lights()

        # ========= Buildings per land plot (block) =========
        road_half = self.road_width / 2.0

        for i in range(len(self.road_x) - 1):
            rx0 = self.road_x[i]
            rx1 = self.road_x[i + 1]

            plot_xmin = rx0 + road_half
            plot_xmax = rx1 - road_half
            if plot_xmin >= plot_xmax:
                continue
            plot_w = plot_xmax - plot_xmin

            for j in range(len(self.road_z) - 1):
                rz0 = self.road_z[j]
                rz1 = self.road_z[j + 1]

                plot_zmin = rz0 + road_half
                plot_zmax = rz1 - road_half
                if plot_zmin >= plot_zmax:
                    continue
                plot_d = plot_zmax - plot_zmin

                # choose grid resolution for this block (2×2 or 3×2)
                grid_nx = 3 if plot_w > 25 else 2
                grid_nz = 3 if plot_d > 25 else 2

                cell_w = plot_w / grid_nx
                cell_d = plot_d / grid_nz

                for gx in range(grid_nx):
                    for gz in range(grid_nz):
                        # center of this cell
                        cx = plot_xmin + (gx + 0.5) * cell_w
                        cz = plot_zmin + (gz + 0.5) * cell_d

                        # jitter
                        jitter_x = (random.random() - 0.5) * 0.3 * cell_w
                        jitter_z = (random.random() - 0.5) * 0.3 * cell_d
                        cx += jitter_x
                        cz += jitter_z

                        dist = math.sqrt(cx * cx + cz * cz)

                        # leave some empty cells
                        if random.random() < 0.12:
                            continue

                        btype = self.pick_building_type(dist)

                        # if btype == "skyscraper":
                        #     self.make_skyscraper(cx, cz, cell_w, cell_d)
                        # elif btype == "apartment":
                        #     self.make_apartment(cx, cz, cell_w, cell_d)
                        # else:
                        #     self.make_house(cx, cz, cell_w, cell_d)

        # ========= Trees along roads (boulevards) =========
        tree_offset = self.road_width / 2 + 1.6
        clear_margin = self.road_width  # no trees close to any intersection

        # along E–W roads
        for z in self.road_z:
            for x in range(-80, 81, 10):
                for sign in (+1, -1):
                    tx = x
                    tz = z + sign * tree_offset
                    if self.is_near_intersection(tx, tz, clear_margin):
                        continue
                    self.make_tree(tx, tz, small=True)

        # along N–S roads
        for x in self.road_x:
            for z in range(-80, 81, 10):
                for sign in (+1, -1):
                    tx = x + sign * tree_offset
                    tz = z
                    if self.is_near_intersection(tx, tz, clear_margin):
                        continue
                    self.make_tree(tx, tz, small=True)

        # ========= Vehicles & Pedestrians =========
        self.init_vehicles()
        self.init_pedestrians()

        print("Building Doan Mon Gate...")
        build_doan_mon(self.scene, x=0, z=-70)

        self.make_airplane()
        self.plane_root.set_position([0, 40, 0])

    # ==========================================================
    # update
    # ==========================================================
    def update(self):
        # Gently rotate the label
        self.label.rotate_y(0.2 * self.delta_time)

        # ---------- Sun: sunrise -> midday -> sunset ----------
        day_speed = 0.08
        theta = (self.time * day_speed) % math.pi

        sun_x = 120.0 * math.cos(theta)          # east (+x) -> west (-x)
        sun_y = 10.0 + 70.0 * math.sin(theta)   # low at horizon, high at midday
        sun_z = -60.0                           # fixed distance in front

        self.sun.set_position([sun_x, sun_y, sun_z])

        # Directional light always points from sun to city center
        target = [0.0, 0.0, 0.0]
        dir_x = target[0] - sun_x
        dir_y = target[1] - sun_y
        dir_z = target[2] - sun_z
        self.sun_light.set_direction([dir_x, dir_y, dir_z])

        # ---------- Traffic lights state ----------
        cycle_time = self.time % self.traffic_cycle

        ns_green = ns_yellow = False
        ew_green = ew_yellow = False

        t1 = self.t_ns_green
        t2 = t1 + self.t_ns_yellow
        t3 = t2 + self.t_ew_green
        t4 = t3 + self.t_ew_yellow 

        if cycle_time < t1:
            # (a) NS green, EW red
            ns_green = True
        elif cycle_time < t2:
            # (b) NS yellow, EW red
            ns_yellow = True
        elif cycle_time < t3:
            # (c) NS red, EW green
            ew_green = True
        else:
            # (d) NS red, EW yellow
            ew_yellow = True

        red_on = [1.0, 0.1, 0.1]
        red_off = [0.2, 0.0, 0.0]
        green_on = [0.2, 1.0, 0.2]
        green_off = [0.0, 0.2, 0.0]
        yellow_on  = [1.0, 1.0, 0.2]
        yellow_off = [0.2, 0.2, 0.0]

        # update bulb colors via set_properties (material is read-only)
        for inter in self.intersection_lights:
            # NS bulbs
            for bulb in inter["ns_red"]:
                bulb.material.set_properties({"baseColor": red_on if not (ns_green or ns_yellow) else red_off})
            for bulb in inter["ns_yellow"]:
                bulb.material.set_properties({"baseColor": yellow_on if ns_yellow else yellow_off})
            for bulb in inter["ns_green"]:
                bulb.material.set_properties({"baseColor": green_on if ns_green else green_off})

            # EW bulbs
            for bulb in inter["ew_red"]:
                bulb.material.set_properties({"baseColor": red_on if not (ew_green or ew_yellow) else red_off})
            for bulb in inter["ew_yellow"]:
                bulb.material.set_properties({"baseColor": yellow_on if ew_yellow else yellow_off})
            for bulb in inter["ew_green"]:
                bulb.material.set_properties({"baseColor": green_on if ew_green else green_off})

        # ---------- Camera, vehicles, pedestrians ----------
        smoothed_dt = min(self.delta_time, 0.033)  # ~max step = 1/30 s
        self.update_vehicles(smoothed_dt, ns_green, ew_green)
        self.update_pedestrians(smoothed_dt)
        self.rig.update(self.input, smoothed_dt)

        # Render main camera (you can re-enable mini-map if you want)
        # self.renderer.render(self.scene, self.sky_camera)
        self.renderer.render(self.scene, self.camera)

        # Calculate circular path
        radius = 40.0
        plane_speed = 0.5
        # Use negative time to fly counter-clockwise, or positive for clockwise
        angle = self.time * plane_speed

        px = radius * math.cos(angle)
        pz = radius * math.sin(angle)
        py = 40

        self.plane_root.set_position([px, py, pz])
        # Rotate to face forward
        # If the plane flies in a circle, its rotation Y matches the angle (+ offset)
        # -angle makes it turn; + 3.14 (pi) might be needed depending on if nose is +Z or -Z
        turn_amount = plane_speed * self.delta_time
        self.plane_root.rotate_y(-turn_amount)


if __name__ == "__main__":
    Example(screen_size=[800, 600]).run()
