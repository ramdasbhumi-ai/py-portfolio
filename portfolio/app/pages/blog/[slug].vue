<script setup>
import { useRoute } from 'vue-router'
import { posts } from '~/data/posts'

const route = useRoute()
const post = posts.find(p => p.slug === route.params.slug)
</script>

<template>
  <div class="max-w-3xl mx-auto py-10">
    <NuxtLink to="/blog" class="underline opacity-70">← Back</NuxtLink>

    <h1 class="text-4xl font-bold mt-4">{{ post.title }}</h1>
    <p class="opacity-60">{{ post.date }} — {{ post.author }}</p>

    <p class="mt-8 text-lg">{{ post.summary }}</p>
  </div>
</template>
