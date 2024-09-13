import { createRubik, changeCubeFaceColors } from '@/js/rubik_utils';
import * as THREE from 'three';
import * as TWEEN from '@tweenjs/tween.js'


// Except JSON from backend
/*
{
  number_moves: XY,
  results: [
    {
      rubik: [[[[...]]]],
      move: X'
    },
    ...
  ]
}


*/

class Rubik3D {
	// Cube info
	x: number;
	y: number;
	z: number;

	scene: THREE.Scene;

	face_colors: Array<Array<Array<string>>>;
	all_cubes: THREE.Mesh<THREE.BoxGeometry, THREE.MeshBasicMaterial[], THREE.Object3DEventMap>[];

	// Animation settings
	second_between_animation: number;
	animation_speed: number;
	animation_is_playing: boolean;

	// Animation visualization
	current_frame: number;
	current_tween: TWEEN.Tween | undefined;
	frames: Array<Object>

	readonly COLORS_MAP: Map<string, number> = new Map<string, number>([
		['1', 0xFFFFFF],  // face 1
		['2', 0xFFFF00], // face 2
		['3', 0x0000FF],   // face 3
		['4', 0x00FF00],  // face 4
		['5', 0xFF0000],    // face 5
		['6', 0xff9700], // face 6
	]);
	constructor(scene: THREE.Scene, default_face_colors?: Array<Array<Array<string>>>, center_x?: number, center_y?: number, center_z?: number) {
		this.x = center_x ?? 0;
		this.y = center_y ?? 0;
		this.z = center_z ?? 0;

		this.scene = scene;

		this.face_colors = default_face_colors ?? [
			[['1', '1', '1'], ['1', '1', '1'], ['1', '1', '1']], // UP
			[['2', '2', '2'], ['2', '2', '2'], ['2', '2', '2']], // DOWN
			[['3', '3', '3'], ['3', '3', '3'], ['3', '3', '3']], // FRONT
			[['4', '4', '4'], ['4', '4', '4'], ['4', '4', '4']], // BACK
			[['5', '5', '5'], ['5', '5', '5'], ['5', '5', '5']], // LEFT
			[['6', '6', '6'], ['6', '6', '6'], ['6', '6', '6']]]; // RIGHT

		this.second_between_animation = 0;
		this.animation_speed = 0.5;

		this.all_cubes = createRubik({center: {x: this.x, y: this.y, z: this.z}});
		this.paint_cube(this.face_colors);
		this.display();

		this.current_frame = 0;

		this.frames = [
			{
				move: "F"
			},
			{
			move: "B"
			},
			{
			move: "R"
			},
			// {
			// move: "U"
			// },
			// {
			// move: "L'"
			// },
			// {
			// move: "R'"
			// },
			// {
			// move: "U'"
			// },
		]

		this.animation_is_playing = false;
	}

	set change_rotation_speed(speed: number) {
		this.animation_speed = speed;
	}

	set change_second_between_movements(second: number) {
		this.second_between_animation = second;
	}

	destroy(): void {
		for (let i = 0; i < this.all_cubes.length; i++) {
			this.scene.remove(this.all_cubes[i]);
			delete this.all_cubes[i];
		}
	}

	display(): void {
		for (let i = 0; i < this.all_cubes.length; i++) {
			this.scene.add(this.all_cubes[i]);
		}
	}

	async play_animation(): Promise<void> {
		// console.log(this.all_cubes);
		this.animation_is_playing = true;
		for (let i = this.current_frame; i < this.frames.length; i++) {
			const element = this.frames[i];
			await this.apply_moves(element.move);
			this.current_frame = i;
		}
		this.current_tween = undefined;
		// this.sort_cubes_by_position();
		this.paint_cube([
			[['1', '1', '1'], ['1', '1', '1'], ['1', '1', '1']], // UP
			[['2', '2', '2'], ['2', '2', '2'], ['2', '2', '2']], // DOWN
			[['3', '3', '3'], ['3', '3', '3'], ['3', '3', '3']], // FRONT
			[['4', '4', '4'], ['4', '4', '4'], ['4', '4', '4']], // BACK
			[['5', '5', '5'], ['5', '5', '5'], ['5', '5', '5']], // LEFT
			[['6', '6', '6'], ['6', '6', '6'], ['6', '6', '6']]])
		// await this.update_face_colors();
	}

