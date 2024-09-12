<template>
  <main class="flex size-full h-screen flex-col items-center justify-center">
    <h1 class=" text-center">Rubik</h1>
    <div class="rubik_canvas_div">
      <!-- <canvas id="rubik_canvas" width="200" height="200"></canvas> -->
    </div>
    <div id="rubik_canvas" ref="threeContainer" class="size-96 min-h-96 min-w-96"></div>
  </main>
</template>

<script setup lang="ts">
import * as THREE from 'three';
import * as TWEEN from '@tweenjs/tween.js'
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';
import { createRubik, changeCubeFaceColors } from '@/js/rubik_utils';

import { onMounted, onUnmounted, ref } from 'vue';

// Déclarer une référence pour le conteneur
const threeContainer = ref(null);
let canva: HTMLElement | null;
let scene: THREE.Scene;
let camera: THREE.PerspectiveCamera;
let pointer: THREE.Vector2;
let raycaster: THREE.Raycaster;
let renderer: THREE.WebGLRenderer;
let controls: OrbitControls;


let INTERSECTED: THREE.Mesh | null;
let INTERSECTED_FACE_INDEX: number | undefined | null;

// Init RUBIK
let rubik3D: Rubik3D;



// Except JSON from backend
/*
{
  number_moves: XY,
  results: [
    {
      rubik: [[[[...]]]],
      move: X'
    },
    ...
  ]
}


*/



class Rubik3D {
  // Cube info
  x: number;
  y: number;
  z: number;

  default_faces_colors: Array<Array<Array<string>>>;
  all_cubes: THREE.Mesh<THREE.BoxGeometry, THREE.MeshBasicMaterial[], THREE.Object3DEventMap>[];

  // Animation settings
  second_between_animation: number;
  animation_speed: number;
  animation_is_playing: boolean;

  // Animation visualization
  current_frame: number;
  current_tween: TWEEN.Tween | undefined;
  frames: Array<Object>

    readonly COLORS_MAP: Map<string, number> = new Map<string, number>([
    ['1', 0xFFFFFF],  // face 1
    ['2', 0xFFFF00], // face 2
    ['3', 0x0000FF],   // face 3
    ['4', 0x00FF00],  // face 4
    ['5', 0xFF0000],    // face 5
    ['6', 0xff9700], // face 6
  ]);
  constructor(default_faces_colors?: Array<Array<Array<string>>>, center_x?: number, center_y?: number, center_z?: number) {
    this.x = center_x ?? 0;
    this.y = center_y ?? 0;
    this.z = center_z ?? 0;

    this.default_faces_colors = default_faces_colors ?? [
      [['1', '1', '1'], ['1', '1', '1'], ['1', '1', '1']], // UP
      [['2', '2', '2'], ['2', '2', '2'], ['2', '2', '2']], // DOWN
      [['3', '3', '3'], ['3', '3', '3'], ['3', '3', '3']], // FRONT
      [['4', '4', '4'], ['4', '4', '4'], ['4', '4', '4']], // BACK
      [['5', '5', '5'], ['5', '5', '5'], ['5', '5', '5']], // LEFT
      [['6', '6', '6'], ['6', '6', '6'], ['6', '6', '6']]]; // RIGHT

    this.second_between_animation = 0;
    this.animation_speed = 0.5;

    this.all_cubes = createRubik({center: {x: this.z, y: this.y, z: this.z}});
    this.paint_cube(this.default_faces_colors);
    this.display();

    this.current_frame = 0;

    this.frames = [
      // {
      //   move: "L"
      // },
      // {
      //   move: "R"
      // },
      // {
      //   move: "U"
      // },
      // {
      //   move: "L'"
      // },
      // {
      //   move: "R'"
      // },
      // {
      //   move: "U'"
      // },
    ]

    this.animation_is_playing = false;
  }

  set change_rotation_speed(speed: number) {
    this.animation_speed = speed;
  }

  set change_second_between_movements(second: number) {
    this.second_between_animation = second;
  }

  destroy(): void {
    for (let i = 0; i < this.all_cubes.length; i++) {
      scene.remove(this.all_cubes[i]);
      delete this.all_cubes[i];
    }
  }

