<template>
  <main
    class=" container my-14 flex w-full flex-col items-center gap-8 text-high-contrast-text dark:text-d-high-contrast-text md:gap-16">
    <div class="flex w-full flex-col gap-4">
      <h1 class=" text-center text-2xl font-black sm:text-3xl md:text-4xl">Ultimate Rubik's Cube Solver</h1>

      <div class="flex min-h-24 w-full items-center justify-center">
        <Transition name="fade">
          <!--:current_moves="rubik3D.current_frame > rubik3D.frames.length - 1 ? rubik3D.frames.length : rubik3D.current_frame" :nb_moves="rubik3D.frames.length - 1"  -->
          <InstructionsBlock v-show="hasSolution && !isLoading" :current_moves="rubikCurrentFrame > 4 ? rubikCurrentFrame - 1 : rubikCurrentFrame" :nb_moves="rubikResult.result ? rubikResult.result.length - 1: 0" description="Stoppppp" @display-modal="toggleSolutionModal" />
          <!-- <InstructionsBlock v-show="hasSolution && !isLoading" description="Stoppppp" @display-modal="toggleSolutionModal" /> -->

        </Transition>
        <Transition name="fade">
          <ErrorBlock v-show="!hasSolution && !isLoading && (errorDescription)" :title="errorTitle" :description="errorDescription"/>
        </Transition>
      </div>
    </div>

    <div class="flex w-full flex-col items-center justify-around gap-8 md:flex-col md:gap-0">

      <!-- Colors Palette -->
      <!-- <Transition name="fade">
        <div v-show="!isLoading && !hasSolution"
          class="flex flex-row items-center justify-center gap-4 max-md:order-2 md:w-1/6 md:flex-col">
          <button class=" color-choose bg-[#FFFFFF]" @click="paintRubikWith(0xFFFFFF)"></button>
          <button class=" color-choose bg-[#FF0000]" @click="paintRubikWith(0xFF0000)"></button>
          <button class=" color-choose bg-[#FF9700]" @click="paintRubikWith(0xff9700)"></button>
          <button class=" color-choose bg-[#FFFF00]" @click="paintRubikWith(0xFFFF00)"></button>
          <button class=" color-choose bg-[#00FF00]" @click="paintRubikWith(0x00FF00)"></button>
          <button class=" color-choose bg-[#2558ff]" @click="paintRubikWith(0x0000FF)"></button>
        </div>
      </Transition> -->

      <!-- Canvas -->
      <!-- <div class="w-1/3 "> -->
      <div class="relative flex size-full items-center justify-center">
        <!-- Canvas -->
        <div id="rubik_canvas" class=" size-full max-h-96 min-h-80 min-w-80 max-w-96 max-md:order-1"></div>

        <Transition name="fade">
          <div v-show="isLoading"
            class="absolute bottom-0 left-0 flex w-full translate-y-[125%] flex-col items-center justify-center gap-4 md:hidden">
            <div class="size-fit animate-spin">
              <SpinnerSvg custom="text-text-high-contrast dark:text-d-text-high-contrast size-16" />
            </div>
            <h1 class=" font-bold">Your cube is being solved... Just a moment!</h1>
          </div>
        </Transition>


      </div>
      <!-- </div> -->

      <!-- Movements -->
      <Transition name="fade">

        <div v-show="!isLoading && !hasSolution" class="flex justify-center max-md:order-3">
          <div class="grid w-fit grid-cols-6 gap-4 md:grid-cols-6">
            <button class="movements" @click="applyMoveOnRubik('U')">U</button>
            <button class="movements" @click="applyMoveOnRubik('U\'')">U'</button>
            <button class="movements" @click="applyMoveOnRubik('D')">D</button>
            <button class="movements" @click="applyMoveOnRubik('D\'')">D'</button>
            <button class="movements" @click="applyMoveOnRubik('F')">F</button>
            <button class="movements" @click="applyMoveOnRubik('F\'')">F'</button>
            <button class="movements" @click="applyMoveOnRubik('B')">B</button>
            <button class="movements" @click="applyMoveOnRubik('B\'')">B'</button>
            <button class="movements" @click="applyMoveOnRubik('L')">L</button>
            <button class="movements" @click="applyMoveOnRubik('L\'')">L'</button>
            <button class="movements" @click="applyMoveOnRubik('R')">R</button>
            <button class="movements" @click="applyMoveOnRubik('R\'')">R'</button>
          </div>
        </div>
      </Transition>


    </div>


    <!-- Bottom layout -->
    <div class="relative min-h-32 w-full min-w-80 max-w-96">
      <Transition name="fade">
        <div v-show="!isLoading && !hasSolution" class="absolute left-0 top-0 flex  w-full flex-col gap-8">
          <div class="hidden flex-row justify-center gap-6 sm:flex">
            <input id="sequence-input" type="text" placeholder="Enter a sequence" class="sequence-input">
            <button class="icon-button" @click="pasteSequences">
              <ClipboardIcon />
            </button>
            <button class="icon-button" @click="applySequences">
              <PlayIcon />
            </button>
          </div>
          <div class="grid w-full grid-cols-3 flex-row place-items-center sm:flex sm:justify-between">
            <button class="icon-button" @click="clearRubik" :disabled="rubikIsAnimating">
              <DeleteIcon />
            </button>
            <button class="icon-button" @click="resetRubik" :disabled="rubikIsAnimating">
              <AutorenewIcon />
            </button>
            <button class="icon-button" @click="toggleGeneratorModal">
              <ShuffleIcon />
            </button>
            <button class="text-button col-span-3 h-12 px-8 max-sm:mt-8 max-sm:px-12" @click="solveRubik" :disabled="rubikIsAnimating">SOLVE</button>
          </div>
        </div>
      </Transition>

      <Transition name="fade">
        <div v-show="hasSolution" class="absolute left-0 top-0 flex  w-full flex-col items-center justify-center gap-8">
          <div class=" flex w-full flex-row justify-between">
            <button @click="rubik3D.firstState" class="icon-button">
              <FirstPageIcon size="size-6"/>
            </button>
            <button @click="rubik3D.play_previous_animation" class="icon-button">
              <FastRewindIcon size="size-6"/>
            </button>
            <button @click="rubik3D.play_animation" class="icon-button">
              <PlayIcon size="size-4"/>
            </button>
            <button @click="rubik3D.play_next_animation" class="icon-button">
              <FastFowardIcon size="size-6"/>
            </button>
            <button @click="rubik3D.lastState" class="icon-button">
              <LastPageIcon size="size-6"/>
            </button>
          </div>
