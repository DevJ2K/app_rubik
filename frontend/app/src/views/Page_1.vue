<template>
  <main>
    <h1 class=" text-center">Rubik</h1>
    <div ref="threeContainer"></div>
  </main>
</template>

<script setup lang="ts">
import * as THREE from 'three';
import * as TWEEN from '@tweenjs/tween.js'
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';

import { onMounted, ref } from 'vue';

// Déclarer une référence pour le conteneur
const threeContainer = ref(null);


// INIT THREE JS
const scene = new THREE.Scene();

const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);

camera.position.x = 8;
camera.position.y = 5;
camera.position.z = 9;

// 45deg top
// camera.position.x = 7;
// camera.position.y = 7;
// camera.position.z = 7;

const renderer = new THREE.WebGLRenderer();
const controls = new OrbitControls( camera, renderer.domElement );

// Config render
renderer.setSize(window.innerWidth, window.innerHeight);
renderer.setClearColor(0x0F0F0F);

const createCube = ({
  colors = "black",
  size = 1,
  id = "cube",
  position = { x: 0, y: 0, z: 0 }
}: {
  colors?: string;
  size?: number;
  id?: string;
  position?: { x: number; y: number; z: number };
}) => {
  const geometry = new THREE.BoxGeometry(size, size, size);

  const textureLoader = new THREE.TextureLoader();
  const texture = textureLoader.load(new URL('../assets/rubik_textures/' + colors + '.png', import.meta.url).href);

  // const textureMaterial = new THREE.MeshBasicMaterial({ map: texture });

  // const defaultMaterial = new THREE.MeshBasicMaterial({ color: 0xFF });

  const cube = new THREE.Mesh(geometry, [
    new THREE.MeshBasicMaterial({ color: 0xFF }),
    new THREE.MeshBasicMaterial({ color: 0xFF }),
    new THREE.MeshBasicMaterial({ color: 0xFF }),
    new THREE.MeshBasicMaterial({ color: 0xFF }),
    new THREE.MeshBasicMaterial({ color: 0xFF }),
    new THREE.MeshBasicMaterial({ color: 0xFF })
  ]);

  changeCubeFaceColors({cube: cube, new_colors: colors});
  cube.position.set(position.x, position.y, position.z);

  cube.name = id;

  return cube;
}

const changeCubeFaceColors = ({
  cube,
  new_colors = "black",
  face_index = undefined
}: {
  cube: THREE.Mesh<THREE.BoxGeometry, THREE.MeshBasicMaterial[], THREE.Object3DEventMap>
  new_colors?: string
  face_index?: number | undefined
}) => {

  const textureLoader = new THREE.TextureLoader();
  const texture = textureLoader.load(new URL('../assets/rubik_textures/' + new_colors + '.png', import.meta.url).href);

  if (face_index != undefined) {
    cube.material[face_index] = new THREE.MeshBasicMaterial({ map: texture });
  } else {
    for (let i = 0; i < cube.material.length; i++) {
      cube.material[i] = new THREE.MeshBasicMaterial({ map: texture });

    }
  }
}

