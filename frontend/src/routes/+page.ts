
import type { PageLoad } from './$types';


export interface Post {
	id: number;
	title: string;
	content: string; 
	created_at: string; 
}

export const load: PageLoad = async ({ fetch }) => {
	try {
		const res = await fetch('http://127.0.0.1:8000/posts');//API

		if (!res.ok) {
			throw new Error('無法取得文章列表');
		}

		const posts: Post[] = await res.json();

		return {
			posts
		};
	} catch (err) {
		console.error(err);
		return {
			posts: []
		};
	}
};