<!--
          <div class="flex w-full flex-col gap-6">
            <div class="flex w-full flex-col items-start gap-4">
              <label id="range_interval_speed_label" for="range_interval_speed" class="subtitle-modal">Interval Speed : 1s</label>
              <div class="relative w-full">
                <input id="range_interval_speed"
                  @input="updateRangeText('range_interval_speed_label', 'Interval Speed : ' + $event.target.value + 's');"
                  class="custom-range-input" type="range" min="0.5" max="5" value="1" step="0.5">
              </div>
            </div>
            <div class="flex w-full flex-col items-start gap-4">
              <label id="range_rotation_speed_label" for="range_rotation_speed" class="subtitle-modal">Rotation Speed : 1s</label>
              <div class="relative w-full">
                <input id="range_rotation_speed"
                  @input="updateRangeText('range_rotation_speed_label', 'Rotation Speed : ' + $event.target.value + 's');"
                  class="custom-range-input" type="range" min="0.5" max="5" value="1" step="0.5">
              </div>
            </div>

          </div> -->



          <div class="text-button col-span-3 h-12 w-fit px-8 max-sm:mt-8 max-sm:px-12" @click="getBack">BACK</div>
        </div>
      </Transition>

      <Transition name="fade">
        <div v-show="isLoading" class="absolute left-0 top-0 hidden w-full flex-col items-center justify-center gap-4 md:flex">
          <div class="size-fit animate-spin">
            <SpinnerSvg custom="text-text-high-contrast dark:text-d-text-high-contrast size-16" />
          </div>
          <h1 class=" font-bold">Your cube is being solved... Just a moment!</h1>
        </div>
      </Transition>
    </div>


  </main>

  <CustomModal :modal-active="generatorModalActive" @close-modal="toggleGeneratorModal">

    <h1 class="text-center text-xl font-extrabold text-high-contrast-text dark:text-d-high-contrast-text">Mixing
      Generator Settings</h1>

    <div class="flex w-full flex-col items-start gap-4 py-5">
      <label id="range_nb_moves_label" for="range_nb_moves" class="subtitle-modal">Number of Moves : 1</label>
      <div class="relative w-full">
        <input id="range_nb_moves"
          @input="updateRangeText('range_nb_moves_label', 'Number of Moves : ' + $event.target.value)"
          class="custom-range-input" type="range" min="1" max="10" value="1">
      </div>
    </div>

    <div class="flex w-full flex-col items-start gap-4 py-5">
      <label id="range_nb_mixes_label" for="range_nb_mixes" class="subtitle-modal">Number of Mixes : 1</label>
      <div class="relative w-full">
        <input id="range_nb_mixes"
          @input="updateRangeText('range_nb_mixes_label', 'Number of Mixes : ' + $event.target.value);"
          class="custom-range-input" type="range" min="1" max="10" value="1">
      </div>
    </div>

    <div class="mb-4 mt-6 flex w-full items-center justify-center">
      <button class="text-button px-4 py-2 text-high-contrast-text dark:text-d-high-contrast-text" @click="generateMix">GENERATE MIX</button>
    </div>

  </CustomModal>

  <CustomModal :modal-active="solutionModalActive" @close-modal="toggleSolutionModal">
    <h1 class="text-center text-xl font-extrabold text-high-contrast-text dark:text-d-high-contrast-text">Solutions</h1>
    <div class="mt-4 flex flex-col gap-1">
      <p class="subtitle-modal">Number of Moves</p>
      <h1 class="font-extrabold text-high-contrast-text dark:text-d-high-contrast-text">20</h1>
    </div>
    <div class="mt-4 flex flex-col gap-2">
      <p class="subtitle-modal">Move Sequence for Solving</p>
      <div class="flex flex-wrap gap-x-8 gap-y-3 font-extrabold text-high-contrast-text dark:text-d-high-contrast-text">
        <div v-for="i in result.all_moves.length" :key="i">
          <h1 v-if="i != result.current_move">{{ result.all_moves[i - 1].move }}</h1>
          <h1 v-else class="neumorphism-sm rounded-md px-2">{{ result.all_moves[i - 1].move }}</h1>
        </div>
      </div>
    </div>
  </CustomModal>

