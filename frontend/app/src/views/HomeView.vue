<template>
  <main class=" container my-12 flex size-full flex-col items-center justify-center gap-24 text-high-contrast-text">
    <div class=" flex w-full flex-col items-center justify-center gap-6">
      <h1 class="text-3xl font-bold">Rubik Solver</h1>
      <p class=" text-center text-low-contrast-text">Est laboris reprehenderit officia laborum aliqua cillum sit. Dolore in irure ad est occaecat ex occaecat.</p>

    </div>

    <div>

    </div>

    <div class="flex w-full flex-col items-center justify-center gap-6">
      <h1 class="text-2xl font-bold">Test Execution</h1>
      <div class="flex w-full flex-col items-center justify-center gap-3">
        <label for="test-input">Lorem ipsum :</label>
        <input type="text" id="test-input" required class="form-input form-input-border w-5/6">
        <button @click="makeRequests"
							class="group flex flex-row items-center gap-1.5 rounded-full border-2 border-accent-color px-6 py-2 text-high-contrast-text transition-colors hover:bg-accent-color dark:text-d-high-contrast-text">
							<span class=" font-semibold transition-colors group-hover:text-white">Submit</span>
					</button>
      </div>
      <div>
        <h1 class=" text-xl font-semibold">API Result</h1>

        <p id="api_result"></p>
      </div>
    </div>
    <!-- <TheWelcome /> -->
  </main>
</template>

<script setup lang="ts">


const makeRequests = async () => {
  console.log("Yo !");
  const input: HTMLElement | null = document.getElementById("test-input");

  let text: String = '';
  if (input) {
    text = input.value;
  }
  const url = "http://127.0.0.1:4000/test";

  try {
        const response = await fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({name: text}),
        });

        const result = await response.json();
        console.log("Response from FastAPI:", result);
        const api_result = document.getElementById("api_result");
        if (api_result) {
          api_result.innerHTML = result.message;
        }
    } catch (error) {
        console.error("Error:", error);
    }
};

</script>
