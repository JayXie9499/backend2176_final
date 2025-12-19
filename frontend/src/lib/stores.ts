import { writable } from 'svelte/store';

// 定義 User 介面
export interface User {
	username: string;
	avatar?: string;
}

// 預設為 null (未登入)
export const user = writable<User | null>(null);