		private selected_cubes(cube_to_select: Array<number>): THREE.Mesh<THREE.BoxGeometry, THREE.MeshBasicMaterial[], THREE.Object3DEventMap>[] {

		const selected_cubes: THREE.Mesh<THREE.BoxGeometry, THREE.MeshBasicMaterial[], THREE.Object3DEventMap>[] = [];

		for (let i = 0; i < cube_to_select.length; i++) {
			const nb = cube_to_select[i];
			if (0 <= nb && nb < this.all_cubes.length) {
			selected_cubes.push(this.all_cubes[nb]);
			}
		}
		return selected_cubes;
	}

	/**
	 * Check if a < b and return value between -1, 0, 1
	 * @param  {[type]} a_pos
	 * @param  {[type]} b_pos
	 * @return {[type]}
	 */
	private condition_minus_position(a_pos: number, b_pos: number): number {
		if (a_pos < b_pos) {
			return (-1);
		}
		else if (a_pos > b_pos) {
			return (1);
		}
		else {
			return (0);
		}
	}

	sort_cubes_by_position(): void {
		const empty_mesh_array: THREE.Mesh<THREE.BoxGeometry, THREE.MeshBasicMaterial[], THREE.Object3DEventMap>[] = []

		const selected_cubes_up = this.all_cubes.filter((cube) => { return cube.position.y > 0.1; });
		const selected_cubes_middle = this.all_cubes.filter((cube) => { return cube.position.y < 0.1 && cube.position.y > -0.1; });
		const selected_cubes_down = this.all_cubes.filter((cube) => { return cube.position.y < -0.1;});

		const sorted_cube_up = empty_mesh_array.concat(
			selected_cubes_up.filter((cube) => {
				return cube.position.z < -0.1;
			}).sort((a, b) => {
				return this.condition_minus_position(a.position.x, b.position.x);
			}),
			selected_cubes_up.filter((cube) => {
				return cube.position.z < 0.1 && cube.position.z > -0.1;
			}).sort((a, b) => {
				return this.condition_minus_position(a.position.x, b.position.x);
			}),
			selected_cubes_up.filter((cube) => {
				return cube.position.z > 0.1;
			}).sort((a, b) => {
				return this.condition_minus_position(a.position.x, b.position.x);
			})
		);

		const sorted_cube_middle = empty_mesh_array.concat(
			selected_cubes_middle.filter((cube) => {
				return cube.position.z < -0.1;
			}).sort((a, b) => {
				return this.condition_minus_position(a.position.x, b.position.x);
			}),
			selected_cubes_middle.filter((cube) => {
				return cube.position.z < 0.1 && cube.position.z > -0.1;
			}).sort((a, b) => {
				return this.condition_minus_position(a.position.x, b.position.x);
			}),
			selected_cubes_middle.filter((cube) => {
				return cube.position.z > 0.1;
			}).sort((a, b) => {
				return this.condition_minus_position(a.position.x, b.position.x);
			})
		);

		const sorted_cube_down = empty_mesh_array.concat(
			selected_cubes_down.filter((cube) => {
				return cube.position.z < -0.1;
			}).sort((a, b) => {
				return this.condition_minus_position(a.position.x, b.position.x);
			}),
			selected_cubes_down.filter((cube) => {
				return cube.position.z < 0.1 && cube.position.z > -0.1;
			}).sort((a, b) => {
				return this.condition_minus_position(a.position.x, b.position.x);
			}),
			selected_cubes_down.filter((cube) => {
				return cube.position.z > 0.1;
			}).sort((a, b) => {
				return this.condition_minus_position(a.position.x, b.position.x);
			})
		);

		this.all_cubes = sorted_cube_up.concat(sorted_cube_middle, sorted_cube_down);
	}

