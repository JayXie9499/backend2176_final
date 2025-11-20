<script lang="ts">
	import type { PageData } from './$types';
	export let data: PageData;
</script>

<div class="mx-auto max-w-3xl px-4 py-12 sm:px-6 lg:py-16">
	<div class="flex flex-col gap-10">
		{#each data.posts as post}
			<article
				class="group relative transform rounded-xl border border-gray-200 bg-white shadow-sm transition-all duration-300 ease-in-out hover:-translate-y-1 hover:shadow-lg"
			>
				<div class="p-6 sm:p-8">
					<div class="mb-3 text-sm font-medium text-blue-600">
						<span>{new Date(post.created_at).toLocaleDateString('zh-TW')}</span>
					</div>

					<h2 class="mb-3 text-2xl font-semibold text-slate-900">
						<a
							href={`/post/${post.id}`}
							class="transition-colors duration-200 group-hover:text-blue-700"
						>
							<span class="absolute inset-0" aria-hidden="true"></span>
							{post.title}
						</a>
					</h2>

					<p class="mb-4 line-clamp-2 text-base text-slate-600">
						{post.content.substring(0, 100)}...
					</p>

					<div class="mt-4 font-semibold text-blue-600">
						閱讀更多 <span aria-hidden="true">&rarr;</span>
					</div>
				</div>
			</article>
		{/each}

		{#if data.posts.length === 0}
			<div class="py-10 text-center">
				<p class="text-xl text-slate-500">尚未發表文章。</p>
			</div>
		{/if}
	</div>
</div>
