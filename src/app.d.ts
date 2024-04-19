import type { Tile } from "$lib/db";
import type { Collection } from 'mongodb';

// See https://kit.svelte.dev/docs/types#app
// for information about these interfaces
declare global {
	namespace App {
		// interface Error {}
		interface Locals {
			tiles: Collection<Tile>
		}
		// interface PageData {}
		// interface PageState {}
		// interface Platform {}
	}
}

export { };