	async update_face_colors(): Promise<void> {
		console.log(this.all_cubes);
		// All cubes depending face
		const selected_cubes_up = this.selected_cubes([0, 1, 2, 3, 4, 5, 6, 7, 8]);
		const selected_cubes_down = this.selected_cubes([20, 19, 18, 23, 22, 21, 26, 25, 24]);
		const selected_cubes_front = this.selected_cubes([6, 7, 8, 15, 16, 17, 24, 25, 26]);
		const selected_cubes_back = this.selected_cubes([2, 1, 0, 11, 10, 9, 20, 19, 18]);
		const selected_cubes_left = this.selected_cubes([0, 3, 6, 9, 12, 15, 18, 21, 24]);
		const selected_cubes_right = this.selected_cubes([8, 5, 2, 17, 14, 11, 26, 23, 20]);

		// To highlight selected_cubes_...
		const highlight_selected_test_only = selected_cubes_right;
		for (let i = 0; i < highlight_selected_test_only.length; i++) {
			changeCubeFaceColors({cube: highlight_selected_test_only[i], new_colors: 0xFF00FF});
			await new Promise<void>((resolve, reject) => {
				setTimeout(resolve, 500);
			})
		}

		// Elle doit recuperer la couleur de chaque phrase et mettre a jour le tableau triple dimensionnel.
		// Ex. elle parcourt selected_cubes_up et met a jour [0][0]...[2][2] en fonction de .getHex() en comparant au dictionnaire this.COLORS_MAP
	}

	paint_cube(new_face_colors: Array<Array<Array<string>>>): void {

		// this.destroy();
		// this.all_cubes = createRubik({center: {x: this.z, y: this.y, z: this.z}});
		// this.display();
		// console.log()
		this.sort_cubes_by_position();

		// All face concatenates
		const face_up: Array<string> = new_face_colors[0][0].concat(new_face_colors[0][1],new_face_colors[0][2]);
		const face_down: Array<string> = new_face_colors[1][0].concat(new_face_colors[1][1],new_face_colors[1][2]);
		const face_front: Array<string> = new_face_colors[2][0].concat(new_face_colors[2][1],new_face_colors[2][2]);
		const face_back: Array<string> = new_face_colors[3][0].concat(new_face_colors[3][1],new_face_colors[3][2]);
		const face_left: Array<string> = new_face_colors[4][0].concat(new_face_colors[4][1],new_face_colors[4][2]);
		const face_right: Array<string> = new_face_colors[5][0].concat(new_face_colors[5][1],new_face_colors[5][2]);

		// All cubes depending face
		const selected_cubes_up = this.selected_cubes([0, 1, 2, 3, 4, 5, 6, 7, 8]);
		const selected_cubes_down = this.selected_cubes([20, 19, 18, 23, 22, 21, 26, 25, 24]);
		const selected_cubes_front = this.selected_cubes([6, 7, 8, 15, 16, 17, 24, 25, 26]);
		const selected_cubes_back = this.selected_cubes([2, 1, 0, 11, 10, 9, 20, 19, 18]);
		const selected_cubes_left = this.selected_cubes([0, 3, 6, 9, 12, 15, 18, 21, 24]);
		const selected_cubes_right = this.selected_cubes([8, 5, 2, 17, 14, 11, 26, 23, 20]);

		// Face_index
		// Face_index - 0 = right
		// Face_index - 1 = left
		// Face_index - 2 = up
		// Face_index - 3 = down
		// Face_index - 4 = front
		// Face_index - 5 = back
		for (let i = 0; i < face_up.length && i < selected_cubes_up.length; i++) {
			changeCubeFaceColors({cube: selected_cubes_up[i], new_colors: this.COLORS_MAP.get(face_up[i]), face: "up"})
		}
		for (let i = 0; i < face_down.length && i < selected_cubes_down.length; i++) {
			changeCubeFaceColors({cube: selected_cubes_down[i], new_colors: this.COLORS_MAP.get(face_down[i]), face: "down"})
		}
		for (let i = 0; i < face_front.length && i < selected_cubes_front.length; i++) {
			changeCubeFaceColors({cube: selected_cubes_front[i], new_colors: this.COLORS_MAP.get(face_front[i]), face: "front"});
		}
		for (let i = 0; i < face_back.length && i < selected_cubes_back.length; i++) {
			changeCubeFaceColors({cube: selected_cubes_back[i], new_colors: this.COLORS_MAP.get(face_back[i]), face: "back"})
		}
		for (let i = 0; i < face_left.length && i < selected_cubes_left.length; i++) {
			changeCubeFaceColors({cube: selected_cubes_left[i], new_colors: this.COLORS_MAP.get(face_left[i]), face: "left"})
		}
		for (let i = 0; i < face_right.length && i < selected_cubes_right.length; i++) {
			changeCubeFaceColors({cube: selected_cubes_right[i], new_colors: this.COLORS_MAP.get(face_right[i]), face: "right"})
		}

		// To highlight selected_cubes_...
		// let highlight_selected_test_only = selected_cubes_front;
		// for (let i = 0; i < highlight_selected_test_only.length; i++) {
		//   changeCubeFaceColors({cube: highlight_selected_test_only[i], new_colors: "red"});
		// }    const intersectedObject: THREE.Mesh = intersects[0].object;
	}

