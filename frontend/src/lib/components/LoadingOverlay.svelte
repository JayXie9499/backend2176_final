<script lang="ts">
	import { fade } from 'svelte/transition';

	// 可以傳入自定義文字，預設為 "載入中..."
	export let message: string = '處理中...';
</script>

<div
	in:fade={{ duration: 200 }}
	out:fade={{ duration: 200 }}
	class="fixed inset-0 z-[100] flex flex-col items-center justify-center bg-white/60 backdrop-blur-md dark:bg-slate-900/60"
>
	<div class="relative flex h-16 w-16 items-center justify-center">
		<div class="absolute h-full w-full animate-ping rounded-full bg-blue-500 opacity-20"></div>
		<div
			class="h-12 w-12 animate-spin rounded-full border-4 border-blue-200 border-t-blue-600"
		></div>
	</div>

	<p class="mt-4 animate-pulse font-medium text-slate-600 dark:text-slate-300">
		{message}
	</p>
</div>
