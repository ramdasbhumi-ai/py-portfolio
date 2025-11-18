<script setup lang="ts">
import type { NavigationMenuItem } from '@nuxt/ui'

const route = useRoute()

const items = computed<NavigationMenuItem[]>(() => [
  {
    label: 'Docs',
    to: '/',
    // active: route.path.startsWith('/')
  },
  {
    label: 'Blogs',
    to: '/blog',
    active: route.path.startsWith('/blog')
  },
  {
    label: 'Projects',
    to: '/projects',
    // target: '_blank'
    active: route.path.startsWith('/projects')
  }
])
</script>

<template>
   <UHeader toggle-side="left">
    <template #title>
      <!-- <Logo class="h-6 w-auto" /> -->
       <img
        src="/logo-svg.png"
        alt="Design showcase"
        class="h-10 w-auto rounded shadow-2xl ring ring-default"
      />
    </template>

    <UNavigationMenu :items="items" />

    <template #right>
      <UColorModeButton />
    </template>

    <template #body>
      <UNavigationMenu :items="items" orientation="vertical" class="-mx-2.5" />
    </template>
  </UHeader>
</template>
