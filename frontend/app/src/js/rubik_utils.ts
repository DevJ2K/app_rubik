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

	// texture.minFilter = THREE.LinearFilter;
	// texture.minFilter = THREE.NearestMipMapLinearFilter;
	// texture.magFilter = THREE.LinearFilter;

	const cube = new THREE.Mesh(geometry, [
	new THREE.MeshBasicMaterial({ map: texture }),
	new THREE.MeshBasicMaterial({ map: texture }),
	new THREE.MeshBasicMaterial({ map: texture }),
	new THREE.MeshBasicMaterial({ map: texture }),
	new THREE.MeshBasicMaterial({ map: texture }),
	new THREE.MeshBasicMaterial({ map: texture })
	]);

	changeCubeFaceColors({cube: cube, new_colors: colors});
	cube.position.set(position.x, position.y, position.z);

	cube.name = id;

	return cube;
}

// function radiansToDegrees(radians: number) {
//     return Math.round(radians * (180 / Math.PI));
// }

// function normalizeAngle(degrees: number) {
//     return (degrees % 360 + 360) % 360;
// }

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

	if (face != undefined) {
		const face_index: number | undefined = getCubeFaceIndex({cube: cube, face: face});
		if (face_index == undefined || face_index == -1) {
			return ;
		}
		cube.material[face_index].color.setHex(new_colors);
	} else {
		for (let i = 0; i < cube.material.length; i++) {
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
