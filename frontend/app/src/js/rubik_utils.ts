import * as THREE from 'three';

const createCube = ({
	colors = 0x000000, //0x989898,
	size = 1,
	id = "cube",
	position = { x: 0, y: 0, z: 0 }
}: {
	colors?: number;
	size?: number;
	id?: string;
	position?: { x: number; y: number; z: number };
}) => {
	const geometry = new THREE.BoxGeometry(size, size, size);

	const textureLoader = new THREE.TextureLoader();
	const texture = textureLoader.load(new URL('../assets/rubik_textures/white.png', import.meta.url).href);

	// const cube = new THREE.Mesh(geometry, [
	//   new THREE.MeshBasicMaterial({ color: 0x0 }),
	//   new THREE.MeshBasicMaterial({ color: 0x0 }),
	//   new THREE.MeshBasicMaterial({ color: 0x0 }),
	//   new THREE.MeshBasicMaterial({ color: 0x0 }),
	//   new THREE.MeshBasicMaterial({ color: 0x0 }),
	//   new THREE.MeshBasicMaterial({ color: 0x0 })
	// ]);
	const cube = new THREE.Mesh(geometry, [
	new THREE.MeshBasicMaterial({ map: texture }),
	new THREE.MeshBasicMaterial({ map: texture }),
	new THREE.MeshBasicMaterial({ map: texture }),
	new THREE.MeshBasicMaterial({ map: texture }),
	new THREE.MeshBasicMaterial({ map: texture }),
	new THREE.MeshBasicMaterial({ map: texture })
	]);

	changeCubeFaceColors({cube: cube, new_colors: "colors"});
	cube.position.set(position.x, position.y, position.z);

	cube.name = id;

	return cube;
}

function radiansToDegrees(radians: number) {
    return Math.round(radians * (180 / Math.PI));
}

function normalizeAngle(degrees: number) {
    return (degrees % 360 + 360) % 360;
}