</template>

<script setup lang="ts">
import AutorenewIcon from '@/assets/Svg/AutorenewIcon.vue';
import ClipboardIcon from '@/assets/Svg/ClipboardIcon.vue';
import DeleteIcon from '@/assets/Svg/DeleteIcon.vue';
import PlayIcon from '@/assets/Svg/PlayIcon.vue';
import ShuffleIcon from '@/assets/Svg/ShuffleIcon.vue';
import CustomModal from '../components/modal/CustomModal.vue';
import { onMounted, onUnmounted, ref } from 'vue';
import InstructionsBlock from '@/components/InstructionsBlock.vue';
import SpinnerSvg from '@/assets/Svg/SpinnerSvg.vue';
import LastPageIcon from '@/assets/Svg/LastPageIcon.vue';
import FastRewindIcon from '@/assets/Svg/FastRewindIcon.vue';
import FastFowardIcon from '@/assets/Svg/FastFowardIcon.vue';
import FirstPageIcon from '@/assets/Svg/FirstPageIcon.vue';

import * as THREE from 'three';
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';
import { Rubik3D } from '@/js/Rubik3D';
import { Deque } from '@/js/Deque';
import ErrorBlock from '@/components/ErrorBlock.vue';
import { checkNotation, RubikMoves } from '@/js/RubikMoves';


// THREE JS
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

// API STATUS
const apiBaseUrl = "http://127.0.0.1:4000";
const errorDescription = ref<string | null>(null);
const errorTitle = ref<string | null>(null);
const result = ref<any>(null);
const isLoading = ref(false);
const hasSolution = ref<boolean>(false);