	private async animate_rubik(
	cube_to_move: THREE.Mesh<THREE.BoxGeometry, THREE.MeshBasicMaterial[], THREE.Object3DEventMap>[],
	new_rotation: { x: number; y: number; z: number }): Promise<void>
	{
		const group = new THREE.Group();
		for (let i = 0; i < cube_to_move.length; i++) {
			const cube = cube_to_move[i];
			group.add(cube)
		}
		this.scene.add(group)

		const targetRotation = {
			x: THREE.MathUtils.degToRad(group.rotation.x + new_rotation.x),
			y: THREE.MathUtils.degToRad(group.rotation.y + new_rotation.y),
			z: THREE.MathUtils.degToRad(group.rotation.z + new_rotation.z)
		};

		return new Promise((resolve) => {
			this.current_tween = new TWEEN.Tween(group.rotation)
			.to(targetRotation, 1000 * this.animation_speed)
			.easing(TWEEN.Easing.Cubic.InOut)
			.onUpdate(() => {})
			.onComplete(async () => {
				// console.log("Rotation complete");
				for (let i = 0; i < cube_to_move.length; i++) {
				const cube = cube_to_move[i];
				this.scene.attach(cube);
				}
				this.scene.remove(group);

				await new Promise<void>((resolve) => {
				setTimeout(resolve, 1000 * this.second_between_animation);
				})
				resolve();
			})
			.start();
		});
	}

	private async apply_moves(move: string): Promise<void> {
		const cube_to_move: THREE.Mesh<THREE.BoxGeometry, THREE.MeshBasicMaterial[], THREE.Object3DEventMap>[] = [];

		let x: number = 0;
		let y: number = 0;
		let z: number = 0;

		for (let i = 0; i < this.all_cubes.length; i++) {
			const cube = this.all_cubes[i];

			if (move === "U" || move === "U'") {
			y = move === "U" ? -90 : 90
			if (cube.position.y > 0.1) {
				cube_to_move.push(cube);
			}
			}
			else if (move === "D" || move === "D'") {
			y = move === "D" ? 90 : -90
			if (cube.position.y < -0.1) {
				cube_to_move.push(cube);
			}
			}
			else if (move === "F" || move === "F'") {
			z = move === "F" ? -90 : 90
			if (cube.position.z > 0.1) {
				cube_to_move.push(cube);
			}
			}
			else if (move === "B" || move === "B'") {
			z = move === "B" ? 90 : -90
			if (cube.position.z < -0.1) {
				cube_to_move.push(cube);
			}
			}
			else if (move === "L" || move === "L'") {
			x = move === "L" ? 90 : -90
			if (cube.position.x < -0.1) {
				cube_to_move.push(cube);
			}
			}
			else if (move === "R" || move === "R'") {
			x = move === "R" ? -90 : 90
			if (cube.position.x > 0.1) {
				cube_to_move.push(cube);
			}
			}
			else {
			// alert("Invalid movement detected !");
			console.log("Invalid movement detected !");
			}
		}
		await this.animate_rubik(cube_to_move, {x: x, y: y, z: z});
	}
}

export { Rubik3D }
