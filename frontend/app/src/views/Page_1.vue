<template>
  <main>
    <h1>Page 1</h1>
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
renderer.setClearColor(0x202020);

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
  size = 1, // Valeur par défaut pour size
  position = { x: 0, y: 0, z: 0 } // Valeur par défaut pour position
}: {
  colors?: String; // Optionnel
  size?: number; // Optionnel
  position?: { x: number; y: number; z: number }; // Optionnel
} = {}) => {
  // Création de la géométrie du cube avec la taille spécifiée
  const geometry = new THREE.BoxGeometry(size, size, size);

  const textureLoader = new THREE.TextureLoader();
  const texture = textureLoader.load(new URL('../assets/rubik_textures/' + colors + '.png', import.meta.url).href); // Charge la texture correctement
  // console.log(texture)
  const textureMaterial = new THREE.MeshBasicMaterial({ map: texture }); // Associe la texture au matériau

  // Si colors est défini, on l'utilise, sinon on applique un matériau par défaut
  const defaultMaterial = new THREE.MeshBasicMaterial({ color: 0xFF });
  const cube = new THREE.Mesh(geometry, [textureMaterial,textureMaterial,textureMaterial,textureMaterial,textureMaterial,textureMaterial]);

  // Positionnement du cube
  cube.position.set(position.x, position.y, position.z);

  // scene.add(cube);
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







class Rubik3D {
  x: number;
  y: number;
  z: number;
  all_cubes: THREE.Mesh<THREE.BoxGeometry, THREE.MeshBasicMaterial[], THREE.Object3DEventMap>[];
  animation_is_playing: boolean;

  tween_group: TWEEN.Group;

  constructor(center_x?: number, center_y?: number, center_z?: number, ) {
    this.x = center_x ?? 0;
    this.y = center_y ?? 0;
    this.z = center_z ?? 0;

    this.tween_group = new TWEEN.Group();

    this.all_cubes = createRubik({center: {x: this.z, y: this.y, z: this.z}})

    this.animation_is_playing = false;
    this.display();
  }

  display(): void {
    for (let i = 0; i < this.all_cubes.length; i++) {
      scene.add(this.all_cubes[i]);

    }
  }

  private animate_rubik(cube_to_move: THREE.Mesh<THREE.BoxGeometry, THREE.MeshBasicMaterial[], THREE.Object3DEventMap>[], new_rotation: { x: number; y: number; z: number }) {
    console.log("Animating...")
    const group = new THREE.Group();
    for (let i = 0; i < cube_to_move.length; i++) {
      const cube = cube_to_move[i];
      group.add(cube)
      console.log("Here");
    }

    console.log(group.rotation)
    // group.rotation.y = THREE.MathUtils.degToRad(90);

    scene.add(group)

    const targetRotation = {
      x: THREE.MathUtils.degToRad(new_rotation.x),
      y: THREE.MathUtils.degToRad(new_rotation.y),
      z: THREE.MathUtils.degToRad(new_rotation.z)
    };

    const tween = new TWEEN.Tween(group.rotation)
      .to(targetRotation, 2000)
      .easing(TWEEN.Easing.Cubic.InOut)
      .onUpdate(() => {
        // Optionnel : Si vous voulez faire quelque chose pendant l'animation
        console.log("Here TWEEN");
      })
      .onComplete(() => {
        console.log(group.rotation)
        console.log("Rotation complete");
      })
      .start()

      // tween.update()
      this.tween_group.add(tween);
  }

  apply_moves(move: string): void {
    const cube_to_move: THREE.Mesh<THREE.BoxGeometry, THREE.MeshBasicMaterial[], THREE.Object3DEventMap>[] = [];
    console.log(("=".repeat(20)) + " " + move + " " + ("=".repeat(20)));
    if (move === "U") {
      for (let i = 0; i < this.all_cubes.length; i++) {
        const cube = this.all_cubes[i];
        if (cube.position.y > 0) {
          cube.material[2].color.setHex(0x00ffff);
          cube_to_move.push(cube);
          // console.log(cube.position);
        }

      }
      this.animate_rubik(cube_to_move, {x: 0, y: -90, z: 0});
      // console.log("HERE")
    }
  }
}



const initThree = () => {
  threeContainer.value.appendChild(renderer.domElement);
  // let all_cubes = createRubik();

  let rubik3D = new Rubik3D();
  rubik3D.apply_moves("U");
  rubik3D.apply_moves("U");
  rubik3D.apply_moves("U");
  // rubik3D.display()

  const animate = (time: number) => {
    // line.rotation.x += 0.01;
    // line.rotation.y += 0.01;
    // cube.rotation.x += 0.01;
    // cube.rotation.y += 0.01;
    controls.update();
    rubik3D.tween_group.update()
    renderer.render(scene, camera);
    requestAnimationFrame(animate);
  };

  requestAnimationFrame(animate);
  // animate();


}

const initThree_ = () => {
  if (threeContainer.value == null) {
    return
  }
  const scene = new THREE.Scene();
  const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
  const renderer = new THREE.WebGLRenderer();

  renderer.setSize(window.innerWidth, window.innerHeight);
  renderer.setClearColor(0x404040);

  // Utiliser la référence définie
  threeContainer.value.appendChild(renderer.domElement);

  // const geometry = new THREE.BoxGeometry();
  const material = new THREE.MeshBasicMaterial({ color: 0x000000 });


  const controls = new OrbitControls( camera, renderer.domElement );

  const group = new THREE.Group();

//   const material = new THREE.ShaderMaterial({
//   uniforms: {
//     thickness: {
//       value: 1.5
//     }
//   },
//   // vertexShader: vertexShader,
//   // fragmentShader: fragmentShader
// });


  camera.position.z = 5;


  const geometry = new THREE.BoxGeometry( 1.5, 1.5, 1.5 );
  const edges = new THREE.EdgesGeometry( geometry );
  const line = new THREE.LineSegments(edges, new THREE.LineBasicMaterial( {
    color: 0xffffff,
    linewidth: 15,
   } ) );


  scene.add( line );

  const cube = new THREE.Mesh(geometry, material);
  scene.add(cube);

  line.rotation.x = 45

  line.rotation.set(45, 45, 0);
  cube.rotation.set(45, 45, 0);

  const animate = () => {
    requestAnimationFrame(animate);
    // line.rotation.x += 0.01;
    // line.rotation.y += 0.01;
    // cube.rotation.x += 0.01;
    // cube.rotation.y += 0.01;
    controls.update();
    renderer.render(scene, camera);
  };

  animate();
}

onMounted(() => {
  initThree();
});
</script>