const rubikResult = ref<any>(Object());
const rubikCurrentFrame = ref<any>(1);


const selectedPaintColors = ref<number | null>(null);
const listMovesToApply = new Deque();
let listMovesToSend: Array<string> = [];

result.value = {
  current_move: 5,
  all_moves: [
    {
      "move": 'R',
    },
    {
      "move": 'L',
    },
    {
      "move": 'F',
    },
    {
      "move": 'B',
    },
    {
      "move": 'U\'',
    },
    {
      "move": 'R',
    },
    {
      "move": 'L',
    },
    {
      "move": 'F',
    },
    {
      "move": 'B',
    },
    {
      "move": 'U\'',
    },
    {
      "move": 'R',
    },
    {
      "move": 'L',
    },
    {
      "move": 'F',
    },
    {
      "move": 'B',
    },
    {
      "move": 'U\'',
    },
    {
      "move": 'R',
    },
    {
      "move": 'L',
    },
  ]
}

const rubikIsAnimating = ref(false);

const generatorModalActive = ref(false);
const solutionModalActive = ref(false);

const toggleGeneratorModal = () => {
  generatorModalActive.value = !generatorModalActive.value;
}

const toggleSolutionModal = () => {
  solutionModalActive.value = !solutionModalActive.value;
}

function updateRangeText(labelId: string, text: string) {
  const labelHtml = document.getElementById(labelId);
  if (!labelHtml) { return; }
  labelHtml.textContent = text;
}



const getBack = () => {
  listMovesToSend = []
  hasSolution.value = false
}

const checkIsSolvable = async () => {
// Check if cube is valid
try {
    const urlCubeChecker = apiBaseUrl + '/check_cube';

    const response = await fetch(urlCubeChecker, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ content: rubik3D.face_colors, sequences: [] }),
    });
    const data = await response.json();
    if (!response.ok) {
      if (data.detail) {
        throw new Error(data.detail);
      } else {
        throw new Error;
      }
    }
    return (data.solvable);
  } catch (e: any) {
    errorTitle.value = "Invalid Cube Format"
    errorDescription.value = e.message || 'An unknown error occurred';
    return (false);
  }
}

const solveRubik = async () => {
  // console.log(rubik3D.face_colors.toString());
  errorTitle.value = null;
  errorDescription.value = null;
  result.value = null;

  if (await checkIsSolvable() == false) {
    return ;
  }

  isLoading.value = true;
  selectedPaintColors.value = null;

  await new Promise((resolve) => setTimeout(resolve, 500));
  try {
    const urlSolve = apiBaseUrl + '/solve';
    const response = await fetch(urlSolve, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ content: rubik3D.face_colors, sequences: listMovesToSend }),
    });
    const data = await response.json();
    if (!response.ok) {
      if (data.detail) {
        throw new Error(data.detail);
      } else {
        throw new Error;
      }
    }
    rubikResult.value.result = data.result;
    rubik3D.current_frame = 1;
    rubik3D.frames = data.result;
    hasSolution.value = true;
    return (data.solvable);
  } catch (e: any) {
    errorTitle.value = 'Request Error';
    errorDescription.value = e.message || 'An unknown error occurred';
  } finally {
    isLoading.value = false;
  }
}







// ****************
// RUBIK COMMANDS *
// ****************

// Palettes
const paintRubikWith = (color: number) => {
  selectedPaintColors.value = color;
}

const disabledPaint = () => {
  selectedPaintColors.value = null;
}

// Rotation
const applyMoveOnRubik = (move: string) => {
  listMovesToSend.push(move);
  console.log(listMovesToSend);
  listMovesToApply.addFront(move);
}


const handleMoveList = async () => {
  if (rubik3D.is_animating == true) {
    return ;
  }
  const value = listMovesToApply.removeBack();
  if (value) {
    rubik3D.apply_move(value);
  }
}


