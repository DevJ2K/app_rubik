<template>
  <main>
    <h1>Page 1</h1>
    <div ref="threeContainer"></div>
  </main>
</template>

<script setup lang="ts">
import * as THREE from 'three';
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
renderer.setClearColor(0x404040);


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
  colors,
  size = 1, // Valeur par défaut pour size
  position = { x: 0, y: 0, z: 0 } // Valeur par défaut pour position
}: {
  colors?: Array<THREE.MeshBasicMaterial>; // Optionnel
  size?: number; // Optionnel
  position?: { x: number; y: number; z: number }; // Optionnel
} = {}) => {
  // Création de la géométrie du cube avec la taille spécifiée
  const geometry = new THREE.BoxGeometry(size, size, size);

  const textureLoader = new THREE.TextureLoader();
  const texture = textureLoader.load(new URL('../assets/rubik_textures/white.png', import.meta.url).href); // Charge la texture correctement
  console.log(texture)
  const textureMaterial = new THREE.MeshBasicMaterial({ map: texture }); // Associe la texture au matériau

  // Si colors est défini, on l'utilise, sinon on applique un matériau par défaut
  const defaultMaterial = new THREE.MeshBasicMaterial({ color: 0xFF });
  const cube = new THREE.Mesh(geometry, colors || [textureMaterial,textureMaterial,textureMaterial,textureMaterial,textureMaterial,textureMaterial]);

  // Positionnement du cube
  cube.position.set(position.x, position.y, position.z);


  // const wireframeGeometry = new THREE.WireframeGeometry(geometry);
  // const wireframeMaterial = new THREE.LineBasicMaterial({ color: 0xFFFFFF, linewidth: 10 }); // Couleur noire pour les bords
  // const wireframe = new THREE.LineSegments(wireframeGeometry, wireframeMaterial);

  // Ajout du wireframe en tant qu'enfant du cube
  // cube.add(wireframe);

  scene.add(cube);
  // return cube;
}



const initThree = () => {
  threeContainer.value.appendChild(renderer.domElement);

  createCube({
    size: 1,
    position: {x: 0, y: 0, z: 0}
  });
  createCube({
    size: 1,
    position: {x: 1, y: 0, z: 0}
  });
  createCube({
    size: 1,
    position: {x: -1, y: 0, z: 0}
  });


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
  console.log("Heree");
  initThree();
});
</script>
