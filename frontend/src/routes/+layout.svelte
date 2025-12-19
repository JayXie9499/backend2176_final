<script lang="ts">
	import { resolve } from '$app/paths';
	import { page } from '$app/stores';
	import '../app.css';
	import { fade } from 'svelte/transition';
	// 修改: 從共用檔案引入 user
	import { user } from '$lib/stores';

	function handleLogout() {
		$user = null;
	}
</script>

<div
	class="flex min-h-screen flex-col bg-slate-50 font-sans text-slate-900 selection:bg-blue-500/30 dark:bg-slate-950 dark:text-slate-100"
>
	<div
		class="pointer-events-none fixed inset-0 z-0 opacity-[0.03] dark:opacity-[0.05]"
		style="background-image: url('data:image/svg+xml,%3Csvg width=\'60\' height=\'60\' viewBox=\'0 0 60 60\' xmlns=\'http://www.w3.org/2000/svg\'%3E%3Cg fill=\'none\' fill-rule=\'evenodd\'%3E%3Cg fill=\'%239C92AC\' fill-opacity=\'1\'%3E%3Cpath d=\'M36 34v-4h-2v4h-4v2h4v4h2v-4h4v-2h-4zm0-30V0h-2v4h-4v2h4v4h2V6h4V4h-4zM6 34v-4H4v4H0v2h4v4h2v-4h4v-2H6zM6 4V0H4v4H0v2h4v4h2V6h4V4H6z\'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E');"
	></div>

	<nav
		class="sticky top-0 z-50 w-full border-b border-slate-200/80 bg-white/80 backdrop-blur-md dark:border-slate-800/80 dark:bg-slate-900/80"
	>
		<div class="mx-auto flex h-16 max-w-5xl items-center justify-between px-4 sm:px-6">
			<a href={resolve('/')} class="group flex items-center gap-2 outline-none">
				<div
					class="flex h-8 w-8 items-center justify-center rounded-lg bg-blue-600 text-white shadow-lg shadow-blue-500/30 transition-transform group-hover:rotate-12"
				>
					<span class="text-lg font-bold">B</span>
				</div>
				<span class="text-xl font-bold tracking-tight text-slate-800 dark:text-white">
					Dev<span class="text-blue-600">Blog</span>
				</span>
			</a>

			<div class="flex items-center gap-3 sm:gap-4">
				{#if $user}
					<a
						href={resolve('/post')}
						class="hidden items-center gap-2 rounded-full bg-slate-900 px-4 py-1.5 text-sm font-medium text-white transition-all hover:bg-slate-700 hover:shadow-lg sm:flex dark:bg-white dark:text-slate-900 dark:hover:bg-slate-200"
					>
						<svg class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
							<path
								stroke-linecap="round"
								stroke-linejoin="round"
								stroke-width="2"
								d="M12 4v16m8-8H4"
							/>
						</svg>
						<span>發表文章</span>
					</a>
				{/if}

				<div class="h-6 w-px bg-slate-200 dark:bg-slate-700"></div>

				{#if $user}
					<div class="flex items-center gap-3">
						<div class="group relative">
							<div
								class="flex cursor-pointer items-center gap-2 rounded-full border border-slate-200 bg-slate-50 py-1 pr-3 pl-1 transition hover:border-blue-300 dark:border-slate-700 dark:bg-slate-800"
							>
								<div
									class="flex h-7 w-7 items-center justify-center rounded-full bg-gradient-to-br from-blue-500 to-purple-600 text-xs font-bold text-white shadow-sm"
								>
									{$user.username.substring(0, 1).toUpperCase()}
								</div>
								<span
									class="max-w-[80px] truncate text-sm font-medium text-slate-700 dark:text-slate-200"
								>
									{$user.username}
								</span>
							</div>
						</div>
						<!-- svelte-ignore a11y_consider_explicit_label -->
						<button
							on:click={handleLogout}
							class="rounded-md p-2 text-slate-500 transition-colors hover:bg-slate-100 hover:text-red-600 dark:text-slate-400 dark:hover:bg-slate-800"
						>
							<svg class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
								<path
									stroke-linecap="round"
									stroke-linejoin="round"
									stroke-width="2"
									d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1"
								/>
							</svg>
						</button>
					</div>
				{:else}
					<nav class="flex items-center gap-2">
						<a
							href={resolve('/login')}
							class="rounded-md px-3 py-1.5 text-sm font-medium text-slate-600 transition hover:text-blue-600 dark:text-slate-300 dark:hover:text-white"
						>
							登入
						</a>
						<a
							href={resolve('/register')}
							class="rounded-md bg-blue-600 px-4 py-1.5 text-sm font-medium text-white shadow-md shadow-blue-500/20 transition hover:bg-blue-700 hover:shadow-lg"
						>
							註冊
						</a>
					</nav>
				{/if}
			</div>
		</div>
	</nav>

	<main class="relative z-10 mx-auto w-full max-w-5xl flex-1 px-4 py-8 sm:px-6 lg:py-12">
		<div in:fade={{ duration: 200 }}>
			<slot />
		</div>
	</main>

	<footer class="border-t border-slate-200 bg-white py-8 dark:border-slate-800 dark:bg-slate-950">
		<div class="mx-auto max-w-5xl px-4 text-center sm:px-6">
			<p class="text-sm text-slate-500 dark:text-slate-400">
				&copy; {new Date().getFullYear()} DevBlog. Built with SvelteKit & Tailwind.
			</p>
		</div>
	</footer>
</div>
