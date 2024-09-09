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
camera.position.z = 7;
camera.position.y = 7;
camera.position.x = 7;

const renderer = new THREE.WebGLRenderer();
const controls = new OrbitControls( camera, renderer.domElement );

// Config render
renderer.setSize(window.innerWidth, window.innerHeight);
renderer.setClearColor(0x0F0F0F);

const createCube_ = ({ colors }: { colors?: Array<THREE.MeshBasicMaterial> | undefined } = {}) => {
  const geometry = new THREE.BoxGeometry(1, 1, 1, 2, 2, 2);
  const material = new THREE.MeshBasicMaterial({color: 0x00FF00});

  const mesh = new THREE.Mesh(
    geometry,
    [
      new THREE.MeshBasicMaterial({color: 0x00FF00}),
      new THREE.MeshBasicMaterial({color: 0x00FF00}),
      new THREE.MeshBasicMaterial({color: 0x00FF00}),
      new THREE.MeshBasicMaterial({color: 0x00FF00}),
      new THREE.MeshBasicMaterial({color: 0x00FF00}),
      new THREE.MeshBasicMaterial({color: 0x00FF00}),
    ]
  );


  mesh.material[1].color.setHex(0x00ffff);
  mesh.material[5].color.setHex(0x00ffff);

  // mesh.geometry.faces[ 5 ].color.setHex( 0x00ffff );


  scene.add(mesh);
}


const createCube = ({
  colors = "white",
  size = 1,
  position = { x: 0, y: 0, z: 0 }
}: {
  colors?: String;
  size?: number;
  position?: { x: number; y: number; z: number };
} = {}) => {
  const geometry = new THREE.BoxGeometry(size, size, size);

  const textureLoader = new THREE.TextureLoader();
  const texture = textureLoader.load(new URL('../assets/rubik_textures/' + colors + '.png', import.meta.url).href);

  const textureMaterial = new THREE.MeshBasicMaterial({ map: texture });

  const defaultMaterial = new THREE.MeshBasicMaterial({ color: 0xFF });
  const cube = new THREE.Mesh(geometry, [textureMaterial,textureMaterial,textureMaterial,textureMaterial,textureMaterial,textureMaterial]);

  cube.position.set(position.x, position.y, position.z);

  return cube;
}