const getCubeFaceIndex = ({
	cube,
	face = undefined
}: {
	cube: THREE.Mesh<THREE.BoxGeometry, THREE.MeshBasicMaterial[], THREE.Object3DEventMap>
	face?: string
}) => {
	// Face_index
	// Face_index - 0 = right
	// Face_index - 1 = left
	// Face_index - 2 = up
	// Face_index - 3 = down
	// Face_index - 4 = front
	// Face_index - 5 = back
	cube.updateMatrixWorld(true);
	const raycaster = new THREE.Raycaster();

	if (face == undefined) {
		return -1
	}
	if (face == "up") {
		const cubePosition = new THREE.Vector3(
			cube.position.x,
			cube.position.y + 1,
			cube.position.z,
		)
		raycaster.set(cubePosition, new THREE.Vector3(0, -1, 0));
		const intersects = raycaster.intersectObject(cube);
		if (intersects.length > 0) {
			return intersects[0].face?.materialIndex;
		}
		// console.log(x_rotation);
		// if (x_rotation === 0) { return UP }
		// if (x_rotation === 90) { return BACK }
		// if (x_rotation === 180) { return DOWN }
		// if (x_rotation === 270) { return FRONT }
	}
	else if (face == "down") {
		const cubePosition = new THREE.Vector3(
			cube.position.x,
			cube.position.y - 1,
			cube.position.z,
		)
		raycaster.set(cubePosition, new THREE.Vector3(0, 1, 0));
		const intersects = raycaster.intersectObject(cube);
		if (intersects.length > 0) {
			return intersects[0].face?.materialIndex;
		}
		// if (x_rotation === 0) { return DOWN }
		// if (x_rotation === 90) { return FRONT }
		// if (x_rotation === 180) { return UP }
		// if (x_rotation === 270) { return BACK }
	}
	else if (face == "front") {
		const cubePosition = new THREE.Vector3(
			cube.position.x,
			cube.position.y,
			cube.position.z + 1,
		)
		raycaster.set(cubePosition, new THREE.Vector3(0, 0, -1));
		const intersects = raycaster.intersectObject(cube);
		if (intersects.length > 0) {
			return intersects[0].face?.materialIndex;
		}
		// if (x_rotation === 0) { return FRONT }
		// if (x_rotation === 90) { return UP }
		// if (x_rotation === 180) { return BACK }
		// if (x_rotation === 270) { return DOWN }
	}
	else if (face == "back") {
		const cubePosition = new THREE.Vector3(
			cube.position.x,
			cube.position.y,
			cube.position.z - 1,
		)
		raycaster.set(cubePosition, new THREE.Vector3(0, 0, 1));
		const intersects = raycaster.intersectObject(cube);
		if (intersects.length > 0) {
			return intersects[0].face?.materialIndex;
		}
		// if (x_rotation === 0) { return BACK }
		// if (x_rotation === 90) { return DOWN }
		// if (x_rotation === 180) { return FRONT }
		// if (x_rotation === 270) { return UP }
	}
	else if (face == "left") {
		const cubePosition = new THREE.Vector3(
			cube.position.x - 1,
			cube.position.y,
			cube.position.z,
		)
		raycaster.set(cubePosition, new THREE.Vector3(1, 0, 0));
		const intersects = raycaster.intersectObject(cube);
		if (intersects.length > 0) {
			return intersects[0].face?.materialIndex;
		}
		// if (z_rotation === 0) { return LEFT }
		// if (z_rotation === 90) { return UP }
		// if (z_rotation === 180) { return RIGHT }
		// if (z_rotation === 270) { return DOWN }
	}
	else if (face == "right") {
		const cubePosition = new THREE.Vector3(
			cube.position.x + 1,
			cube.position.y,
			cube.position.z,
		)
		raycaster.set(cubePosition, new THREE.Vector3(-1, 0, 0));
		const intersects = raycaster.intersectObject(cube);
		if (intersects.length > 0) {
			return intersects[0].face?.materialIndex;
		}
		// if (z_rotation === 0) { return RIGHT }
		// if (z_rotation === 90) { return DOWN }
		// if (z_rotation === 180) { return LEFT }
		// if (z_rotation === 270) { return UP }
	}
	return (-1);
}

const changeCubeFaceColors = ({
	cube,
	new_colors = 0x989898,
	face = undefined
}: {
	cube: THREE.Mesh<THREE.BoxGeometry, THREE.MeshBasicMaterial[], THREE.Object3DEventMap>
	new_colors?: number
	face?: string | undefined
}) => {

	const textureLoader = new THREE.TextureLoader();
	const texture = textureLoader.load(new URL('../assets/rubik_textures/' + new_colors + '.png', import.meta.url).href);

	if (face != undefined) {
		// cube.material[face_index] = new THREE.MeshBasicMaterial({ map: texture });
		const face_index: number = getCubeFaceIndex({cube: cube, face: face});
		if (face_index == -1) {
			return ;
		}
		cube.material[face_index].color.setHex(new_colors);
	} else {
		for (let i = 0; i < cube.material.length; i++) {
			// cube.material[i] = new THREE.MeshBasicMaterial({ map: texture });
			cube.material[i].color.setHex(new_colors);
		}
	}
}

const createRubik = ({
	center = { x: 0, y: 0, z: 0 }
}: {
	center?: { x: number; y: number; z: number }; // Optionnel
} = {}) => {

	const all_cubes: Array<THREE.Mesh<THREE.BoxGeometry, THREE.MeshBasicMaterial[], THREE.Object3DEventMap>> = [];
	let cube_id = 0;
	for (let y = center.y + 1; y >= center.y - 1; y--) {
	for (let z = center.z - 1; z <= center.z + 1; z++) {
		for (let x = center.x - 1; x <= center.x + 1; x++) {
		all_cubes.push(
		createCube({
		size: 1,
		id: cube_id.toString(),
		position: {x: x, y: y, z: z}
		}));
		cube_id++;
		}
	}
	}
	return all_cubes
}


export { createCube, changeCubeFaceColors, createRubik, getCubeFaceIndex }
