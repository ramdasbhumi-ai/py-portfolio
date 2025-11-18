<!-- <template>
  <div class="space-y-4 py-8">
    <div
      v-for="post in posts"
      :key="post.slug"
      class="p-4 border rounded-lg hover:bg-gray-100 transition"
    >
      <NuxtLink :to="`/blog/${post.slug}`" class="block">
        <h2 class="text-xl font-semibold">{{ post.title }}</h2>
        <p class="text-gray-600 text-sm">{{ post.description }}</p>
      </NuxtLink>
    </div>
  </div>
</template>

<script setup>
import { posts } from '~/composables/blog-posts'
</script>

<style scoped>
.cursor-pointer {
  cursor: pointer;
}
</style> -->

<template>
  <UContainer class="py-10">
    <h1 class="text-4xl font-bold mb-8">Blog</h1>

    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
      <NuxtLink
        v-for="post in posts"
        :key="post.slug"
        :to="`/blog/${post.slug}`"
        class="block rounded-2xl overflow-hidden shadow bg-white dark:bg-gray-900 hover:shadow-lg transition duration-200 hover:-translate-y-1"
      >
        <img
          :src="post.image"
          class="h-48 w-full object-cover"
          alt="Blog Image"
        />

        <div class="p-4">
          <h2 class="text-lg font-semibold text-gray-900 dark:text-white mb-2">
            {{ post.title }}
          </h2>

          <p class="text-gray-700 dark:text-gray-300 text-sm line-clamp-2">
            {{ post.description }}
          </p>

          <p class="text-xs text-gray-500 mt-3">{{ post.date }}</p>
        </div>
      </NuxtLink>
    </div>
  </UContainer>
</template>

<script setup>
import { posts } from '~/composables/blog-posts'
</script>
