import { MongoClient } from "mongodb"
import { MONGODB_URI } from "$env/static/private";
import type { Handle } from '@sveltejs/kit';

const client = new MongoClient(MONGODB_URI as string);
await client.connect();

export const handle: Handle = (async ({ event, resolve }) => {
    event.locals.tiles = client.db('giaveno').collection('tiles');

    return resolve(event)
});
