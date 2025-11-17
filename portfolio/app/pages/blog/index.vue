<script setup>
import { posts } from '~/data/posts'
</script>

<template>
  <div class="max-w-3xl mx-auto py-10">
    <h1 class="text-3xl font-bold mb-10">Blog Timeline</h1>

    <div class="space-y-6 relative border-l pl-6">
      <div v-for="post in posts" :key="post.slug" class="relative">
        <span class="absolute -left-3 top-2 w-3 h-3 bg-primary-500 rounded-full"></span>

        <NuxtLink :to="`/blog/${post.slug}`">
          <h2 class="text-xl font-semibold hover:text-primary-500">
            {{ post.title }}
          </h2>
        </NuxtLink>
        <p class="text-sm opacity-70">{{ post.date }} | {{ post.category }}</p>
        <p class="opacity-80">{{ post.summary }}</p>

        <div class="flex gap-2 mt-2">
          <UBadge variant="soft" color="green">{{ post.tag }}</UBadge>
          <UBadge variant="soft" color="blue">{{ post.author }}</UBadge>
        </div>
      </div>
    </div>
  </div>
</template>