  display(): void {
    for (let i = 0; i < this.all_cubes.length; i++) {
      scene.add(this.all_cubes[i]);
    }
  }

  async play_animation(): Promise<void> {
    this.animation_is_playing = true;
    for (let i = this.current_frame; i < this.frames.length; i++) {
      const element = this.frames[i];
      await this.apply_moves(element.move);
      this.current_frame = i;
    }
    this.current_tween = undefined;
  }

  private selected_cubes(cube_to_select: Array<number>): THREE.Mesh<THREE.BoxGeometry, THREE.MeshBasicMaterial[], THREE.Object3DEventMap>[] {

    const selected_cubes: THREE.Mesh<THREE.BoxGeometry, THREE.MeshBasicMaterial[], THREE.Object3DEventMap>[] = [];

    for (let i = 0; i < cube_to_select.length; i++) {
      const nb = cube_to_select[i];
      if (0 <= nb && nb < this.all_cubes.length) {
        selected_cubes.push(this.all_cubes[nb]);
      }
    }
    return selected_cubes;
  }

  paint_cube(new_faces_colors: Array<Array<Array<string>>>): void {

    this.destroy();
    this.all_cubes = createRubik({center: {x: this.z, y: this.y, z: this.z}});
    this.display();

    // All faces concatenates
    const face_up: Array<string> = new_faces_colors[0][0].concat(new_faces_colors[0][1],new_faces_colors[0][2]);
    const face_down: Array<string> = new_faces_colors[1][0].concat(new_faces_colors[1][1],new_faces_colors[1][2]);
    const face_front: Array<string> = new_faces_colors[2][0].concat(new_faces_colors[2][1],new_faces_colors[2][2]);
    const face_back: Array<string> = new_faces_colors[3][0].concat(new_faces_colors[3][1],new_faces_colors[3][2]);
    const face_left: Array<string> = new_faces_colors[4][0].concat(new_faces_colors[4][1],new_faces_colors[4][2]);
    const face_right: Array<string> = new_faces_colors[5][0].concat(new_faces_colors[5][1],new_faces_colors[5][2]);

    // All cubes depending faces
    const selected_cubes_up = this.selected_cubes([0, 1, 2, 3, 4, 5, 6, 7, 8]);
    const selected_cubes_down = this.selected_cubes([20, 19, 18, 23, 22, 21, 26, 25, 24]);
    const selected_cubes_front = this.selected_cubes([6, 7, 8, 15, 16, 17, 24, 25, 26]);
    const selected_cubes_back = this.selected_cubes([2, 1, 0, 11, 10, 9, 20, 19, 18]);
    const selected_cubes_left = this.selected_cubes([0, 3, 6, 9, 12, 15, 18, 21, 24]);
    const selected_cubes_right = this.selected_cubes([8, 5, 2, 17, 14, 11, 26, 23, 20]);

    // Face_index
    // Face_index - 0 = right
    // Face_index - 1 = left
    // Face_index - 2 = up
    // Face_index - 3 = down
    // Face_index - 4 = front
    // Face_index - 5 = back
    for (let i = 0; i < face_up.length && i < selected_cubes_up.length; i++) {
      changeCubeFaceColors({cube: selected_cubes_up[i], new_colors: this.COLORS_MAP.get(face_up[i]), face_index: 2})
    }
    for (let i = 0; i < face_down.length && i < selected_cubes_down.length; i++) {
      changeCubeFaceColors({cube: selected_cubes_down[i], new_colors: this.COLORS_MAP.get(face_down[i]), face_index: 3})
    }
    for (let i = 0; i < face_front.length && i < selected_cubes_front.length; i++) {
      changeCubeFaceColors({cube: selected_cubes_front[i], new_colors: this.COLORS_MAP.get(face_front[i]), face_index: 4});
    }
    for (let i = 0; i < face_back.length && i < selected_cubes_back.length; i++) {
      changeCubeFaceColors({cube: selected_cubes_back[i], new_colors: this.COLORS_MAP.get(face_back[i]), face_index: 5})
    }
    for (let i = 0; i < face_left.length && i < selected_cubes_left.length; i++) {
      changeCubeFaceColors({cube: selected_cubes_left[i], new_colors: this.COLORS_MAP.get(face_left[i]), face_index: 1})
    }
    for (let i = 0; i < face_right.length && i < selected_cubes_right.length; i++) {
      changeCubeFaceColors({cube: selected_cubes_right[i], new_colors: this.COLORS_MAP.get(face_right[i]), face_index: 0})
    }

    // To highlight selected_cubes_...
    // let highlight_selected_test_only = selected_cubes_front;
    // for (let i = 0; i < highlight_selected_test_only.length; i++) {
    //   changeCubeFaceColors({cube: highlight_selected_test_only[i], new_colors: "red"});
    // }
  }