// Bottom Button
const clearRubik = () => {
  listMovesToSend = [];
  rubik3D.paint_cube([
			[['-1', '-1', '-1'], ['-1', '-1', '-1'], ['-1', '-1', '-1']],
			[['-1', '-1', '-1'], ['-1', '-1', '-1'], ['-1', '-1', '-1']],
			[['-1', '-1', '-1'], ['-1', '-1', '-1'], ['-1', '-1', '-1']],
			[['-1', '-1', '-1'], ['-1', '-1', '-1'], ['-1', '-1', '-1']],
			[['-1', '-1', '-1'], ['-1', '-1', '-1'], ['-1', '-1', '-1']],
			[['-1', '-1', '-1'], ['-1', '-1', '-1'], ['-1', '-1', '-1']]
		]);
}

const resetRubik = () => {
  listMovesToSend = [];
  rubik3D.paint_cube([
			[['1', '1', '1'], ['1', '1', '1'], ['1', '1', '1']], // UP
			[['2', '2', '2'], ['2', '2', '2'], ['2', '2', '2']], // DOWN
			[['3', '3', '3'], ['3', '3', '3'], ['3', '3', '3']], // FRONT
			[['4', '4', '4'], ['4', '4', '4'], ['4', '4', '4']], // BACK
			[['5', '5', '5'], ['5', '5', '5'], ['5', '5', '5']], // LEFT
			[['6', '6', '6'], ['6', '6', '6'], ['6', '6', '6']] // RIGHT
  ])
}

const pasteSequences = async () => {
  const text = await navigator.clipboard.readText();
  const sequence_input = document.getElementById("sequence-input");
  if (sequence_input) {
    sequence_input.value = text;
  }
}


const applySequences = () => {
  errorDescription.value = null;
  errorTitle.value = null;
  const sequence_input = document.getElementById("sequence-input")
  // sequence_input.value = "R2 D' B' (RU4R'U')4"
  const sequence_value: string = sequence_input?.value;
  if (!sequence_input || !sequence_value || sequence_value.length == 0) {
    return ;
  }
  // sequence_input.value = null;
  // console.log(sequence_value);

  const sequences_list_str = sequence_value.trimStart().trimEnd().split(/\s+/);
  // console.log(sequences_list_str);
  for (const sequence_str of sequences_list_str) {
    // console.log(sequence_str)
    if (checkNotation(sequence_str) == false) {
      errorTitle.value = 'Sequence Error'
      errorDescription.value = `'${sequence_str}' is not a valid notation.`
      return ;
    }
  }
  const sequences_list_not_join = sequences_list_str.map(notation => new RubikMoves(notation).sequences);
  // console.log(sequences_list_not_join);
  let sequences_list: Array<string> = [];
  for (const expandSequences of sequences_list_not_join) {
      sequences_list = sequences_list.concat(expandSequences);
  }
  // console.log(sequences_list);
  for (const move of sequences_list) {
    // console.log(move);
    applyMoveOnRubik(move);
    // listMovesToApply.addFront(move);
  }
}


const getRandom = (arr: Array<any>, n: number) => {
    var result = new Array(n),
        len = arr.length,
        taken = new Array(len);
    if (n > len)
        throw new RangeError("getRandom: more elements taken than available");
    while (n--) {
        var x = Math.floor(Math.random() * len);
        result[n] = arr[x in taken ? taken[x] : x];
        taken[x] = --len in taken ? taken[len] : len;
    }
    return result;
}

const generateMix = () => {
  const movements_list = ['U', 'U\'', 'D', 'D\'', 'F', 'F\'', 'B', 'B\'', 'L', 'L\'', 'R', 'R\'']

  const nb_moves = document.getElementById("range_nb_moves")?.value;
  const nb_mixes = document.getElementById("range_nb_mixes")?.value;

  if (!nb_moves || !nb_mixes) {
    return ;
  }
  for (let i = 0; i < nb_mixes; i++) {
    const random_moves = getRandom(movements_list, nb_moves);
    for (let index = 0; index < random_moves.length; index++) {
      applyMoveOnRubik(random_moves[index]);
      // listMovesToApply.addFront(random_moves[index]);
    }
  }

  toggleGeneratorModal();
}


// *************************
// EVENT LISTENER FUNCTION *
// *************************