const createRubik = ({
  center = { x: 0, y: 0, z: 0 }
}: {
  center?: { x: number; y: number; z: number }; // Optionnel
} = {}) => {

  let all_cubes: Array<THREE.Mesh<THREE.BoxGeometry, THREE.MeshBasicMaterial[], THREE.Object3DEventMap>> = [];
  // let cube_id = 0;
  for (let y = center.y + 1; y >= center.y - 1; y--) {
    for (let z = center.z - 1; z <= center.z + 1; z++) {
      for (let x = center.x - 1; x <= center.x + 1; x++) {
        all_cubes.push(
        createCube({
        size: 1,
        // id: cube_id.toString(),
        position: {x: x, y: y, z: z}
      }));
      // cube_id++;
      }
    }
  }
  return all_cubes
}



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

    readonly COLORS_MAP: Map<string, string> = new Map<string, string>([
    ['1', 'white'],  // face 1
    ['2', 'yellow'], // face 2
    ['3', 'blue'],   // face 3
    ['4', 'green'],  // face 4
    ['5', 'red'],    // face 5
    ['6', 'orange'], // face 6
  ]);
  constructor(default_faces_colors?: Array<Array<Array<string>>>, center_x?: number, center_y?: number, center_z?: number) {
    this.x = center_x ?? 0;
    this.y = center_y ?? 0;
    this.z = center_z ?? 0;

    console.log(default_faces_colors)

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
      {
        move: "U'"
      },
    ]
    /*
    this.frames = [
      // {
      //   move: "U"
      // },
      // {
      //   move: "R"
      // },
      // {
      //   move: "L"
      // },
      // {
      //   move: "U'"
      // },
      // {
      //   move: "R'"
      // },
      // {
      //   move: "L'"
      // },
      // {
      //   move: "F'"
      // },
      // {
      //   move: "B'"
      // },


      // {
      //   move: "B"
      // },
      // {
      //   move: "F"
      // },
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
    */
    this.animation_is_playing = false;
  }




  set change_rotation_speed(speed: number) {
    this.animation_speed = speed;
  }

  set change_second_between_movements(second: number) {
    this.second_between_animation = second;
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
      console.log(element);
      await this.apply_moves(element.move);
      this.current_frame = i;
    }
    this.current_tween = undefined;


    await new Promise<void>((resolve, reject) => {
      setTimeout(resolve, 1000);
    })
    this.paint_cube([[['1', '1', '1'], ['1', '1', '1'], ['1', '1', '1']], [['2', '2', '2'], ['2', '2', '2'], ['2', '2', '2']], [['3', '3', '3'], ['3', '3', '3'], ['3', '3', '3']], [['4', '4', '4'], ['4', '4', '4'], ['4', '4', '4']], [['5', '5', '5'], ['5', '5', '5'], ['5', '5', '5']], [['6', '6', '6'], ['6', '6', '6'], ['6', '6', '6']]])
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

    // All faces concatenates
    const face_up: Array<string> = new_faces_colors[0][0].concat(new_faces_colors[0][1],new_faces_colors[0][2]);
    const face_down: Array<string> = new_faces_colors[1][0].concat(new_faces_colors[1][1],new_faces_colors[1][2]);
    const face_front: Array<string> = new_faces_colors[2][0].concat(new_faces_colors[2][1],new_faces_colors[2][2]);
    const face_back: Array<string> = new_faces_colors[3][0].concat(new_faces_colors[3][1],new_faces_colors[3][2]);
    const face_left: Array<string> = new_faces_colors[4][0].concat(new_faces_colors[4][1],new_faces_colors[4][2]);
    const face_right: Array<string> = new_faces_colors[5][0].concat(new_faces_colors[5][1],new_faces_colors[5][2]);

    // All cubes depending faces

    const selected_cubes_up = this.all_cubes.filter((cube) => cube.position.y > 0.1);
    const selected_cubes_down = this.all_cubes.filter((cube) => cube.position.y < -0.1);
    const selected_cubes_front = this.all_cubes.filter((cube) => cube.position.z > 0.1);
    const selected_cubes_back = this.all_cubes.filter((cube) => cube.position.z < -0.1);
    const selected_cubes_left = this.all_cubes.filter((cube) => cube.position.x < -0.1);
    const selected_cubes_right = this.all_cubes.filter((cube) => cube.position.x > 0.1);

    // console.log(selected_cubes_front)

    console.log(this.all_cubes);

    // const selected_cubes_up = this.selected_cubes([0, 1, 2, 3, 4, 5, 6, 7, 8]);
    // const selected_cubes_down = this.selected_cubes([20, 19, 18, 23, 22, 21, 26, 25, 24]);
    // const selected_cubes_front = this.selected_cubes([6, 7, 8, 15, 16, 17, 24, 25, 26]);
    // const selected_cubes_back = this.selected_cubes([2, 1, 0, 11, 10, 9, 20, 19, 18]);
    // const selected_cubes_left = this.selected_cubes([0, 3, 6, 9, 12, 15, 18, 21, 24]);
    // const selected_cubes_right = this.selected_cubes([8, 5, 2, 17, 14, 11, 26, 23, 20]);

    console.log(selected_cubes_front);
    // Face_index
    // Face_index - 0 = right
    // Face_index - 1 = left
    // Face_index - 2 = up
    // Face_index - 3 = down
    // Face_index - 4 = front
    // Face_index - 5 = back
    // for (let i = 0; i < face_up.length && i < selected_cubes_up.length; i++) {
    //   changeCubeFaceColors({cube: selected_cubes_up[i], new_colors: this.COLORS_MAP.get(face_up[i]), face_index: 2})
    // }
    // for (let i = 0; i < face_down.length && i < selected_cubes_down.length; i++) {
    //   changeCubeFaceColors({cube: selected_cubes_down[i], new_colors: this.COLORS_MAP.get(face_down[i]), face_index: 3})
    // }
    for (let i = 0; i < face_front.length && i < selected_cubes_front.length; i++) {
      console.log(face_front[i]);
      changeCubeFaceColors({cube: selected_cubes_front[i], new_colors: this.COLORS_MAP.get(face_front[i]), face_index: 4})
      changeCubeFaceColors({cube: selected_cubes_front[2], new_colors: "yellow", face_index: 4})
    }
    // for (let i = 0; i < face_back.length && i < selected_cubes_back.length; i++) {
    //   changeCubeFaceColors({cube: selected_cubes_back[i], new_colors: this.COLORS_MAP.get(face_back[i]), face_index: 5})
    // }
    // for (let i = 0; i < face_left.length && i < selected_cubes_left.length; i++) {
    //   changeCubeFaceColors({cube: selected_cubes_left[i], new_colors: this.COLORS_MAP.get(face_left[i]), face_index: 1})
    // }
    // for (let i = 0; i < face_right.length && i < selected_cubes_right.length; i++) {
    //   changeCubeFaceColors({cube: selected_cubes_right[i], new_colors: this.COLORS_MAP.get(face_right[i]), face_index: 0})
    // }

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
          console.log("Rotation complete");
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

