import type { LayoutServerLoad } from './$types';

export const load: LayoutServerLoad = async ({ locals }) => {
    const { tiles } = locals;

    const tilesDb = await tiles.find().toArray();

    //SK can't serialize Mongo's complex _id type, need to turn it into a string
    const tilesStringId = tilesDb.map(tile => ({ ...tile, _id: tile._id.toString() }));

    return {
        tiles: tilesStringId
    };
}