const createRubik = ({
  center = { x: 0, y: 0, z: 0 }
}: {
  center?: { x: number; y: number; z: number }; // Optionnel
} = {}) => {

  let all_cubes: Array<THREE.Mesh<THREE.BoxGeometry, THREE.MeshBasicMaterial[], THREE.Object3DEventMap>> = [];

  for (let x = center.x - 1; x <= center.x + 1; x++) {
    for (let y = center.y - 1; y <= center.y + 1; y++) {
      for (let z = center.z - 1; z <= center.z + 1; z++) {
        all_cubes.push(
        createCube({
        size: 1,
        position: {x: x, y: y, z: z}
      }));
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
  all_cubes: THREE.Mesh<THREE.BoxGeometry, THREE.MeshBasicMaterial[], THREE.Object3DEventMap>[];

  // Animation settings
  second_between_animation: number;
  animation_speed: number;
  animation_is_playing: boolean;

  // Animation visualization
  current_frame: number;
  current_tween: TWEEN.Tween | undefined;
  frames: Array<Object>

  constructor(center_x?: number, center_y?: number, center_z?: number, ) {
    this.x = center_x ?? 0;
    this.y = center_y ?? 0;
    this.z = center_z ?? 0;

    this.second_between_animation = 0;
    this.animation_speed = 1;

    this.all_cubes = createRubik({center: {x: this.z, y: this.y, z: this.z}});
    this.display();

    this.current_frame = 0;
    this.frames = [
      {
        move: "U"
      },
      {
        move: "U'"
      },
      {
        move: "D"
      },
      {
        move: "D'"
      },
      {
        move: "F"
      },
      {
        move: "F'"
      },
      {
        move: "B"
      },
      {
        move: "B'"
      },
      {
        move: "L"
      },
      {
        move: "L'"
      },
      {
        move: "R"
      },
      {
        move: "R'"
      },
    ]

    this.animation_is_playing = false;
  }


  set change_rotation_speed(speed: number) {
    this.animation_speed = speed;
  }

  set change_second_between_movements(second: number) {
    this.second_between_animation = second;
  }

  async play_animation(): Promise<void> {
    this.animation_is_playing = true;
    for (let i = 0; i < this.frames.length; i++) {
      const element = this.frames[i];
      console.log(element);
      await this.apply_moves(element.move);

    }
    this.current_tween = undefined;
  }

  display(): void {
    for (let i = 0; i < this.all_cubes.length; i++) {
      scene.add(this.all_cubes[i]);

    }
  }

  // play_animation(): void {
  //   this.tween_group.removeAll();
  //   for (let i = 0; i + 1 < this.all_tweens.length; i++) {
  //     const element = this.all_tweens[i];
  //     element.chain(this.all_tweens[i + 1]);

  //   }
  //   for (let i = 0; i < this.all_tweens.length; i++) {
  //     this.tween_group.add(this.all_tweens[i]);
  //   }
  //   this.animation_is_playing = true;
  // }

  private async animate_rubik(cube_to_move: THREE.Mesh<THREE.BoxGeometry, THREE.MeshBasicMaterial[], THREE.Object3DEventMap>[], new_rotation: { x: number; y: number; z: number }): Promise<void> {
    console.log("Animating...")
    const group = new THREE.Group();
    for (let i = 0; i < cube_to_move.length; i++) {
      const cube = cube_to_move[i];
      group.add(cube)
    }

    scene.add(group)

    // console.log(group.rotation);
    // await new Promise<void>((resolve, reject) => {
    //   setTimeout(resolve, 1000);
    // })

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
          cube.material[2].color.setHex(0xffffff);
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
        y = move === "U" ? 90 : -90
        if (cube.position.y > 0) {
            cube.material[2].color.setHex(0x00ffff);
            cube_to_move.push(cube);
        }
      }
      else if (move === "D" || move === "D'") {
        y = move === "D" ? 90 : -90
        if (cube.position.y < 0) {
            cube.material[2].color.setHex(0x00ffff);
            cube_to_move.push(cube);
        }
      }
      else if (move === "F" || move === "F'") {
        z = move === "F" ? -90 : 90
        if (cube.position.z > 0) {
            cube.material[2].color.setHex(0x00ffff);
            cube_to_move.push(cube);
        }
      }
      else if (move === "B" || move === "B'") {
        z = move === "B" ? 90 : -90
        if (cube.position.z < 0) {
            cube.material[2].color.setHex(0x00ffff);
            cube_to_move.push(cube);
        }
      }
      else if (move === "L" || move === "L'") {
        x = move === "L" ? 90 : -90
        if (cube.position.x < 0) {
            cube.material[2].color.setHex(0x00ffff);
            cube_to_move.push(cube);
        }
      }
      else if (move === "R" || move === "R'") {
        x = move === "R" ? -90 : 90
        if (cube.position.x > 0) {
            cube.material[2].color.setHex(0x00ffff);
            cube_to_move.push(cube);
        }
      }
      else {
        alert("Invalid movement detected !")
        console.log("Invalid movement detected !");
      }
    }


    await this.animate_rubik(cube_to_move, {x: x, y: y, z: z});
  }
}



const initThree = () => {
  threeContainer.value.appendChild(renderer.domElement);
  // let all_cubes = createRubik();

  let rubik3D = new Rubik3D();
  rubik3D.play_animation();
  // // rubik3D.display()

  const animate = (time: number) => {
    // line.rotation.x += 0.01;
    // line.rotation.y += 0.01;
    // cube.rotation.x += 0.01;
    // cube.rotation.y += 0.01;
    controls.update();
    if (rubik3D.animation_is_playing && rubik3D.current_tween) {
      rubik3D.current_tween.update();
    }
    renderer.render(scene, camera);
    requestAnimationFrame(animate);
  };

  requestAnimationFrame(animate);
  // animate();


}

onMounted(() => {
  initThree();
});
</script>
