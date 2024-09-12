import * as THREE from 'three';

const createCube = ({
	colors = 0x989898,
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

	changeCubeFaceColors({cube: cube, new_colors: colors});
	cube.position.set(position.x, position.y, position.z);

	cube.name = id;

	return cube;
}

const changeCubeFaceColors = ({
	cube,
	new_colors = 0x989898,
	face_index = undefined
}: {
	cube: THREE.Mesh<THREE.BoxGeometry, THREE.MeshBasicMaterial[], THREE.Object3DEventMap>
	new_colors?: number
	face_index?: number | undefined
}) => {

	const textureLoader = new THREE.TextureLoader();
	const texture = textureLoader.load(new URL('../assets/rubik_textures/' + new_colors + '.png', import.meta.url).href);

	if (face_index != undefined) {
	// cube.material[face_index] = new THREE.MeshBasicMaterial({ map: texture });
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


export { createCube, changeCubeFaceColors, createRubik }