function onWindowResize() {
  if (!canva) {
    return ;
  }
  camera.aspect = canva.offsetWidth / canva.offsetHeight;
  camera.updateProjectionMatrix();
  // console.log(canva);
  renderer.setSize( canva.offsetWidth, canva.offsetHeight );
}

function onCanvaMousedown( event: MouseEvent ) {
  mousedown_coordinates.x = event.clientX;
  mousedown_coordinates.y = event.clientY;
}


function onPointerMove( event: MouseEvent ) {
  if (!canva) {
    return ;
  }
  const rect = canva.getBoundingClientRect();

  pointer.x = ((event.clientX - rect.left) / rect.width) * 2 - 1;
  pointer.y = -((event.clientY - rect.top) / rect.height) * 2 + 1;
}


function onCanvaMouseup( event: MouseEvent ) {
  if (typeof selectedPaintColors.value !== "number" || rubik3D.is_animating || listMovesToApply.getLength() != 0) {
    return ;
  }

  if (mousedown_coordinates.x - 10 > event.clientX || mousedown_coordinates.x + 10 < event.clientX) {
    return ;
  }
  if (mousedown_coordinates.y - 10 > event.clientY || mousedown_coordinates.y + 10 < event.clientY) {
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
        INTERSECTED.material[INTERSECTED_FACE_INDEX].color.setHex(selectedPaintColors.value);
        // @ts-ignore
        INTERSECTED.currentHex = INTERSECTED.material[INTERSECTED_FACE_INDEX].color.getHex();
        rubik3D.update_face_colors();
      }
  }
}

// *****************
// UTILS FOR RUBIK *
// *****************

function checkPointerIntersects() {
  if (rubik3D.is_animating || listMovesToApply.getLength() != 0) {
    canva.style.cursor = "not-allowed";
    return ;
  }
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
  rubikCurrentFrame.value = rubik3D.current_frame;
  controls.update();
  if (typeof selectedPaintColors.value === "number") {
    checkPointerIntersects();
  }
  handleMoveList();
  rubikIsAnimating.value = rubik3D.is_animating || listMovesToApply.getLength() != 0;
  if (rubik3D.is_animating && rubik3D.current_tween) {
    rubik3D.current_tween.update();
  }
  renderer.render(scene, camera);
  requestAnimationFrame(animate);
};

const initThree = () => {
  canva = document.getElementById('rubik_canvas');
  if (canva == null || canva == undefined) {
    return ;
  }

  scene = new THREE.Scene();
  camera = new THREE.PerspectiveCamera(75, canva.offsetWidth / canva.offsetHeight, 0.1, 1000);
  pointer = new THREE.Vector2();
  pointer.x = -1;
  pointer.y = 1;
  raycaster = new THREE.Raycaster();

  camera.position.x = 2.5;
  camera.position.y = 2.5;
  camera.position.z = 2.5;


  renderer = new THREE.WebGLRenderer({antialias: true, alpha: true});
  controls = new OrbitControls( camera, renderer.domElement );
  controls.enableZoom = false;

    // Config render
  renderer.setSize(canva.offsetWidth, canva.offsetHeight);
  renderer.setClearColor(0x0F0F0F, 0);
  canva.appendChild(renderer.domElement);

  rubik3D = new Rubik3D(scene);

  requestAnimationFrame(animate);
  window.addEventListener( 'resize', onWindowResize );
  document.addEventListener( 'mousemove', onPointerMove );
  canva.addEventListener('mousedown', onCanvaMousedown );
  canva.addEventListener('mouseup', onCanvaMouseup );
}

onMounted(() => {
  initThree();
});

onUnmounted(() => {
  window.removeEventListener( 'resize', onWindowResize );
  document.removeEventListener( 'mousemove', onPointerMove );
  canva?.removeEventListener('mousedown', onCanvaMousedown );
  canva?.removeEventListener('mouseup', onCanvaMouseup );
});

</script>

<style scoped>
/* Add some transition effects */
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

/* Loading spinner styles */
.animate-spin {
  animation: spin 2s linear infinite;
}

@keyframes spin {
  0% {
    transform: rotate(0deg);
  }

  100% {
    transform: rotate(360deg);
  }
}
</style>