  private async animate_rubik(
  cube_to_move: THREE.Mesh<THREE.BoxGeometry, THREE.MeshBasicMaterial[], THREE.Object3DEventMap>[],
  new_rotation: { x: number; y: number; z: number }): Promise<void>
  {
    const group = new THREE.Group();
    for (let i = 0; i < cube_to_move.length; i++) {
      const cube = cube_to_move[i];
      group.add(cube)
    }
    scene.add(group)

    const targetRotation = {
      x: THREE.MathUtils.degToRad(group.rotation.x + new_rotation.x),
      y: THREE.MathUtils.degToRad(group.rotation.y + new_rotation.y),
      z: THREE.MathUtils.degToRad(group.rotation.z + new_rotation.z)
    };

    return new Promise((resolve) => {
      this.current_tween = new TWEEN.Tween(group.rotation)
        .to(targetRotation, 1000 * this.animation_speed)
        .easing(TWEEN.Easing.Cubic.InOut)
        .onUpdate(() => {})
        .onComplete(async () => {
          // console.log("Rotation complete");
          for (let i = 0; i < cube_to_move.length; i++) {
            const cube = cube_to_move[i];
            scene.attach(cube);
          }
          scene.remove(group);

          await new Promise<void>((resolve) => {
            setTimeout(resolve, 1000 * this.second_between_animation);
          })
          resolve();
        })
        .start();
    });
  }

  private async apply_moves(move: string): Promise<void> {
    const cube_to_move: THREE.Mesh<THREE.BoxGeometry, THREE.MeshBasicMaterial[], THREE.Object3DEventMap>[] = [];

    let x: number = 0;
    let y: number = 0;
    let z: number = 0;

    for (let i = 0; i < this.all_cubes.length; i++) {
      const cube = this.all_cubes[i];

      if (move === "U" || move === "U'") {
        y = move === "U" ? -90 : 90
        if (cube.position.y > 0.1) {
            cube_to_move.push(cube);
        }
      }
      else if (move === "D" || move === "D'") {
        y = move === "D" ? 90 : -90
        if (cube.position.y < -0.1) {
            cube_to_move.push(cube);
        }
      }
      else if (move === "F" || move === "F'") {
        z = move === "F" ? -90 : 90
        if (cube.position.z > 0.1) {
            cube_to_move.push(cube);
        }
      }
      else if (move === "B" || move === "B'") {
        z = move === "B" ? 90 : -90
        if (cube.position.z < -0.1) {
            cube_to_move.push(cube);
        }
      }
      else if (move === "L" || move === "L'") {
        x = move === "L" ? 90 : -90
        if (cube.position.x < -0.1) {
            cube_to_move.push(cube);
        }
      }
      else if (move === "R" || move === "R'") {
        x = move === "R" ? -90 : 90
        if (cube.position.x > 0.1) {
            cube_to_move.push(cube);
        }
      }
      else {
        // alert("Invalid movement detected !");
        console.log("Invalid movement detected !");
      }
    }
    await this.animate_rubik(cube_to_move, {x: x, y: y, z: z});
  }
}

