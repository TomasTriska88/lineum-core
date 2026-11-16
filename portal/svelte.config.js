import adapter from '@sveltejs/adapter-node';
import { mdsvex } from 'mdsvex';

/** @type {import('@sveltejs/kit').Config} */
const config = {
	extensions: ['.svelte', '.md', '.svx'],
	preprocess: [
		mdsvex({
			extensions: ['.md', '.svx']
		})
	],
	kit: {
		adapter: adapter(),
		prerender: {
			entries: process.env.VITE_LINEUM_PRESENTATION_ONLY === '1' ? ['/', '/about', '/brand', '/codex', '/privacy', '/support', '/wiki'] : ['*'],
			handleHttpError: process.env.VITE_LINEUM_PRESENTATION_ONLY === '1' ? 'warn' : 'fail',
			handleMissingId: process.env.VITE_LINEUM_PRESENTATION_ONLY === '1' ? 'warn' : 'fail',
			handleUnseenRoutes: process.env.VITE_LINEUM_PRESENTATION_ONLY === '1' ? 'warn' : 'fail'
		},
		alias: {
			'$whitepapers': 'src/lib/data/whitepapers'
		}
	}
};

export default config;
