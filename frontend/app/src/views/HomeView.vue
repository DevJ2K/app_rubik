<template>
  <main
    class=" container my-14 flex w-full flex-col items-center gap-8 text-high-contrast-text dark:text-d-high-contrast-text md:gap-16">
    <div class="flex w-full flex-col gap-4">
      <h1 class=" text-center text-2xl font-black sm:text-3xl md:text-4xl">Ultimate Rubik's Cube Solver</h1>

      <div class="flex min-h-24 w-full items-center justify-center">
        <Transition name="fade">
          <InstructionsBlock v-show="hasSolution" @display-modal="toggleSolutionModal" />
        </Transition>
      </div>
    </div>

    <div class="flex w-full flex-col items-center justify-around gap-8 md:flex-row md:gap-0">

      <!-- Colors Palette -->
      <Transition name="fade">
        <div v-show="!isLoading && !hasSolution"
          class="flex flex-row items-center justify-center gap-4 max-md:order-2 md:w-1/6 md:flex-col">
          <div class=" color-choose bg-white"></div>
          <div class=" color-choose bg-red-500"></div>
          <div class=" color-choose bg-orange-400"></div>
          <div class=" color-choose bg-yellow-300"></div>
          <div class=" color-choose bg-green-400"></div>
          <div class=" color-choose bg-blue-500"></div>
        </div>
      </Transition>

      <!-- Canvas -->
      <!-- <div class="w-1/3 "> -->
      <div class="relative flex size-full justify-center">
        <div class=" size-full max-h-96 min-h-80 min-w-80 max-w-96 bg-black/20 max-md:order-1"></div>

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

        <div v-show="!isLoading && !hasSolution" class="flex justify-center max-md:order-3 md:w-1/6">
          <div class="grid w-fit grid-cols-6 gap-4 md:grid-cols-2">
            <div class="movements">U</div>
            <div class="movements">U'</div>
            <div class="movements">D</div>
            <div class="movements">D'</div>
            <div class="movements">F</div>
            <div class="movements">F'</div>
            <div class="movements">B</div>
            <div class="movements">B'</div>
            <div class="movements">L</div>
            <div class="movements">L'</div>
            <div class="movements">R</div>
            <div class="movements">R'</div>
          </div>
        </div>
      </Transition>


    </div>


    <!-- Bottom layout -->
    <div class="relative min-h-32 w-full min-w-80 max-w-96">
      <Transition name="fade">
        <div v-show="!isLoading && !hasSolution" class="absolute left-0 top-0 flex  w-full flex-col gap-8">
          <div class="hidden flex-row justify-center gap-6 sm:flex">
            <input type="text" placeholder="Enter a sequence" class="sequence-input">
            <div class="icon-button">
              <ClipboardIcon />
            </div>
            <div class="icon-button">
              <PlayIcon />
            </div>
          </div>
          <div class="grid w-full grid-cols-3 flex-row place-items-center sm:flex sm:justify-between">
            <div class="icon-button">
              <DeleteIcon />
            </div>
            <div class="icon-button">
              <AutorenewIcon />
            </div>
            <div class="icon-button" @click="toggleGeneratorModal">
              <ShuffleIcon />
            </div>
            <div class="text-button col-span-3 h-12 px-8 max-sm:mt-8 max-sm:px-12" @click="solveRubik">SOLVE</div>
          </div>
        </div>
      </Transition>

      <Transition name="fade">
        <div v-show="hasSolution" class="absolute left-0 top-0 flex  w-full flex-col items-center justify-center gap-8">
          <div class=" flex w-full flex-row justify-between">
            <div class="icon-button">
              <FirstPageIcon size="size-6"/>
            </div>
            <div class="icon-button">
              <FastRewindIcon size="size-6"/>
            </div>
            <div class="icon-button">
              <PlayIcon size="size-4"/>
            </div>
            <div class="icon-button">
              <FastFowardIcon size="size-6"/>
            </div>
            <div class="icon-button">
              <LastPageIcon size="size-6"/>
            </div>
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
      <button class="text-button px-4 py-2 text-high-contrast-text dark:text-d-high-contrast-text">GENERATE MIX</button>
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
import { ref } from 'vue';
import InstructionsBlock from '@/components/InstructionsBlock.vue';
import SpinnerSvg from '@/assets/Svg/SpinnerSvg.vue';
import LastPageIcon from '@/assets/Svg/LastPageIcon.vue';
import FastRewindIcon from '@/assets/Svg/FastRewindIcon.vue';
import FastFowardIcon from '@/assets/Svg/FastFowardIcon.vue';
import FirstPageIcon from '@/assets/Svg/FirstPageIcon.vue';

const error = ref<string | null>(null);
const result = ref<any>(null);
const isLoading = ref(false);
const hasSolution = ref<boolean>(true);


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

const generatorModalActive = ref(false);
const solutionModalActive = ref(true);

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
  hasSolution.value = false
}

const solveRubik = async () => {
  isLoading.value = true;
  error.value = null;
  result.value = null;
  // Desactiver la peinture du rubik cube...
  await new Promise((resolve) => setTimeout(resolve, 1000));
  try {
    hasSolution.value = true;
    console.log("Make requests...")
  } catch (e: any) {
    error.value = e.message || 'An unknown error occurred';
  } finally {
    isLoading.value = false;
  }
}

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