const initThree = () => {
  if (threeContainer.value == null) {
    return ;
  }
  threeContainer.value.appendChild(renderer.domElement);
  // let rubik3D = new Rubik3D()
  let rubik3D = new Rubik3D([[['1', '5', '2'], ['1', '1', '1'], ['2', '6', '1']], [['4', '6', '6'], ['2', '2', '2'], ['5', '5', '3']], [['3', '1', '5'], ['5', '3', '3'], ['6', '3', '3']], [['4', '1', '6'], ['6', '4', '4'], ['5', '4', '4']], [['4', '3', '6'], ['2', '5', '4'], ['2', '5', '1']], [['3', '4', '5'], ['2', '6', '3'], ['2', '6', '1']]])
  // let rubik3D = new Rubik3D([[['3', '5', '5'], ['1', '1', '1'], ['2', '6', '1']], [['4', '6', '6'], ['2', '2', '2'], ['1', '5', '2']], [['3', '1', '4'], ['5', '3', '3'], ['6', '3', '3']], [['5', '4', '4'], ['6', '4', '4'], ['6', '1', '5']], [['1', '3', '6'], ['4', '5', '2'], ['1', '5', '3']], [['2', '4', '5'], ['2', '6', '3'], ['2', '6', '4']]]);
  rubik3D.play_animation();

  const animate = () => {
    controls.update();
    if (rubik3D.animation_is_playing && rubik3D.current_tween) {
      rubik3D.current_tween.update();
    }
    renderer.render(scene, camera);
    requestAnimationFrame(animate);
  };
  requestAnimationFrame(animate);
}

onMounted(() => {
  initThree();
});



