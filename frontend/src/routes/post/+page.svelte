<script lang="ts">
	let title = '';

	let content = '';

	function handleSubmit() {
		console.log('發表新文章:', { title, content });
	}
</script>

<div class="mx-auto max-w-3xl px-4 py-10">
	<h1 class="mb-8 text-center text-4xl font-bold text-white">撰寫新文章</h1>

	<form class="flex flex-col gap-6" on:submit|preventDefault={handleSubmit}>
		<div class="text-left">
			<label for="title" class="mb-2 block text-xl font-medium text-white">標題</label>

			<input
				type="text"
				id="title"
				bind:value={title}
				required
				placeholder="文章標題..."
				class="w-full rounded-md border border-gray-300 bg-white px-4 py-3 text-lg text-gray-800 focus:border-blue-500 focus:ring-4 focus:ring-blue-500/20 focus:outline-none"
			/>
		</div>

		<div class="text-left">
			<label for="content" class="mb-2 block text-xl font-medium text-white"
				>內容 (支援 Markdown)</label
			>

			<textarea
				id="content"
				bind:value={content}
				required
				rows="15"
				placeholder="在這裡輸入您的文章內容..."
				class="w-full rounded-md border border-gray-300 bg-white px-4 py-3 font-mono text-lg text-gray-800 focus:border-blue-500 focus:ring-4 focus:ring-blue-500/20 focus:outline-none"
			></textarea>
		</div>

		<button
			type="submit"
			class="mt-4 rounded-md bg-green-600 px-6 py-3.5 text-lg font-semibold text-white transition hover:bg-green-700 focus:ring-4 focus:ring-green-500/50 focus:outline-none"
		>
			立即發表
		</button>
	</form>
</div>
