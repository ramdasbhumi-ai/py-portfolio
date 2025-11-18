<script setup lang="ts">
import { useRoute } from 'vue-router'
import { posts } from '~/composables/blog-posts'

const route = useRoute()

// ensure slug is string
const slug = computed(() => String(route.params.slug))

const post = computed(() =>
  posts.find(p => p.slug === slug.value)
)
</script>

<template>
  <UContainer class="py-10">

    <div v-if="post">
      <UBlogPost
        :slug="post.slug"
        :title="post.title"
        :description="post.description"
        :image="post.image"
        :date="post.date"
      />
    </div>

    <p v-else>❌ Post not found — wrong slug!</p>
  </UContainer>
</template>