/*
INITIAL POS____
[[['1', '1', '1'], ['1', '1', '1'], ['1', '1', '1']], [['2', '2', '2'], ['2', '2', '2'], ['2', '2', '2']], [['3', '3', '3'], ['3', '3', '3'], ['3', '3', '3']], [['4', '4', '4'], ['4', '4', '4'], ['4', '4', '4']], [['5', '5', '5'], ['5', '5', '5'], ['5', '5', '5']], [['6', '6', '6'], ['6', '6', '6'], ['6', '6', '6']]]
[['4', '4', '4'], ['4', '4', '4'], ['4', '4', '4']]
MOVE : B
[[['5', '5', '5'], ['1', '1', '1'], ['1', '1', '1']], [['6', '6', '6'], ['2', '2', '2'], ['2', '2', '2']], [['3', '3', '3'], ['3', '3', '3'], ['3', '3', '3']], [['4', '4', '4'], ['4', '4', '4'], ['4', '4', '4']], [['5', '5', '2'], ['5', '5', '2'], ['5', '5', '2']], [['6', '6', '1'], ['6', '6', '1'], ['6', '6', '1']]]
[['3', '3', '3'], ['3', '3', '3'], ['3', '3', '3']]
MOVE : F
[[['5', '5', '5'], ['1', '1', '1'], ['5', '5', '5']], [['6', '6', '6'], ['2', '2', '2'], ['6', '6', '6']], [['3', '3', '3'], ['3', '3', '3'], ['3', '3', '3']], [['4', '4', '4'], ['4', '4', '4'], ['4', '4', '4']], [['2', '5', '2'], ['2', '5', '2'], ['2', '5', '2']], [['1', '6', '1'], ['1', '6', '1'], ['1', '6', '1']]]
[['2', '2', '2'], ['5', '5', '5'], ['2', '2', '2']]
MOVE : L
[[['4', '5', '5'], ['4', '1', '1'], ['4', '5', '5']], [['3', '6', '6'], ['3', '2', '2'], ['3', '6', '6']], [['5', '3', '3'], ['1', '3', '3'], ['5', '3', '3']], [['6', '4', '4'], ['2', '4', '4'], ['6', '4', '4']], [['2', '2', '2'], ['5', '5', '5'], ['2', '2', '2']], [['1', '6', '1'], ['1', '6', '1'], ['1', '6', '1']]]
[['1', '1', '1'], ['6', '6', '6'], ['1', '1', '1']]
MOVE : R
[[['4', '5', '3'], ['4', '1', '3'], ['4', '5', '3']], [['3', '6', '4'], ['3', '2', '4'], ['3', '6', '4']], [['5', '3', '6'], ['1', '3', '2'], ['5', '3', '6']], [['6', '4', '5'], ['2', '4', '1'], ['6', '4', '5']], [['2', '2', '2'], ['5', '5', '5'], ['2', '2', '2']], [['1', '1', '1'], ['6', '6', '6'], ['1', '1', '1']]]
[['4', '4', '4'], ['5', '1', '5'], ['3', '3', '3']]
MOVE : U
[[['4', '4', '4'], ['5', '1', '5'], ['3', '3', '3']], [['3', '6', '4'], ['3', '2', '4'], ['3', '6', '4']], [['1', '1', '1'], ['1', '3', '2'], ['5', '3', '6']], [['2', '2', '2'], ['2', '4', '1'], ['6', '4', '5']], [['5', '3', '6'], ['5', '5', '5'], ['2', '2', '2']], [['6', '4', '5'], ['6', '6', '6'], ['1', '1', '1']]]
[['6', '5', '2'], ['3', '5', '2'], ['5', '5', '2']]
MOVE : L'
[[['1', '4', '4'], ['1', '1', '5'], ['5', '3', '3']], [['2', '6', '4'], ['2', '2', '4'], ['6', '6', '4']], [['3', '1', '1'], ['3', '3', '2'], ['3', '3', '6']], [['4', '2', '2'], ['5', '4', '1'], ['3', '4', '5']], [['6', '5', '2'], ['3', '5', '2'], ['5', '5', '2']], [['6', '4', '5'], ['6', '6', '6'], ['1', '1', '1']]]
[['5', '6', '1'], ['4', '6', '1'], ['6', '6', '1']]
MOVE : R'
[[['1', '4', '2'], ['1', '1', '1'], ['5', '3', '5']], [['2', '6', '1'], ['2', '2', '2'], ['6', '6', '6']], [['3', '1', '4'], ['3', '3', '5'], ['3', '3', '3']], [['4', '2', '4'], ['5', '4', '4'], ['3', '4', '4']], [['6', '5', '2'], ['3', '5', '2'], ['5', '5', '2']], [['5', '6', '1'], ['4', '6', '1'], ['6', '6', '1']]]
[['2', '1', '5'], ['4', '1', '3'], ['1', '1', '5']]
MOVE : U'
[[['2', '1', '5'], ['4', '1', '3'], ['1', '1', '5']], [['2', '6', '1'], ['2', '2', '2'], ['6', '6', '6']], [['6', '5', '2'], ['3', '3', '5'], ['3', '3', '3']], [['5', '6', '1'], ['5', '4', '4'], ['3', '4', '4']], [['4', '2', '4'], ['3', '5', '2'], ['5', '5', '2']], [['3', '1', '4'], ['4', '6', '1'], ['6', '6', '1']]]

*/
</script>

