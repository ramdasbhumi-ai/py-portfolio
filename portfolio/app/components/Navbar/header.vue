<script setup lang="ts">
import { ref, computed } from 'vue'

const searchTerm = ref('')

// Example projects list
const allProjects = [
  { id: 1, name: 'Project Alpha', path: '/projects/alpha' },
  { id: 2, name: 'Project Beta', path: '/projects/beta' },
  { id: 3, name: 'Project Gamma', path: '/projects/gamma' }
]

const groups = computed(() => [{
  id: 'projects',
  label: searchTerm.value ? `Projects matching “${searchTerm.value}”...` : 'Projects',
  items: allProjects
    .filter(p => p.name.toLowerCase().includes(searchTerm.value.toLowerCase()))
    .map(p => ({ label: p.name, to: p.path })),
  ignoreFilter: true
}])
</script>
<template>
  <UHeader toggle-side="left">
    <template #title>
      <img
        src="/logo-svg.png"
        alt="Design showcase"
        class="h-10 w-auto rounded shadow-2xl ring ring-default"
      />
    </template>

    <UNavigationMenu :items="[
      { label: 'Docs', to: '/' },
      { label: 'Blogs', to: '/blog' }
    ]" />

    <template #right>
      <!-- Open Projects Command Palette -->
      <UModal>
        <UButton
          label="Projects"
          color="neutral"
          variant="outline"
          icon="i-lucide-search"
        />

        <template #content>
          <UCommandPalette
            v-model:search-term="searchTerm"
            :groups="groups"
            placeholder="Search projects..."
            class="h-80"
          />
        </template>
      </UModal>

      <UColorModeButton />
    </template>
  </UHeader>
</template>