function checkPointerIntersects() {
  raycaster.setFromCamera(pointer, camera);
  const intersects = raycaster.intersectObjects(scene.children, false);

  if (intersects.length > 0) {
    const intersectedObject: THREE.Mesh = intersects[0].object;
    const faceIndex = intersects[0].face?.materialIndex;

    // If the prev Intersected object is not the same
    if (INTERSECTED != intersectedObject || INTERSECTED_FACE_INDEX != faceIndex) {


    // @ts-ignore: Edit the prev Intersected object color if is existing
      if (INTERSECTED && INTERSECTED.material && INTERSECTED_FACE_INDEX != null && INTERSECTED.material[INTERSECTED_FACE_INDEX]) {
        // @ts-ignore
        INTERSECTED.material[INTERSECTED_FACE_INDEX].color.setHex(INTERSECTED.currentHex);

      }
      // Update the Intersected object
      INTERSECTED = intersectedObject;
      INTERSECTED_FACE_INDEX = faceIndex;

      //  @ts-ignore
      if (INTERSECTED.material && INTERSECTED_FACE_INDEX != null && INTERSECTED.material[INTERSECTED_FACE_INDEX]) {
        // @ts-ignore
        INTERSECTED.currentHex = INTERSECTED.material[INTERSECTED_FACE_INDEX].color.getHex();


        // @ts-ignore
        INTERSECTED.material[INTERSECTED_FACE_INDEX].color.offsetHSL(0, 0, 0.25);
        // INTERSECTED.material[INTERSECTED_FACE_INDEX].color.setHex(0xd4d4d4);
      }
    }

  } else {
    // @ts-ignore
    if (INTERSECTED && INTERSECTED.material && INTERSECTED.material[INTERSECTED_FACE_INDEX]) {
      // @ts-ignore
      INTERSECTED.material[INTERSECTED_FACE_INDEX].color.setHex(INTERSECTED.currentHex);
      // @ts-ignore
      INTERSECTED.material[INTERSECTED_FACE_INDEX].color.offsetHSL(0, 0, 0);
    }

    INTERSECTED = null;
    INTERSECTED_FACE_INDEX = null;
  }
}

const animate = () => {
  controls.update();
  checkPointerIntersects();
  if (rubik3D.animation_is_playing && rubik3D.current_tween) {
    rubik3D.current_tween.update();
  }
  renderer.render(scene, camera);
  requestAnimationFrame(animate);
};

const initThree = () => {
  if (threeContainer.value == null) {
    return ;
  }
  const canva: HTMLElement = threeContainer.value;

  // INIT THREE JS
  scene = new THREE.Scene();
  camera = new THREE.PerspectiveCamera(75, canva.offsetWidth / canva.offsetHeight, 0.1, 1000);
  pointer = new THREE.Vector2();
  pointer.x = -1;
  pointer.y = 1;
  raycaster = new THREE.Raycaster();

  camera.position.x = 3;
  camera.position.y = 3;
  camera.position.z = 3;

  renderer = new THREE.WebGLRenderer({antialias: true, alpha: true});
  controls = new OrbitControls( camera, renderer.domElement );

  // Config render
  renderer.setSize(canva.offsetWidth, canva.offsetHeight);
  renderer.setClearColor(0x0F0F0F, 1);
  canva.appendChild(renderer.domElement);



  // canva = threeContainer.value;

  if (!canva) {
    return ;
  }
  rubik3D = new Rubik3D();
  rubik3D.play_animation();

  // canva.appendChild(renderer.domElement);



  requestAnimationFrame(animate);

  window.addEventListener( 'resize', onWindowResize );
  document.addEventListener( 'mousemove', onPointerMove );


}

function onWindowResize() {
  if (!canva) {
    return ;
  }
  camera.aspect = canva.offsetWidth / canva.offsetHeight;
  camera.updateProjectionMatrix();
  // console.log(canva);
  renderer.setSize( canva.offsetWidth, canva.offsetHeight );
}

function onPointerMove( event: MouseEvent ) {
  if (!canva) {
    return ;
  }
    // Correction pour tenir compte des décalages du canvas
  const rect = canva.getBoundingClientRect();

  pointer.x = ((event.clientX - rect.left) / rect.width) * 2 - 1;
  pointer.y = -((event.clientY - rect.top) / rect.height) * 2 + 1;
  // pointer.x = ( event.clientX / canva.offsetWidth ) * 2 - 1;
  // pointer.y = - ( event.clientY / canva.offsetHeight ) * 2 + 1;
}


onMounted(() => {
  canva = document.getElementById('rubik_canvas');
  if (canva) {
    initThree();
  }
});

onUnmounted(() => {
  window.removeEventListener( 'resize', onWindowResize );
  document.removeEventListener( 'mousemove', onPointerMove );
})
</script>

