<script lang="ts">
	import type { PageData } from './$types';

	export let data: PageData;
</script>

<div class="mx-auto max-w-3xl px-4 py-12 sm:px-6 lg:py-16">
	<div class="mb-12 border-b border-gray-200 pb-8 text-center">
		<h1 class="text-4xl font-extrabold tracking-tight text-gray-900 sm:text-5xl">我的技術日誌</h1>
		<p class="mt-4 text-xl text-gray-500">紀錄學習 Svelte, FastAPI 與 Tailwind CSS 的點滴。</p>
	</div>

	<div class="flex flex-col gap-10">
		{#each data.posts as post}
			<article
				class="group relative transform rounded-xl border border-gray-200 bg-white shadow-sm transition-all duration-300 ease-in-out hover:-translate-y-1 hover:shadow-lg"
			>
				<div class="p-6 sm:p-8">
					<div class="mb-3 text-sm font-medium text-blue-600">
						<span>{new Date(post.metadata.date).toLocaleDateString('zh-TW')}</span>
					</div>

					<h2 class="mb-3 text-2xl font-semibold text-gray-900">
						<a
							href={`/post/${post.slug}`}
							class="transition-colors duration-200 group-hover:text-blue-700"
						>
							<span class="absolute inset-0" aria-hidden="true"></span>
							{post.metadata.title}
						</a>
					</h2>

					<p class="mb-4 line-clamp-2 text-base text-gray-600">
						{post.metadata.excerpt}
					</p>

					<div class="mt-4 font-semibold text-blue-600">
						閱讀更多 <span aria-hidden="true">&rarr;</span>
					</div>
				</div>
			</article>
		{/each}

		{#if data.posts.length === 0}
			<p class="text-center text-xl text-gray-500">目前還沒有文章... 趕快去寫一篇吧！</p>
		{/if}
	</div>
</div>
