<template>
  <main class=" container my-12 flex size-full flex-col items-center justify-center gap-24 text-high-contrast-text dark:text-d-high-contrast-text">
    <h1 class=" text-5xl font-black">Ultimate Rubik's Cube Solver</h1>

    <div class="flex w-full flex-row items-center justify-around">

      <!-- Colors Palette -->
      <div class="flex flex-col gap-4">
        <div class=" size-8 rounded-md bg-white"></div>
        <div class=" size-8 rounded-md bg-red-500"></div>
        <div class=" size-8 rounded-md bg-orange-400"></div>
        <div class=" size-8 rounded-md bg-yellow-300"></div>
        <div class=" size-8 rounded-md bg-green-400"></div>
        <div class=" size-8 rounded-md bg-blue-500"></div>
      </div>

      <!-- Canvas -->
      <div class=" size-96 bg-blue-100">

      </div>

      <!-- Movements -->
      <div class="flex flex-col gap-4">
        <div class=" size-8 rounded-md bg-red-500"></div>
        <div class=" size-8 rounded-md bg-red-500"></div>
        <div class=" size-8 rounded-md bg-red-500"></div>
        <div class=" size-8 rounded-md bg-red-500"></div>
        <div class=" size-8 rounded-md bg-red-500"></div>
        <div class=" size-8 rounded-md bg-red-500"></div>
      </div>
    </div>


    <div class="flex flex-row">
      <input type="text">
      <button>APPLY</button>
      <button>PLAY</button>
    </div>
  </main>
</template>

<script setup lang="ts">


// const makeRequests = async () => {
//   console.log("Yo !");
//   const input: HTMLElement | null = document.getElementById("test-input");

//   let text: String = '';
//   if (input) {
//     text = input.value;
//   }
//   const url = "http://127.0.0.1:4000/test";

//   try {
//         const response = await fetch(url, {
//             method: 'POST',
//             headers: {
//                 'Content-Type': 'application/json',
//             },
//             body: JSON.stringify({name: text}),
//         });

//         const result = await response.json();
//         console.log("Response from FastAPI:", result);
//         const api_result = document.getElementById("api_result");
//         if (api_result) {
//           api_result.innerHTML = result.message;
//         }
//     } catch (error) {
//         console.error("Error:", error);
//     }
// };

</script>
