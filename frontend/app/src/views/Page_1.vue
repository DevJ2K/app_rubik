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
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';
import { Rubik3D } from '@/js/Rubik3D';

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

let rubik3D: Rubik3D;

let INTERSECTED: THREE.Mesh | null;
let INTERSECTED_FACE_INDEX: number | undefined | null;

let mousedown_coordinates: Object = Object.create(null);

function onCanvaMousedown( event: MouseEvent ) {
  mousedown_coordinates.x = event.clientX;
  mousedown_coordinates.y = event.clientY;
}

function onCanvaMouseup( event: MouseEvent ) {

  if (mousedown_coordinates.x - 10 > event.clientX || mousedown_coordinates.x + 10 < event.clientX) {
    // console.log("HERE1");
    return ;
  }
  if (mousedown_coordinates.y - 10 > event.clientY || mousedown_coordinates.y + 10 < event.clientY) {
    // console.log("HERE2");
    return ;
  }

  raycaster.setFromCamera(pointer, camera);
  const intersects = raycaster.intersectObjects(scene.children, false);

  if (intersects.length > 0) {
    INTERSECTED = intersects[0].object;
    INTERSECTED_FACE_INDEX = intersects[0].face?.materialIndex

    // @ts-ignore
    if (INTERSECTED.material && INTERSECTED_FACE_INDEX != null && INTERSECTED.material[INTERSECTED_FACE_INDEX]) {
        // @ts-ignore
        INTERSECTED.material[INTERSECTED_FACE_INDEX].color.setHex(0x0000FF);
        // @ts-ignore
        INTERSECTED.currentHex = INTERSECTED.material[INTERSECTED_FACE_INDEX].color.getHex();
        rubik3D.update_face_colors();
      }
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
      // @ts-ignore: Canva cannot be null
      canva.style.cursor = "pointer";

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
    // @ts-ignore: Canva cannot be null
    canva.style.cursor = "default";
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
  if (rubik3D.is_animating && rubik3D.current_tween) {
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

  if (!canva) {
    return ;
  }
  rubik3D = new Rubik3D(scene);
  rubik3D.play_animation();

  requestAnimationFrame(animate);
  window.addEventListener( 'resize', onWindowResize );
  document.addEventListener( 'mousemove', onPointerMove );
  canva.addEventListener('mousedown', onCanvaMousedown );
  canva.addEventListener('mouseup', onCanvaMouseup );

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
  const rect = canva.getBoundingClientRect();

  pointer.x = ((event.clientX - rect.left) / rect.width) * 2 - 1;
  pointer.y = -((event.clientY - rect.top) / rect.height) * 2 + 1;
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
  canva?.removeEventListener('mousedown', onCanvaMousedown );
  canva?.removeEventListener('mouseup', onCanvaMouseup );
})
</script>

