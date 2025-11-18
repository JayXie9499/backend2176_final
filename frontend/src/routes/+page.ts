import type { PageLoad } from './$types';

interface PostMetadata {
	title: string;
	date: string;
	excerpt: string;
}

export interface Post {
	metadata: PostMetadata;
	slug: string;
}

export const load: PageLoad = async () => {
	const postFiles = import.meta.glob<true, string, { metadata: PostMetadata }>(
		'/src/lib/posts/*.md',
		{ eager: true }
	);

	const posts: Post[] = Object.entries(postFiles)
		.map(([path, module]) => {
			const slug = path.split('/').pop()?.replace('.md', '') ?? '';

			return {
				metadata: module.metadata,
				slug: slug
			};
		})
		.sort((a, b) => new Date(b.metadata.date).getTime() - new Date(a.metadata.date).getTime());
	return {
		posts: posts
	};
};
